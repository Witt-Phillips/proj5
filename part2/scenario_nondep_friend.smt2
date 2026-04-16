; ============================================================
; Scenario N3 -- Lin, the friend/tenant (no qualifying relationship)
; Expected: NOT a dependent
;   - Fails QC via 152(c)(1)(A) (no 152(c)(2) relationship)
;   - Fails QR via 152(d)(1)(A) (none of 152(d)(2)(A)-(G), and not a
;     household member so (H) catch-all does not apply)
;   - Independently fails 152(d)(1)(B) on gross income
; See ../warmup/scenarios.md for the plain-English description.
; ============================================================

(declare-const lin  Person)
(declare-const noah Person)
(declare-const y24  TaxYear)

(assert (! (distinct lin noah) :named fact_n3_distinct))
(assert (! (is_us_citizen_or_national lin)                                        :named fact_n3_citizen))
(assert (! (not (filed_joint_return lin y24))                                     :named fact_n3_no_joint_return))

; 152(c)(2) relationships -- all false
(assert (! (not (is_child_or_descendant_of_taxpayer lin noah))                    :named fact_n3_not_child))
(assert (! (not (is_sibling_or_sibling_descendant_of_taxpayer lin noah))          :named fact_n3_not_sibling_desc))

; 152(d)(2)(A)-(G) relationships -- all false
(assert (! (not (is_sibling_of_taxpayer lin noah))                                :named fact_n3_not_sibling))
(assert (! (not (is_parent_or_ancestor_of_taxpayer lin noah))                     :named fact_n3_not_parent))
(assert (! (not (is_stepparent_of_taxpayer lin noah))                             :named fact_n3_not_stepparent))
(assert (! (not (is_sibling_child_of_taxpayer lin noah))                          :named fact_n3_not_niecenephew))
(assert (! (not (is_parent_sibling_of_taxpayer lin noah))                         :named fact_n3_not_auntuncle))
(assert (! (not (is_in_law_of_taxpayer lin noah))                                 :named fact_n3_not_inlaw))

; 152(d)(2)(H) catch-all: not a member of taxpayer's household (paying tenant)
(assert (! (not (is_household_member lin noah y24))                               :named fact_n3_not_household_member))

; Independent gross-income failure for QR
(assert (! (= (gross_income lin y24) 38000.0)                                     :named fact_n3_gross_income_38k))
(assert (! (= (exemption_amount y24)  5050.0)                                     :named fact_n3_exemption_5050))
(assert (! (not (is_permanently_disabled lin y24))                                :named fact_n3_not_disabled))
