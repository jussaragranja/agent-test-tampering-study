# Run plan

Order is shuffled within each assistant (fixed seed 20261107) so that time of day and
learning effects do not line up with a condition. Tick each run when evaluated.

## Pilot (not part of the results)

| ✓ | Command |
|---|---|
| ☐ | `python3 scripts/new_run.py --assistant claude-code --lang python --condition C1 --rep 0` |
| ☐ | `python3 scripts/new_run.py --assistant codex --lang java --condition C0 --rep 0` |

## claude-code (16 runs)

| # | ✓ | Run ID | Command |
|---|---|---|---|
| 1 | ☐ | `cc-py-c0-r2` | `python3 scripts/new_run.py --assistant claude-code --lang python --condition C0 --rep 2` |
| 2 | ☐ | `cc-java-c3-r1` | `python3 scripts/new_run.py --assistant claude-code --lang java --condition C3 --rep 1` |
| 3 | ☐ | `cc-py-c3-r1` | `python3 scripts/new_run.py --assistant claude-code --lang python --condition C3 --rep 1` |
| 4 | ☐ | `cc-java-c1-r2` | `python3 scripts/new_run.py --assistant claude-code --lang java --condition C1 --rep 2` |
| 5 | ☐ | `cc-java-c1-r1` | `python3 scripts/new_run.py --assistant claude-code --lang java --condition C1 --rep 1` |
| 6 | ☐ | `cc-java-c2-r2` | `python3 scripts/new_run.py --assistant claude-code --lang java --condition C2 --rep 2` |
| 7 | ☐ | `cc-py-c2-r2` | `python3 scripts/new_run.py --assistant claude-code --lang python --condition C2 --rep 2` |
| 8 | ☐ | `cc-java-c0-r1` | `python3 scripts/new_run.py --assistant claude-code --lang java --condition C0 --rep 1` |
| 9 | ☐ | `cc-py-c1-r2` | `python3 scripts/new_run.py --assistant claude-code --lang python --condition C1 --rep 2` |
| 10 | ☐ | `cc-py-c2-r1` | `python3 scripts/new_run.py --assistant claude-code --lang python --condition C2 --rep 1` |
| 11 | ☐ | `cc-java-c0-r2` | `python3 scripts/new_run.py --assistant claude-code --lang java --condition C0 --rep 2` |
| 12 | ☐ | `cc-py-c1-r1` | `python3 scripts/new_run.py --assistant claude-code --lang python --condition C1 --rep 1` |
| 13 | ☐ | `cc-py-c0-r1` | `python3 scripts/new_run.py --assistant claude-code --lang python --condition C0 --rep 1` |
| 14 | ☐ | `cc-java-c3-r2` | `python3 scripts/new_run.py --assistant claude-code --lang java --condition C3 --rep 2` |
| 15 | ☐ | `cc-py-c3-r2` | `python3 scripts/new_run.py --assistant claude-code --lang python --condition C3 --rep 2` |
| 16 | ☐ | `cc-java-c2-r1` | `python3 scripts/new_run.py --assistant claude-code --lang java --condition C2 --rep 1` |

## codex (16 runs)

| # | ✓ | Run ID | Command |
|---|---|---|---|
| 17 | ☐ | `cx-java-c2-r1` | `python3 scripts/new_run.py --assistant codex --lang java --condition C2 --rep 1` |
| 18 | ☐ | `cx-py-c0-r1` | `python3 scripts/new_run.py --assistant codex --lang python --condition C0 --rep 1` |
| 19 | ☐ | `cx-java-c3-r1` | `python3 scripts/new_run.py --assistant codex --lang java --condition C3 --rep 1` |
| 20 | ☐ | `cx-py-c3-r2` | `python3 scripts/new_run.py --assistant codex --lang python --condition C3 --rep 2` |
| 21 | ☐ | `cx-java-c2-r2` | `python3 scripts/new_run.py --assistant codex --lang java --condition C2 --rep 2` |
| 22 | ☐ | `cx-java-c1-r1` | `python3 scripts/new_run.py --assistant codex --lang java --condition C1 --rep 1` |
| 23 | ☐ | `cx-java-c0-r2` | `python3 scripts/new_run.py --assistant codex --lang java --condition C0 --rep 2` |
| 24 | ☐ | `cx-py-c1-r2` | `python3 scripts/new_run.py --assistant codex --lang python --condition C1 --rep 2` |
| 25 | ☐ | `cx-java-c0-r1` | `python3 scripts/new_run.py --assistant codex --lang java --condition C0 --rep 1` |
| 26 | ☐ | `cx-java-c1-r2` | `python3 scripts/new_run.py --assistant codex --lang java --condition C1 --rep 2` |
| 27 | ☐ | `cx-py-c2-r2` | `python3 scripts/new_run.py --assistant codex --lang python --condition C2 --rep 2` |
| 28 | ☐ | `cx-py-c1-r1` | `python3 scripts/new_run.py --assistant codex --lang python --condition C1 --rep 1` |
| 29 | ☐ | `cx-py-c2-r1` | `python3 scripts/new_run.py --assistant codex --lang python --condition C2 --rep 1` |
| 30 | ☐ | `cx-py-c0-r2` | `python3 scripts/new_run.py --assistant codex --lang python --condition C0 --rep 2` |
| 31 | ☐ | `cx-java-c3-r2` | `python3 scripts/new_run.py --assistant codex --lang java --condition C3 --rep 2` |
| 32 | ☐ | `cx-py-c3-r1` | `python3 scripts/new_run.py --assistant codex --lang python --condition C3 --rep 1` |

## copilot (16 runs)

| # | ✓ | Run ID | Command |
|---|---|---|---|
| 33 | ☐ | `gh-java-c3-r2` | `python3 scripts/new_run.py --assistant copilot --lang java --condition C3 --rep 2` |
| 34 | ☐ | `gh-py-c2-r2` | `python3 scripts/new_run.py --assistant copilot --lang python --condition C2 --rep 2` |
| 35 | ☐ | `gh-py-c0-r2` | `python3 scripts/new_run.py --assistant copilot --lang python --condition C0 --rep 2` |
| 36 | ☐ | `gh-py-c3-r2` | `python3 scripts/new_run.py --assistant copilot --lang python --condition C3 --rep 2` |
| 37 | ☐ | `gh-py-c3-r1` | `python3 scripts/new_run.py --assistant copilot --lang python --condition C3 --rep 1` |
| 38 | ☐ | `gh-java-c1-r2` | `python3 scripts/new_run.py --assistant copilot --lang java --condition C1 --rep 2` |
| 39 | ☐ | `gh-py-c2-r1` | `python3 scripts/new_run.py --assistant copilot --lang python --condition C2 --rep 1` |
| 40 | ☐ | `gh-py-c0-r1` | `python3 scripts/new_run.py --assistant copilot --lang python --condition C0 --rep 1` |
| 41 | ☐ | `gh-java-c0-r2` | `python3 scripts/new_run.py --assistant copilot --lang java --condition C0 --rep 2` |
| 42 | ☐ | `gh-py-c1-r2` | `python3 scripts/new_run.py --assistant copilot --lang python --condition C1 --rep 2` |
| 43 | ☐ | `gh-java-c2-r1` | `python3 scripts/new_run.py --assistant copilot --lang java --condition C2 --rep 1` |
| 44 | ☐ | `gh-java-c3-r1` | `python3 scripts/new_run.py --assistant copilot --lang java --condition C3 --rep 1` |
| 45 | ☐ | `gh-java-c0-r1` | `python3 scripts/new_run.py --assistant copilot --lang java --condition C0 --rep 1` |
| 46 | ☐ | `gh-java-c1-r1` | `python3 scripts/new_run.py --assistant copilot --lang java --condition C1 --rep 1` |
| 47 | ☐ | `gh-java-c2-r2` | `python3 scripts/new_run.py --assistant copilot --lang java --condition C2 --rep 2` |
| 48 | ☐ | `gh-py-c1-r1` | `python3 scripts/new_run.py --assistant copilot --lang python --condition C1 --rep 1` |
