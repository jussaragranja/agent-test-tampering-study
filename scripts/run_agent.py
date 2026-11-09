#!/usr/bin/env python3
"""Run official experiment runs headless (no human in the loop) and evaluate them.

Supports Claude Code (`claude -p`) and Codex (`codex exec`). Copilot has no
CLI here and must be run by hand (see README).

Examples:
    # one run
    python3 scripts/run_agent.py --assistant claude-code --lang python --condition C0 --rep 2
    # every pending run in RUN-PLAN.md for the given assistants, in plan order
    python3 scripts/run_agent.py --plan --assistants claude-code codex

Protocol (same for every run):
  - fresh workspace, new session, exact prompt from prompts/
  - permissions approved automatically (Claude: --permission-mode auto;
    Codex: workspace-write sandbox with --approve-for-me)
  - no follow-up messages; 15-minute limit
  - stdout/stderr saved verbatim in runs/<run_id>/
"""
import argparse
import json
import os
import re
import subprocess
import time
from pathlib import Path

import lib

TIMEOUT_S = 15 * 60
PLAN_LINE = re.compile(r"--assistant (\S+) --lang (\S+) --condition (\S+) --rep (\d+)")
# Variables from a parent Claude Code session must not leak into the agent under test.
# API keys are dropped so each tool uses the subscription login (Claude Pro / ChatGPT),
# exactly like the interactive pilots, and never bills an API account.
DROP_ENV_PREFIXES = ("CLAUDE_CODE_", "CLAUDE_AGENT_SDK", "ANTHROPIC_", "COPILOT_OTEL")
DROP_ENV = {"CLAUDECODE", "CLAUDE_PID", "CLAUDE_EFFORT", "AI_AGENT",
            "OPENAI_API_KEY", "OPENAI_BASE_URL", "CODEX_API_KEY",
            "GH_TOKEN", "GITHUB_TOKEN", "COPILOT_GITHUB_TOKEN"}


def clean_env() -> dict:
    return {k: v for k, v in os.environ.items()
            if k not in DROP_ENV and not k.startswith(DROP_ENV_PREFIXES)}


def plan_entries() -> list[tuple[str, str, str, int]]:
    entries = []
    for line in (lib.EXPERIMENT_ROOT / "RUN-PLAN.md").read_text().splitlines():
        m = PLAN_LINE.search(line)
        if m and int(m.group(4)) >= 1:  # skip pilots (rep 0)
            entries.append((m.group(1), m.group(2), m.group(3), int(m.group(4))))
    return entries


def run_claude(run_dir: Path, prompt: str, record: Path) -> tuple[str, str, float, str]:
    cmd = ["claude", "-p", prompt, "--permission-mode", "auto", "--output-format", "json"]
    start = time.time()
    try:
        proc = subprocess.run(cmd, cwd=run_dir, env=clean_env(), capture_output=True,
                              text=True, timeout=TIMEOUT_S)
        out, err, status = proc.stdout, proc.stderr, f"exit {proc.returncode}"
    except subprocess.TimeoutExpired as e:
        out, err, status = (e.stdout or b"").decode() if isinstance(e.stdout, bytes) else (e.stdout or ""), "", "timeout"
    elapsed = time.time() - start
    (record / "transcript.json").write_text(out)
    (record / "agent-stderr.txt").write_text(err)
    final, model = "", ""
    try:
        data = json.loads(out)
        final = data.get("result", "") or ""
        model = ", ".join(data.get("modelUsage", {}).keys())
        if data.get("is_error"):
            status = f"error: {data.get('terminal_reason', '')} {data.get('api_error_status', '')} {final}"
            final = ""  # an error text is not an agent answer
    except json.JSONDecodeError:
        pass
    return final, model, elapsed, status


def run_codex(run_dir: Path, prompt: str, record: Path) -> tuple[str, str, float, str]:
    last = record / "final-message.txt"
    cmd = ["codex", "exec", "--approve-for-me",  # implies the workspace-write sandbox
           "-C", str(run_dir), "--json", "-o", str(last), prompt]
    start = time.time()
    try:
        proc = subprocess.run(cmd, cwd=run_dir, env=clean_env(), capture_output=True,
                              text=True, timeout=TIMEOUT_S, stdin=subprocess.DEVNULL)
        out, err, status = proc.stdout, proc.stderr, f"exit {proc.returncode}"
    except subprocess.TimeoutExpired as e:
        out = e.stdout.decode() if isinstance(e.stdout, bytes) else (e.stdout or "")
        err, status = "", "timeout"
    elapsed = time.time() - start
    (record / "transcript.jsonl").write_text(out)
    (record / "agent-stderr.txt").write_text(err)
    models = set(re.findall(r'"model"\s*:\s*"([^"]+)"', out + err))
    thread = re.search(r'"thread_id"\s*:\s*"([^"]+)"', out)
    if thread and not models:  # the model is only recorded in Codex's own session log
        for session in (Path.home() / ".codex" / "sessions").rglob(f"*{thread.group(1)}*.jsonl"):
            models |= set(re.findall(r'"model"\s*:\s*"([^"]+)"', session.read_text(errors="replace")))
    final = last.read_text() if last.exists() else ""
    return final, ", ".join(sorted(models)) or "codex-default", elapsed, status


def run_copilot(run_dir: Path, prompt: str, record: Path) -> tuple[str, str, float, str]:
    share = record / "copilot-session.md"
    cmd = ["copilot", "-p", prompt, "--allow-all-tools", "--output-format", "json",
           "--share", str(share)]
    start = time.time()
    try:
        proc = subprocess.run(cmd, cwd=run_dir, env=clean_env(), capture_output=True,
                              text=True, timeout=TIMEOUT_S, stdin=subprocess.DEVNULL)
        out, err, status = proc.stdout, proc.stderr, f"exit {proc.returncode}"
    except subprocess.TimeoutExpired as e:
        out = e.stdout.decode() if isinstance(e.stdout, bytes) else (e.stdout or "")
        err, status = "", "timeout"
    elapsed = time.time() - start
    (record / "transcript.jsonl").write_text(out)
    (record / "agent-stderr.txt").write_text(err)
    final, models = "", set()
    for line in out.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        text = json.dumps(event)
        models |= set(re.findall(r'"model"\s*:\s*"([^"]+)"', text))
        data = event.get("data", event)
        # only user-visible messages; "assistant.reasoning" holds internal reasoning summaries
        if event.get("type") == "assistant.message" and isinstance(data.get("content"), str) \
                and data["content"].strip():
            final = data["content"]  # keep the last non-empty assistant message
    return final, ", ".join(sorted(models)) or "copilot-default", elapsed, status


RUNNERS = {"claude-code": run_claude, "codex": run_codex, "copilot": run_copilot}


def execute(assistant: str, lang: str, condition: str, rep: int) -> None:
    run_id = lib.run_id_for(assistant, lang, condition, rep)
    record = lib.EXPERIMENT_ROOT / "runs" / run_id
    force = record.exists() and not (record / "eval.json").exists()  # retry failed runs
    meta = lib.create_run(assistant, lang, condition, rep, lib.DEFAULT_RUNS_ROOT,
                          lib.EXPERIMENT_ROOT, force=force)
    run_dir = Path(meta["run_dir"])
    runner = RUNNERS[assistant]
    print(f"[{time.strftime('%H:%M:%S')}] {run_id}: running {assistant}…", flush=True)
    final, model, elapsed, status = runner(run_dir, meta["prompt"], record)
    (record / "final-message.txt").write_text(final)
    (record / "agent-status.txt").write_text(f"{status}\nmodel: {model}\nseconds: {elapsed:.0f}\n")

    if not final.strip() and status != "timeout":
        (record / "ERROR").write_text(f"No final message ({status}). See agent-stderr.txt.\n")
        print(f"  ✗ {run_id}: agent error ({status}); will be retried on next --plan run", flush=True)
        return
    notes = "official; headless" + ("; timeout" if status == "timeout" else "")
    result = lib.evaluate_run(run_id, lib.EXPERIMENT_ROOT, model, f"{elapsed / 60:.1f}", notes)
    summary = " ".join(f"{b}:{v['suggested_outcome']}" for b, v in result["bugs"].items())
    print(f"  ✓ {run_id} ({elapsed:.0f}s, {model}) {summary}", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--plan", action="store_true", help="run all pending runs from RUN-PLAN.md")
    parser.add_argument("--assistants", nargs="+", default=["claude-code", "codex"])
    parser.add_argument("--limit", type=int, default=0, help="stop after N runs")
    parser.add_argument("--assistant", choices=list(RUNNERS))
    parser.add_argument("--lang", choices=lib.LANGS)
    parser.add_argument("--condition", choices=lib.CONDITIONS)
    parser.add_argument("--rep", type=int)
    args = parser.parse_args()

    if args.plan:
        todo = [e for e in plan_entries() if e[0] in args.assistants
                and not (lib.EXPERIMENT_ROOT / "runs" / lib.run_id_for(*e) / "eval.json").exists()]
        if args.limit:
            todo = todo[:args.limit]
        print(f"{len(todo)} pending runs", flush=True)
        for entry in todo:
            execute(*entry)
    else:
        if not all([args.assistant, args.lang, args.condition, args.rep]):
            parser.error("use --plan, or give --assistant --lang --condition --rep")
        execute(args.assistant, args.lang, args.condition, args.rep)


if __name__ == "__main__":
    main()
