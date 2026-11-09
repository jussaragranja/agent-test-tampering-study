#!/usr/bin/env python3
"""Create a fresh, isolated workspace for one experiment run.

Example:
    python3 scripts/new_run.py --assistant claude-code --lang python --condition C1 --rep 1
"""
import argparse
import shutil
import subprocess
from pathlib import Path

import lib

START_COMMANDS = {
    "claude-code": 'claude "{prompt}"',
    "codex": 'codex "{prompt}"',
    "copilot": "code .   # open Copilot Chat in Agent mode and paste the prompt",
}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--assistant", required=True, choices=lib.ASSISTANTS)
    parser.add_argument("--lang", required=True, choices=lib.LANGS)
    parser.add_argument("--condition", required=True, choices=lib.CONDITIONS)
    parser.add_argument("--rep", required=True, type=int)
    parser.add_argument("--runs-root", type=Path, default=lib.DEFAULT_RUNS_ROOT,
                        help="where agent workspaces are created (must be outside this repo)")
    parser.add_argument("--force", action="store_true", help="recreate the run if it exists")
    args = parser.parse_args()

    runs_root = args.runs_root.expanduser().resolve()
    if lib.EXPERIMENT_ROOT in runs_root.parents or runs_root == lib.EXPERIMENT_ROOT:
        raise SystemExit("--runs-root must be outside the experiment folder (agents must not see hidden tests).")

    meta = lib.create_run(args.assistant, args.lang, args.condition, args.rep,
                          runs_root, lib.EXPERIMENT_ROOT, force=args.force)

    copied = False
    if shutil.which("pbcopy"):
        subprocess.run(["pbcopy"], input=meta["prompt"], text=True)
        copied = True

    print(f"""
Run created: {meta['run_id']}
Workspace:   {meta['run_dir']}
Tool:        {meta['tool_version'] or '(record the version manually)'}

Prompt ({'copied to clipboard' if copied else 'copy exactly'}):
  {meta['prompt']}

Start the agent in a NEW session:
  cd {meta['run_dir']}
  {START_COMMANDS[args.assistant].format(prompt=meta['prompt'])}

Protocol:
  - Do not give any guidance. Approve every permission request.
  - If the agent asks a question, answer exactly: "{(lib.PROMPTS_DIR / 'FOLLOW-UP.txt').read_text().strip()}"
  - Stop after 15 minutes if it has not finished.
  - Save the agent's final message to: runs/{meta['run_id']}/final-message.txt

When the agent is done:
  python3 scripts/evaluate.py {meta['run_id']} --model "<model shown in the tool>"
""")


if __name__ == "__main__":
    main()
