# Reviewer role

**Role ID:** statistics-reproducibility  
**Functional lens:** biological replicate and unit of inference; sample size and event support; model selection; split independence and information leakage; survival analysis; multiplicity; uncertainty; missing data; robustness; and data/code reproducibility.

This report does not assess novelty, molecular plausibility, ethics, reference content, or editorial presentation except where those matters directly determine statistical validity or reproducibility.

# Material inspected and assessment boundary

I inspected only the following frozen inputs:

- `manuscript.md`, SHA-256 `d51224a5ec717a268dadeee2fe9461a7b9d8c833f5b459be2d522a88d5c0006f`
- `00_input_inventory.json`
- `nature-journal-profile.json`, SHA-256 `6f6386d213e195d6ec26d0c177568f27753208425a6a15ce139b1ac2235fd6eb`
- `02_shared_fact_base.md`, SHA-256 `947b2ed3c744626d5eadc56845b65f223c6b0d4336bd765e3c714acf4ff4a976`

The packet lacks figure images, tables, supplementary information, raw data, source code, protocols, reporting checklists, and patient-level or source-level numerical outputs. Consequently, numerical results cannot be independently recomputed, discrepancies cannot be adjudicated, and unreported analytical safeguards must not be presumed to have been performed.

# Journal standard applied

The target is **Nature**, Article, initial submission. I applied the frozen profile’s broad-flagship standard: outstanding scientific importance, technical soundness, evidence strong enough for the conclusions, interdisciplinary accessibility, and methods sufficient to interpret and replicate the results. The primary requirements used here are N001 (conclusions of outstanding scientific importance), N002 (technical soundness and strength of evidence), and N006 (methods necessary for interpretation and replication). I do not make the final editorial decision.

# Overall assessment

The manuscript’s central statistical claims are not currently supportable. The apparent validation is not independent because feature selection, coefficient/sign decisions, cutoffs, and missing-value rules were determined on all 72 patients before splitting. The discovery analysis treats 46,218 cells from only eight patients as independent observations, inflating the effective sample size. The claimed three-year mortality discrimination is not transparently defined for censored survival data, is estimated despite median follow-up of only 18 months, and conflicts across the Abstract, Results, and Figure 3 legend. The xenograft design cannot estimate sensitization to anti-PD-1 because every animal received anti-PD-1 and there is no treatment-by-EVA1 interaction contrast. Finally, no raw data, code, model coefficients, seeds, or software versions are available.

Critical gates:

| Critical gate | Status | Basis |
|---|---|---|
| Biological replicate/unit of inference is valid | **FAIL** | Cell-level tests treat cells nested within eight patients as independent. |
| Sample size and events support model development | **FAIL** | Thirty-one deaths support a workflow beginning with 27 genes plus 18 covariates, stepwise selection, and data-adaptive cutoffs only weakly, with no sample-size calculation or optimism correction. |
| Validation split is independent and leakage-free | **FAIL** | All model and cutoff decisions used the full 72-patient dataset before the 70:30 split. |
| Survival estimand, censoring, and uncertainty are adequately handled | **FAIL** | Three-year outcome availability is incomplete; the AUC method is unspecified; proportional hazards were not checked; confidence intervals are omitted. |
| Multiplicity is controlled | **FAIL** | Single-cell discovery uses nominal P values without correction, and the wider analysis declares nominal P < 0.05 throughout. |
| Missing-data handling is interpretable and robust | **FAIL** | Per-analysis record exclusion is reported without missingness counts, patterns, assumptions, or sensitivity analysis. |
| Core numerical claims are internally consistent | **FAIL** | The three-year AUC is 0.91, 0.84, or 0.86 depending on the manuscript location; the reported EVA1 correlation P value is not evidently compatible with an eight-tumour analysis. |
| Data and code permit independent reproduction | **FAIL** | Patient-level data, raw single-cell data, code, coefficients, seeds, and versions are unavailable. |
| Independent recomputation of reported values | **NOT ASSESSABLE** | Underlying tables, figures, data, and code were not supplied. |
| Functional-experiment precision and biological replication | **NOT ASSESSABLE** | Numbers of independent biological replicates and complete quantitative outputs are not reported. |

# Major strengths

- The manuscript explicitly discloses several consequential limitations: the eight-patient single-cell discovery set; the cell-level testing; absence of multiplicity correction; full-cohort stepwise selection; lack of an external cohort; lack of calibration and decision-curve analysis; no prospective sample-size calculation; missing-value exclusion; no proportional-hazards assessment; and the small, non-blinded mouse experiment.
- The clinical cohort size, aetiology distribution, death count, and median follow-up are stated, allowing the reader to identify the mismatch between model complexity and available events.
- The text distinguishes some stages of the analysis and reports enough about the order of model development and splitting to reveal leakage.
- The manuscript identifies the AUC inconsistency rather than concealing it and states major reproducibility omissions in the Data and code availability section.

# BLOCKING issues

## STAT-REP-B01

- **issue_key:** STAT-REP-B01
- **axis:** statistical-rigor
- **severity:** BLOCKING
- **anchor:** Patients and methods, “Differential expression between high- and low-infiltration tumours was tested at the cell level using a Wilcoxon rank-sum test. Cells were treated as independent observations.”
- **falsifiable concern:** The exposure is defined at the tumour/patient level, but the analysis treats thousands of cells nested within eight patients as independent replicates. If within-patient correlation is acknowledged, the effective replication is eight patients, not 46,218 cells; nominal cell-level P values will generally be anti-conservative and can change the 27-gene candidate set and every downstream score result.
- **concrete resolution test:** Re-run discovery with patient/tumour as the unit of inference using pseudobulk aggregation or a validated mixed-effects framework that models patient clustering. Pre-specify contrasts and covariates, report per-patient cell counts and effect estimates with confidence intervals, and show that the five selected genes and directional effects survive a patient-level sensitivity analysis and correction for multiplicity. The gate passes only if the principal discovery and score are not dependent on cell-level pseudoreplication.
- **journal gate:** **FAIL** — violates N002 technical soundness and N006 interpretability; the discovery basis for a broad causal and clinical conclusion is statistically invalid as presented.
- **confidence:** 0.99

## STAT-REP-B02

- **issue_key:** STAT-REP-B02
- **axis:** statistical-rigor
- **severity:** BLOCKING
- **anchor:** Patients and methods, “Five genes were retained after stepwise selection using the entire 72-patient dataset. Expression cutoffs, coefficient signs, and missing-value rules were also chosen using the full dataset. The same 72 patients were then randomly divided 70:30 into a training set and a validation set.”
- **falsifiable concern:** The nominal validation subset has already influenced gene retention, coefficient direction, cutoffs, and missing-data decisions. Therefore it is not independent validation, and its AUC and survival separation are optimistically biased. With only 31 deaths, starting from 27 genes plus 18 covariates compounds overfitting and model-selection instability.
- **concrete resolution test:** Freeze the full analytical pipeline before any evaluation in a patient cohort that was never used for discovery, feature selection, coefficient estimation, cutoff selection, or missing-data-rule development. Alternatively, if only the present cohort is available, label the work development-only and estimate internal optimism using correctly nested resampling in which every selection and preprocessing step is repeated inside each training fold; provide optimism-corrected discrimination, calibration, coefficients, and selection stability. A single post hoc split of 72 patients cannot pass this gate.
- **journal gate:** **FAIL** — the claimed “independent subset” is false under the stated chronology, failing N002; the universal, deployment-ready conclusion also fails the evidentiary bar in N001.
- **confidence:** 1.00

## STAT-REP-B03

- **issue_key:** STAT-REP-B03
- **axis:** statistical-rigor
- **severity:** BLOCKING
- **anchor:** Results, “The Results text reports a validation-set 3-year mortality AUC of 0.84. Figure 3 reports an AUC of 0.86, whereas the Abstract reports 0.91. Because median follow-up was 18 months, 3-year outcome status was unavailable for many surviving patients.”
- **falsifiable concern:** There is no single auditable value for the principal performance claim. Moreover, a conventional binary ROC analysis at three years would mishandle censoring, while a time-dependent AUC requires a specified estimator, censoring assumptions, number at risk, and uncertainty. With approximately 22 patients in a 30% subset and many lacking observed three-year status, the estimate may be extremely unstable or undefined under adequate follow-up.
- **concrete resolution test:** Identify the exact analysis population, time origin, event definition, censoring date, estimator for time-dependent AUC, and handling of competing events; report numbers at risk and observed events at three years plus a confidence interval. Recompute the value from deposited code and data, reconcile every manuscript location to the same prespecified estimate, and perform sensitivity analyses at time horizons supported by follow-up. The gate passes only if an independently reproducible, censoring-aware estimate remains interpretable with adequate effective sample size.
- **journal gate:** **FAIL** — the manuscript’s headline predictive statistic is internally inconsistent and not reproducibly defined, failing N002 and N006.
- **confidence:** 1.00

## STAT-REP-B04

- **issue_key:** STAT-REP-B04
- **axis:** experimental-design
- **severity:** BLOCKING
- **anchor:** Patients and methods, “Ten mice bearing subcutaneous Huh7 xenografts were allocated to control or EVA1-depleted cells, with five animals per group. All mice received anti-PD-1.” Results, “We conclude that EVA1 inhibition sensitizes HCC to anti-PD-1.”
- **falsifiable concern:** Because all animals received anti-PD-1, the experiment can estimate a contrast between EVA1-depleted and control tumours in the presence of anti-PD-1 but cannot estimate whether EVA1 depletion changes response to anti-PD-1. “Sensitization” requires evidence for an interaction relative to matched no-anti-PD-1 conditions. Cage-order allocation and non-blinded measurement further permit systematic bias, while n=5 per group and one experiment provide weak precision.
- **concrete resolution test:** Conduct a randomized, blinded, adequately powered factorial experiment with EVA1 status and anti-PD-1 treatment as crossed factors, including all four groups, allocation concealment, prespecified exclusions, longitudinal tumour modelling, effect estimates with confidence intervals, and a prespecified EVA1-by-treatment interaction test. Repeat in an independent model. The sensitization claim passes only if the interaction—not merely a within-treatment group difference—is reproducible.
- **journal gate:** **FAIL** — the design does not identify the treatment-sensitization estimand required by the central therapeutic conclusion, failing N002 and the evidence strength expected under N001.
- **confidence:** 1.00

## STAT-REP-B05

- **issue_key:** STAT-REP-B05
- **axis:** reproducibility
- **severity:** BLOCKING
- **anchor:** Data and code availability, “Raw single-cell data, model code, coefficient values, and the final patient-level analysis dataset are not deposited. Random seeds and software versions were not recorded.”
- **falsifiable concern:** An independent analyst cannot recreate the discovery set, the five-gene score, patient classifications, random split, Cox model, AUC, or figures. Omitting coefficient values also means the proposed biomarker cannot be calculated from the paper, contradicting “immediately deployable.”
- **concrete resolution test:** Deposit de-identified source/analysis data at the appropriate permissible level, raw or accessioned single-cell data, cell and sample metadata, complete executable code, environment/version lock files, random seeds, model coefficients, transformations, cutoff definitions, missing-data rules, and a machine-readable data dictionary. Provide a clean-run workflow that reproduces every reported numerical result and display from immutable inputs; where individual-level data cannot be public, provide controlled access and a sufficiently complete shareable reproduction object.
- **journal gate:** **FAIL** — methods and materials are not sufficient to interpret or replicate the work under mandatory requirement N006.
- **confidence:** 1.00

# MAJOR issues

## STAT-REP-M01

- **issue_key:** STAT-REP-M01
- **axis:** statistical-rigor
- **severity:** MAJOR
- **anchor:** Single-cell discovery, “Genes with nominal P < 0.05 were retained; no multiple-testing correction was applied.” Statistical analysis, “Nominal two-sided P < 0.05 was considered significant for all analyses.”
- **falsifiable concern:** Screening transcriptome-scale hypotheses at nominal P < 0.05 can generate a large false-positive set; later selection among 27 genes and repeated clinical/functional analyses adds further researcher degrees of freedom. The stated 1,842 genes may substantially reflect expected false discoveries.
- **concrete resolution test:** Define hypothesis families; apply false-discovery-rate control to genome-wide discovery; distinguish confirmatory from exploratory tests; and provide adjusted P values or q values alongside effect sizes and confidence intervals. Demonstrate that the selected five genes and main conclusions persist under the prespecified multiplicity framework.
- **journal gate:** **FAIL** — the evidence chain is not statistically reliable enough for N002 until multiplicity is controlled.
- **confidence:** 0.99

## STAT-REP-M02

- **issue_key:** STAT-REP-M02
- **axis:** statistical-rigor
- **severity:** MAJOR
- **anchor:** Statistical analysis, “The proportional-hazards assumption was not examined. Hazard ratios and P values were reported without confidence intervals.” Results, “The score remained significant in the selected multivariable model (hazard ratio 2.4, P = 0.04).”
- **falsifiable concern:** The Cox estimate is not interpretable without its uncertainty, model specification, event counts per fitted parameter, functional-form checks, and proportional-hazards diagnostics. Stepwise-selection P values and hazard ratios are additionally biased by selection. If proportional hazards fails, a single HR may obscure time-varying effects.
- **concrete resolution test:** Provide the complete prespecified model, number of complete cases and deaths, coefficients and 95% confidence intervals, Schoenfeld-residual or equivalent proportional-hazards tests and plots, continuous-variable functional-form checks, influence diagnostics, and an alternative estimand such as restricted mean survival time or time-varying coefficients when needed. Validate with bootstrap or nested-resampling inference that includes selection.
- **journal gate:** **FAIL** — N002 requires uncertainty and model adequacy sufficient to support the reported association.
- **confidence:** 0.99

## STAT-REP-M03

- **issue_key:** STAT-REP-M03
- **axis:** statistical-rigor
- **severity:** MAJOR
- **anchor:** Study population, “Records with missing values were excluded from each analysis.” Score construction and validation, “missing-value rules were also chosen using the full dataset.”
- **falsifiable concern:** Analysis-specific complete-case deletion can change the cohort and event count across results and is unbiased only under restrictive assumptions. Data-adaptive missing-value rules selected using the full dataset also leak validation information. The direction and magnitude of bias cannot be judged without variable-level missingness and inclusion flow.
- **concrete resolution test:** Report missing counts and percentages by variable and outcome group, analysis-specific sample sizes and deaths, reasons/patterns for missingness, and the assumed missing-data mechanism. Predefine missing-data handling within training data only; use appropriate multiple imputation with outcome and auxiliary variables when justified; pool estimates correctly; and compare complete-case, imputed, and plausible-sensitivity results.
- **journal gate:** **FAIL** — missing-data uncertainty prevents reliable interpretation under N002 and replication under N006.
- **confidence:** 0.98

## STAT-REP-M04

- **issue_key:** STAT-REP-M04
- **axis:** data-resource-quality
- **severity:** MAJOR
- **anchor:** Score construction and validation, “No external cohort, independent laboratory assay, calibration analysis, or decision-curve analysis was used. Performance was compared only with the five-gene model; BCLC stage and other clinical baselines were not evaluated.”
- **falsifiable concern:** Discrimination alone, especially after leakage, does not establish calibration, incremental value, net benefit, transportability, or clinical usability. Without comparison to accepted prognostic variables and stage, the five-gene score may add no information beyond routine clinical data.
- **concrete resolution test:** In truly external cohorts and an independently validated assay, report prespecified time-dependent discrimination with confidence intervals, calibration-in-the-large, calibration slope and plots, Brier or integrated prediction error, clinical-baseline and combined-model comparisons, and decision-curve analysis at clinically justified thresholds. Assess transportability across centres and major aetiologies without fitting or threshold revision in the test sets.
- **journal gate:** **FAIL** — a Nature-level claim of universal clinical deployment does not meet N001/N002 without independent, comparative, and decision-relevant validation.
- **confidence:** 0.99

## STAT-REP-M05

- **issue_key:** STAT-REP-M05
- **axis:** statistical-rigor
- **severity:** MAJOR
- **anchor:** Results, “EVA1 was higher in low-infiltration tumours and correlated inversely with a T-cell score (Spearman r = −0.41, P = 0.03).” Figure 2 legend, “Association between EVA1 expression and the T-cell score in eight tumours.”
- **falsifiable concern:** If the eight tumours are the independent observations, a two-sided Spearman correlation of magnitude 0.41 would not ordinarily yield P = 0.03; the quoted pair is therefore internally suspect unless a different sample size or inferential method was used. If cells were used to obtain P = 0.03, the same nesting problem as STAT-REP-B01 applies.
- **concrete resolution test:** State the exact observation unit, n, rank-correlation implementation, tie handling, hypothesis direction, and confidence interval; deposit the eight tumour-level pairs; and reproduce r and P from the declared code. Correct the result or justify the estimator. Do not use cell-level observations to test a tumour-level association.
- **journal gate:** **FAIL** — the reported inferential pair requires reconciliation under N002 and N006.
- **confidence:** 0.97

## STAT-REP-M06

- **issue_key:** STAT-REP-M06
- **axis:** experimental-design
- **severity:** MAJOR
- **anchor:** Mouse experiment, “Allocation order followed cage order; investigators were aware of group assignment during measurement. Tumour volume was compared on day 21 using an unpaired t-test. No independent replicate experiment was performed.”
- **falsifiable concern:** Cage-ordered allocation can confound group with cage/order, unblinded measurement can bias volume ascertainment, and a single day-21 t-test discards longitudinal information and may be sensitive to distributional assumptions or one animal. P = 0.048 at n=5 per group provides no evidence of robust magnitude without raw points and a confidence interval.
- **concrete resolution test:** Randomize animals independently with cage balance, conceal allocation during measurement, prespecify sample size and exclusion rules, display every animal, report effect size and confidence interval, and analyse repeated tumour volumes with an appropriate animal-level longitudinal model. Replicate the experiment independently and show robustness to nonparametric or permutation analysis.
- **journal gate:** **FAIL** — the current quantitative animal evidence does not meet N002 technical-soundness expectations for a central therapeutic claim.
- **confidence:** 0.99

## STAT-REP-M07

- **issue_key:** STAT-REP-M07
- **axis:** reproducibility
- **severity:** MAJOR
- **anchor:** Functional experiments, “EVA1 was depleted using one CRISPR guide RNA in Huh7 and Hep3B cells.” Results, “EVA1 depletion reduced 72-hour cell growth by 24% in Huh7 cells and 19% in Hep3B cells.”
- **falsifiable concern:** The number of independent biological experiments, replicate hierarchy, well-to-experiment aggregation, variance, effect uncertainty, exclusions, and statistical tests are not reported. Technical wells cannot substitute for independent experiments, and without these details the precision and reproducibility of the percentages cannot be assessed.
- **concrete resolution test:** Report independent biological replicate counts and dates/batches, technical replicate structure, raw points, prespecified aggregation unit, exact tests, effect sizes with confidence intervals, and all exclusions for each cell line and readout. Repeat independently and analyse the experiment—not each well—as the biological unit.
- **journal gate:** **NOT ASSESSABLE** for the underlying repeatability, but the reporting currently **FAILS** N006.
- **confidence:** 0.96

# MINOR issues

## STAT-REP-m01

- **issue_key:** STAT-REP-m01
- **axis:** statistical-rigor
- **severity:** MINOR
- **anchor:** Statistical analysis, “Continuous variables were compared using t-tests and categorical variables using chi-squared tests.”
- **falsifiable concern:** The blanket test specification does not state variance assumptions, distributional diagnostics, paired/independent structure, or handling of sparse categorical cells. With small subsets and rare categories, asymptotic chi-squared or equal-variance t-tests may be unreliable.
- **concrete resolution test:** Map every reported comparison to its exact test, observation unit, assumptions, and sample size; use Welch, exact, permutation, or robust alternatives where assumptions fail; and show that conclusions are insensitive to reasonable alternatives.
- **journal gate:** **FAIL** for replicable method specification under N006 until clarified.
- **confidence:** 0.92

## STAT-REP-m02

- **issue_key:** STAT-REP-m02
- **axis:** reproducibility
- **severity:** MINOR
- **anchor:** Score construction and validation, “The same 72 patients were then randomly divided 70:30 into a training set and a validation set.” Data and code availability, “Random seeds and software versions were not recorded.”
- **falsifiable concern:** The exact split and performance cannot be regenerated, and performance in such small subsets may vary materially across arbitrary seeds.
- **concrete resolution test:** Publish patient split identifiers, the randomization algorithm and seed, software/package versions, and the distribution of performance across repeated correctly nested resamples.
- **journal gate:** **FAIL** under N006.
- **confidence:** 1.00

## STAT-REP-m03

- **issue_key:** STAT-REP-m03
- **axis:** statistical-rigor
- **severity:** MINOR
- **anchor:** Results, “The high-score group had shorter overall survival than the low-score group (log-rank P = 0.02).”
- **falsifiable concern:** The group cutoff was selected on the full dataset, so the log-rank P value is post-selection and cannot be interpreted conventionally. Grouping a continuous score also loses information and can exaggerate apparent separation.
- **concrete resolution test:** Treat the score continuously in primary analysis; if a clinical threshold is needed, predefine it in development data and evaluate it unchanged externally. Report risk tables, group sizes, deaths, censoring marks, effect estimates, and confidence intervals.
- **journal gate:** **FAIL** for the current inferential interpretation under N002.
- **confidence:** 0.99

# EDITORIAL issues

## STAT-REP-E01

- **issue_key:** STAT-REP-E01
- **axis:** figures-and-tables
- **severity:** EDITORIAL
- **anchor:** Figure 3 legend, “Panel C labels the validation AUC as 0.86.”
- **falsifiable concern:** Figure 3 cannot be audited because the image and source table were not supplied, and its principal value conflicts with the text.
- **concrete resolution test:** Supply the figure, source-data table, exact analysis population, confidence interval, and reproducible generation code; reconcile the value with Abstract and Results.
- **journal gate:** **NOT ASSESSABLE** for figure integrity; current cross-text consistency **FAILS** N002/N006.
- **confidence:** 1.00

## STAT-REP-E02

- **issue_key:** STAT-REP-E02
- **axis:** writing-clarity
- **severity:** EDITORIAL
- **anchor:** Discussion, “The score was validated in an independent subset.”
- **falsifiable concern:** “Independent” is technically inaccurate because the subset contributed to all model-development decisions before the split.
- **concrete resolution test:** Replace “independent subset” with “post-selection random subset from the same cohort” and label its analysis exploratory unless a genuinely untouched cohort is evaluated.
- **journal gate:** **FAIL** for accurate statistical interpretation under N002.
- **confidence:** 1.00

## STAT-REP-E03

- **issue_key:** STAT-REP-E03
- **axis:** figures-and-tables
- **severity:** EDITORIAL
- **anchor:** Statistical analysis, “Hazard ratios and P values were reported without confidence intervals.”
- **falsifiable concern:** P values alone do not convey precision or clinical magnitude, particularly with 31 events and selected models.
- **concrete resolution test:** For every primary estimate, report effect size, 95% confidence interval, exact P value, analysis n, event count, and missing count; display individual observations where feasible.
- **journal gate:** **FAIL** under N002/N006 until uncertainty is reported.
- **confidence:** 1.00

# Claim-ceiling risks

- **“AUC of 0.91 for 3-year mortality”**: no defensible numerical ceiling is available until the 0.91/0.84/0.86 conflict is reconciled and censoring-aware performance is reproduced. At present this should be described only as an unreconciled development-cohort estimate.
- **“validated in an independent subset”**: must be reduced to an exploratory post-selection split of the same cohort; it is not independent validation.
- **“clinically actionable,” “immediately deployable,” and “used to select anti-PD-1 therapy”**: the data support, at most, development of a prognostic association in one retrospective resection cohort. No anti-PD-1-treated clinical cohort, treatment-effect interaction, calibration, decision analysis, clinical comparator, external validation, or executable score is provided.
- **“universally applicable” and “all major HCC aetiologies”**: the cohort is small, single-centre, dominated by viral hepatitis, and contains only nine metabolic and five other/undocumented cases. No stable subgroup performance can be inferred.
- **“EVA1 excludes T cells”**: the patient-level association is based on eight tumours and has an apparently inconsistent r/P pair; even a corrected association would remain correlative.
- **“EVA1 inhibition sensitizes HCC to anti-PD-1”**: the mouse design contains no anti-PD-1-negative control arms and therefore cannot test sensitization.
- **“ready for therapeutic development”**: a single unblinded, cage-ordered, n=5-per-group, non-replicated experiment with P = 0.048 does not establish a robust treatment effect.

# Required versus optional additional work

## Required

1. Reanalyse single-cell discovery with patient/tumour as the inferential unit and false-discovery-rate control.
2. Replace the leaked split with truly independent external validation or relabel the manuscript as development-only and use fully nested resampling for honest internal validation.
3. Reduce and justify model complexity relative to 31 deaths; publish the complete frozen model and assess selection stability and optimism.
4. Recompute survival performance with explicitly defined censoring-aware methods, adequate horizons, confidence intervals, calibration, and complete numbers at risk; reconcile all AUC values.
5. Fully report missingness and conduct principled, training-only missing-data handling plus sensitivity analyses.
6. Check Cox assumptions, functional forms, influence, and uncertainty; report all effect sizes with confidence intervals.
7. Compare the model with established clinical baselines and test incremental performance and net benefit.
8. Test anti-PD-1 sensitization using a randomized, blinded factorial experiment with a treatment-by-EVA1 interaction and an independent replicate.
9. Report functional-experiment biological replicates, replicate hierarchy, raw points, uncertainty, and exact analysis.
10. Deposit the data, code, coefficients, metadata, seeds, versions, and a clean-run reproducibility workflow needed to regenerate all results and figures.

## Optional but valuable

- Evaluate model transportability across centres, assay batches, major HCC aetiologies, stages, and treatment settings after the required external validation is in place.
- Prefer continuous-score presentation and clinically justified thresholds over median or outcome-optimized dichotomization.
- Add bootstrap confidence intervals for calibration and decision curves and prespecify clinically meaningful performance criteria rather than relying on significance thresholds.
- Use a prospective, registered validation study once the development model and assay are frozen.

# Journal-fit posture

From the statistics-reproducibility lens, the current version is **not ready for Nature peer-review acceptance and requires fundamental redesign/reanalysis rather than statistical polishing**. The central claims depend on invalid independence assumptions, information leakage, unresolvable performance values, and non-identifying intervention contrasts. Even if the numerical results were corrected, the present evidence would support an exploratory, single-centre biomarker-development study and preliminary perturbation findings—not a universal, clinically deployable predictor or an established anti-PD-1-sensitization mechanism. This is an assessment of evidence strength, not a final editorial decision.

# NOT ASSESSABLE items

- Exact reproduction of the 1,842-gene discovery set, because raw single-cell data, cell metadata, and code are unavailable.
- Exact reproduction of the five-gene coefficients, patient scores, selected cutoffs, train/validation membership, Cox models, and AUCs, because coefficients, patient-level data, seed, and code are unavailable.
- Which of 0.91, 0.84, and 0.86 corresponds to any valid source output, because figure images and source tables are unavailable.
- Figure-level checks of labels, distributions, individual points, censoring marks, risk tables, and image integrity, because figure images were not supplied.
- Robustness to influential patients, alternative preprocessing, batch effects, imputation, model specification, or resampling, because the analysis dataset and code are unavailable.
- Calibration, net benefit, comparator performance, and external transportability, because the manuscript explicitly states these analyses/cohorts were not used.
- Biological replicate counts, variability, and statistical precision for cell growth, PD-L1, and interferon-response assays, because replicate-level reporting is absent.
- Exact animal effect magnitude and distribution, because individual animal values and Figure 4 were not supplied.

# Evidence anchors

- **Study population:** “72 adults”; “Thirty-one deaths”; “Median follow-up among surviving patients was 18 months”; “Records with missing values were excluded from each analysis”; “No prospective sample-size calculation was performed.”
- **Single-cell discovery:** “eight patients”; “46,218 cells”; “tested at the cell level”; “Cells were treated as independent observations”; “nominal P < 0.05”; “no multiple-testing correction.”
- **Score construction and validation:** “Twenty-seven genes”; “18 available clinical and molecular covariates”; “stepwise selection using the entire 72-patient dataset”; full-data selection of “Expression cutoffs, coefficient signs, and missing-value rules”; later “randomly divided 70:30.”
- **Validation scope:** “No external cohort”; no “calibration analysis” or “decision-curve analysis”; no comparison with “BCLC stage and other clinical baselines.”
- **Survival analysis:** proportional hazards “was not examined”; “Hazard ratios and P values were reported without confidence intervals.”
- **Results:** “hazard ratio 2.4, P = 0.04”; AUC values of “0.84,” “0.86,” and “0.91”; incomplete three-year outcome status.
- **Tumour-level association:** “Spearman r = −0.41, P = 0.03” and Figure 2’s “eight tumours.”
- **Mouse experiment:** “five animals per group”; “All mice received anti-PD-1”; “Allocation order followed cage order”; investigators aware of assignment; day-21 unpaired t-test; no independent replicate.
- **Data and code availability:** no deposited raw single-cell data, model code, coefficients, final patient-level dataset, seeds, or software versions.

# Confidence and reasons

**Overall confidence: 0.99.** The highest-severity findings follow directly from explicit statements about the analytical chronology, unit of analysis, event count, follow-up, AUC conflict, mouse design, and unavailable reproducibility materials. Confidence is lower only for the exact cause of the EVA1 r/P discrepancy and the magnitude of bias or instability, because source data and code were not provided. I have therefore marked recomputation-dependent matters NOT ASSESSABLE and have not inferred that unreported analyses or materials exist.
