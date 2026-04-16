; ============================================================
; Scenario D2 -- Jacob, the 21-year-old full-time student
; Expected: dependent (QC via 152(c)(3)(A)(ii) student exception)
; See ../warmup/scenarios.md for the plain-English description.
; ============================================================

(declare-const jacob Person)
(declare-const ravi  Person)
(declare-const y24   TaxYear)

(assert (! (distinct jacob ravi) :named fact_d2_distinct))
(assert (! (is_us_citizen_or_national jacob)                        :named fact_d2_citizen))
(assert (! (is_child_or_descendant_of_taxpayer jacob ravi)          :named fact_d2_is_child))
(assert (! (same_abode_majority jacob ravi y24)                     :named fact_d2_abode))
(assert (! (is_younger_than jacob ravi y24)                         :named fact_d2_younger))
(assert (! (= (age_at_year_end jacob y24) 21)                       :named fact_d2_age_21))
(assert (! (is_student jacob y24)                                   :named fact_d2_is_student))
(assert (! (not (provided_over_half_own_support jacob y24))         :named fact_d2_no_self_support))
(assert (! (not (filed_joint_return jacob y24))                     :named fact_d2_no_joint_return))
(assert (! (not (relationship_violates_local_law jacob ravi y24))   :named fact_d2_local_law_ok))
(assert (! (not (is_permanently_disabled jacob y24))                :named fact_d2_not_disabled))
