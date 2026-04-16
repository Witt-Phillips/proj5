; ============================================================
; Scenario N1 -- Sarah, the 17-year-old who filed a joint return
; Expected: NOT a dependent (blocked by 152(b)(2))
; See ../warmup/scenarios.md for the plain-English description.
; ============================================================

(declare-const sarah Person)
(declare-const priya Person)
(declare-const y24   TaxYear)

(assert (! (distinct sarah priya) :named fact_n1_distinct))
(assert (! (is_us_citizen_or_national sarah)                        :named fact_n1_citizen))
(assert (! (is_child_or_descendant_of_taxpayer sarah priya)         :named fact_n1_is_child))
(assert (! (same_abode_majority sarah priya y24)                    :named fact_n1_abode))
(assert (! (is_younger_than sarah priya y24)                        :named fact_n1_younger))
(assert (! (= (age_at_year_end sarah y24) 17)                       :named fact_n1_age_17))
(assert (! (not (provided_over_half_own_support sarah y24))         :named fact_n1_no_self_support))
(assert (! (not (relationship_violates_local_law sarah priya y24))  :named fact_n1_local_law_ok))
(assert (! (not (is_permanently_disabled sarah y24))                :named fact_n1_not_disabled))

; KEY disqualifying facts: Sarah filed a joint return and it was NOT
; solely for a refund claim (real tax liability paid).
(assert (! (filed_joint_return sarah y24)                           :named fact_n1_filed_joint_return))
(assert (! (not (filed_joint_return_only_for_refund sarah y24))     :named fact_n1_not_refund_only))
