# Reviewer role

Independent reviewer 03 (`role_id: study-design`). Functional lens: integrated design validity across the retrospective clinical cohort, biomarker/prediction intended use, single-cell biological unit, wet-lab mechanism controls, and animal/translational experiment. I assess whether the stated designs can identify the claimed effects; I do not adjudicate matters outside this lens or make the final editorial decision.

# Material inspected and assessment boundary

I inspected only the following frozen inputs:

- `manuscript.md`, SHA-256 `d51224a5ec717a268dadeee2fe9461a7b9d8c833f5b459be2d522a88d5c0006f`.
- `00_input_inventory.json`.
- `nature-journal-profile.json`, SHA-256 `6f6386d213e195d6ec26d0c177568f27753208425a6a15ce139b1ac2235fd6eb`.
- `02_shared_fact_base.md`, SHA-256 `947b2ed3c744626d5eadc56845b65f223c6b0d4336bd765e3c714acf4ff4a976`.

The packet contains manuscript text and figure legends, but not figure images, tables, supplementary information, raw data, patient-level data, source code, protocols, or reporting checklists. Numerical outputs and implementation fidelity are therefore not independently verifiable. Absence from this packet is not treated as proof that an unmentioned procedure was not performed; by contrast, procedures that the manuscript explicitly says were not performed are assessed as such.

# Journal standard applied

I applied the frozen Nature Article, initial-submission profile. The controlling standards for this review are N001 (original research of outstanding scientific importance with an interdisciplinary conclusion), N002 (technical soundness, strength of evidence, novelty, field importance, and general interest), N006 (Methods sufficient to interpret and replicate the results), and N007 (required declarations in the submission sequence). For a broad flagship claim, concordance across weak or non-identifying designs is not a substitute for causal completeness, genuinely independent validation, generalizability, and an explicit link between biomarker use and treatment benefit.

# Overall assessment

The manuscript poses a clinically important question and attempts to connect single-cell discovery, clinical outcome modelling, perturbation, and an in vivo experiment. However, every critical inferential bridge is currently broken. The score is developed using the entire cohort before the nominal split, so the reported “validation” is contaminated. The retrospective resection cohort measures overall survival, not differential benefit from anti-PD-1, so it cannot support treatment selection. The single-cell test treats 46,218 cells as independent although the relevant biological replication is eight patients. A single-guide depletion without rescue or direct target confirmation cannot identify an EVA1-specific mechanism. Finally, because all mice receive anti-PD-1 and the experiment lacks an untreated arm, it cannot estimate sensitization or an EVA1-by-treatment interaction.

Critical gate outcomes:

| Critical gate | Outcome | Basis |
|---|---|---|
| Clinical prediction development and independent validation | **FAIL** | Full-cohort feature selection, coefficient/cutoff choices, and missing-value rules precede the 70:30 split. |
| Biomarker intended use: selection of anti-PD-1 therapy | **FAIL** | The cohort is defined by resection and overall survival; no anti-PD-1 treatment comparison or treatment-by-score interaction is reported. |
| Single-cell biological unit and multiplicity control | **FAIL** | Cells are treated as independent observations across eight tumours, with nominal \(P<0.05\) and no multiple-testing correction. |
| EVA1-specific perturbation and immune mechanism | **FAIL** | One guide, no rescue, no direct target-engagement assay, and no immune-cell functional system. |
| In vivo anti-PD-1 sensitization | **FAIL** | All animals receive anti-PD-1; there is no factorial untreated control and no immune readout. |
| Animal model suitability for immune-checkpoint inference | **NOT ASSESSABLE** | Host strain/species, immune status, anti-PD-1 reagent/species reactivity, and engraftment context are not reported. |
| Ethics and animal-welfare reporting | **FAIL** | Approving bodies, protocol identifiers, consent procedure, animal protocol, and humane endpoints are not reported. |
| Reproducible model specification and numerical verification | **FAIL** for specification; **NOT ASSESSABLE** for numerical verification | Coefficients, code, final patient-level dataset, seeds, and software versions are not deposited; figures/tables/source outputs were not supplied. |

# Major strengths

- The question linking tumour state, immune context, prognosis, and therapeutic response is potentially important across cancer biology and translational oncology.
- The manuscript is unusually explicit about several design limitations, including “Cells were treated as independent observations,” full-dataset score construction, use of one CRISPR guide, absence of rescue, cage-order allocation, lack of blinding, and lack of an independent animal replicate. This transparency makes the inferential problems identifiable.
- The planned multi-layer architecture could become valuable if each layer used an appropriate biological unit and if the clinical and in vivo experiments directly tested the intended treatment-selection claim.
- The two-cell-line observation is a preliminary replication of a growth phenotype, although it does not yet establish target specificity or immune mechanism.

# BLOCKING issues

## SD-B01 — The nominal validation set is contaminated by full-cohort model development

- **issue_key:** `SD-B01_FULL_COHORT_LEAKAGE`
- **axis:** statistical-rigor
- **severity:** BLOCKING
- **anchor:** Patients and methods, “Twenty-seven genes selected from the single-cell comparison were entered into a Cox regression model with the 18 available clinical and molecular covariates. Five genes were retained after stepwise selection using the entire 72-patient dataset. Expression cutoffs, coefficient signs, and missing-value rules were also chosen using the full dataset.” Also, “The same 72 patients were then randomly divided 70:30 into a training set and a validation set.”
- **falsifiable concern:** Information from every future “validation” patient influenced feature selection, coefficient direction, cutoffs, and missing-data handling. The held-out subset is therefore not independent, and its AUC is an optimistically biased reuse estimate. With 31 deaths and a search over 27 genes plus 18 covariates, model instability and severe overfitting are also plausible.
- **concrete resolution test:** Freeze the estimand, eligible predictors, preprocessing, missing-data procedure, and performance metrics before outcome access in a genuinely external cohort. Develop the complete pipeline using only a development cohort, incorporating all selection and tuning within resampling, then evaluate the untouched external cohort once. Report the full coefficient formula, optimism-corrected discrimination, calibration-in-the-large, calibration slope, time-specific calibration, confidence intervals, and comparison with prespecified clinical baselines. Bootstrap inclusion frequencies or comparable stability analysis should show that the five-gene composition and coefficients are not artifacts of sampling.
- **journal gate:** **FAIL** — N002 technical soundness and strength of evidence; N001 outstanding importance cannot rest on a contaminated validation.
- **confidence:** 0.99

## SD-B02 — The clinical cohort cannot test the stated anti-PD-1 treatment-selection use

- **issue_key:** `SD-B02_INTENDED_USE_MISMATCH`
- **axis:** clinical-validity
- **severity:** BLOCKING
- **anchor:** Impact and implications, “This study identifies a five-gene score that can be measured at diagnosis and used to select anti-PD-1 therapy.” Study population, “The clinical cohort included 72 adults who underwent resection for HCC.” Results, “The high-score group had shorter overall survival than the low-score group.”
- **falsifiable concern:** A prognostic association with overall survival in resected HCC does not identify benefit from anti-PD-1. No defined anti-PD-1-treated population, comparator treatment, response endpoint, treatment allocation mechanism, or score-by-treatment interaction is reported. The same score could be prognostic yet have no predictive value, or even predict harm, for anti-PD-1.
- **concrete resolution test:** State a precise intended-use population, specimen timing, assay, decision threshold, treatment choices, and clinical endpoint. Test the locked score in an independent cohort or, preferably, a prospective-retrospective randomized-trial specimen set containing anti-PD-1 and an appropriate comparator. Estimate a prespecified treatment-by-score interaction with confidence intervals and assess calibration and net benefit at clinically relevant thresholds. Until such evidence exists, replace all treatment-selection and “immediately deployable” claims with a preliminary prognostic-association claim.
- **journal gate:** **FAIL** — N002 strength of evidence and clinical validity; N001 broad significance is not demonstrated for the asserted therapeutic use.
- **confidence:** 0.99

## SD-B03 — Cell-level pseudoreplication and uncontrolled multiplicity invalidate the discovery inference

- **issue_key:** `SD-B03_SC_BIOLOGICAL_UNIT`
- **axis:** experimental-design
- **severity:** BLOCKING
- **anchor:** Single-cell discovery, “Single-cell RNA sequencing was performed on tumour and adjacent tissue from eight patients,” and “Differential expression between high- and low-infiltration tumours was tested at the cell level using a Wilcoxon rank-sum test. Cells were treated as independent observations. Genes with nominal P < 0.05 were retained; no multiple-testing correction was applied.”
- **falsifiable concern:** Infiltration status varies at the tumour/patient level, so thousands of cells from eight patients do not constitute thousands of independent replicates. The reported \(P\) values are anti-conservative, and retaining 1,842 genes at nominal \(P<0.05\) without multiplicity control makes the 27-gene input set highly vulnerable to false discoveries and patient-composition effects.
- **concrete resolution test:** Reanalyse at the patient level with pseudobulk or a hierarchical mixed model that preserves patient as the independent unit and accounts for paired tumour/adjacent sampling where applicable. Prespecify cell-type/state definitions and infiltration grouping, control false discovery rate, report effect sizes and uncertainty, and demonstrate robustness to leave-one-patient-out analysis and compositional covariates. Confirm prioritized genes in an independent patient cohort with an orthogonal assay.
- **journal gate:** **FAIL** — N002 technical soundness and strength of evidence; N001 requires a reproducible biological conclusion, not a cell-count-driven signal.
- **confidence:** 0.99

## SD-B04 — The perturbation design does not identify an EVA1-specific immune mechanism

- **issue_key:** `SD-B04_PERTURBATION_SPECIFICITY`
- **axis:** mechanism-evidence
- **severity:** BLOCKING
- **anchor:** Functional experiments, “EVA1 was depleted using one CRISPR guide RNA in Huh7 and Hep3B cells,” and “The study did not include a second guide, rescue construct, direct target-engagement assay, or immune-cell co-culture.” Results, “These findings show that EVA1 directly suppresses anti-tumour immunity.”
- **falsifiable concern:** A phenotype after one guide can arise from off-target activity, editing toxicity, clonal effects, or a generic change in proliferation. Changes in PD-L1 and three interferon-response transcripts in tumour-only cultures are not a direct measure of immune evasion. The experiment therefore does not establish EVA1 specificity, direction of causality, or a functional effect on immune-cell recognition or killing.
- **concrete resolution test:** Reproduce the phenotype with at least two independent sequence-distinct perturbations; quantify EVA1 depletion/editing and relevant protein target engagement; rescue with a guide-resistant EVA1 construct; and use non-clonal or multiple independent clones where relevant. Then show a prespecified immune-functional phenotype in an appropriate co-culture or organoid system (for example, immune-cell activation or tumour-cell killing) with controls that separate growth rate from immune susceptibility. A causal chain should require EVA1 perturbation, molecular pathway change, and immune-function change, each reversed by rescue.
- **journal gate:** **FAIL** — N002 mechanism and technical soundness; N001 major conceptual advance requires target-specific and functionally immune evidence.
- **confidence:** 0.99

## SD-B05 — The mouse experiment cannot estimate anti-PD-1 sensitization

- **issue_key:** `SD-B05_NO_TREATMENT_INTERACTION`
- **axis:** causal-vs-correlative
- **severity:** BLOCKING
- **anchor:** Mouse experiment, “Ten mice bearing subcutaneous Huh7 xenografts were allocated to control or EVA1-depleted cells, with five animals per group. All mice received anti-PD-1.” Results, “We conclude that EVA1 inhibition sensitizes HCC to anti-PD-1.”
- **falsifiable concern:** With anti-PD-1 held constant and no untreated control, the observed day-21 volume difference cannot distinguish reduced baseline tumour fitness from enhanced anti-PD-1 response. The study does not estimate an EVA1-depletion-by-anti-PD-1 interaction, which is the defining test of sensitization.
- **concrete resolution test:** Use a prespecified factorial design containing control versus EVA1 perturbation crossed with isotype/vehicle versus anti-PD-1, with adequate biological replication. The sensitization claim should require a reproducible interaction effect with confidence intervals, not significance within one treatment arm. Confirm persistent EVA1 perturbation in tumours and measure immune infiltration/activation and tumour-cell killing endpoints. If the model cannot support human checkpoint pharmacology, use a model with an intact, relevant immune system and validated reagent cross-reactivity.
- **journal gate:** **FAIL** — N002 causal strength and translational validity; N001 major advance cannot be inferred without the defining treatment interaction.
- **confidence:** 0.99

## SD-B06 — Human and animal ethics reporting is insufficient

- **issue_key:** `SD-B06_ETHICS_GOVERNANCE`
- **axis:** ethical-governance
- **severity:** BLOCKING
- **anchor:** Ethics, “The manuscript states that the study complied with institutional requirements. The approving committee, protocol number, consent procedure, animal protocol, and humane endpoints are not reported.”
- **falsifiable concern:** Readers and editors cannot verify prospective human-subject oversight, consent/waiver status, animal-use approval, or welfare safeguards. For the animal experiment, absent humane endpoints also prevents assessment of whether tumour burden and termination procedures were ethically governed.
- **concrete resolution test:** Provide the human approving committee, protocol identifier, approval status/date, consent or waiver procedure, and applicable regulatory framework. Provide the animal oversight committee, protocol identifier, species/strain/sex/age, housing and monitoring, analgesia where relevant, prespecified humane endpoints, maximum tumour-burden limits, and confirmation of compliance. Supporting approval documentation should reconcile with the study dates and procedures.
- **journal gate:** **FAIL** — N007 required declarations and N002 technical/ethical assessability.
- **confidence:** 0.98

# MAJOR issues

## SD-M01 — Three-year prediction is not supported by follow-up or a defined censoring-aware estimator

- **issue_key:** `SD-M01_THREE_YEAR_ENDPOINT`
- **axis:** statistical-rigor
- **severity:** MAJOR
- **anchor:** Study population, “Median follow-up among surviving patients was 18 months.” Results, “Because median follow-up was 18 months, 3-year outcome status was unavailable for many surviving patients.”
- **falsifiable concern:** A conventional binary ROC at three years would misclassify or exclude censored patients, and even a censoring-aware time-dependent AUC may be unstable if few patients remain at risk. The reported AUC cannot be interpreted without the estimator, censoring distribution, number at risk, and uncertainty.
- **concrete resolution test:** Report the censoring-aware estimand and estimator, number at risk and observed events by three years, censoring distribution, confidence interval, and sensitivity analyses at adequately supported horizons. If data support is insufficient, remove the three-year metric and use a follow-up horizon justified by the risk set.
- **journal gate:** **FAIL** — N002 statistical soundness and N006 interpretability.
- **confidence:** 0.98

## SD-M02 — The retrospective survival model lacks confounding, missingness, and assumption safeguards

- **issue_key:** `SD-M02_SURVIVAL_MODEL_VALIDITY`
- **axis:** statistical-rigor
- **severity:** MAJOR
- **anchor:** Study population, “Records with missing values were excluded from each analysis.” Statistical analysis, “The proportional-hazards assumption was not examined. Hazard ratios and P values were reported without confidence intervals.”
- **falsifiable concern:** Analysis-specific complete-case populations can differ systematically and yield unstable estimates in a 72-patient cohort. Post-recurrence treatment, stage-related factors, and other variables may confound overall survival, while an unchecked proportional-hazards assumption can make a single hazard ratio misleading. P values without confidence intervals conceal imprecision.
- **concrete resolution test:** Report missingness by variable and analysis, analysis population flow, reasons for missingness, and sensitivity to principled multiple imputation versus complete case. Prespecify a parsimonious covariate set based on the estimand, assess proportional hazards, report confidence intervals and absolute risk estimates, and test robustness to post-baseline treatment handling without conditioning improperly on post-baseline variables.
- **journal gate:** **FAIL** — N002 strength and transparency of evidence; N006 reproducible analysis specification.
- **confidence:** 0.96

## SD-M03 — The score has no clinically relevant comparator, calibration, or transportability evidence

- **issue_key:** `SD-M03_CLINICAL_INCREMENT`
- **axis:** clinical-validity
- **severity:** MAJOR
- **anchor:** Score construction and validation, “No external cohort, independent laboratory assay, calibration analysis, or decision-curve analysis was used. Performance was compared only with the five-gene model; BCLC stage and other clinical baselines were not evaluated.”
- **falsifiable concern:** Discrimination of an isolated model does not show incremental value over standard clinical information, reliable absolute risk, assay reproducibility, or decision benefit. A molecular score could appear strong while adding no useful information to staging or failing across platforms and centres.
- **concrete resolution test:** In independent multi-centre data, compare the locked score with prespecified clinical models and their combination; report discrimination with uncertainty, calibration, reclassification only if properly justified, and decision-curve/net-benefit analysis tied to an explicit decision. Validate the measurement assay and demonstrate cross-platform/centre reproducibility before claiming deployability.
- **journal gate:** **FAIL** — N001 broad clinical importance and N002 evidence strength.
- **confidence:** 0.98

## SD-M04 — The in vivo experiment has allocation, blinding, precision, and endpoint-design weaknesses

- **issue_key:** `SD-M04_ANIMAL_RIGOR`
- **axis:** experimental-design
- **severity:** MAJOR
- **anchor:** Mouse experiment, “Allocation order followed cage order; investigators were aware of group assignment during measurement. Tumour volume was compared on day 21 using an unpaired t-test. No independent replicate experiment was performed.”
- **falsifiable concern:** Cage-ordered allocation can confound group with cage/order; unblinded measurement introduces observer bias; five animals per group without a reported power basis yields low precision; and a single day-21 t-test discards longitudinal tumour trajectories. A marginal \(P=0.048\) in one experiment is fragile.
- **concrete resolution test:** Randomize at the correct experimental unit with cage balance, conceal allocation where feasible, blind measurement and analysis, justify sample size from a prespecified biologically meaningful interaction, model repeated tumour volumes appropriately, report effect sizes and confidence intervals, account for attrition, and reproduce the result in an independent experiment.
- **journal gate:** **FAIL** — N002 technical soundness and reproducibility.
- **confidence:** 0.99

## SD-M05 — The evidence cannot support universality across HCC aetiologies or settings

- **issue_key:** `SD-M05_GENERALIZABILITY`
- **axis:** claim-moderation
- **severity:** MAJOR
- **anchor:** Study population, “The analysis included 58 patients with viral hepatitis, 9 with metabolic liver disease, and 5 with other or undocumented aetiologies.” Discussion, “the single-cell sample size and mechanistic experiments support application across HCC aetiologies and treatment settings.”
- **falsifiable concern:** Eight single-cell donors and a single-centre cohort dominated by viral hepatitis cannot establish performance in metabolic, alcohol-related, mixed, advanced/unresectable, or immunotherapy-treated populations. Two cell lines and one subcutaneous xenograft do not bridge these clinical domains.
- **concrete resolution test:** Replace “universal,” “all major HCC aetiologies,” and cross-setting claims with population-bounded language. To restore them, prospectively validate the locked assay in adequately represented, prespecified aetiology and treatment strata across centres and geographic populations, testing heterogeneity and reporting stratum-specific calibration and performance.
- **journal gate:** **FAIL** — N001 interdisciplinary/general importance and N002 external validity.
- **confidence:** 0.99

## SD-M06 — Correlation across eight tumours is interpreted as T-cell exclusion

- **issue_key:** `SD-M06_CORRELATION_TO_EXCLUSION`
- **axis:** causal-vs-correlative
- **severity:** MAJOR
- **anchor:** Results, “EVA1 was higher in low-infiltration tumours and correlated inversely with a T-cell score (Spearman r = −0.41, P = 0.03). We interpreted this association as evidence that EVA1 excludes T cells from HCC.” Figure 2 legend, “Association between EVA1 expression and the T-cell score in eight tumours.”
- **falsifiable concern:** A cross-sectional correlation in eight tumours does not establish exclusion directionality and may reflect tumour purity, subtype, aetiology, cell-state composition, or other patient-level confounding. The nominal \(P=0.03\) also requires reconciliation with the stated eight-tumour unit.
- **concrete resolution test:** Report the exact observational unit and data used for the correlation, effect uncertainty, and sensitivity to tumour purity/composition and patient covariates. Establish directionality with spatially resolved validation or a controlled immune-functional model showing that EVA1 manipulation changes T-cell recruitment, localization, activation, or killing, with target-specific rescue.
- **journal gate:** **FAIL** — N002 causal evidence and statistical soundness.
- **confidence:** 0.98

# MINOR issues

## SD-m01 — Eligibility, attrition, and analytic denominators are insufficiently specified

- **issue_key:** `SD-m01_COHORT_FLOW`
- **axis:** reproducibility
- **severity:** MINOR
- **anchor:** Study population, “The clinical cohort included 72 adults who underwent resection for HCC at Lakeside Medical Center between January 2018 and December 2022,” and “Records with missing values were excluded from each analysis.”
- **falsifiable concern:** Without inclusion/exclusion criteria, case-ascertainment method, number screened, exclusions, index date, and per-analysis denominators, selection bias and reproducibility cannot be assessed.
- **concrete resolution test:** Add a cohort flow diagram and explicit eligibility, recruitment/ascertainment, index date, follow-up definition, censoring date, exclusions with reasons, and denominator for every analysis.
- **journal gate:** **FAIL** — N006 interpretability and replication.
- **confidence:** 0.95

## SD-m02 — The single-cell grouping and paired sampling structure are not reproducibly defined

- **issue_key:** `SD-m02_SC_GROUP_DEFINITION`
- **axis:** reproducibility
- **severity:** MINOR
- **anchor:** Single-cell discovery, “Differential expression between high- and low-infiltration tumours was tested,” and “Single-cell RNA sequencing was performed on tumour and adjacent tissue from eight patients.”
- **falsifiable concern:** The infiltration metric, cutoff, group sizes, use of adjacent tissue, and handling of tumour/adjacent pairing are unspecified; reasonable alternative definitions could change the gene list.
- **concrete resolution test:** Provide the infiltration-score definition, threshold provenance, patient counts per group, sample-level metadata, paired-sample handling, tumour-cell calling criteria, QC thresholds, and sensitivity analyses across reasonable thresholds.
- **journal gate:** **FAIL** — N006 reproducible Methods.
- **confidence:** 0.94

## SD-m03 — Endpoint and model terminology is internally ambiguous

- **issue_key:** `SD-m03_ENDPOINT_TERMINOLOGY`
- **axis:** writing-clarity
- **severity:** MINOR
- **anchor:** Abstract, “AUC of 0.91 for 3-year mortality”; Results, “validation-set 3-year mortality AUC of 0.84”; Figure 3 legend, “Panel C labels the validation AUC as 0.86.”
- **falsifiable concern:** The inconsistent values and lack of estimator definition make it impossible to know which performance result corresponds to the asserted endpoint.
- **concrete resolution test:** Recompute from a frozen analysis, reconcile all locations to one prespecified estimate, name the estimator and analysis set, and provide its confidence interval and risk-set support.
- **journal gate:** **FAIL** — N002 evidentiary consistency and N006 interpretability.
- **confidence:** 0.99

# EDITORIAL issues

## SD-E01 — “Independent subset” is inaccurate design language

- **issue_key:** `SD-E01_INDEPENDENCE_LABEL`
- **axis:** writing-clarity
- **severity:** EDITORIAL
- **anchor:** Discussion, “The score was validated in an independent subset and therefore overcomes the limitations of earlier single-centre signatures.”
- **falsifiable concern:** The subset is from the same centre and was exposed to full-cohort model development; “independent” is factually misleading.
- **concrete resolution test:** Relabel it as a contaminated internal split or, after a complete leakage-free redevelopment, an internal holdout. Reserve “independent validation” for an untouched external dataset.
- **journal gate:** **FAIL** — N002 transparent presentation.
- **confidence:** 0.99

## SD-E02 — Readiness language must be tied to completed validation stages

- **issue_key:** `SD-E02_READINESS_LANGUAGE`
- **axis:** claim-moderation
- **severity:** EDITORIAL
- **anchor:** Results, “ready for therapeutic development”; Discussion, “biomarker ready for clinical deployment” and “Future prospective studies may refine, but are not required to establish, clinical utility.”
- **falsifiable concern:** These phrases collapse preliminary biological association, assay validation, clinical validation, clinical utility, and treatment development into a single unsupported readiness claim.
- **concrete resolution test:** Replace with stage-specific language: hypothesis-generating prognostic signature and preliminary EVA1 dependency requiring target-specific mechanistic, independent clinical, analytical assay, and prospective utility validation.
- **journal gate:** **FAIL** — N001/N002 claim-to-evidence alignment.
- **confidence:** 0.99

# Claim-ceiling risks

- `SD-B02_INTENDED_USE_MISMATCH` sets the clinical ceiling: the present cohort may support, at most, a preliminary prognostic association in resected single-centre HCC; it cannot support anti-PD-1 treatment selection, clinical actionability, immediate deployment, or human treatment benefit.
- `SD-B03_SC_BIOLOGICAL_UNIT` and `SD-M06_CORRELATION_TO_EXCLUSION` set the discovery ceiling: the current analysis may describe an exploratory cell-level association, not a patient-level immune-evasion programme or T-cell exclusion mechanism.
- `SD-B04_PERTURBATION_SPECIFICITY` sets the wet-lab ceiling: the data may support a preliminary association between one-guide perturbation and short-term growth/marker changes, not EVA1-specific causality or direct suppression of anti-tumour immunity.
- `SD-B05_NO_TREATMENT_INTERACTION` sets the animal ceiling: the experiment may support a difference between two cell preparations under universal anti-PD-1 exposure, not sensitization to anti-PD-1 or therapeutic synergy.
- `SD-M05_GENERALIZABILITY` sets the transportability ceiling: no universal, pan-aetiology, or cross-treatment-setting claim is supportable from the current sampling frame.
- Cross-layer concordance does not raise these ceilings because the layers share non-identifying designs and do not independently validate the same causal estimand.

# Required versus optional additional work

**Required for the present central claims:**

1. Leakage-free redevelopment and genuinely external validation of a fully locked score, with sufficient events, censoring-aware survival performance, calibration, clinical baselines, missing-data safeguards, and complete model specification.
2. Direct evaluation of the claimed anti-PD-1 treatment-selection intended use in a cohort with a valid treatment comparator and a prespecified score-by-treatment interaction; preferably a randomized-trial specimen set or prospective design.
3. Patient-level single-cell inference with multiplicity control, robustness to patient composition, and independent orthogonal validation.
4. Target-specific EVA1 perturbation using independent guides, direct target measurement, rescue, and immune-functional assays that separate immune susceptibility from generic growth effects.
5. A biologically suitable, rigorously randomized/blinded factorial animal study that tests the EVA1-by-anti-PD-1 interaction, includes immune/mechanistic readouts, and is independently reproduced.
6. Complete human and animal ethics declarations and sufficient methodological/data/code reporting for interpretation and replication.
7. Removal or strict qualification of “causal,” “universal,” “clinically actionable,” “immediately deployable,” and human-benefit claims until the corresponding tests pass.

**Optional but valuable after the required gates pass:**

- Cross-platform analytical validation and assay transfer across laboratories.
- Spatial validation of EVA1 expression relative to T-cell localization in independent tumours.
- Orthotopic and aetiology-relevant HCC models, pharmacologic EVA1 perturbation if a selective reagent exists, toxicity/pharmacodynamic studies, and validation across sex and biological context.
- Prospective impact analysis showing that using the score improves decisions or outcomes relative to standard care.

# Journal-fit posture

In its current form, the study does not meet the evidence threshold for a Nature Article. The cross-disciplinary framing is potentially suitable, but the reported work is an exploratory, single-centre, small-sample chain in which the clinical, single-cell, mechanistic, and animal designs do not identify the central causal or treatment-predictive claims. This is not a matter of polishing or adding caveats alone: the flagship claims require new independent clinical validation and redesigned mechanistic and in vivo experiments. A substantially narrowed manuscript could present preliminary associations, but that narrower contribution would not by itself demonstrate the outstanding scientific importance and major conceptual advance expected under N001.

# NOT ASSESSABLE items

- **Animal immunology suitability:** Host species/strain, sex, age, immune status, xenograft compatibility, anti-PD-1 clone/dose/schedule, species reactivity, and isotype control are not reported. Therefore checkpoint-mechanism interpretability is **NOT ASSESSABLE** beyond the definite absence of an untreated arm.
- **Numerical verification:** Figure images, tables, patient-level outputs, and code are not supplied. Exact AUCs, hazard ratios, tumour-volume values, cell-growth values, and \(P\) values are **NOT ASSESSABLE**, while their internal textual inconsistencies remain assessable.
- **Raw-data QC:** Library-level sequencing quality, batch structure, donor/sample balance, ambient RNA/doublet handling, and inferred-CNV implementation are **NOT ASSESSABLE** from the supplied text.
- **Reference claim support:** Whether the cited papers support the novelty and treatment-selection statements is **NOT ASSESSABLE** because cited-paper full text was outside the permitted frozen inputs.
- **Unreported experimental procedures:** Procedures not mentioned in the packet are not presumed absent from the underlying study. However, the manuscript explicitly states that multiple correction, external validation, calibration, decision-curve analysis, a second guide, rescue, direct target engagement, immune co-culture, random allocation, blinded measurement, and independent animal replication were not performed; those are assessable failures, not missing-material assumptions.

# Evidence anchors

| Anchor | Design inference |
|---|---|
| Single-cell discovery: “Cells were treated as independent observations.” | Patient/tumour clustering was ignored. |
| Single-cell discovery: “no multiple-testing correction was applied.” | Discovery list lacks multiplicity control. |
| Score construction: “stepwise selection using the entire 72-patient dataset.” | The subsequent split cannot provide independent validation. |
| Score construction: “Expression cutoffs, coefficient signs, and missing-value rules were also chosen using the full dataset.” | Leakage affects the entire prediction pipeline, not feature choice alone. |
| Study population: “72 adults who underwent resection for HCC” | Population does not itself represent anti-PD-1 treatment selection. |
| Functional experiments: “one CRISPR guide RNA” and no “second guide, rescue construct, direct target-engagement assay, or immune-cell co-culture” | EVA1 specificity and immune function are not established. |
| Mouse experiment: “All mice received anti-PD-1.” | Sensitization interaction is not estimable. |
| Mouse experiment: “Allocation order followed cage order; investigators were aware” | Allocation and observer-bias safeguards fail. |
| Ethics: approving committee, protocol number, consent procedure, animal protocol, and humane endpoints “are not reported.” | Ethical and welfare oversight cannot be verified. |
| Data and code availability: raw data, model code, coefficient values, final patient-level dataset, seeds, and versions are not available/deposited or recorded | Model and analysis are not independently reproducible from the manuscript. |

# Confidence and reasons

**Overall confidence: 0.99.** The central conclusions follow directly from explicit design statements rather than assumptions about absent materials. Confidence is highest for leakage, intended-use mismatch, pseudoreplication, lack of perturbation specificity, and inability to estimate anti-PD-1 sensitization. Confidence is lower only for the biological suitability of the xenograft/checkpoint model, because the host and reagent details are not reported; that component is therefore marked **NOT ASSESSABLE**, not failed by presumption.
