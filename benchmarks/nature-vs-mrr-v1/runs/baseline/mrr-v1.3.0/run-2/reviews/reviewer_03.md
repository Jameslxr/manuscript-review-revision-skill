# Reviewer role

`role_id: study-design` — manuscript-specific integrated design validity, with emphasis on the single-cell biological unit and pseudoreplication; biomarker discovery/validation separation; wet-lab perturbation causality and controls; and animal/translational design, including identification of treatment interaction.

# Material inspected and assessment boundary

Inspected only:

- `/tmp/manuscript-skill-benchmark-20260720.zGfMWO/shared/manuscript.md` (SHA-256 `d51224a5ec717a268dadeee2fe9461a7b9d8c833f5b459be2d522a88d5c0006f`)
- `/tmp/manuscript-skill-benchmark-20260720.zGfMWO/shared/00_input_inventory.json`
- `/tmp/manuscript-skill-benchmark-20260720.zGfMWO/shared/nature-journal-profile.json` (SHA-256 `6f6386d213e195d6ec26d0c177568f27753208425a6a15ce139b1ac2235fd6eb`)
- `/tmp/manuscript-skill-benchmark-20260720.zGfMWO/shared/02_shared_fact_base.md` (SHA-256 `947b2ed3c744626d5eadc56845b65f223c6b0d4336bd765e3c714acf4ff4a976`)
- The named Skill and its routed review references.

This is a read-only scientific review. Figure images, tables, supplementary information, raw data, source code, protocols, reporting checklists, and underlying analysis outputs were not supplied. Their contents are not presumed absent from the underlying study; verification that depends on them is marked `NOT ASSESSABLE`. No literature or journal browsing was performed, and no other reviewer output or prior run was inspected.

# Journal standard applied

Target: **Nature**, Article, initial submission. The frozen journal profile classifies Nature as a broad flagship requiring original research of outstanding scientific importance, a major conceptual advance of interdisciplinary interest, technical soundness, strong evidence, broad relevance, appropriately bounded claims, and Methods sufficient for interpretation and replication. The operative frozen requirements are N001 (outstanding importance and interdisciplinary conclusion), N002 (technical soundness, evidence strength, novelty and broad interest), and N006 (Methods sufficient to interpret and replicate).

Design ceilings applied:

- A retrospective single-centre association cannot alone establish universal generalizability or therapeutic selection utility.
- Internal reuse or splitting of the same cohort cannot alone establish external validation.
- A perturbation comparison that does not identify a treatment interaction cannot alone establish sensitization.

# Overall assessment

The integrated design is conceptually interesting but the central study-design gates are **FAIL** as written. The single-cell discovery treats cells rather than patients as independent; biomarker construction reuses all 72 patients before a nominal split; the clinical cohort does not test anti-PD-1 benefit; the animal experiment gives anti-PD-1 to every animal and therefore cannot identify sensitization; and the one-guide perturbation lacks the specificity, rescue, target-engagement and immune-functional controls needed to establish a direct causal immune-evasion mechanism. These limitations are not cosmetic. They break the inferential chain connecting cell-state discovery, prognosis, immune escape, treatment selection and therapeutic sensitization.

A bounded exploratory conclusion remains possible: the packet nominates an EVA1-associated transcriptional signal and a candidate five-gene prognostic score for independent validation, and reports preliminary phenotypic changes after EVA1-targeting perturbation. It does not presently support a universal, clinically actionable predictor, direct causal driver, or anti-PD-1 sensitizer.

# Major strengths

- The study attempts cross-layer triangulation across single-cell profiling, a clinical cohort, two HCC cell lines and an in vivo experiment.
- The manuscript clearly states several decisive design choices, including cell-level testing, full-cohort stepwise selection, lack of an external cohort, one-guide perturbation, absence of rescue and immune-cell co-culture, and anti-PD-1 exposure in all mice. This makes the principal inferential boundaries assessable.
- Testing the perturbation in both Huh7 and Hep3B is stronger than a single-cell-line observation, although it does not solve perturbation specificity or immune-mechanism identification.

# BLOCKING issues

## B1. Cells are used as independent replicates for patient-level discovery

- **Severity:** `BLOCKING`
- **Controlled axis:** `experimental-design`
- **Proposed issue_key:** `sc-biological-unit`
- **Exact manuscript anchor:** Patients and methods, “Single-cell discovery”: “Single-cell RNA sequencing was performed on tumour and adjacent tissue from eight patients”; “Differential expression … was tested at the cell level”; “Cells were treated as independent observations.” Results, “Single-cell discovery identifies an immune-evasion programme”: “1,842 nominally significant genes” and “EVA1 was higher in low-infiltration tumours.”
- **Falsifiable concern:** High/low infiltration is a tumour/patient-level attribute, but the analysis treats 46,218 nested cells as independent observations. If patient-level dependence is modelled, the reported significance and gene ranking may materially change or disappear; the current nominal cell-level P values therefore do not establish reproducible patient-level differential expression. No multiple-testing correction further inflates discovery.
- **Concrete resolution test:** Re-run discovery with patient as the biological unit using a prespecified pseudobulk or appropriately specified mixed-effects framework that respects pairing and batch; report eight-patient group allocation, effect sizes and uncertainty; control the genome-wide false-discovery rate; and show leave-one-patient-out or comparable influence analyses. The gene set entering score construction must be regenerated without using outcome information from the downstream validation cohort.
- **Journal gate if applicable:** N002 technical soundness and strength of evidence; N006 interpretability and replication. Gate status: `FAIL`.
- **Confidence:** `0.99`
- **Required versus optional:** `REQUIRED` to retain a single-cell-derived discovery claim. Claim narrowing to an explicitly exploratory cell-level observation is required if a valid patient-level reanalysis cannot support the signal.

## B2. Full-cohort model construction invalidates the claimed validation

- **Severity:** `BLOCKING`
- **Controlled axis:** `clinical-validity`
- **Proposed issue_key:** `model-reuse-no-external-validation`
- **Exact manuscript anchor:** Patients and methods, “Score construction and validation”: “Five genes were retained after stepwise selection using the entire 72-patient dataset”; “Expression cutoffs, coefficient signs, and missing-value rules were also chosen using the full dataset”; “The same 72 patients were then randomly divided 70:30”; “No external cohort, independent laboratory assay, calibration analysis, or decision-curve analysis was used.” Discussion: “The score was validated in an independent subset.”
- **Falsifiable concern:** Because feature selection, coefficients, cutoffs and missing-data rules were chosen using all 72 patients before splitting, the nominal validation subset influenced model construction and is not independent. Apparent discrimination can therefore be optimistically biased. A random subset of the reused, single-centre cohort does not test transportability, assay reproducibility or generalizability.
- **Concrete resolution test:** Lock the complete score, coefficients, threshold, preprocessing, assay and missing-data policy without access to a genuinely independent cohort, then evaluate it in an external intended-use cohort with patient-level separation. Report discrimination with confidence intervals, calibration, clinically relevant operating characteristics, comparison with a prespecified clinical baseline, and decision utility. If no external validation is available, present the model only as internally derived and exploratory, use honest internal validation that repeats the entire modelling pipeline, and remove “validated,” “independent,” “clinically actionable,” “immediately deployable” and “universally applicable.”
- **Journal gate if applicable:** N001 major broadly relevant advance; N002 strength of evidence and broad relevance. Gate status: `FAIL`.
- **Confidence:** `1.00`
- **Required versus optional:** `REQUIRED` for validated, clinically actionable or universal biomarker claims. Rigorous internal validation plus claim narrowing is the minimum required for an exploratory derivation report but does not substitute for external validation.

## B3. A prognostic resection cohort cannot identify anti-PD-1 treatment benefit

- **Severity:** `BLOCKING`
- **Controlled axis:** `clinical-validity`
- **Proposed issue_key:** `prognostic-not-treatment-predictive`
- **Exact manuscript anchor:** Patients and methods, “Study population”: “72 adults who underwent resection for HCC”; available variables include “treatment after recurrence,” but no randomized or comparative anti-PD-1 exposure is defined. Impact and implications: the score can be “used to select anti-PD-1 therapy.” Discussion: “Its high AUC supports immediate use for selecting anti-PD-1 therapy.”
- **Falsifiable concern:** Association with overall survival in a retrospective resection cohort is prognostic, not evidence that the score predicts differential benefit from anti-PD-1. Without a defined treatment comparison and a score-by-treatment interaction, the score could identify baseline risk while having no treatment-selection utility.
- **Concrete resolution test:** In a prespecified, appropriately powered independent cohort or trial with clearly defined anti-PD-1 and comparator treatment groups, test a locked score-by-treatment interaction on a clinically relevant endpoint, with confounding control appropriate to the design, calibration and decision-utility analysis. Alternatively, remove every treatment-selection and deployability claim and define the result as exploratory prognostic association only.
- **Journal gate if applicable:** N001 interdisciplinary/conceptual consequence; N002 strength of evidence. Gate status: `FAIL`.
- **Confidence:** `1.00`
- **Required versus optional:** `REQUIRED` to claim anti-PD-1 selection utility. Claim removal is required if treatment-interaction evidence is not added.

## B4. The animal design cannot identify sensitization to anti-PD-1

- **Severity:** `BLOCKING`
- **Controlled axis:** `experimental-design`
- **Proposed issue_key:** `anti-pd1-interaction-unidentified`
- **Exact manuscript anchor:** Patients and methods, “Mouse experiment”: “control or EVA1-depleted cells, with five animals per group. All mice received anti-PD-1.” Results, “EVA1 perturbation supports a therapeutic mechanism”: “We conclude that EVA1 inhibition sensitizes HCC to anti-PD-1.”
- **Falsifiable concern:** With anti-PD-1 administered to every mouse, the observed tumour-size difference estimates an EVA1-perturbation effect under anti-PD-1 exposure; it cannot distinguish general growth suppression from enhanced drug response. The design contains no anti-PD-1 main-effect estimate and no EVA1-by-treatment interaction, so sensitization is unidentified.
- **Concrete resolution test:** Use an adequately powered factorial design crossing EVA1 status/intervention with anti-PD-1 versus matched control treatment, with randomized allocation, blinded measurement and a prespecified interaction analysis. Demonstrate target engagement and immune-relevant pharmacodynamic effects in a model in which the checkpoint reagent, tumour and host immune system are biologically compatible. Replicate the result in an independent relevant model. If this is not done, restrict the conclusion to smaller xenografts after EVA1-depleted cell implantation in anti-PD-1-treated animals.
- **Journal gate if applicable:** N002 technical soundness and strength of evidence. Gate status: `FAIL`.
- **Confidence:** `1.00`
- **Required versus optional:** `REQUIRED` for “sensitizes,” therapeutic synergy, or anti-PD-1-combination claims.

## B5. The perturbation package does not establish a direct causal immune-evasion driver

- **Severity:** `BLOCKING`
- **Controlled axis:** `mechanism-evidence`
- **Proposed issue_key:** `single-guide-causality`
- **Exact manuscript anchor:** Patients and methods, “Functional experiments”: “one CRISPR guide RNA”; “The study did not include a second guide, rescue construct, direct target-engagement assay, or immune-cell co-culture.” Results: EVA1 depletion “reduced 72-hour cell growth,” PD-L1 decreased and three interferon-response transcripts increased; “These findings show that EVA1 directly suppresses anti-tumour immunity.”
- **Falsifiable concern:** A phenotype from one guide can reflect off-target activity or nonspecific growth effects. PD-L1 and transcript changes in tumour-cell monoculture do not demonstrate functional immune escape, direct pathway control or causal ordering. Reduced xenograft growth may simply extend the in vitro growth phenotype.
- **Concrete resolution test:** Reproduce the phenotype with at least one independent on-target perturbation, verify target engagement, rescue the phenotype with a perturbation-resistant construct, and show gain/loss symmetry where biologically justified. Establish temporal or mediation ordering and demonstrate an immune-functional phenotype using appropriate effector-cell or immunocompetent in vivo assays with relevant controls. Direct-mechanism language additionally requires evidence distinguishing direct from indirect regulation.
- **Journal gate if applicable:** N001 major conceptual advance; N002 technical soundness and causal evidence. Gate status: `FAIL`.
- **Confidence:** `0.99`
- **Required versus optional:** `REQUIRED` for “causal driver,” “directly controls,” “directly suppresses anti-tumour immunity,” or therapeutic-target claims. Otherwise these claims must be reduced to preliminary perturbation-associated effects.

# MAJOR issues

## M1. Animal internal validity and translational relevance are inadequate

- **Severity:** `MAJOR`
- **Controlled axis:** `experimental-design`
- **Proposed issue_key:** `animal-internal-validity`
- **Exact manuscript anchor:** Patients and methods, “Mouse experiment”: ten mice, five per group; “Allocation order followed cage order”; “investigators were aware of group assignment”; day-21 unpaired t-test; “No independent replicate experiment was performed.” Results: “The experiment did not measure immune infiltration, survival, toxicity, or EVA1 expression after implantation.”
- **Falsifiable concern:** Cage-order allocation permits systematic allocation bias, unblinded measurement permits ascertainment bias, a single terminal comparison does not use the longitudinal tumour-volume structure, and the small unreplicated experiment is vulnerable to instability. Without post-implantation EVA1 target engagement, immune infiltration, toxicity or a clinically interpretable endpoint, the experiment does not establish the proposed immune or translational mechanism.
- **Concrete resolution test:** Repeat with concealed randomized allocation, blinded outcome measurement, prespecified inclusion/exclusion and attrition reporting, an a priori sample-size rationale, cage/litter structure handled where applicable, longitudinal analysis appropriate to repeated measurements, confirmed in vivo target engagement, immune readouts and toxicity, and independent replication in a relevant model.
- **Journal gate if applicable:** N002 technical soundness and evidence strength; N006 replication. Gate status: `FAIL`.
- **Confidence:** `0.99`
- **Required versus optional:** `REQUIRED` for a Nature-level in vivo mechanistic or translational claim. Survival can be optional if another clinically justified endpoint is prespecified and the claim is bounded, but target engagement and immune-mechanism evidence are required for the stated mechanism.

## M2. The three-year outcome assessment is not shown to be estimable or stable

- **Severity:** `MAJOR`
- **Controlled axis:** `clinical-validity`
- **Proposed issue_key:** `three-year-endpoint-immature`
- **Exact manuscript anchor:** Patients and methods, “Study population”: 31 deaths and “Median follow-up among surviving patients was 18 months.” Results, “The five-gene score predicts survival”: “Because median follow-up was 18 months, 3-year outcome status was unavailable for many surviving patients.” The Abstract, Results and Figure 3 legend report AUCs of 0.91, 0.84 and 0.86, respectively.
- **Falsifiable concern:** With limited follow-up and many unknown three-year statuses, an ordinary binary AUC can be biased or undefined depending on censoring handling; the packet does not specify a time-dependent method. The mutually inconsistent AUC values prevent knowing which result supports the claim.
- **Concrete resolution test:** Define time origin, censoring and the exact three-year estimand; report numbers at risk and event counts at three years; use an appropriate time-dependent discrimination estimator with uncertainty and justified censoring assumptions; reconcile one reproducible value across text and figure; and test sensitivity to censoring. If follow-up cannot support the horizon, choose a defensible endpoint or collect sufficient follow-up.
- **Journal gate if applicable:** N002 evidence strength; N006 interpretability and replication. Gate status: `FAIL`.
- **Confidence:** `0.98`
- **Required versus optional:** `REQUIRED` for any three-year discrimination claim.

## M3. The sampled population cannot support universal application across HCC aetiologies and settings

- **Severity:** `MAJOR`
- **Controlled axis:** `claim-moderation`
- **Proposed issue_key:** `universal-generalizability`
- **Exact manuscript anchor:** Patients and methods, “Study population”: single centre, 58 of 72 patients with viral hepatitis, 9 with metabolic liver disease and 5 with other or undocumented aetiologies. Impact and implications: “all major HCC aetiologies.” Discussion: “application across HCC aetiologies and treatment settings.” Title and Abstract use “universal” and “universally applicable.”
- **Falsifiable concern:** The single-centre, predominantly viral, resection cohort does not sample enough patients, centres, assays or treatment settings to establish transportability across major aetiologies, unresectable disease or treatment contexts. Performance may differ materially in metabolic, alcohol-associated, geographically distinct or advanced-disease populations.
- **Concrete resolution test:** Validate the locked assay and model in independent multicentre cohorts that prospectively cover the claimed aetiologies and intended treatment settings, with prespecified subgroup performance, calibration and interaction/heterogeneity analyses. Otherwise remove universal and all-aetiology language and limit conclusions to this retrospective cohort.
- **Journal gate if applicable:** N001 broad relevance; N002 evidence strength. Gate status: `FAIL` for the current universal claim.
- **Confidence:** `0.99`
- **Required versus optional:** `REQUIRED` for universal/all-aetiology/all-setting claims; otherwise claim narrowing is required.

## M4. Essential animal-model and governance details are not reported

- **Severity:** `MAJOR`
- **Controlled axis:** `reproducibility`
- **Proposed issue_key:** `animal-methods-governance`
- **Exact manuscript anchor:** Patients and methods, “Mouse experiment,” which identifies only a subcutaneous Huh7 xenograft, group sizes, anti-PD-1 exposure, allocation and endpoint. Ethics: “The approving committee, protocol number, consent procedure, animal protocol, and humane endpoints are not reported.”
- **Falsifiable concern:** Host strain/immune competence, sex, age, reagent identity/species compatibility, dosing schedule, housing, humane endpoints, exclusions, attrition and approval details are necessary to interpret whether anti-PD-1 could act through the proposed immune mechanism and to replicate the experiment. Their absence from the manuscript makes model relevance and ethical governance unverifiable.
- **Concrete resolution test:** Report the complete animal model, host immune status, sex/age/strain, housing and cage structure, tumour implantation, treatment reagent/dose/schedule, randomization/blinding, exclusions/attrition, welfare monitoring and humane endpoints, and institutional approval identifier. Demonstrate that the checkpoint reagent and host/tumour system permit the claimed immune mechanism. If approvals or humane-endpoint records do not exist, the animal evidence cannot be used.
- **Journal gate if applicable:** N006 Methods sufficient for interpretation and replication; N002 technical soundness. Gate status: `FAIL` for reporting; underlying compliance is `NOT ASSESSABLE`.
- **Confidence:** `0.99`
- **Required versus optional:** `REQUIRED`.

# MINOR issues

## m1. Analysis populations are not reproducibly defined after variable-wise missing-data exclusion

- **Severity:** `MINOR`
- **Controlled axis:** `reproducibility`
- **Proposed issue_key:** `analysis-population-missingness`
- **Exact manuscript anchor:** Patients and methods, “Study population”: “Records with missing values were excluded from each analysis.”
- **Falsifiable concern:** Different complete-case subsets may underlie each analysis, but their sizes, missingness patterns and relation to outcome are not reported. The stated results therefore cannot be mapped to a stable analysis population, and selection due to missingness cannot be assessed.
- **Concrete resolution test:** Provide a participant/analysis flow, per-variable missingness, exact denominator and event count for every model and figure, the missing-data strategy, and a sensitivity analysis when exclusions are nontrivial. Lock these rules before external validation.
- **Journal gate if applicable:** N006 interpretability and replication. Gate status: `FAIL` for current reporting.
- **Confidence:** `0.95`
- **Required versus optional:** `REQUIRED` reporting correction; advanced imputation sensitivity is conditional on the extent and mechanism of missingness.

# EDITORIAL issues

No separate presentation-only issue is identified. Terms such as “independent subset,” “validated,” “sensitized,” “causal,” “clinically actionable” and “universal” are scientifically consequential and are therefore handled above rather than classified as editorial wording.

# Claim-ceiling risks

- **Single-cell evidence ceiling:** patient-nested cell-level association and candidate nomination; not a reproducible patient-level immune-evasion programme until biological-unit-aware analysis and multiplicity control succeed.
- **Biomarker ceiling:** exploratory internally derived prognostic score; not independent validation, universal applicability, deployability or clinical utility.
- **Treatment-selection ceiling:** prognostic association in resected patients; not prediction of benefit from anti-PD-1.
- **Wet-lab ceiling:** preliminary phenotype associated with one EVA1-targeting guide; not a specific direct causal immune-evasion mechanism.
- **Animal ceiling:** smaller day-21 xenografts after implantation of EVA1-depleted cells when all animals received anti-PD-1; not sensitization, synergy or human therapeutic efficacy.
- **Generalizability ceiling:** findings in one predominantly viral, single-centre resection cohort; not all HCC aetiologies or treatment settings.

# Required versus optional additional work

**Required to retain the central claims:**

1. Patient-level single-cell reanalysis with multiplicity control and robustness to individual patients.
2. Complete leakage-free model development and genuinely independent external validation of a locked score and assay.
3. Direct evidence of score-by-treatment interaction for anti-PD-1 selection.
4. A randomized, blinded factorial animal experiment that identifies EVA1-by-anti-PD-1 interaction in an immunologically compatible model.
5. Orthogonal EVA1 perturbation, target engagement, rescue and immune-functional evidence sufficient to distinguish direct mechanism from correlated phenotype.
6. Reproducible three-year outcome analysis, reconciliation of AUC values, appropriate handling of censoring, and complete analysis-population reporting.
7. Complete animal Methods, welfare and approval reporting.
8. Multicentre/aetiology-diverse validation for universal claims, or mandatory claim narrowing.

**Optional strengthening after the required gates pass:**

- Additional mechanistically distinct HCC models, spatial or orthogonal tissue validation, and prospective implementation studies.
- Survival endpoints in animals if a different prespecified endpoint already supports the bounded claim.
- Broader multi-region validation beyond the populations needed for the explicitly defined intended use.

Optional studies cannot compensate for failure of the biological-unit, leakage, treatment-interaction or perturbation-specificity gates.

# Journal-fit posture

As written, the design does not meet the frozen Nature Article standard for technical soundness, causal completeness, independent validation, broad relevance or a major conceptual advance. The work would require major new analysis and new independent clinical, mechanistic and treatment-interaction evidence before Nature fit could be reassessed. If the available evidence remains unchanged, the manuscript should be reframed as an exploratory candidate-discovery study with materially narrowed claims and considered against a journal standard appropriate to that evidence level; this is a study-design posture, not a prediction of editorial outcome.

# NOT ASSESSABLE items

- Numerical reconciliation of figure panels, patient-level source outputs and reported effects: `NOT ASSESSABLE` because figure images, tables, raw data and code were not supplied.
- Whether undocumented animal procedures, approvals, humane endpoints, randomization records or model-compatibility checks existed in the underlying study: `NOT ASSESSABLE`; the manuscript's reporting deficiency is assessable and fails N006.
- Exact single-cell QC, batch structure, doublet/ambient-RNA handling, annotation robustness and processed-data reproducibility: `NOT ASSESSABLE` from the supplied packet.
- Exact model coefficients, feature values, seeds, preprocessing implementation and resampling reproducibility: `NOT ASSESSABLE` because the manuscript states these were not deposited and the analysis materials were not supplied.
- Reference-level support for novelty and treatment claims: `NOT ASSESSABLE` in this reviewer seat because source papers were not inspected.
- Ethics and consent compliance in the underlying human study: `NOT ASSESSABLE`; the approving committee, protocol number and consent procedure are not reported.

# Evidence anchors

- Abstract: “clinically actionable, universally applicable predictor”; “causal driver”; “sensitized xenografts.”
- Impact and implications: “used to select anti-PD-1 therapy”; “immediately deployable”; “all major HCC aetiologies.”
- Patients and methods — Study population: 72 single-centre resected patients, 31 deaths, 18-month median follow-up among survivors, aetiology distribution, variable-wise exclusion.
- Patients and methods — Single-cell discovery: eight patients, 46,218 cells, cells treated as independent, nominal P threshold and no multiplicity correction.
- Patients and methods — Score construction and validation: full-cohort feature/cutoff/rule selection followed by a 70:30 split of the same cohort; no external cohort, calibration, decision curve or clinical baseline.
- Patients and methods — Functional experiments: one guide, no second guide, rescue, target-engagement assay or immune-cell co-culture.
- Patients and methods — Mouse experiment: five animals per group, all anti-PD-1, cage-order allocation, no blinded measurement, single day-21 test and no independent replicate.
- Results — The five-gene score predicts survival: inconsistent AUC values and incomplete three-year outcome availability.
- Results — EVA1 perturbation supports a therapeutic mechanism: growth, PD-L1 and transcript changes; absent immune infiltration, survival, toxicity and post-implantation EVA1 measurement.
- Discussion: claims of independent validation, immediate treatment selection, generality, universal mechanism and application across aetiologies/settings.
- Data and code availability and Ethics: non-deposited analytical materials and missing governance identifiers.

# Confidence and reasons

**Overall confidence: `0.99`.** The highest-severity findings follow directly from explicit design statements rather than inference from absent materials: cells were treated as independent, model choices used the full cohort before splitting, no external cohort was used, the clinical design did not compare anti-PD-1 benefit, all mice received anti-PD-1, and only one guide without rescue or immune-functional testing was used. Confidence is lower only for questions that require absent source data, figure images, detailed protocols or governance records; those are retained as `NOT ASSESSABLE` rather than treated as evidence of nonperformance.
