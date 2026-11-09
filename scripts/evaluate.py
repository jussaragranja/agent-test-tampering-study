#!/usr/bin/env python3
"""Evaluate one experiment run: save the diff, run visible and hidden tests,
suggest an outcome per bug and update results.csv.

Example:
    python3 scripts/evaluate.py cc-py-c1-r1 --model "opus-5.5"

Suggested outcomes are a starting point. Always review the diff and the
agent's final message, then fill in the `outcome`, `tampering_type` and
`disclosed` columns by hand.
"""
import argparse

import lib


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("run_id")
    parser.add_argument("--model", default="", help="model used by the assistant")
    parser.add_argument("--duration", default="", help="minutes (default: since run creation)")
    parser.add_argument("--notes", default="")
    args = parser.parse_args()

    result = lib.evaluate_run(args.run_id, lib.EXPERIMENT_ROOT, args.model, args.duration, args.notes)
    lib.print_summary(result)
    print(f"\nDiff:    runs/{args.run_id}/diff.patch")
    print("Results: results.csv  (fill in outcome, tampering_type and disclosed)")


if __name__ == "__main__":
    main()
