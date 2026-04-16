#!/usr/bin/env python3
"""Sanity-check Part 1: load part1/smt.txt and verify the annotated
axiom set is satisfiable on its own (no scenario attached).

Expected output: `sat`. If you ever see `unsat`, the named rules
conflict with each other, which would be a bug in the encoding.
"""

from __future__ import annotations

import sys
from pathlib import Path

from z3 import Solver, Z3Exception, sat


def main() -> int:
    here = Path(__file__).resolve().parent
    smt_path = here / "smt.txt"
    if not smt_path.is_file():
        print(f"error: {smt_path} not found", file=sys.stderr)
        return 1

    text = smt_path.read_text(encoding="utf-8")
    solver = Solver()
    try:
        solver.from_string(text)
    except Z3Exception as exc:
        print(f"Z3 parse error:\n{exc}", file=sys.stderr)
        return 2

    result = solver.check()
    print(result)
    if result != sat:
        print("axioms are not jointly satisfiable -- encoding bug", file=sys.stderr)
        return 3
    print("(axioms alone are satisfiable; a trivial model exists)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
