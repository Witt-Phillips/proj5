; ============================================================
; Scenario N2 -- Marcus, the 22-year-old self-supporting son
; Expected: NOT a dependent
;   - Fails QC via 152(c)(1)(C) (age 22, not student, not disabled)
;     and 152(c)(1)(D) (provided over half of own support)
;   - Fails QR via 152(d)(1)(B) (gross income exceeds exemption)
;     and 152(d)(1)(C) (taxpayer did not provide over half)
; See ../warmup/scenarios.md for the plain-English description.
; ============================================================

(declare-const marcus Person)
(declare-const dmitri Person)
(declare-const y24    TaxYear)

(assert (! (distinct marcus dmitri) :named fact_n2_distinct))
(assert (! (is_us_citizen_or_national marcus)                         :named fact_n2_citizen))
(assert (! (is_child_or_descendant_of_taxpayer marcus dmitri)         :named fact_n2_is_child))
(assert (! (same_abode_majority marcus dmitri y24)                    :named fact_n2_abode))
(assert (! (is_younger_than marcus dmitri y24)                        :named fact_n2_younger))
(assert (! (not (filed_joint_return marcus y24))                      :named fact_n2_no_joint_return))
(assert (! (not (relationship_violates_local_law marcus dmitri y24))  :named fact_n2_local_law_ok))

; 152(c)(3) age failure: 22, not a student, not disabled
(assert (! (= (age_at_year_end marcus y24) 22)                        :named fact_n2_age_22))
(assert (! (not (is_student marcus y24))                              :named fact_n2_not_student))
(assert (! (not (is_permanently_disabled marcus y24))                 :named fact_n2_not_disabled))

; 152(c)(1)(D) self-support failure
(assert (! (provided_over_half_own_support marcus y24)                :named fact_n2_self_support))

; 152(d)(1)(B) gross-income failure: 41000 >= 5050
(assert (! (= (gross_income marcus y24) 41000.0)                      :named fact_n2_gross_income_41k))
(assert (! (= (exemption_amount y24)     5050.0)                      :named fact_n2_exemption_5050))

; 152(d)(1)(C) support failure: taxpayer did NOT provide over half
(assert (! (not (taxpayer_provided_over_half_support dmitri marcus y24))  :named fact_n2_support_fail))
(assert (! (not (qualifies_under_multiple_support_agreement dmitri marcus y24)) :named fact_n2_no_multi_support))
