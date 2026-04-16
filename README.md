# Project 5 -- "Law, Logic and LLMs"

Annotated SMT formalization of 26 U.S.C. 152 (dependent definition), compliance checking of six LLM-generated scenarios via unsatisfiable-core extraction, and legal + layperson explanations derived from those cores.

This directory is **standalone** -- it contains everything needed to run the project end-to-end, with no dependency on `../proj4`. The carried-over source is:

- `usc.txt` -- copied verbatim from `../proj4/usc.txt` (reference text of 26 U.S.C. 152).
- `requirements.txt` -- copied verbatim from `../proj4/part1/requirements.txt`.
- `part1/smt.txt` -- built from `../proj4/part1/smt.txt`: the uninterpreted sorts, primitive predicates, and helper `define-fun`s were kept; the three top-level definitions (`is_qualifying_child`, `is_qualifying_relative`, `is_dependent`) were refactored into uninterpreted predicates characterized by a set of `:named` axioms so that Z3's `(get-unsat-core)` can surface individual statutory clauses.

## Layout

```
proj5/
  README.md                 -- this file
  requirements.txt          -- Python deps (z3-solver)
  usc.txt                   -- statutory text for reference
  warmup/
    scenarios.md            -- the six plain-English scenarios
  part1/
    smt.txt                 -- annotated SMT encoding of 26 USC 152
    run_z3.py               -- sanity-check: axioms alone are sat
  part2/
    scenario_*.smt2         -- six SMT-LIB fact files (one per scenario)
    run_part2.py            -- solve + extract unsat cores
    solver_output.txt       -- human-readable results
    solver_output.json      -- machine-readable results (consumed by Part 3)
  part3/
    rule_text.py            -- rule-name / fact-name -> English sentence
    run_part3.py            -- core -> legal explanation
    legal_explanations.md   -- generated legal explanations for all six scenarios
  part4/
    layperson_explanations.md  -- LLM-rephrased plain-English explanations
    llm_transcript.md          -- prompts used
```

## How to run

```bash
pip install -r requirements.txt

python part1/run_z3.py         # expect: sat
python part2/run_part2.py      # expect: ALL PASS; writes solver_output.{txt,json}
python part3/run_part3.py      # writes legal_explanations.md
```

Part 4 is static markdown (authored by the LLM and committed as-is).

## Expected results

| scenario | slug | individual | expected | drives core |
|---|---|---|---|---|
| D1 | `dep_child`    | Maya  (9)  | dependent     | `rule_152c1_qc_sufficient`, `rule_152a_dependent_sufficient` |
| D2 | `dep_student`  | Jacob (21) | dependent     | `rule_152c1_qc_sufficient`, `rule_152a_dependent_sufficient` |
| D3 | `dep_mother`   | Elena (72) | dependent     | `rule_152d1_qr_sufficient`, `rule_152a_dependent_sufficient` |
| N1 | `nondep_joint` | Sarah (17) | not dependent | `rule_152b2_joint_return` |
| N2 | `nondep_income`| Marcus (22)| not dependent | `rule_152c1C_qc_age`, `rule_152d1C_qr_support`, `rule_152a_dependent_is_qc_or_qr` |
| N3 | `nondep_friend`| Lin (34)   | not dependent | `rule_152c1A_qc_relationship`, `rule_152d1A_qr_relationship`, `rule_152a_dependent_is_qc_or_qr` |

## Grading checklist

- [x] Annotated SMT file with `(set-option :produce-unsat-cores true)` and `(! ... :named ...)` labels for each statutory rule: [`part1/smt.txt`](part1/smt.txt).
- [x] Six plain-English scenarios (3 compliant, 3 non-compliant): [`warmup/scenarios.md`](warmup/scenarios.md).
- [x] SMT-LIB versions of the scenarios: [`part2/scenario_*.smt2`](part2/).
- [x] Code used: [`part1/run_z3.py`](part1/run_z3.py), [`part2/run_part2.py`](part2/run_part2.py), [`part3/run_part3.py`](part3/run_part3.py), [`part3/rule_text.py`](part3/rule_text.py).
- [x] SMT solver results (sat / unsat) for each scenario: [`part2/solver_output.txt`](part2/solver_output.txt).
- [x] Extracted cores and named rules involved: [`part2/solver_output.txt`](part2/solver_output.txt) / [`part2/solver_output.json`](part2/solver_output.json).
- [x] Legal explanations: [`part3/legal_explanations.md`](part3/legal_explanations.md).
- [x] Layperson rephrasings: [`part4/layperson_explanations.md`](part4/layperson_explanations.md) (with [`part4/llm_transcript.md`](part4/llm_transcript.md) recording the prompts).
