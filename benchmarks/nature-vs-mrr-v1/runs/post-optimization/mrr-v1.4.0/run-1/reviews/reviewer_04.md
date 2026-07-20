# Reviewer role

Role_id: `statistics-reproducibility` (CORE). Owned axes: statistical-rigor; reproducibility; data-resource-quality. Other domains are excluded unless statistical design directly limits a stated claim.

# Material inspected and assessment boundary

Inspected the specified frozen manuscript, journal profile, inventory, and fact base; supplied hashes were verified. Scientific-review only. Figures, tables, supplements, raw data, code, protocols, and checklists were not supplied. The manuscript remained read-only.

# Journal standard applied

Nature Article, initial submission: technical soundness, strength of evidence, independent validation, replicability, and Methods sufficient to interpret and reproduce results (profile requirements N001, N002, N006).

# Overall assessment

The central quantitative claims are unsupported. Pseudoreplication and uncorrected screening compromise discovery; full-cohort selection contaminates validation; and the 3-year AUC is inconsistent and not assessable under reported follow-up. The clinical model and mouse study also lack design-compatible inference.

# Major strengths

- Patient, cell, event, and mouse counts and key design limitations are stated.
- The reported events, follow-up, candidate count, selection, missingness, and absent PH/CI checks permit audit.
- The three data domains could support future validation if analysed at correct biological units.

# BLOCKING issues

## SR-01

- concern_id: SR-01
- proposed issue_key: `single_cell_pseudoreplication_multiplicity`
- axis: `statistical-rigor`
- role_scope: `PRIMARY`
- severity: `BLOCKING`
- exact claim_pointer: Results, “Single-cell discovery identifies an immune-evasion programme”; Abstract, “A five-gene immune-evasion score”.
- exact evidence_pointer/unavailable reason: Patients and methods, “Single-cell discovery”: eight patients, 46,218 cells, cell-level Wilcoxon tests, cells treated as independent, nominal P < 0.05, no multiple-testing correction; Results reports 1,842 nominal genes and EVA1 Spearman r = −0.41, P = 0.03 across eight tumours.
- evidence_status: `LOCATED`
- falsifiable concern: Treating cells as independent inflates the effective sample size and ignores patient clustering; nominal screening of thousands of genes creates extensive false discovery. Moreover, r = −0.41 with only eight independent tumours is not evidently compatible with the reported two-sided P = 0.03. The candidate pool and EVA1 association may not survive patient-level inference and multiplicity control.
- concrete resolution_test: Reanalyse with patient as the biological unit (pseudobulk or a patient-aware mixed model), prespecified contrasts, FDR control, and leave-one-patient-out sensitivity; independently recompute the eight-tumour correlation. Report effect sizes, adjusted P values, and reconcile r/P. The discovery must remain materially stable.
- journal_gate: N002/N006 technical soundness and interpretable, replicable Methods.
- confidence: 0.99

## SR-02

- concern_id: SR-02
- proposed issue_key: `full_data_selection_validation_leakage`
- axis: `statistical-rigor`
- role_scope: `PRIMARY`
- severity: `BLOCKING`
- exact claim_pointer: Discussion, “The score was validated in an independent subset”; Abstract, reported AUC and survival separation.
- exact evidence_pointer/unavailable reason: Patients and methods, “Score construction and validation”: stepwise gene selection, cutoffs, coefficient signs, and missing-value rules were chosen using all 72 patients before the same cohort was split 70:30; no external cohort was used.
- evidence_status: `LOCATED`
- falsifiable concern: The nominal validation subset contributed to feature and rule selection and is therefore not independent. Its performance is optimistically biased and cannot validate the locked score.
- concrete resolution_test: Apply a completely prespecified formula to an external cohort processed independently, or estimate internal performance with nested resampling in which every selection and cutoff operation occurs inside each training fold. Report optimism-corrected performance with confidence intervals; reserve “independent validation” for untouched data.
- journal_gate: Nature-level strong evidence, independent validation, and replicability under N002/N006.
- confidence: 1.00

## SR-03

- concern_id: SR-03
- proposed issue_key: `three_year_auc_unreconciled_censoring`
- axis: `statistical-rigor`
- role_scope: `PRIMARY`
- severity: `BLOCKING`
- exact claim_pointer: Abstract AUC 0.91; Results validation-set AUC 0.84; Figure 3 legend AUC 0.86; Discussion, “Its high AUC supports immediate use”.
- exact evidence_pointer/unavailable reason: Study population reports median follow-up among survivors of 18 months; Results states 3-year outcome was unavailable for many survivors. The time-dependent ROC estimator, censoring treatment, event/at-risk counts, confidence interval, and source outputs are not supplied.
- evidence_status: `LOCATED`
- falsifiable concern: Three incompatible AUCs and incomplete 3-year observation make the headline discrimination estimate unreconciled and potentially biased or undefined under the analysis actually used.
- concrete resolution_test: Identify the exact evaluation set and prespecified 3-year time-dependent AUC estimator; report censoring method, numbers at risk/events, uncertainty, and complete output provenance. One value must reproduce from deposited code/data, and sensitivity to censoring assumptions must be acceptable.
- journal_gate: N002 technical soundness and N006 interpretability/replicability.
- confidence: 1.00

# MAJOR issues

## SR-04

- concern_id: SR-04
- proposed issue_key: `clinical_model_instability_incomplete_inference`
- axis: `statistical-rigor`
- role_scope: `PRIMARY`
- severity: `MAJOR`
- exact claim_pointer: Results, “The score remained significant in the selected multivariable model (hazard ratio 2.4, P = 0.04).”
- exact evidence_pointer/unavailable reason: 31 deaths; 27 genes plus 18 clinical/molecular covariates entered the workflow; stepwise selection used all 72 patients; analysis-specific complete-case exclusion; no prospective sample-size calculation; PH not examined; hazard ratios reported without confidence intervals; final model composition is unavailable.
- evidence_status: `LOCATED`
- falsifiable concern: Candidate complexity relative to 31 events, data-driven selection, unquantified complete-case attrition, and unchecked model assumptions can yield unstable coefficients and anti-conservative inference.
- concrete resolution_test: Provide a cohort/missingness flow and effective N/events for every model; prespecify or use justified penalization; report the complete model, coefficient/effect-size CIs, PH diagnostics, and bootstrap stability/optimism. Conclusions must remain under plausible missing-data and modelling sensitivities.
- journal_gate: N002 strength/technical soundness; N006 sufficient Methods.
- confidence: 0.99

## SR-05

- concern_id: SR-05
- proposed issue_key: `analysis_resources_not_reproducible`
- axis: `reproducibility; data-resource-quality`
- role_scope: `PRIMARY`
- severity: `MAJOR`
- exact claim_pointer: Data and code availability; the claimed five-gene score throughout Abstract, Methods, Results, and Discussion.
- exact evidence_pointer/unavailable reason: Raw single-cell data, model code, coefficient values, and final patient-level dataset are explicitly not deposited; only request-based processed summaries are offered; seeds and software versions were not recorded. Inventory confirms raw data, source code, figures, tables, and supplements were not supplied.
- evidence_status: `LOCATED`
- falsifiable concern: Neither the discovery nor score can be independently reconstructed, audited, or applied; request-only summaries do not establish accession readiness or computational provenance.
- concrete resolution_test: Deposit de-identified raw/processed data with stable accessions and metadata, executable code, exact formula/cutoffs/missingness rules, seeds, software/environment lockfile, and a clean-run reproduction log matching every reported estimate.
- journal_gate: N006 replicable Methods and Nature-level replicability.
- confidence: 1.00

## SR-06

- concern_id: SR-06
- proposed issue_key: `mouse_design_cannot_test_sensitization`
- axis: `statistical-rigor`
- role_scope: `PRIMARY`
- severity: `MAJOR`
- exact claim_pointer: Abstract and Results, “sensitized xenografts to anti-PD-1”; Results, “EVA1 inhibition sensitizes HCC to anti-PD-1”.
- exact evidence_pointer/unavailable reason: Mouse experiment: n = 5 per EVA1 group, all mice received anti-PD-1, cage-order allocation, unblinded measurement, day-21 unpaired t-test, no independent repeat.
- evidence_status: `LOCATED`
- falsifiable concern: With no anti-PD-1-negative arms, treatment sensitization is an untested EVA1-by-treatment interaction. Cage-order assignment can confound groups, and a single small terminal comparison provides fragile inference.
- concrete resolution_test: Conduct randomized, allocation-concealed, blinded, replicated 2×2 EVA1-status × anti-PD-1 experiments; prespecify exclusions and a repeated-measures or tumour-growth-summary model; report interaction effect sizes and CIs. Sensitization requires a reproducible interaction, not a within-treatment group difference.
- journal_gate: N002 strong, technically sound evidence; N006 reproducible design.
- confidence: 1.00

# MINOR issues

None.

# EDITORIAL issues

None.

# Claim-ceiling risks

- The score is an exploratory, internally developed association, not an independently validated predictor.
- No numerical 3-year discrimination claim is supportable until the AUC and censoring analysis reproduce.
- The mouse experiment supports at most a preliminary day-21 association under anti-PD-1; it does not estimate sensitization.
- Universal performance cannot be inferred from one centre, 31 events, and no transportability test.

# Required versus optional additional work

Required: resolve SR-01–SR-06, including patient-level/FDR-controlled discovery, leakage-free independent validation, reproducible time-dependent AUC, stable survival modelling, accessible analysis resources, and a treatment-interaction animal design.

Optional after those gates pass: subgroup performance by aetiology and additional prespecified sensitivity analyses.

# Journal-fit posture

The current evidence does not meet Nature’s technical-soundness, independent-validation, and replicability expectations for the stated central claims. This is an evidence posture, not a prediction of editorial disposition.

# NOT APPLICABLE items

- Competing-risk modelling is not required for the reported all-cause overall-survival endpoint itself.
- Meta-analytic between-site heterogeneity is not applicable because only one clinical centre is reported.

# NOT ASSESSABLE items

- Raw outputs, figure/table agreement beyond AUC labels, and patient-level event/censoring patterns: source materials not supplied.
- Exact AUC implementation, model formula, coefficients, baseline hazard, cutoffs, calibration, and resampling variability: code/output not supplied.
- Distributional suitability of t-tests/chi-squared tests and influence diagnostics: group-level data not supplied.
- Whether undisclosed batch, library, cage, or assay effects were modelled: design matrices and metadata not supplied.

# Evidence anchors

- Manuscript: Patients and methods—Study population, Single-cell discovery, Score construction and validation, Mouse experiment, Statistical analysis.
- Manuscript: Results—Single-cell discovery, five-gene survival prediction, EVA1 perturbation.
- Manuscript: Data and code availability; Figure legends, especially Figure 3.
- Inventory: absent figures, tables, supplements, raw data, code, protocols, and checklists.
- Shared fact base: reported evidence, analysis details, and assessment boundaries.

# Confidence and reasons

Overall confidence: 0.99. The decisive concerns follow from explicit design and reporting statements rather than inferred omissions. Confidence is lower only for the direction and magnitude of reanalysed effects because source data and code are unavailable.

Omitted concerns: 0.
