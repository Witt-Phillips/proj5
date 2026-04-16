"""Mapping from each `:named` rule in part1/smt.txt to the statutory
sentence it encodes (quoted or close-paraphrased from 26 U.S.C. 152).

Used by part3/run_part3.py to turn an UNSAT core into a readable legal
explanation. Also contains a mapping for scenario-fact labels so the
explanations can cite the specific facts that triggered each rule.
"""

from __future__ import annotations

RULE_TEXT: dict[str, str] = {
    # ----- 152(c) Qualifying Child -----
    "rule_152c1A_qc_relationship": (
        "26 U.S.C. \u00a7152(c)(1)(A) \u2013 To be a qualifying child, the individual "
        "must bear one of the relationships to the taxpayer described in \u00a7152(c)(2) "
        "(child or descendant of a child, or sibling or descendant of a sibling)."
    ),
    "rule_152c1B_qc_abode": (
        "26 U.S.C. \u00a7152(c)(1)(B) \u2013 A qualifying child must have the same "
        "principal place of abode as the taxpayer for more than one-half of the taxable year."
    ),
    "rule_152c1C_qc_age": (
        "26 U.S.C. \u00a7152(c)(1)(C), (3) \u2013 A qualifying child must be younger than "
        "the taxpayer and either under age 19 at year-end, or under age 24 and a full-time "
        "student; a permanently and totally disabled individual is treated as meeting the age test."
    ),
    "rule_152c1D_qc_self_support": (
        "26 U.S.C. \u00a7152(c)(1)(D) \u2013 A qualifying child must not have provided over "
        "one-half of such individual's own support for the calendar year."
    ),
    "rule_152c1E_qc_joint_return": (
        "26 U.S.C. \u00a7152(c)(1)(E) \u2013 A qualifying child must not have filed a joint "
        "return with a spouse, except a joint return filed solely to claim a refund of withholding."
    ),
    "rule_152c1_qc_sufficient": (
        "26 U.S.C. \u00a7152(c)(1) \u2013 An individual who satisfies all of the "
        "relationship, abode, age, self-support, and joint-return tests (and whose "
        "relationship does not violate local law under \u00a7152(f)(3)) is a qualifying child."
    ),
    "rule_152f3_local_law_qc": (
        "26 U.S.C. \u00a7152(f)(3) \u2013 An individual is not treated as a member of "
        "the taxpayer's household if the relationship between them is, at any time during "
        "the taxable year, in violation of local law."
    ),

    # ----- 152(d) Qualifying Relative -----
    "rule_152d1A_qr_relationship": (
        "26 U.S.C. \u00a7152(d)(1)(A), (2) \u2013 A qualifying relative must bear one of "
        "the enumerated relationships to the taxpayer (child or descendant, sibling, parent "
        "or ancestor, step-parent, niece/nephew, aunt/uncle, in-law) or, under \u00a7152(d)(2)(H), "
        "be a member of the taxpayer's household for the taxable year."
    ),
    "rule_152d1B_qr_gross_income": (
        "26 U.S.C. \u00a7152(d)(1)(B) \u2013 A qualifying relative's gross income for the "
        "calendar year must be less than the exemption amount as defined in \u00a7151(d)."
    ),
    "rule_152d1C_qr_support": (
        "26 U.S.C. \u00a7152(d)(1)(C) \u2013 The taxpayer must provide over one-half of the "
        "individual's support for the calendar year (or qualify under the \u00a7152(d)(3) "
        "multiple-support agreement)."
    ),
    "rule_152d1D_qr_not_qc": (
        "26 U.S.C. \u00a7152(d)(1)(D) \u2013 A qualifying relative must not be a qualifying "
        "child of the taxpayer or of any other taxpayer for any taxable year beginning in "
        "the calendar year in question."
    ),
    "rule_152d1_qr_sufficient": (
        "26 U.S.C. \u00a7152(d)(1) \u2013 An individual who satisfies all of the "
        "relationship, gross-income, support, and not-a-qualifying-child tests is a qualifying relative."
    ),

    # ----- 152(a), (b) Dependent -----
    "rule_152a_dependent_is_qc_or_qr": (
        "26 U.S.C. \u00a7152(a) \u2013 A dependent must be either a qualifying child "
        "(under \u00a7152(c)) or a qualifying relative (under \u00a7152(d))."
    ),
    "rule_152b2_joint_return": (
        "26 U.S.C. \u00a7152(b)(2) \u2013 An individual is not a dependent if such "
        "individual has filed a joint return with the individual's spouse for the taxable "
        "year beginning in the calendar year in which the taxpayer's taxable year begins. "
        "(Unlike \u00a7152(c)(1)(E), this subsection has no refund-only exception.)"
    ),
    "rule_152b3_citizenship": (
        "26 U.S.C. \u00a7152(b)(3)(A) \u2013 A dependent must be a citizen or national of "
        "the United States, or a resident of the United States or a contiguous country."
    ),
    "rule_152a_dependent_sufficient": (
        "26 U.S.C. \u00a7152(a)+(b) \u2013 An individual who is a qualifying child or "
        "qualifying relative of the taxpayer, who has not filed a disqualifying joint return, "
        "and who satisfies the citizenship/residency requirement, is a dependent."
    ),
    "rule_152b1_no_dep_of_dep": (
        "26 U.S.C. \u00a7152(b)(1) \u2013 An individual who is a dependent of another "
        "taxpayer is treated as having no dependents of their own for the same calendar year."
    ),
}


FACT_TEXT: dict[str, str] = {
    # ----- D1 Maya -----
    "fact_d1_distinct":         "Maya and Jane are different persons.",
    "fact_d1_citizen":          "Maya is a U.S. citizen.",
    "fact_d1_is_child":         "Maya is Jane's biological daughter (a child per \u00a7152(c)(2)(A)).",
    "fact_d1_abode":            "Maya shares Jane's principal place of abode for more than half the year.",
    "fact_d1_younger":          "Maya is younger than Jane.",
    "fact_d1_age_9":            "Maya is 9 years old at year end (under 19).",
    "fact_d1_no_self_support":  "Maya did not provide over half of her own support.",
    "fact_d1_no_joint_return":  "Maya did not file a joint return.",
    "fact_d1_local_law_ok":     "The relationship does not violate local law.",
    "fact_d1_not_disabled":     "Maya is not permanently and totally disabled.",

    # ----- D2 Jacob -----
    "fact_d2_distinct":         "Jacob and Ravi are different persons.",
    "fact_d2_citizen":          "Jacob is a U.S. citizen.",
    "fact_d2_is_child":         "Jacob is Ravi's biological son (a child per \u00a7152(c)(2)(A)).",
    "fact_d2_abode":            "Jacob's principal place of abode is Ravi's home for more than half the year.",
    "fact_d2_younger":          "Jacob is younger than Ravi.",
    "fact_d2_age_21":           "Jacob is 21 years old at year end.",
    "fact_d2_is_student":       "Jacob is a full-time student (\u00a7152(f)(2)), allowing the under-24 age branch.",
    "fact_d2_no_self_support":  "Jacob did not provide over half of his own support.",
    "fact_d2_no_joint_return":  "Jacob did not file a joint return.",
    "fact_d2_local_law_ok":     "The relationship does not violate local law.",
    "fact_d2_not_disabled":     "Jacob is not permanently and totally disabled.",

    # ----- D3 Elena -----
    "fact_d3_distinct":         "Elena and Marcos are different persons.",
    "fact_d3_us_resident":      "Elena is a U.S. resident (lawful permanent resident), satisfying \u00a7152(b)(3)(A).",
    "fact_d3_is_mother":        "Elena is Marcos's biological mother (\u00a7152(d)(2)(C)).",
    "fact_d3_gross_income_3000":"Elena's gross income for the year is $3,000.",
    "fact_d3_exemption_5050":   "The exemption amount for the tax year is $5,050.",
    "fact_d3_support":          "Marcos provides over one-half of Elena's support.",
    "fact_d3_not_qc_of_any":    "Elena is not a qualifying child of any taxpayer.",
    "fact_d3_no_joint_return":  "Elena did not file a joint return.",
    "fact_d3_not_disabled":     "Elena is not permanently and totally disabled (so the \u00a7152(d)(4) sheltered-workshop adjustment does not apply).",

    # ----- N1 Sarah -----
    "fact_n1_distinct":         "Sarah and Priya are different persons.",
    "fact_n1_citizen":          "Sarah is a U.S. citizen.",
    "fact_n1_is_child":         "Sarah is Priya's biological daughter.",
    "fact_n1_abode":            "Sarah shares Priya's principal place of abode for more than half the year.",
    "fact_n1_younger":          "Sarah is younger than Priya.",
    "fact_n1_age_17":           "Sarah is 17 years old at year end.",
    "fact_n1_no_self_support":  "Sarah did not provide over half of her own support.",
    "fact_n1_local_law_ok":     "The relationship does not violate local law.",
    "fact_n1_not_disabled":     "Sarah is not permanently and totally disabled.",
    "fact_n1_filed_joint_return":"Sarah filed a joint return with her spouse.",
    "fact_n1_not_refund_only":  "The joint return was NOT filed solely to claim a refund of withholding.",

    # ----- N2 Marcus -----
    "fact_n2_distinct":         "Marcus and Dmitri are different persons.",
    "fact_n2_citizen":          "Marcus is a U.S. citizen.",
    "fact_n2_is_child":         "Marcus is Dmitri's biological son.",
    "fact_n2_abode":            "Marcus shares Dmitri's principal place of abode.",
    "fact_n2_younger":          "Marcus is younger than Dmitri.",
    "fact_n2_no_joint_return":  "Marcus did not file a joint return.",
    "fact_n2_local_law_ok":     "The relationship does not violate local law.",
    "fact_n2_age_22":           "Marcus is 22 years old at year end (over 19).",
    "fact_n2_not_student":      "Marcus is not a student (\u00a7152(f)(2) branch closed).",
    "fact_n2_not_disabled":     "Marcus is not permanently and totally disabled (\u00a7152(c)(3)(B) branch closed).",
    "fact_n2_self_support":     "Marcus provided over half of his own support.",
    "fact_n2_gross_income_41k": "Marcus's gross income for the year is $41,000.",
    "fact_n2_exemption_5050":   "The exemption amount for the tax year is $5,050.",
    "fact_n2_support_fail":     "Dmitri did not provide over one-half of Marcus's support.",
    "fact_n2_no_multi_support": "No \u00a7152(d)(3) multiple-support agreement applies.",

    # ----- N3 Lin -----
    "fact_n3_distinct":         "Lin and Noah are different persons.",
    "fact_n3_citizen":          "Lin is a U.S. citizen.",
    "fact_n3_no_joint_return":  "Lin did not file a joint return.",
    "fact_n3_not_child":        "Lin is not a child or descendant of Noah.",
    "fact_n3_not_sibling_desc": "Lin is not a sibling or sibling-descendant of Noah.",
    "fact_n3_not_sibling":      "Lin is not a sibling (or step-sibling) of Noah.",
    "fact_n3_not_parent":       "Lin is not a parent or ancestor of Noah.",
    "fact_n3_not_stepparent":   "Lin is not a step-parent of Noah.",
    "fact_n3_not_niecenephew":  "Lin is not a niece or nephew of Noah.",
    "fact_n3_not_auntuncle":    "Lin is not an aunt or uncle of Noah.",
    "fact_n3_not_inlaw":        "Lin is not an in-law of Noah.",
    "fact_n3_not_household_member":"Lin is not a member of Noah's household (she is a paying tenant).",
    "fact_n3_gross_income_38k": "Lin's gross income for the year is $38,000.",
    "fact_n3_exemption_5050":   "The exemption amount for the tax year is $5,050.",
    "fact_n3_not_disabled":     "Lin is not permanently and totally disabled.",

    # Synthetic query labels inserted by the Part 2 runner
    "query_is_dependent":       "(query: assume the individual is a dependent)",
    "query_not_dependent":      "(query: assume the individual is not a dependent)",
}


def rule_sentence(rule_name: str) -> str:
    return RULE_TEXT.get(rule_name, f"[unknown rule: {rule_name}]")


def fact_sentence(fact_name: str) -> str:
    return FACT_TEXT.get(fact_name, f"[unlabeled fact: {fact_name}]")
