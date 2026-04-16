# Part 3 -- Legal Explanations from UNSAT Cores

This file is generated from `part2/solver_output.json`. For each scenario, it cites the named §152 rules that appeared in the minimal unsatisfiable core Z3 returned, and restates them in legal English. For a **dependent** verdict the rules are *justifying* (they, together with the facts, force the dependency conclusion); for a **not-a-dependent** verdict they are *violated* (the scenario facts directly contradict them).

### Scenario D1 -- Maya, 9-year-old biological child

- Individual: `maya` &nbsp;&nbsp; Taxpayer: `jane` &nbsp;&nbsp; Tax year: `y24`
- Z3 verdict: **dependent**
- Query A `is_dependent` → `sat`; Query B `not is_dependent` → `unsat`.

**Legal explanation.** `maya` is a dependent of `jane` for tax year `y24`. The following statutory clauses, taken together with the scenario facts, *justify* this conclusion (these are the rules that appear in the unsatisfiable core when we assume the individual is *not* a dependent):

Rules involved:

- **`rule_152a_dependent_sufficient`** — 26 U.S.C. §152(a)+(b) – An individual who is a qualifying child or qualifying relative of the taxpayer, who has not filed a disqualifying joint return, and who satisfies the citizenship/residency requirement, is a dependent.
- **`rule_152c1_qc_sufficient`** — 26 U.S.C. §152(c)(1) – An individual who satisfies all of the relationship, abode, age, self-support, and joint-return tests (and whose relationship does not violate local law under §152(f)(3)) is a qualifying child.

Scenario facts cited by the core:

- `fact_d1_abode` — Maya shares Jane's principal place of abode for more than half the year.
- `fact_d1_age_9` — Maya is 9 years old at year end (under 19).
- `fact_d1_citizen` — Maya is a U.S. citizen.
- `fact_d1_is_child` — Maya is Jane's biological daughter (a child per §152(c)(2)(A)).
- `fact_d1_local_law_ok` — The relationship does not violate local law.
- `fact_d1_no_joint_return` — Maya did not file a joint return.
- `fact_d1_no_self_support` — Maya did not provide over half of her own support.
- `fact_d1_younger` — Maya is younger than Jane.

In plain legal language:

> Under 26 U.S.C. §152(a) and §152(c), Maya is a dependent of Jane because Maya meets every element of the qualifying-child test in §152(c)(1): the relationship requirement of §152(c)(2), the more-than-half-year abode requirement, the age requirement of §152(c)(3), the requirement that the individual not have provided over one-half of their own support, and the no-joint-return rule of §152(c)(1)(E). The individual has not filed a disqualifying joint return under §152(b)(2) and satisfies the citizenship/residency requirement of §152(b)(3).

---

### Scenario D2 -- Jacob, 21-year-old full-time student

- Individual: `jacob` &nbsp;&nbsp; Taxpayer: `ravi` &nbsp;&nbsp; Tax year: `y24`
- Z3 verdict: **dependent**
- Query A `is_dependent` → `sat`; Query B `not is_dependent` → `unsat`.

**Legal explanation.** `jacob` is a dependent of `ravi` for tax year `y24`. The following statutory clauses, taken together with the scenario facts, *justify* this conclusion (these are the rules that appear in the unsatisfiable core when we assume the individual is *not* a dependent):

Rules involved:

- **`rule_152a_dependent_sufficient`** — 26 U.S.C. §152(a)+(b) – An individual who is a qualifying child or qualifying relative of the taxpayer, who has not filed a disqualifying joint return, and who satisfies the citizenship/residency requirement, is a dependent.
- **`rule_152c1_qc_sufficient`** — 26 U.S.C. §152(c)(1) – An individual who satisfies all of the relationship, abode, age, self-support, and joint-return tests (and whose relationship does not violate local law under §152(f)(3)) is a qualifying child.

Scenario facts cited by the core:

- `fact_d2_abode` — Jacob's principal place of abode is Ravi's home for more than half the year.
- `fact_d2_age_21` — Jacob is 21 years old at year end.
- `fact_d2_citizen` — Jacob is a U.S. citizen.
- `fact_d2_is_child` — Jacob is Ravi's biological son (a child per §152(c)(2)(A)).
- `fact_d2_is_student` — Jacob is a full-time student (§152(f)(2)), allowing the under-24 age branch.
- `fact_d2_local_law_ok` — The relationship does not violate local law.
- `fact_d2_no_joint_return` — Jacob did not file a joint return.
- `fact_d2_no_self_support` — Jacob did not provide over half of his own support.
- `fact_d2_younger` — Jacob is younger than Ravi.

In plain legal language:

> Under 26 U.S.C. §152(a) and §152(c), Jacob is a dependent of Ravi because Jacob meets every element of the qualifying-child test in §152(c)(1): the relationship requirement of §152(c)(2), the more-than-half-year abode requirement, the age requirement of §152(c)(3), the requirement that the individual not have provided over one-half of their own support, and the no-joint-return rule of §152(c)(1)(E). The individual has not filed a disqualifying joint return under §152(b)(2) and satisfies the citizenship/residency requirement of §152(b)(3).

---

### Scenario D3 -- Elena, 72-year-old resident mother

- Individual: `elena` &nbsp;&nbsp; Taxpayer: `marcos` &nbsp;&nbsp; Tax year: `y24`
- Z3 verdict: **dependent**
- Query A `is_dependent` → `sat`; Query B `not is_dependent` → `unsat`.

**Legal explanation.** `elena` is a dependent of `marcos` for tax year `y24`. The following statutory clauses, taken together with the scenario facts, *justify* this conclusion (these are the rules that appear in the unsatisfiable core when we assume the individual is *not* a dependent):

Rules involved:

- **`rule_152a_dependent_sufficient`** — 26 U.S.C. §152(a)+(b) – An individual who is a qualifying child or qualifying relative of the taxpayer, who has not filed a disqualifying joint return, and who satisfies the citizenship/residency requirement, is a dependent.
- **`rule_152d1_qr_sufficient`** — 26 U.S.C. §152(d)(1) – An individual who satisfies all of the relationship, gross-income, support, and not-a-qualifying-child tests is a qualifying relative.

Scenario facts cited by the core:

- `fact_d3_exemption_5050` — The exemption amount for the tax year is $5,050.
- `fact_d3_gross_income_3000` — Elena's gross income for the year is $3,000.
- `fact_d3_is_mother` — Elena is Marcos's biological mother (§152(d)(2)(C)).
- `fact_d3_no_joint_return` — Elena did not file a joint return.
- `fact_d3_not_disabled` — Elena is not permanently and totally disabled (so the §152(d)(4) sheltered-workshop adjustment does not apply).
- `fact_d3_not_qc_of_any` — Elena is not a qualifying child of any taxpayer.
- `fact_d3_support` — Marcos provides over one-half of Elena's support.
- `fact_d3_us_resident` — Elena is a U.S. resident (lawful permanent resident), satisfying §152(b)(3)(A).

In plain legal language:

> Under 26 U.S.C. §152(a) and §152(d), Elena is a dependent of Marcos because Elena meets every element of the qualifying-relative test in §152(d)(1): a qualifying relationship under §152(d)(2), gross income below the §151(d) exemption amount, support by the taxpayer in excess of one-half, and the individual is not a qualifying child of any taxpayer. The §152(b)(2) and (b)(3) conditions are also satisfied.

---

### Scenario N1 -- Sarah, 17-year-old who filed a joint return

- Individual: `sarah` &nbsp;&nbsp; Taxpayer: `priya` &nbsp;&nbsp; Tax year: `y24`
- Z3 verdict: **not dependent**
- Query A `is_dependent` → `unsat`; Query B `not is_dependent` → `sat`.

**Legal explanation.** `sarah` is **not** a dependent of `priya` for tax year `y24`. The following statutory clauses are *violated* by the scenario facts (these are the rules that appear in the unsatisfiable core when we assume the individual *is* a dependent):

Rules involved:

- **`rule_152b2_joint_return`** — 26 U.S.C. §152(b)(2) – An individual is not a dependent if such individual has filed a joint return with the individual's spouse for the taxable year beginning in the calendar year in which the taxpayer's taxable year begins. (Unlike §152(c)(1)(E), this subsection has no refund-only exception.)

Scenario facts cited by the core:

- `fact_n1_filed_joint_return` — Sarah filed a joint return with her spouse.

In plain legal language:

> Under 26 U.S.C. §152, Sarah cannot be treated as a dependent of Priya. The scenario facts are incompatible with §152(b)(2), which categorically excludes an individual who has filed a joint return with a spouse (there is no refund-only exception at this level of the statute). Because neither the qualifying-child definition of §152(c) nor the qualifying-relative definition of §152(d) is satisfied, §152(a) is not met and the individual fails the dependent test.

---

### Scenario N2 -- Marcus, 22-year-old self-supporting son

- Individual: `marcus` &nbsp;&nbsp; Taxpayer: `dmitri` &nbsp;&nbsp; Tax year: `y24`
- Z3 verdict: **not dependent**
- Query A `is_dependent` → `unsat`; Query B `not is_dependent` → `sat`.

**Legal explanation.** `marcus` is **not** a dependent of `dmitri` for tax year `y24`. The following statutory clauses are *violated* by the scenario facts (these are the rules that appear in the unsatisfiable core when we assume the individual *is* a dependent):

Rules involved:

- **`rule_152a_dependent_is_qc_or_qr`** — 26 U.S.C. §152(a) – A dependent must be either a qualifying child (under §152(c)) or a qualifying relative (under §152(d)).
- **`rule_152c1C_qc_age`** — 26 U.S.C. §152(c)(1)(C), (3) – A qualifying child must be younger than the taxpayer and either under age 19 at year-end, or under age 24 and a full-time student; a permanently and totally disabled individual is treated as meeting the age test.
- **`rule_152d1C_qr_support`** — 26 U.S.C. §152(d)(1)(C) – The taxpayer must provide over one-half of the individual's support for the calendar year (or qualify under the §152(d)(3) multiple-support agreement).

Scenario facts cited by the core:

- `fact_n2_age_22` — Marcus is 22 years old at year end (over 19).
- `fact_n2_no_multi_support` — No §152(d)(3) multiple-support agreement applies.
- `fact_n2_not_disabled` — Marcus is not permanently and totally disabled (§152(c)(3)(B) branch closed).
- `fact_n2_not_student` — Marcus is not a student (§152(f)(2) branch closed).
- `fact_n2_support_fail` — Dmitri did not provide over one-half of Marcus's support.

In plain legal language:

> Under 26 U.S.C. §152, Marcus cannot be treated as a dependent of Dmitri. The scenario facts are incompatible with §152(c)(1)(C) and the age test in §152(c)(3); §152(d)(1)(C) (taxpayer did not provide over one-half of support). Because neither the qualifying-child definition of §152(c) nor the qualifying-relative definition of §152(d) is satisfied, §152(a) is not met and the individual fails the dependent test.

---

### Scenario N3 -- Lin, friend / tenant (no qualifying relationship)

- Individual: `lin` &nbsp;&nbsp; Taxpayer: `noah` &nbsp;&nbsp; Tax year: `y24`
- Z3 verdict: **not dependent**
- Query A `is_dependent` → `unsat`; Query B `not is_dependent` → `sat`.

**Legal explanation.** `lin` is **not** a dependent of `noah` for tax year `y24`. The following statutory clauses are *violated* by the scenario facts (these are the rules that appear in the unsatisfiable core when we assume the individual *is* a dependent):

Rules involved:

- **`rule_152a_dependent_is_qc_or_qr`** — 26 U.S.C. §152(a) – A dependent must be either a qualifying child (under §152(c)) or a qualifying relative (under §152(d)).
- **`rule_152c1A_qc_relationship`** — 26 U.S.C. §152(c)(1)(A) – To be a qualifying child, the individual must bear one of the relationships to the taxpayer described in §152(c)(2) (child or descendant of a child, or sibling or descendant of a sibling).
- **`rule_152d1A_qr_relationship`** — 26 U.S.C. §152(d)(1)(A), (2) – A qualifying relative must bear one of the enumerated relationships to the taxpayer (child or descendant, sibling, parent or ancestor, step-parent, niece/nephew, aunt/uncle, in-law) or, under §152(d)(2)(H), be a member of the taxpayer's household for the taxable year.

Scenario facts cited by the core:

- `fact_n3_not_auntuncle` — Lin is not an aunt or uncle of Noah.
- `fact_n3_not_child` — Lin is not a child or descendant of Noah.
- `fact_n3_not_household_member` — Lin is not a member of Noah's household (she is a paying tenant).
- `fact_n3_not_inlaw` — Lin is not an in-law of Noah.
- `fact_n3_not_niecenephew` — Lin is not a niece or nephew of Noah.
- `fact_n3_not_parent` — Lin is not a parent or ancestor of Noah.
- `fact_n3_not_sibling` — Lin is not a sibling (or step-sibling) of Noah.
- `fact_n3_not_sibling_desc` — Lin is not a sibling or sibling-descendant of Noah.
- `fact_n3_not_stepparent` — Lin is not a step-parent of Noah.

In plain legal language:

> Under 26 U.S.C. §152, Lin cannot be treated as a dependent of Noah. The scenario facts are incompatible with §152(c)(1)(A) / (c)(2) (no qualifying-child relationship); §152(d)(1)(A) and §152(d)(2) (none of the enumerated qualifying-relative relationships, including the household-member catch-all). Because neither the qualifying-child definition of §152(c) nor the qualifying-relative definition of §152(d) is satisfied, §152(a) is not met and the individual fails the dependent test.

---
