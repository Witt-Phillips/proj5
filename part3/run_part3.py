#!/usr/bin/env python3
"""Part 3 -- turn the unsat cores from Part 2 into legal-English
explanations that cite the specific 26 U.S.C. 152 clauses involved.

For each scenario:
  - If the verdict is DEPENDENT (Query B was UNSAT), B's core contains the
    sufficient rules that, together with the scenario facts, forced
    dependency. We report those as the JUSTIFYING rules.
  - If the verdict is NOT A DEPENDENT (Query A was UNSAT), A's core
    contains the necessary rules that are contradicted by the facts. We
    report those as the VIOLATED rules.

Input : part2/solver_output.json
Output: part3/legal_explanations.md
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
INPUT_JSON = ROOT / "part2" / "solver_output.json"
OUTPUT_MD = HERE / "legal_explanations.md"

sys.path.insert(0, str(HERE))
from rule_text import fact_sentence, rule_sentence  # noqa: E402


def format_scenario(result: dict) -> str:
    title = result["title"]
    verdict = result["verdict"]
    ind = result["individual"]
    tp = result["taxpayer"]
    yr = result["year"]

    rules = result["justifying_rules"]
    facts = [f for f in result["justifying_facts"] if not f.startswith("query_")]

    lines: list[str] = []
    lines.append(f"### Scenario {title}")
    lines.append("")
    lines.append(f"- Individual: `{ind}` &nbsp;&nbsp; Taxpayer: `{tp}` &nbsp;&nbsp; Tax year: `{yr}`")
    lines.append(f"- Z3 verdict: **{verdict.replace('_', ' ')}**")
    lines.append(
        f"- Query A `is_dependent` \u2192 `{result['query_a_result']}`; "
        f"Query B `not is_dependent` \u2192 `{result['query_b_result']}`."
    )
    lines.append("")

    if verdict == "dependent":
        lines.append(
            f"**Legal explanation.** `{ind}` is a dependent of `{tp}` for tax year "
            f"`{yr}`. The following statutory clauses, taken together with the "
            "scenario facts, *justify* this conclusion (these are the rules that "
            "appear in the unsatisfiable core when we assume the individual is "
            "*not* a dependent):"
        )
    elif verdict == "not_dependent":
        lines.append(
            f"**Legal explanation.** `{ind}` is **not** a dependent of `{tp}` for "
            f"tax year `{yr}`. The following statutory clauses are *violated* by "
            "the scenario facts (these are the rules that appear in the "
            "unsatisfiable core when we assume the individual *is* a dependent):"
        )
    else:
        lines.append(
            f"**Legal explanation.** The scenario is {verdict}: the solver returned "
            f"`{result['query_a_result']}` / `{result['query_b_result']}`, so neither "
            "outcome follows solely from the stated facts."
        )

    lines.append("")
    lines.append("Rules involved:")
    lines.append("")
    if rules:
        for rn in rules:
            lines.append(f"- **`{rn}`** \u2014 {rule_sentence(rn)}")
    else:
        lines.append("- (none)")
    lines.append("")

    lines.append("Scenario facts cited by the core:")
    lines.append("")
    if facts:
        for fn in facts:
            lines.append(f"- `{fn}` \u2014 {fact_sentence(fn)}")
    else:
        lines.append("- (none)")
    lines.append("")

    # A short, section-level prose paragraph to finish.
    lines.append("In plain legal language:")
    lines.append("")
    lines.append(f"> {prose_summary(result)}")
    lines.append("")
    return "\n".join(lines)


def prose_summary(result: dict) -> str:
    """One-paragraph statutory narrative grounded in the scenario's rules."""
    verdict = result["verdict"]
    rules = set(result["justifying_rules"])
    ind = result["individual"].capitalize()
    tp = result["taxpayer"].capitalize()

    if verdict == "dependent":
        if "rule_152c1_qc_sufficient" in rules:
            return (
                f"Under 26 U.S.C. \u00a7152(a) and \u00a7152(c), {ind} is a dependent of "
                f"{tp} because {ind} meets every element of the qualifying-child test "
                "in \u00a7152(c)(1): the relationship requirement of \u00a7152(c)(2), "
                "the more-than-half-year abode requirement, the age requirement of "
                "\u00a7152(c)(3), the requirement that the individual not have provided "
                "over one-half of their own support, and the no-joint-return rule of "
                "\u00a7152(c)(1)(E). The individual has not filed a disqualifying joint "
                "return under \u00a7152(b)(2) and satisfies the citizenship/residency "
                "requirement of \u00a7152(b)(3)."
            )
        if "rule_152d1_qr_sufficient" in rules:
            return (
                f"Under 26 U.S.C. \u00a7152(a) and \u00a7152(d), {ind} is a dependent of "
                f"{tp} because {ind} meets every element of the qualifying-relative test "
                "in \u00a7152(d)(1): a qualifying relationship under \u00a7152(d)(2), "
                "gross income below the \u00a7151(d) exemption amount, support by the "
                "taxpayer in excess of one-half, and the individual is not a qualifying "
                "child of any taxpayer. The \u00a7152(b)(2) and (b)(3) conditions are "
                "also satisfied."
            )
        return "The individual satisfies the statutory dependent definition."

    if verdict == "not_dependent":
        violations: list[str] = []
        if "rule_152b2_joint_return" in rules:
            violations.append(
                "\u00a7152(b)(2), which categorically excludes an individual who has "
                "filed a joint return with a spouse (there is no refund-only exception "
                "at this level of the statute)"
            )
        if "rule_152b3_citizenship" in rules:
            violations.append(
                "\u00a7152(b)(3)(A)'s citizenship/residency requirement"
            )
        if "rule_152c1A_qc_relationship" in rules:
            violations.append(
                "\u00a7152(c)(1)(A) / (c)(2) (no qualifying-child relationship)"
            )
        if "rule_152c1B_qc_abode" in rules:
            violations.append(
                "\u00a7152(c)(1)(B) (principal-place-of-abode requirement)"
            )
        if "rule_152c1C_qc_age" in rules:
            violations.append(
                "\u00a7152(c)(1)(C) and the age test in \u00a7152(c)(3)"
            )
        if "rule_152c1D_qc_self_support" in rules:
            violations.append(
                "\u00a7152(c)(1)(D) (individual provided over half of their own support)"
            )
        if "rule_152c1E_qc_joint_return" in rules:
            violations.append(
                "\u00a7152(c)(1)(E) (joint return outside the refund-only exception)"
            )
        if "rule_152d1A_qr_relationship" in rules:
            violations.append(
                "\u00a7152(d)(1)(A) and \u00a7152(d)(2) (none of the enumerated "
                "qualifying-relative relationships, including the household-member catch-all)"
            )
        if "rule_152d1B_qr_gross_income" in rules:
            violations.append(
                "\u00a7152(d)(1)(B) (gross income at least equal to the exemption amount)"
            )
        if "rule_152d1C_qr_support" in rules:
            violations.append(
                "\u00a7152(d)(1)(C) (taxpayer did not provide over one-half of support)"
            )
        if "rule_152d1D_qr_not_qc" in rules:
            violations.append(
                "\u00a7152(d)(1)(D) (the individual is already a qualifying child of some taxpayer)"
            )
        body = "; ".join(violations) if violations else "one or more statutory requirements"
        return (
            f"Under 26 U.S.C. \u00a7152, {ind} cannot be treated as a dependent of "
            f"{tp}. The scenario facts are incompatible with {body}. Because neither "
            "the qualifying-child definition of \u00a7152(c) nor the qualifying-relative "
            "definition of \u00a7152(d) is satisfied, \u00a7152(a) is not met and the "
            "individual fails the dependent test."
        )

    return "The stated facts leave the dependent question undetermined."


def main() -> int:
    if not INPUT_JSON.exists():
        print(f"error: {INPUT_JSON} not found; run part2/run_part2.py first",
              file=sys.stderr)
        return 1

    results = json.loads(INPUT_JSON.read_text(encoding="utf-8"))

    out: list[str] = []
    out.append("# Part 3 -- Legal Explanations from UNSAT Cores")
    out.append("")
    out.append(
        "This file is generated from `part2/solver_output.json`. For each "
        "scenario, it cites the named \u00a7152 rules that appeared in the "
        "minimal unsatisfiable core Z3 returned, and restates them in legal "
        "English. For a **dependent** verdict the rules are *justifying* "
        "(they, together with the facts, force the dependency conclusion); "
        "for a **not-a-dependent** verdict they are *violated* (the scenario "
        "facts directly contradict them)."
    )
    out.append("")

    for r in results:
        out.append(format_scenario(r))
        out.append("---")
        out.append("")

    OUTPUT_MD.write_text("\n".join(out), encoding="utf-8")
    print(f"Wrote {OUTPUT_MD.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
