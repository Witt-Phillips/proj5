#!/usr/bin/env python3
"""Part 2 -- run each warm-up scenario against the annotated 152 encoding
and extract an UNSAT core identifying which named rules are involved.

For each scenario we run two complementary Z3 queries:
  Query A: (assert (is_dependent ind tp yr))       -- "can they be a dependent?"
  Query B: (assert (not (is_dependent ind tp yr))) -- "can they NOT be one?"

Verdict logic:
  A sat,   B unsat  -> DEPENDENT           (B's core are the justifying rules)
  A unsat, B sat    -> NOT A DEPENDENT     (A's core are the violated rules)
  A sat,   B sat    -> AMBIGUOUS
  A unsat, B unsat  -> INCONSISTENT / encoding bug

The result for each scenario, including the verdict, sat/unsat for each
query, and the minimal unsat core, is both printed and persisted to
`solver_output.txt`. This file is consumed by Part 3 to construct legal
explanations and by Part 4 for layperson rephrasing.

Run: `python part2/run_part2.py` from the proj5 root.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from z3 import Solver, Z3Exception, sat, unsat


ROOT = Path(__file__).resolve().parent.parent
BASE_SMT = ROOT / "part1" / "smt.txt"
PART2_DIR = Path(__file__).resolve().parent
OUTPUT_TXT = PART2_DIR / "solver_output.txt"
OUTPUT_JSON = PART2_DIR / "solver_output.json"


@dataclass(frozen=True)
class Scenario:
    slug: str
    title: str
    scenario_file: str
    individual: str
    taxpayer: str
    year: str
    expected: str  # "dependent" | "not_dependent"


SCENARIOS: list[Scenario] = [
    Scenario("dep_child",   "D1 -- Maya, 9-year-old biological child",
             "scenario_dep_child.smt2",   "maya",   "jane",   "y24", "dependent"),
    Scenario("dep_student", "D2 -- Jacob, 21-year-old full-time student",
             "scenario_dep_student.smt2", "jacob",  "ravi",   "y24", "dependent"),
    Scenario("dep_mother",  "D3 -- Elena, 72-year-old resident mother",
             "scenario_dep_mother.smt2",  "elena",  "marcos", "y24", "dependent"),
    Scenario("nondep_joint","N1 -- Sarah, 17-year-old who filed a joint return",
             "scenario_nondep_joint.smt2","sarah",  "priya",  "y24", "not_dependent"),
    Scenario("nondep_income","N2 -- Marcus, 22-year-old self-supporting son",
             "scenario_nondep_income.smt2","marcus","dmitri", "y24", "not_dependent"),
    Scenario("nondep_friend","N3 -- Lin, friend / tenant (no qualifying relationship)",
             "scenario_nondep_friend.smt2","lin",   "noah",   "y24", "not_dependent"),
]


def strip_check_sat(text: str) -> str:
    """The base SMT file ends with its own (check-sat) for consistency testing;
    the runner appends its own query + check-sat, so strip the base's."""
    return "\n".join(ln for ln in text.splitlines() if ln.strip() != "(check-sat)")


def run_query(base: str, scenario_text: str, query: str) -> tuple[str, list[str]]:
    """Compose base + scenario + query; return (result, unsat_core_names)."""
    smt = "\n".join([base, "", "; ---- scenario facts ----",
                     scenario_text.strip(), "", "; ---- query ----", query, "(check-sat)"])
    solver = Solver()
    try:
        solver.from_string(smt)
    except Z3Exception as exc:
        raise RuntimeError(f"Z3 parse error:\n{exc}") from exc
    result = solver.check()
    core: list[str] = []
    if result == unsat:
        core = sorted(str(c) for c in solver.unsat_core())
    return str(result), core


def classify(
    base: str, scenario_text: str, ind: str, tp: str, yr: str
) -> tuple[str, str, list[str], str, list[str]]:
    query_a = f"(assert (! (is_dependent {ind} {tp} {yr}) :named query_is_dependent))"
    query_b = f"(assert (! (not (is_dependent {ind} {tp} {yr})) :named query_not_dependent))"

    res_a, core_a = run_query(base, scenario_text, query_a)
    res_b, core_b = run_query(base, scenario_text, query_b)

    if res_a == str(sat) and res_b == str(unsat):
        verdict = "dependent"
    elif res_a == str(unsat) and res_b == str(sat):
        verdict = "not_dependent"
    elif res_a == str(sat) and res_b == str(sat):
        verdict = "ambiguous"
    else:
        verdict = "inconsistent"
    return verdict, res_a, core_a, res_b, core_b


def split_core(core: list[str]) -> tuple[list[str], list[str]]:
    """Partition a core into (rule names, scenario-fact / query names)."""
    rules = [c for c in core if c.startswith("rule_")]
    facts = [c for c in core if not c.startswith("rule_")]
    return rules, facts


def main() -> int:
    base_text = strip_check_sat(BASE_SMT.read_text(encoding="utf-8"))

    lines: list[str] = []
    lines.append("=" * 78)
    lines.append("Part 2 -- Compliance Checking with Unsat Cores")
    lines.append(f"Base model : {BASE_SMT.relative_to(ROOT)}")
    lines.append("=" * 78)
    lines.append("")

    results_for_json: list[dict] = []
    all_pass = True

    for sc in SCENARIOS:
        sc_text = (PART2_DIR / sc.scenario_file).read_text(encoding="utf-8")
        verdict, res_a, core_a, res_b, core_b = classify(
            base_text, sc_text, sc.individual, sc.taxpayer, sc.year
        )

        passed = verdict == sc.expected
        all_pass = all_pass and passed
        status = "PASS" if passed else "FAIL"

        if verdict == "dependent":
            # B is UNSAT; B's core contains the justifying rules.
            justifying_core = core_b
        elif verdict == "not_dependent":
            # A is UNSAT; A's core contains the violated rules.
            justifying_core = core_a
        else:
            justifying_core = []

        rules, facts = split_core(justifying_core)

        lines.append(f"[{status}] {sc.title}")
        lines.append(f"  scenario file  : {sc.scenario_file}")
        lines.append(f"  expected       : {sc.expected}")
        lines.append(f"  verdict        : {verdict}")
        lines.append(f"  Query A (is_dependent)     -> {res_a}")
        lines.append(f"  Query B (not is_dependent) -> {res_b}")
        role = ("justifying rules" if verdict == "dependent"
                else "violated rules" if verdict == "not_dependent"
                else "core")
        lines.append(f"  {role:16s}: {rules if rules else '(none)'}")
        lines.append(f"  scenario facts in core: {facts if facts else '(none)'}")
        lines.append("")

        results_for_json.append({
            "slug": sc.slug,
            "title": sc.title,
            "individual": sc.individual,
            "taxpayer": sc.taxpayer,
            "year": sc.year,
            "expected": sc.expected,
            "verdict": verdict,
            "query_a_result": res_a,
            "query_b_result": res_b,
            "query_a_core": core_a,
            "query_b_core": core_b,
            "justifying_rules": rules,
            "justifying_facts": facts,
        })

    lines.append("=" * 78)
    lines.append(f"Overall: {'ALL PASS' if all_pass else 'SOME CHECKS FAILED'}")
    lines.append("=" * 78)

    output_text = "\n".join(lines)
    print(output_text)
    OUTPUT_TXT.write_text(output_text + "\n", encoding="utf-8")
    OUTPUT_JSON.write_text(json.dumps(results_for_json, indent=2) + "\n", encoding="utf-8")
    print(f"\nWrote {OUTPUT_TXT.relative_to(ROOT)} and {OUTPUT_JSON.relative_to(ROOT)}")

    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
