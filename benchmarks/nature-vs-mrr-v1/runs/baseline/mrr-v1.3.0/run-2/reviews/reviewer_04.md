# Reviewer role

`statistics-reproducibility` — statistical validity and reproducibility, with emphasis on the biological unit of inference, multiplicity, feature/model selection, split independence, survival analysis and censoring, performance uncertainty and calibration, robustness, data/code availability, and exact numerical consistency.

# Material inspected and assessment boundary

Inspected the frozen manuscript (`manuscript.md`, SHA-256 `d51224a5ec717a268dadeee2fe9461a7b9d8c833f5b459be2d522a88d5c0006f`), `00_input_inventory.json`, the frozen Nature journal profile (SHA-256 `6f6386d213e195d6ec26d0c177568f27753208425a6a15ce139b1ac2235fd6eb`), and the shared factual intake (SHA-256 `947b2ed3c744626d5eadc56845b65f223c6b0d4336bd765e3c714acf4ff4a976`). The assessment is read-only and limited to the supplied text and legends. Figure images, tables, supplements, patient-level data, raw single-cell data, model outputs, code, protocols, and reporting checklists were not supplied. Consequently, source-level numerical verification and visual figure assessment are `NOT ASSESSABLE`; explicit statements in the manuscript about analyses not performed or materials not deposited are assessable.

# Journal standard applied

Nature Article, initial submission; broad-flagship standard. The work is assessed for outstanding scientific importance and a major conceptual advance of interdisciplinary interest, technical soundness, strength of evidence, appropriately bounded conclusions, and Methods sufficient for interpretation and replication. The following design ceilings are enforced: a retrospective single-centre association cannot by itself establish universal generalizability or treatment-selection utility; reuse or splitting of a dataset after full-dataset feature/model selection is not independent validation; and a perturbation experiment without a design that estimates a treatment interaction cannot establish sensitization.

# Overall assessment

`FAIL` for statistical validity, validation independence, numerical coherence, central treatment-selection inference, and reproducibility as presently reported. `NOT ASSESSABLE` for source-data reconciliation and any unreported analyses that may exist outside the packet. The central claims depend on a pseudoreplicated, uncorrected discovery analysis; a highly adaptive full-cohort model-selection pipeline followed by a non-independent split; incompletely specified survival-performance estimation with follow-up shorter than the claimed horizon; and a mouse design that cannot identify anti-PD-1 sensitization. These are not presentation defects. They undermine the inferential chain supporting a universal, clinically actionable predictor and a treatment-sensitization mechanism.

# Major strengths

- The manuscript states key design limitations unusually clearly, including the eight-patient single-cell discovery set, 31 deaths, lack of prospective sample-size calculation, full-cohort stepwise selection, absence of external validation, absence of calibration and decision-curve analyses, and the small unblinded mouse study.
- Patient counts, cell counts, event counts, follow-up, and major modelling stages are reported separately, allowing the unit-of-inference and overfitting risks to be identified.
- The manuscript reports an interpretable clinical outcome and names candidate clinical covariates, which could support a properly prespecified, leakage-free reanalysis.
- The use of two cell lines and a non-targeting guide provides a preliminary perturbational signal, although it does not resolve the causal or treatment-interaction claims.

# BLOCKING issues

## B1

- **Severity:** `BLOCKING`
- **Controlled axis:** `statistical-rigor`
- **Proposed issue_key:** `SC_PATIENT_UNIT_MULTIPLICITY`
- **Exact manuscript anchor:** Patients and methods, “Single-cell discovery”: “Differential expression between high- and low-infiltration tumours was tested at the cell level using a Wilcoxon rank-sum test. Cells were treated as independent observations. Genes with nominal P < 0.05 were retained; no multiple-testing correction was applied.”
- **Falsifiable concern:** The exposure is defined at the tumour/patient level, but 46,218 cells from only eight patients were analysed as independent observations. This inflates the effective sample size and yields invalid standard errors and P values under within-patient correlation. Retaining genes at nominal `P < 0.05` across a transcriptome-scale screen also makes false discovery expected. The 1,842 selected genes, including the 27 passed into modelling, therefore lack a valid discovery error rate.
- **Concrete resolution test:** Re-run differential expression with patient as the independent unit using a documented pseudobulk or patient-aware mixed-model strategy that respects pairing and batch structure; define the high/low-infiltration contrast reproducibly; apply a prespecified multiple-testing procedure; report effect sizes, uncertainty, adjusted P values, and sensitivity to each of the eight patients. The downstream signature must be rebuilt without using genes that fail this corrected discovery gate.
- **Journal gate if applicable:** Nature profile `N002` (technical soundness and strength of evidence) and `N006` (Methods sufficient for interpretation and replication).
- **Confidence:** `0.99`
- **Required versus optional:** `REQUIRED`

## B2

- **Severity:** `BLOCKING`
- **Controlled axis:** `statistical-rigor`
- **Proposed issue_key:** `FULL_DATA_SELECTION_LEAKAGE`
- **Exact manuscript anchor:** Patients and methods, “Score construction and validation”: “Five genes were retained after stepwise selection using the entire 72-patient dataset. Expression cutoffs, coefficient signs, and missing-value rules were also chosen using the full dataset. The same 72 patients were then randomly divided 70:30 into a training set and a validation set.”
- **Falsifiable concern:** Outcome-informed feature selection and tuning were completed on all 72 patients before the split. The nominal validation subset therefore influenced gene retention, cutoffs, coefficient signs, and missing-data rules and is not independent. Its AUC and survival separation are optimistically biased; describing it as validation is false under the stated workflow.
- **Concrete resolution test:** Demonstrate a fully locked score evaluated in a genuinely untouched external cohort, or repeat the complete discovery/selection/tuning pipeline inside each training resample using nested resampling while reserving a never-accessed test set. All preprocessing, missingness rules, cutoffs, feature selection, and hyperparameter choices must occur without outcome access in the assessment data. Report optimism-corrected performance with uncertainty and label internal resampling as internal validation only.
- **Journal gate if applicable:** Nature profile `N001` (outstanding-importance Article conclusion), `N002`, and `N006`.
- **Confidence:** `1.00`
- **Required versus optional:** `REQUIRED`

## B3

- **Severity:** `BLOCKING`
- **Controlled axis:** `statistical-rigor`
- **Proposed issue_key:** `SURVIVAL_AUC_CENSORING_INCOHERENCE`
- **Exact manuscript anchor:** Study population: “Thirty-one deaths were observed. Median follow-up among surviving patients was 18 months.” Results, “The five-gene score predicts survival”: “The Results text reports a validation-set 3-year mortality AUC of 0.84. Figure 3 reports an AUC of 0.86, whereas the Abstract reports 0.91. Because median follow-up was 18 months, 3-year outcome status was unavailable for many surviving patients.”
- **Falsifiable concern:** Three mutually inconsistent AUC values are reported for what appears to be the same endpoint, and the analysis method does not explain how censoring before three years was handled. A conventional binary ROC analysis that treats incompletely followed survivors as known three-year outcomes would be biased. With an approximately 30% validation subset and many censored before the horizon, the effective number of assessable events/non-events may be too small for a stable estimate.
- **Concrete resolution test:** Reconcile Abstract, Results, and Figure 3 against one frozen output; state the exact analysis population, event definition, prediction horizon, number at risk and number of events by three years, censoring distribution, and time-dependent AUC estimator; show its handling of censoring assumptions; and report a confidence interval derived without leakage. If reliable three-year estimation is not supported by follow-up, remove that horizon or collect adequate follow-up.
- **Journal gate if applicable:** Nature profile `N002` and `N006`.
- **Confidence:** `1.00`
- **Required versus optional:** `REQUIRED`

## B4

- **Severity:** `BLOCKING`
- **Controlled axis:** `clinical-validity`
- **Proposed issue_key:** `NO_TREATMENT_SELECTION_ESTIMAND`
- **Exact manuscript anchor:** Impact and implications: “used to select anti-PD-1 therapy”; Patients and methods, “Study population”: a resection cohort with “treatment after recurrence” listed among available variables; Discussion: “Its high AUC supports immediate use for selecting anti-PD-1 therapy.”
- **Falsifiable concern:** Prognosis after resection is not a treatment-selection estimand. The manuscript reports neither a defined anti-PD-1-treated clinical cohort nor a comparison treatment, treatment-by-score interaction, randomized allocation, counterfactual framework, or decision threshold. An AUC for mortality cannot establish differential benefit from anti-PD-1.
- **Concrete resolution test:** Either remove all predictive treatment-selection and immediate-use claims, or evaluate a prespecified score-by-treatment interaction in an appropriately designed and independently validated cohort with a defined treatment, comparator, outcome time origin, confounder strategy, calibration, and decision-relevant performance. The evidence must distinguish prognostic association from predictive treatment effect.
- **Journal gate if applicable:** Nature profile `N001` and `N002`; clinical-utility claim gate.
- **Confidence:** `1.00`
- **Required versus optional:** `REQUIRED`

## B5

- **Severity:** `BLOCKING`
- **Controlled axis:** `experimental-design`
- **Proposed issue_key:** `ANTI_PD1_INTERACTION_UNIDENTIFIED`
- **Exact manuscript anchor:** Patients and methods, “Mouse experiment”: “All mice received anti-PD-1.” Results, “In mice, day-21 tumours were smaller in the EVA1-depleted group (P = 0.048)”; Abstract: “sensitized xenografts to anti-PD-1 treatment.”
- **Falsifiable concern:** Comparing EVA1-depleted versus control tumours when every mouse receives anti-PD-1 identifies, at most, an EVA1-depletion effect under anti-PD-1 exposure. It cannot identify sensitization, which requires evidence that the effect of anti-PD-1 differs by EVA1 status. The same growth effect seen in vitro without immune-cell co-culture further leaves a treatment-independent growth mechanism plausible.
- **Concrete resolution test:** Use a randomized factorial design containing EVA1 control/depletion crossed with anti-PD-1/control treatment, with prespecified primary endpoint and a formal EVA1-by-treatment interaction estimate and confidence interval. Establish target engagement and adequate biological replication. Without such evidence, replace “sensitizes” with a design-supported statement limited to smaller tumours under the observed conditions.
- **Journal gate if applicable:** Nature profile `N002`; treatment-sensitization claim gate.
- **Confidence:** `1.00`
- **Required versus optional:** `REQUIRED`

# MAJOR issues

## M1

- **Severity:** `MAJOR`
- **Controlled axis:** `statistical-rigor`
- **Proposed issue_key:** `EVENTS_MODEL_COMPLEXITY_INSTABILITY`
- **Exact manuscript anchor:** Study population: “Thirty-one deaths were observed” and “No prospective sample-size calculation was performed.” Score construction: “Twenty-seven genes selected from the single-cell comparison were entered into a Cox regression model with the 18 available clinical and molecular covariates. Five genes were retained after stepwise selection using the entire 72-patient dataset.”
- **Falsifiable concern:** Forty-five candidate inputs, additional data-derived cutoffs/rules, and stepwise selection are far too adaptive for 31 observed events to support stable coefficients or reproducible variable retention without strong shrinkage and rigorous internal validation. Reported significance after selection does not account for selection uncertainty.
- **Concrete resolution test:** Provide a prespecified sample-size/precision rationale tied to event count; substantially reduce or prespecify candidate degrees of freedom, or use an appropriate penalized model; quantify global and coefficient shrinkage, optimism, and selection stability with nested resampling; and report the full distribution of model performance and coefficient variability.
- **Journal gate if applicable:** Nature profile `N002` and `N006`.
- **Confidence:** `0.99`
- **Required versus optional:** `REQUIRED`

## M2

- **Severity:** `MAJOR`
- **Controlled axis:** `statistical-rigor`
- **Proposed issue_key:** `SURVIVAL_MODEL_DIAGNOSTICS_MISSING`
- **Exact manuscript anchor:** Statistical analysis: “The proportional-hazards assumption was not examined. Hazard ratios and P values were reported without confidence intervals.” Results: “hazard ratio 2.4, P = 0.04.”
- **Falsifiable concern:** The Cox effect estimate is not interpretable without its precision, analysis sample, covariate specification, functional forms, and assessment of proportional hazards. A data-selected model with a marginal P value may be unstable, and an untested PH assumption can make a single hazard ratio misleading.
- **Concrete resolution test:** Report the exact multivariable formula, analysis `n` and events, coefficient/hazard-ratio confidence intervals, tests and graphical diagnostics for proportional hazards, functional-form checks for continuous predictors, influential-observation diagnostics, and a prespecified alternative such as time-varying effects or restricted mean survival time if PH fails.
- **Journal gate if applicable:** Nature profile `N002` and `N006`.
- **Confidence:** `0.99`
- **Required versus optional:** `REQUIRED`

## M3

- **Severity:** `MAJOR`
- **Controlled axis:** `data-resource-quality`
- **Proposed issue_key:** `COMPLETE_CASE_DENOMINATORS_SELECTION`
- **Exact manuscript anchor:** Study population: “Records with missing values were excluded from each analysis.” Score construction: “missing-value rules were also chosen using the full dataset.”
- **Falsifiable concern:** Analysis-specific complete-case exclusion can produce different, undisclosed denominators and selection bias when missingness relates to prognosis. Outcome-informed selection of missing-value rules adds leakage and model degrees of freedom. Reproducibility and comparability of reported estimates are therefore impaired.
- **Concrete resolution test:** Supply a variable-by-patient missingness summary, denominators and event counts for every analysis, reasons for missingness, comparison of included versus excluded patients, and a prespecified missing-data strategy performed within training/resampling folds. Include sensitivity analyses under plausible missing-data mechanisms.
- **Journal gate if applicable:** Nature profile `N002` and `N006`.
- **Confidence:** `0.98`
- **Required versus optional:** `REQUIRED`

## M4

- **Severity:** `MAJOR`
- **Controlled axis:** `statistical-rigor`
- **Proposed issue_key:** `PERFORMANCE_INFERENCE_INCOMPLETE`
- **Exact manuscript anchor:** Score construction and validation: “No external cohort, independent laboratory assay, calibration analysis, or decision-curve analysis was used. Performance was compared only with the five-gene model; BCLC stage and other clinical baselines were not evaluated.”
- **Falsifiable concern:** Discrimination alone, particularly after leakage, does not establish useful prediction. The manuscript gives no calibration, absolute-risk accuracy, clinically relevant threshold performance, uncertainty, failure analysis, or incremental value over standard prognostic information.
- **Concrete resolution test:** In independent data, report time-specific discrimination with confidence intervals, calibration-in-the-large, calibration slope and plots, prediction error/Brier score, clinically interpretable risk strata and thresholds, and decision-curve or other justified utility analysis. Compare fairly against prespecified clinical baselines such as BCLC using the same patients, horizon, censoring method, and uncertainty procedure.
- **Journal gate if applicable:** Nature profile `N001`, `N002`, and `N006`.
- **Confidence:** `1.00`
- **Required versus optional:** `REQUIRED` for clinical-actionability claims; otherwise the claim must be narrowed to exploratory prognostic association.

## M5

- **Severity:** `MAJOR`
- **Controlled axis:** `statistical-rigor`
- **Proposed issue_key:** `EVA1_CORRELATION_NUMERIC_INCONSISTENCY`
- **Exact manuscript anchor:** Results, “Single-cell discovery identifies an immune-evasion programme”: “EVA1 was higher in low-infiltration tumours and correlated inversely with a T-cell score (Spearman r = −0.41, P = 0.03).” Figure 2 legend: “Association between EVA1 expression and the T-cell score in eight tumours.”
- **Falsifiable concern:** A Spearman correlation of magnitude 0.41 across only eight independent tumours is not compatible with a conventional two-sided `P = 0.03`; standard large-sample approximation gives a non-significant value near 0.3, with exact inference likewise unable to support the reported strength. The discrepancy suggests an incorrect denominator, cell-level pseudoreplication, or transcription/output error.
- **Concrete resolution test:** State the exact unit and `n`, handling of ties, correlation and P-value implementation, and provide the eight tumour-level paired values. Recompute an exact or permutation-based tumour-level Spearman test with confidence interval and reconcile the Results and Figure 2 source output. If cells were used as replicates, repeat at the patient level.
- **Journal gate if applicable:** Nature profile `N002` and `N006`.
- **Confidence:** `0.98`
- **Required versus optional:** `REQUIRED`

## M6

- **Severity:** `MAJOR`
- **Controlled axis:** `reproducibility`
- **Proposed issue_key:** `SCORE_NOT_EXECUTABLE`
- **Exact manuscript anchor:** Score construction and validation: “A locked five-gene formula was evaluated”; Data and code availability: “model code, coefficient values, and the final patient-level analysis dataset are not deposited. Random seeds and software versions were not recorded.”
- **Falsifiable concern:** A claimed locked predictor cannot be independently calculated or audited without gene identities, coefficients, transformations, cutoffs, coefficient signs, assay/preprocessing specification, and missing-value rules. The random split and performance estimates also cannot be reproduced without seeds, versions, code, and analysis data.
- **Concrete resolution test:** Provide a complete executable model specification and analysis workflow; record software/package versions, seeds, split indices, preprocessing and endpoint code; deposit code plus sufficiently de-identified patient-level data or a controlled-access route with a reproducible data dictionary; and demonstrate that an independent rerun reproduces every reported coefficient, sample size, event count, and performance value.
- **Journal gate if applicable:** Nature profile `N006`.
- **Confidence:** `1.00`
- **Required versus optional:** `REQUIRED`

## M7

- **Severity:** `MAJOR`
- **Controlled axis:** `experimental-design`
- **Proposed issue_key:** `MOUSE_RANDOMIZATION_BLINDING_PRECISION`
- **Exact manuscript anchor:** Mouse experiment: “five animals per group,” “Allocation order followed cage order; investigators were aware of group assignment during measurement,” “Tumour volume was compared on day 21 using an unpaired t-test,” and “No independent replicate experiment was performed.”
- **Falsifiable concern:** Cage-order allocation is not demonstrated randomization and may confound group with cage/order. Unblinded measurement can bias a manually measured outcome. With `n = 5` per group, a single endpoint P value of 0.048 without effect size, confidence interval, distributional diagnostics, attrition accounting, or independent replication provides fragile evidence.
- **Concrete resolution test:** Repeat with concealed randomized allocation, blinded measurement, prespecified primary endpoint and sample-size rationale, explicit animal-level exclusions/attrition, effect size and confidence interval, and analysis appropriate to longitudinal tumour measurements and clustering/cage structure. Show robustness to influential animals and reproduce the result in an independent experiment.
- **Journal gate if applicable:** Nature profile `N002` and `N006`.
- **Confidence:** `0.99`
- **Required versus optional:** `REQUIRED` for the therapeutic-mechanism claim.

## M8

- **Severity:** `MAJOR`
- **Controlled axis:** `experimental-design`
- **Proposed issue_key:** `IN_VITRO_REPLICATES_UNCERTAINTY`
- **Exact manuscript anchor:** Functional experiments: “Cell growth was measured after 72 hours. Interferon-response transcripts and PD-L1 protein were measured in the same cultures.” Results: “reduced 72-hour cell growth by 24% in Huh7 cells and 19% in Hep3B cells.”
- **Falsifiable concern:** The number and definition of biological versus technical replicates, independent experimental runs, exclusion rules, raw distributions, effect uncertainty, and multiplicity across growth, PD-L1, and transcript outcomes are not reported. The supplied percentages therefore cannot be evaluated for sampling uncertainty or reproducibility.
- **Concrete resolution test:** Report independent biological replicate counts and experimental runs for every endpoint, technical nesting, randomization/blinding where applicable, exact effect estimates with confidence intervals and plotted raw biological-unit data, and a prespecified multiplicity strategy. Replicate the principal effect independently.
- **Journal gate if applicable:** Nature profile `N002` and `N006`.
- **Confidence:** `0.96`
- **Required versus optional:** `REQUIRED`

# MINOR issues

## m1

- **Severity:** `MINOR`
- **Controlled axis:** `statistical-rigor`
- **Proposed issue_key:** `GENERIC_TEST_ASSUMPTIONS`
- **Exact manuscript anchor:** Statistical analysis: “Continuous variables were compared using t-tests and categorical variables using chi-squared tests.”
- **Falsifiable concern:** This generic description does not identify the contrasts, analysis denominators, variance assumptions, sparse-cell handling, paired structure, or diagnostics. With small subgroups such as five patients with other/undocumented aetiology, chi-squared approximations may be invalid.
- **Concrete resolution test:** Map every reported comparison to its test and biological unit; state equal/unequal-variance handling, independence/paired structure, sparse-count alternative, and diagnostics; report effect sizes and confidence intervals rather than P values alone.
- **Journal gate if applicable:** Nature profile `N006`.
- **Confidence:** `0.91`
- **Required versus optional:** `REQUIRED`

## m2

- **Severity:** `MINOR`
- **Controlled axis:** `writing-clarity`
- **Proposed issue_key:** `VALIDATION_TERMINOLOGY`
- **Exact manuscript anchor:** Figure 3 legend: “Development and validation of the five-gene mortality model”; Discussion: “The score was validated in an independent subset.”
- **Falsifiable concern:** “Independent subset” is statistically inaccurate because the subset participated in full-dataset feature and rule selection. This wording may cause readers to infer an independence that the design explicitly lacks.
- **Concrete resolution test:** Replace “independent validation” with “post-selection random subset evaluation” or another exact description until a genuinely untouched cohort is used; ensure all manuscript sections and Figure 3 use the same terminology.
- **Journal gate if applicable:** Nature profile `N002`.
- **Confidence:** `1.00`
- **Required versus optional:** `REQUIRED`

# EDITORIAL issues

## E1

- **Severity:** `EDITORIAL`
- **Controlled axis:** `writing-clarity`
- **Proposed issue_key:** `STATISTICAL_REPORTING_MAP`
- **Exact manuscript anchor:** Statistical analysis: “Nominal two-sided P < 0.05 was considered significant for all analyses.”
- **Falsifiable concern:** A single blanket significance sentence obscures which analyses were confirmatory versus exploratory and which multiplicity families were controlled. It also encourages dichotomous interpretation despite the small and adaptive analyses.
- **Concrete resolution test:** Label analyses as prespecified confirmatory or exploratory; define each multiplicity family and adjustment; report exact P values together with effect sizes and confidence intervals; avoid using threshold crossing as the primary evidentiary interpretation.
- **Journal gate if applicable:** Nature profile `N006`.
- **Confidence:** `0.95`
- **Required versus optional:** `REQUIRED` for transparent reporting after the analyses are corrected.

# Claim-ceiling risks

- **Universal applicability:** `FAIL`. Anchor: Abstract, “universally applicable predictor,” and Discussion, “application across HCC aetiologies and treatment settings.” The single-centre cohort contains 58/72 patients with viral hepatitis, only nine with metabolic liver disease, and five with other or undocumented aetiologies. No external cohort supports transport across sites, assays, aetiologies, disease stages, or treatment settings.
- **Clinical actionability and immediate deployment:** `FAIL`. Anchor: Impact and implications, “immediately deployable biomarker,” and Discussion, “immediate use for selecting anti-PD-1 therapy.” No independently validated, executable model; calibrated absolute risks; operating threshold; clinical comparator; decision utility; or treatment-effect interaction is presented.
- **Independent validation:** `FAIL`. Anchor: Discussion, “validated in an independent subset.” The outcome-informed full-cohort selection and tuning preceded the split.
- **Causal immune-evasion driver:** `FAIL`. Anchor: Abstract, “causal driver of immune escape,” and Results, “directly suppresses anti-tumour immunity.” The tumour-level association is numerically inconsistent as reported, the in vitro design lacks immune-cell co-culture, and growth/PD-L1/transcript changes do not by themselves identify causal immune exclusion.
- **Anti-PD-1 sensitization:** `FAIL`. Anchor: Abstract, “sensitized xenografts to anti-PD-1 treatment.” With all mice receiving anti-PD-1, no interaction is estimable.
- **Exploratory association and preliminary dependency:** Potentially supportable only after valid patient-level single-cell inference, leakage-free survival modelling, numerical reconciliation, and uncertainty reporting. This lower ceiling does not establish clinical utility or broad-flagship generality.

# Required versus optional additional work

## Required

1. Reanalyse single-cell discovery at the patient level with multiplicity control and patient-level robustness.
2. Rebuild and evaluate the score with leakage-free selection and genuinely independent external validation, or narrow the work to exploratory model development and report honest internal optimism correction.
3. Fully specify survival endpoints, time origins, censoring handling, analysis denominators, PH diagnostics, effect uncertainty, and a valid time-dependent performance estimator.
4. Reconcile all AUC values and the EVA1 correlation from auditable source outputs.
5. Address model complexity, missing data, selection instability, calibration, clinical comparators, threshold performance, and decision utility in proportion to the intended claim.
6. Use a factorial experiment and treatment-interaction analysis to support sensitization; otherwise remove that claim.
7. Provide reproducible score coefficients/rules, code, seeds, environments, split indices, and an auditable data-access route; report complete replicate-level methods and uncertainty for cell and mouse experiments.
8. Restrict universal, causal, clinical-deployment, and treatment-selection language to what the corrected design can establish.

## Optional

- After the required gates are passed, evaluate temporal and geographically distinct validation cohorts, prespecified aetiology/site/sex/disease-stage subgroup performance, assay transferability, and failure modes. These strengthen transportability but cannot substitute for the required independent validation.
- Compare alternative parsimonious or penalized model specifications and report sensitivity to modelling choices.
- Add net-reclassification summaries only if they are prespecified, uncertainty-quantified, and secondary to calibration and decision utility.

# Journal-fit posture

`FAIL` for the present Nature Article claim package. Even if the reported associations were reproduced, a small retrospective single-centre development cohort, eight-patient discovery set, non-independent validation, and non-factorial perturbation study do not presently support the manuscript’s claimed universal predictor, immediate clinical utility, or anti-PD-1 sensitization at a broad-flagship evidentiary threshold. A substantially narrower exploratory biomarker/mechanism manuscript might become technically defensible after the blocking analyses are corrected, but Nature-level outstanding importance and interdisciplinary reach would still require independently replicated, causally coherent, and clinically consequential evidence. This is a journal-fit posture, not a prediction of editorial outcome.

# NOT ASSESSABLE items

- `NOT ASSESSABLE`: Whether any raw or processed numerical output supports the reported AUCs, hazard ratio, correlation, cell effects, and mouse P value, because source data, model outputs, tables, and figure images were not supplied.
- `NOT ASSESSABLE`: Exact model coefficients, gene identities, transformations, split membership, analysis denominators, event/censoring tables, calibration, subgroup results, and robustness outputs beyond what the manuscript explicitly reports.
- `NOT ASSESSABLE`: Whether the underlying study has additional unreported experiments, code, protocols, raw data, or reporting checklists. Packet absence is not treated as proof that these do not exist.
- `NOT ASSESSABLE`: Figure-level visual integrity, error-bar definitions, point counts, raw-data overlays, consistency of plotted values, and image-related exclusions because figure images were not supplied.
- `NOT ASSESSABLE`: Independent reproduction of the analysis, because the manuscript states that code, coefficients, patient-level data, random seeds, and software versions were not deposited or recorded.
- `NOT ASSESSABLE`: Reference-level semantic support, because browsing and full-text reference inspection are outside this reviewer boundary.

# Evidence anchors

- Patients and methods, “Single-cell discovery”: eight patients; cell-level Wilcoxon analysis; cells treated as independent; nominal `P < 0.05`; no multiplicity correction.
- Patients and methods, “Study population”: 72 patients; 31 deaths; median follow-up among survivors 18 months; analysis-specific record exclusion; no prospective sample-size calculation.
- Patients and methods, “Score construction and validation”: 27 genes plus 18 covariates; full-cohort stepwise selection and rule tuning; subsequent 70:30 split; no external cohort, calibration, decision curve, independent assay, or clinical baseline.
- Statistical analysis: PH assumption not examined; no confidence intervals; blanket nominal significance threshold.
- Results, “The five-gene score predicts survival,” plus Abstract and Figure 3 legend: AUC `0.84`, `0.86`, and `0.91` for the claimed three-year endpoint.
- Results, “Single-cell discovery identifies an immune-evasion programme,” and Figure 2 legend: Spearman `r = −0.41`, `P = 0.03`, across eight tumours.
- Patients and methods, “Mouse experiment”: all mice received anti-PD-1; `n = 5` per group; cage-order allocation; unblinded measurement; day-21 t-test; no independent replicate.
- Data and code availability: no deposited raw single-cell data, model code, coefficients, or final patient-level dataset; seeds and software versions not recorded.

# Confidence and reasons

Overall confidence: `0.99`. The principal failures follow directly from explicit manuscript statements rather than from unavailable packet components: cells were treated as independent; no multiple-testing correction was used; full-dataset selection and tuning occurred before the split; follow-up is shorter than the claimed prediction horizon for many survivors; AUC values conflict; all mice received anti-PD-1; and core reproducibility materials were not deposited or recorded. Confidence is slightly below 1 only because source outputs and figure images are unavailable, so the exact magnitude of numerical errors and the possibility of additional unreported analyses cannot be assessed.
