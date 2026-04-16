; ============================================================
; Scenario D3 -- Elena, the 72-year-old resident mother
; Expected: dependent (qualifying-relative path)
; See ../warmup/scenarios.md for the plain-English description.
; ============================================================

(declare-const elena  Person)
(declare-const marcos Person)
(declare-const y24    TaxYear)

(assert (! (distinct elena marcos) :named fact_d3_distinct))

; 152(b)(3) citizenship/residency -- green-card holder is a U.S. resident
(assert (! (is_us_resident elena) :named fact_d3_us_resident))

; 152(d)(2)(C) -- "father, mother, or an ancestor of either"
(assert (! (is_parent_or_ancestor_of_taxpayer elena marcos) :named fact_d3_is_mother))

; 152(d)(1)(B) -- gross income < exemption amount
(assert (! (= (gross_income elena y24) 3000.0)     :named fact_d3_gross_income_3000))
(assert (! (= (exemption_amount y24)   5050.0)     :named fact_d3_exemption_5050))

; 152(d)(1)(C) -- taxpayer provides over half of support
(assert (! (taxpayer_provided_over_half_support marcos elena y24) :named fact_d3_support))

; 152(d)(1)(D) -- not a qualifying child of any taxpayer
(assert (! (not (is_qc_of_any_taxpayer elena y24)) :named fact_d3_not_qc_of_any))

; 152(b)(2) -- no joint return
(assert (! (not (filed_joint_return elena y24)) :named fact_d3_no_joint_return))

; Effective gross income: not disabled -> effective = gross
(assert (! (not (is_permanently_disabled elena y24)) :named fact_d3_not_disabled))
