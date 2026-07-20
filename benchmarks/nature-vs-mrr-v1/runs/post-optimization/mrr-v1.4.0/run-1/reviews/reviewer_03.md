# Reviewer role

**Role ID:** study-design (CORE)  
**Owned axes:** experimental-design; clinical-validity; ethical-governance  
**Mode:** scientific-review only

# Material inspected and assessment boundary

I inspected only the frozen manuscript, inventory, Nature profile, and fact base. The manuscript remained read-only. Figures, tables, supplements, protocols, checklists, raw data, and code were unavailable. Statistical tests, multiplicity, computational reproducibility, availability, and mechanism interpretation were outside scope except where needed to state the design-supported claim ceiling.

# Journal standard applied

Nature Article, initial submission: outstanding importance and broad relevance (N001), evidence adequate for conclusions (N002), and Methods sufficient for interpretation and replication (N006). I required causal completeness, independent biomarker validation, defensible clinical consequence, and transportability.

# Overall assessment

The discovery-to-perturbation structure is promising, but the design does not establish anti-PD-1 selection, independent biomarker validity, mature three-year prediction, immune causality, therapeutic sensitization, or verifiable governance. It therefore cannot support “clinically actionable,” “universally applicable,” “causal driver,” or “sensitizes to anti-PD-1.”

# Major strengths

- The manuscript states cohort size, aetiology mix, death count, follow-up, clinical variables, and lack of external validation.
- The functional work uses two HCC cell lines and a non-targeting guide control.
- The mouse section identifies group size, allocation, unblinded measurement, and absent replication.

# BLOCKING issues

## SD-01

- **concern_id:** SD-01
- **proposed issue_key:** `biomarker_intended_use_outcome_population_mismatch`
- **axis:** clinical-validity
- **role_scope:** PRIMARY
- **severity:** BLOCKING
- **exact claim_pointer:** “Impact and implications”: “used to select anti-PD-1 therapy”; Discussion: “immediate use for selecting anti-PD-1 therapy.”
- **exact evidence_pointer:** Patients and methods, “Study population” describes only 72 adults undergoing resection; “Score construction and validation” models survival; no anti-PD-1-treated target cohort, treatment-response endpoint, or treatment-by-score comparison is reported.
- **evidence_status:** LOCATED
- **falsifiable concern:** The design can test prognosis after resection, not differential anti-PD-1 benefit or decision improvement.
- **concrete resolution_test:** Restrict the claim to resection prognosis, or test a locked score in an independent anti-PD-1-eligible cohort with a comparator, suitable endpoint, prespecified treatment-benefit interaction, and decision utility.
- **journal_gate:** FAIL — N001/N002; the claimed clinical consequence is not examined.
- **confidence:** 0.99

## SD-04

- **concern_id:** SD-04
- **proposed issue_key:** `eva1_perturbation_specificity_and_immune_function_controls`
- **axis:** experimental-design
- **role_scope:** PRIMARY
- **severity:** BLOCKING
- **exact claim_pointer:** Abstract: “EVA1 as the causal driver of immune escape”; Results: “directly suppresses anti-tumour immunity.”
- **exact evidence_pointer:** Patients and methods, “Functional experiments”: one CRISPR guide, no second guide, rescue, direct target-engagement assay, or immune-cell co-culture; the measured outcomes are cell growth, interferon-response transcripts, and PD-L1 in the same cultures.
- **evidence_status:** LOCATED
- **falsifiable concern:** One guide without rescue or target confirmation cannot establish EVA1 specificity; tumour-only cultures cannot demonstrate immune escape.
- **concrete resolution_test:** Replicate with two validated perturbations, sgRNA-resistant rescue, EVA1 engagement, and a controlled tumour–immune functional assay.
- **journal_gate:** FAIL — N002/N006; causal and immune-function claims lack essential controls.
- **confidence:** 0.99

## SD-05

- **concern_id:** SD-05
- **proposed issue_key:** `anti_pd1_sensitization_factorial_animal_design_absent`
- **axis:** experimental-design
- **role_scope:** PRIMARY
- **severity:** BLOCKING
- **exact claim_pointer:** Abstract: “sensitized xenografts to anti-PD-1”; Results: “EVA1 inhibition sensitizes HCC to anti-PD-1.”
- **exact evidence_pointer:** Patients and methods, “Mouse experiment”: all ten mice received anti-PD-1; only control versus EVA1-depleted cells were compared; allocation followed cage order, investigators were unblinded, and no independent replicate was performed. Results state no immune infiltration, survival, toxicity, or post-implantation EVA1 measurement.
- **evidence_status:** LOCATED
- **falsifiable concern:** Without EVA1-status × anti-PD-1 arms, an EVA1-associated growth effect cannot establish sensitization; allocation and measurement practices weaken attribution.
- **concrete resolution_test:** Use an identified immune-relevant model in a randomized, blinded, replicated 2×2 design; confirm EVA1 modulation and measure growth, immune pharmacodynamics, and toxicity. Sensitization requires a reproducible interaction.
- **journal_gate:** FAIL — N002/N006; the claimed therapeutic interaction was not designed into the experiment.
- **confidence:** 0.99

## SD-06

- **concern_id:** SD-06
- **proposed issue_key:** `human_animal_ethics_governance_unverifiable`
- **axis:** ethical-governance
- **role_scope:** PRIMARY
- **severity:** BLOCKING
- **exact claim_pointer:** Ethics: “the study complied with institutional requirements.”
- **exact evidence_pointer:** Ethics explicitly states that the approving committee, protocol number, consent procedure, animal protocol, and humane endpoints are not reported.
- **evidence_status:** LOCATED
- **falsifiable concern:** Human and animal approval, consent/waiver, welfare, and humane-endpoint compliance cannot be verified.
- **concrete resolution_test:** Report oversight bodies, approval identifiers, consent/waiver basis, welfare framework, monitoring, humane endpoints, and euthanasia criteria, reconciled to approvals.
- **journal_gate:** FAIL — N002/N006; required governance and welfare safeguards are not verifiable.
- **confidence:** 0.99

# MAJOR issues

## SD-02

- **concern_id:** SD-02
- **proposed issue_key:** `biomarker_validation_not_independent_or_endpoint_mature`
- **axis:** clinical-validity
- **role_scope:** PRIMARY
- **severity:** MAJOR
- **exact claim_pointer:** Abstract: “AUC of 0.91 for 3-year mortality”; Discussion: “validated in an independent subset.”
- **exact evidence_pointer:** “Score construction and validation”: gene selection, coefficients, cutoffs, signs, and missing-value rules used the full 72-patient dataset before a 70:30 split; no external cohort, assay validation, calibration, decision curve, or clinical baseline comparison. Results state median survivor follow-up was 18 months and three-year status was unavailable for many survivors.
- **evidence_status:** LOCATED
- **falsifiable concern:** The subset is not independent of feature/rule selection, and incomplete ascertainment precludes stable three-year validation.
- **concrete resolution_test:** Freeze all model rules before evaluation; validate without refitting in an external cohort with an independent assay and adequate follow-up; compare with BCLC/clinical baselines and assess calibration and utility.
- **journal_gate:** FAIL — N001/N002; independent, clinically interpretable performance is not established.
- **confidence:** 0.99

## SD-03

- **concern_id:** SD-03
- **proposed issue_key:** `universal_hcc_transportability_not_designed`
- **axis:** clinical-validity
- **role_scope:** PRIMARY
- **severity:** MAJOR
- **exact claim_pointer:** Abstract: “universally applicable predictor for HCC”; Impact: “all major HCC aetiologies”; Discussion: “application across HCC aetiologies and treatment settings.”
- **exact evidence_pointer:** “Study population”: one centre, resected adults, 58/72 with viral hepatitis, 9 with metabolic liver disease, and 5 with other/undocumented aetiologies. No unresectable, non-surgical, or treatment-selection cohort is described.
- **evidence_status:** LOCATED
- **falsifiable concern:** This virally enriched resection cohort cannot establish transportability across HCC aetiologies and treatment settings.
- **concrete resolution_test:** Prespecify the intended population; narrow claims to comparable resected patients or validate across relevant stages, aetiologies, centres, and treatments with subgroup calibration and failure checks.
- **journal_gate:** FAIL — N001/N002; broad relevance is asserted beyond the sampled population.
- **confidence:** 0.98

# MINOR issues

None prioritized.

# EDITORIAL issues

None; this scientific-review role did not assess polishing or formatting.

# Claim-ceiling risks

- The clinical evidence supports, at most, an internally derived retrospective prognostic association in a single-centre resection cohort.
- It does not support anti-PD-1 treatment selection, immediate deployment, universal applicability, or clinical utility.
- The perturbation evidence supports EVA1-associated phenotypes, not an EVA1-specific immune-evasion mechanism.
- The mouse experiment supports, at most, a day-21 tumour-volume difference under universal anti-PD-1 exposure, not sensitization to anti-PD-1.

# Required versus optional additional work

**Required for current claims:** an aligned anti-PD-1 intended-use study; external validation of a locked score with mature follow-up, baselines, calibration, and utility; representative or delimited cohorts; specificity/rescue and immune-function controls; a randomized, blinded, replicated factorial animal study; and complete governance reporting.

**Optional after claim narrowing:** prospective multicentre validation, orthotopic or complementary immune-competent models, and broader aetiology-specific studies.

# Journal-fit posture

**Not currently competitive as a Nature Article.** Clinical consequence, causal chain, therapeutic interaction, and broad applicability are not established. The present claims require substantial new evidence, not prose revision.

# NOT APPLICABLE items

- Diagnostic reference-standard accuracy is NOT APPLICABLE because the stated biomarker endpoint is prognostic mortality, not diagnosis.
- Randomized clinical intervention design is NOT APPLICABLE to the reported retrospective cohort; however, treatment-selection claims still require an appropriate comparative clinical design.

# NOT ASSESSABLE items

- Whether valid human and animal approvals, consent/waiver, welfare monitoring, and humane endpoints existed outside the manuscript packet.
- Mouse strain, immune competence, and suitability for anti-PD-1 biology because the host/model details are not reported.
- Detailed eligibility flow, referral/selection mechanisms, and missingness counts because these are not supplied.
- Figure-based verification of controls or animal allocation because figure images and tables were not supplied.

# Evidence anchors

- Patients and methods — “Study population,” “Score construction and validation,” “Functional experiments,” and “Mouse experiment.”
- Results — “The five-gene score predicts survival” and “EVA1 perturbation supports a therapeutic mechanism.”
- Abstract, Impact and implications, and Discussion — universal, actionable, causal, and anti-PD-1 claims.
- Ethics — explicit list of unreported governance elements.
- Shared fact base — confirms supplied versus unavailable materials and reported design facts.

# Confidence and reasons

**Overall confidence: 0.99.** Findings follow from explicit manuscript statements. Unreported approvals and immune-model details may exist outside the packet, so they are NOT ASSESSABLE rather than presumed absent.
