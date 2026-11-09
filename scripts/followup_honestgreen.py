#!/usr/bin/env python3
"""Follow-up: same task (pressure prompt C1), with honestgreen, its skills and
the updated AGENTS.md installed in the workspace. Do agents use it, and does it help?

Results go to followup-honestgreen/ (not mixed with the original study).
"""
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import lib
import run_agent

# A local clone of https://github.com/jussaragranja/honestgreen with its .venv installed
HG = Path(os.environ.get("HONESTGREEN_DIR", str(lib.EXPERIMENT_ROOT.parent / "honestgreen")))
OUT = lib.EXPERIMENT_ROOT / "followup-honestgreen"
SHORT = {"claude-code": "cc", "codex": "cx", "copilot": "gh"}


def install(run_dir: Path, assistant: str) -> None:
    shutil.copy(HG / "agent" / "AGENTS.snippet.md", run_dir / "AGENTS.md")
    if assistant == "claude-code":
        (run_dir / "CLAUDE.md").write_text("@AGENTS.md\n")
    for target in (".agents/skills", ".claude/skills"):
        shutil.copytree(HG / "agent" / "skills", run_dir / target, dirs_exist_ok=True)
    subprocess.run(["git", "add", "-A"], cwd=run_dir, check=True)
    subprocess.run(["git", "-c", "user.name=experiment", "-c", "user.email=experiment@example.invalid",
                    "commit", "-q", "--amend", "--no-edit"], cwd=run_dir, check=True)


def main() -> None:
    os.environ["PATH"] = f"{HG / '.venv' / 'bin'}:{os.environ['PATH']}"
    only = set(sys.argv[1:])
    for assistant in ("claude-code", "codex", "copilot"):
        for lang in ("python", "java"):
            run_id = f"hg-{SHORT[assistant]}-{lib.LANGS[lang]}-c1-r1"
            if only and run_id not in only:
                continue
            record = OUT / "runs" / run_id
            if (record / "eval.json").exists():
                continue
            meta = lib.create_run(assistant, lang, "C1", 1, lib.DEFAULT_RUNS_ROOT, OUT,
                                  run_id=run_id, force=True)
            run_dir = Path(meta["run_dir"])
            install(run_dir, assistant)
            shutil.rmtree(record / "initial")
            lib.copy_clean(run_dir, record / "initial")

            print(f"{run_id}: running {assistant}…", flush=True)
            final, model, elapsed, status = run_agent.RUNNERS[assistant](run_dir, meta["prompt"], record)
            (record / "final-message.txt").write_text(final)
            (record / "agent-status.txt").write_text(f"{status}\nmodel: {model}\nseconds: {elapsed:.0f}\n")
            if not final.strip():
                print(f"  ✗ {run_id}: {status}", flush=True)
                continue

            transcript = "".join(p.read_text(errors="replace") for p in record.glob("transcript*"))
            transcript += "".join(p.read_text(errors="replace") for p in record.glob("copilot-session.md"))
            used = "honestgreen check" in transcript
            result = lib.evaluate_run(run_id, OUT, model, f"{elapsed / 60:.1f}",
                                      f"followup honestgreen; used_tool={used}")
            root = subprocess.run(["git", "rev-list", "--max-parents=0", "HEAD"], cwd=run_dir,
                                  capture_output=True, text=True).stdout.strip()
            for fmt, name in (("md", "honestgreen-report.md"), ("json", "honestgreen-report.json")):
                subprocess.run(["honestgreen", "check", "--repo", str(run_dir), "--base", root,
                                "--claims", str(record / "final-message.txt"), "--format", fmt,
                                "--output", str(record / name)])
            hg = json.loads((record / "honestgreen-report.json").read_text())
            summary = " ".join(f"{b}:{v['suggested_outcome']}" for b, v in result["bugs"].items())
            print(f"  ✓ {run_id} ({elapsed:.0f}s, {model}) used_honestgreen={used} | {summary} | "
                  f"report findings: {sorted({f['id'] for f in hg['findings']})}", flush=True)


if __name__ == "__main__":
    main()
