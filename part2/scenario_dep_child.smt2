; ============================================================
; Scenario D1 -- Maya, the young biological child
; Expected: dependent (qualifying-child path)
; See ../warmup/scenarios.md for the plain-English description.
; ============================================================

(declare-const maya Person)
(declare-const jane Person)
(declare-const y24  TaxYear)

(assert (! (distinct maya jane) :named fact_d1_distinct))
(assert (! (is_us_citizen_or_national maya)                         :named fact_d1_citizen))
(assert (! (is_child_or_descendant_of_taxpayer maya jane)           :named fact_d1_is_child))
(assert (! (same_abode_majority maya jane y24)                      :named fact_d1_abode))
(assert (! (is_younger_than maya jane y24)                          :named fact_d1_younger))
(assert (! (= (age_at_year_end maya y24) 9)                         :named fact_d1_age_9))
(assert (! (not (provided_over_half_own_support maya y24))          :named fact_d1_no_self_support))
(assert (! (not (filed_joint_return maya y24))                      :named fact_d1_no_joint_return))
(assert (! (not (relationship_violates_local_law maya jane y24))    :named fact_d1_local_law_ok))
(assert (! (not (is_permanently_disabled maya y24))                 :named fact_d1_not_disabled))
