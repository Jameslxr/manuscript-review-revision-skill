# Reviewer role

Independent reviewer 07  
role_id: `adversarial-causal-chain`  
Functional lens: adversarial falsification of the proposed chain from single-cell association, to a five-gene mortality score, to an EVA1 immune mechanism, to anti-PD-1 sensitivity and clinical utility. I assess whether each link is identified by the reported design and what evidence would discriminate the claimed explanation from plausible alternatives. I do not render an editorial decision.

# Material inspected and assessment boundary

I inspected only the following frozen inputs:

- `manuscript.md`, SHA-256 `d51224a5ec717a268dadeee2fe9461a7b9d8c833f5b459be2d522a88d5c0006f`
- `00_input_inventory.json`
- `nature-journal-profile.json`, SHA-256 `6f6386d213e195d6ec26d0c177568f27753208425a6a15ce139b1ac2235fd6eb`
- `02_shared_fact_base.md`, SHA-256 `947b2ed3c744626d5eadc56845b65f223c6b0d4336bd765e3c714acf4ff4a976`

The packet does not contain figure images, tables, supplementary information, raw data, source code, protocols, reporting checklists, or a cover letter. Consequently, numerical source outputs, image-based claims, model implementation, and unreported experimental details are not independently verifiable. Absence from the packet is not treated as proof that an unreported procedure was absent unless the manuscript explicitly states that it was not performed.

# Journal standard applied

The frozen Nature profile identifies the target as a broad flagship journal and the submission as an Article at initial submission. I applied requirement N001: original research of outstanding scientific importance reaching a conclusion of interdisciplinary interest; N002: assessment of technical soundness, strength of evidence, novelty, field importance, and general scientific interest; and N006: Methods must contain the elements needed to interpret and replicate the results. Under the supplied strictness card, the central causal claim requires strong causal completeness, independent multi-layer validation, broad accessibility, and reproducible methods. Observational, retrospective, cell-line, and xenograft evidence cannot by itself establish universal clinical actionability or human treatment benefit.

# Overall assessment

The manuscript poses a potentially important question and attempts to connect tumour-cell state, prognosis, mechanism, and therapy. However, adversarial reconstruction shows that the central chain is not presently identified. The first link is already unstable because eight patients, not 46,218 cells, are the relevant independent units for tumour-level immune infiltration, yet the analysis treats cells as independent and performs uncorrected discovery. The next link fails because the score, coefficients, cutoffs, and missing-data rules were all chosen on the full 72-patient cohort before that cohort was split. The clinical cohort measures overall survival after resection, not anti-PD-1 response or treatment interaction. The EVA1 perturbation lacks independent on-target verification and an immune-effector assay. Finally, the mouse study compares EVA1 states only while every mouse receives anti-PD-1, so it cannot distinguish baseline growth suppression from drug sensitization.

Thus, concordance across layers is compatible with several non-causal alternatives: patient-level confounding creates the single-cell association; overfitting creates the apparent mortality performance; EVA1 depletion reduces general proliferative fitness; and smaller xenografts reflect that fitness defect rather than enhanced anti-PD-1 response. No reported analysis connects these layers by mediation, treatment interaction, or prospective prediction. The title-level conclusion therefore exceeds the evidence by multiple inferential steps.

Critical gates:

| Critical gate | Status | Basis |
|---|---|---|
| Patient-level single-cell discovery supports an EVA1 immune-exclusion association | **FAIL** | Cells are treated as independent for a tumour-level exposure across eight patients; 1,842 genes are selected at nominal `P < 0.05` without multiplicity control. |
| Five-gene score has independent prognostic validation | **FAIL** | Feature selection and all model-defining choices use the full cohort before the 70:30 split. |
| Score predicts benefit from anti-PD-1 rather than prognosis | **FAIL** | The cohort is resected HCC with overall survival; no anti-PD-1 response endpoint or treated-versus-comparator interaction is reported. |
| EVA1 is an on-target regulator of anti-tumour immunity | **FAIL** | One guide, no rescue, no target-engagement assay, no immune-cell co-culture, and a concurrent growth defect leave off-target and generic fitness explanations open. |
| EVA1 depletion sensitizes tumours to anti-PD-1 | **FAIL** | All mice receive anti-PD-1; there is no EVA1-by-treatment factorial contrast. |
| Central chain is independently reproduced across biological layers | **FAIL** | The layers use non-independent discovery/modeling or non-discriminating experiments, and no mediation or cross-layer linkage is shown. |
| Human clinical utility and universal applicability are established | **FAIL** | Single-centre retrospective resection cohort, no external cohort, no assay validation, no clinical baseline comparison, no calibration, and no decision analysis. |
| Source-level numerical and figure verification | **NOT ASSESSABLE** | Figures, tables, raw data, and code were not supplied. |

# Major strengths

- The manuscript states key limitations unusually explicitly, including cell-level independence, nominal testing, full-dataset model selection, lack of external validation, one-guide perturbation, absence of rescue and immune-cell co-culture, and the non-randomized, non-blinded mouse design. These disclosures make the causal audit possible.
- The attempted evidence architecture spans human tissue, a clinical cohort, two cell lines, and an in vivo experiment. If redesigned around independent units and causal contrasts, this could become a useful translational programme.
- The clinical dataset reportedly includes several important prognostic covariates, and the experimental section measures more than proliferation alone, including PD-L1 protein and interferon-response transcripts.
- The manuscript reports discrepant AUC values and limited follow-up rather than concealing them; these can be resolved with a frozen analysis and source-level audit.

# BLOCKING issues

## 1. Tumour-level immune exclusion is inferred from pseudoreplicated, uncorrected cell-level discovery

- **issue_key:** `CAC-01-single-cell-unit`
- **axis:** `causal-vs-correlative`
- **severity:** `BLOCKING`
- **anchor:** Patients and methods, “Differential expression between high- and low-infiltration tumours was tested at the cell level using a Wilcoxon rank-sum test. Cells were treated as independent observations”; Results, “EVA1 was higher in low-infiltration tumours and correlated inversely with a T-cell score (Spearman r = −0.41, P = 0.03). We interpreted this association as evidence that EVA1 excludes T cells from HCC.”
- **falsifiable concern:** Immune infiltration is assigned at the tumour/patient level, so the effective independent sample is eight tumours, not the number of tumour cells. Treating correlated cells as independent can produce anticonservative P values and allow one or a few patients, tumour-cell proportions, inferred copy-number states, or aetiologies to drive the EVA1 signal. An inverse cross-sectional correlation also does not distinguish EVA1-driven exclusion from immune pressure inducing or selecting EVA1-high cells, tumour purity/state confounding, or a third patient-level factor.
- **concrete resolution test:** Reanalyse discovery with patient as the unit using pseudobulk or a mixed model with patient-level random effects, predefined covariates where supportable, and multiple-testing control. Show leave-one-patient-out stability of the EVA1 effect, per-patient paired tumour/adjacent summaries, and effect sizes with uncertainty. Then test directionality in an independent patient cohort and in a perturbational immune-competent system where EVA1 is manipulated before measuring immune recruitment or cytotoxicity. The exclusion claim survives only if the patient-level effect is stable, externally reproduced, and EVA1 perturbation changes immune-cell behaviour independent of tumour-cell number.
- **journal gate:** **FAIL** — N001/N002 strength-of-evidence and supplied strong-causal-completeness gate.
- **confidence:** `0.99`

## 2. The “validation” split occurs after full-cohort model selection and cannot estimate out-of-sample performance

- **issue_key:** `CAC-02-model-leakage`
- **axis:** `statistical-rigor`
- **severity:** `BLOCKING`
- **anchor:** Patients and methods, “Five genes were retained after stepwise selection using the entire 72-patient dataset. Expression cutoffs, coefficient signs, and missing-value rules were also chosen using the full dataset”; immediately followed by “The same 72 patients were then randomly divided 70:30 into a training set and a validation set. The locked five-gene formula was evaluated in both subsets.”
- **falsifiable concern:** The validation patients contributed to feature selection, coefficient direction, cutoffs, and missingness rules. The reported validation AUC therefore measures reuse of information, not independent generalization. With 31 deaths, 27 genes plus 18 covariates and stepwise selection create extreme optimism and selection instability. The apparent survival link may disappear under a leakage-free pipeline.
- **concrete resolution test:** Freeze the complete pipeline before outcome access in a genuinely independent, adequately powered cohort encompassing intended-use HCC populations. Alternatively, for development only, nest every operation—gene screening, stepwise selection, coefficient estimation, cutoff choice, and missing-data handling—inside repeated nested resampling and report optimism-corrected discrimination, calibration, Brier score, confidence intervals, and selection stability. External validation must use the untouched formula and assay. The claim survives only if performance remains clinically meaningful and calibrated without outcome leakage and improves on prespecified clinical baselines.
- **journal gate:** **FAIL** — N002 technical soundness/strength of evidence and the independent-validation component of the supplied Nature standard.
- **confidence:** `1.00`

## 3. A post-resection mortality model is presented as a predictor of anti-PD-1 benefit

- **issue_key:** `CAC-03-prognostic-predictive-jump`
- **axis:** `clinical-validity`
- **severity:** `BLOCKING`
- **anchor:** Patients and methods, “The clinical cohort included 72 adults who underwent resection for HCC”; Impact and implications, “This study identifies a five-gene score that can be measured at diagnosis and used to select anti-PD-1 therapy”; Discussion, “Its high AUC supports immediate use for selecting anti-PD-1 therapy.”
- **falsifiable concern:** Overall survival in a resected retrospective cohort can establish, at most, prognosis under the observed mixture of recurrence and post-recurrence treatments. It does not identify differential benefit from anti-PD-1. Prognostic association, treatment selection, subsequent therapy, recurrence, liver function, and competing causes can all generate score–survival association without any score-by-anti-PD-1 interaction. There is no reported immunotherapy-treated cohort, comparator arm, response endpoint, or causal treatment-effect design.
- **concrete resolution test:** Define the intended-use setting and test the frozen assay in a prospective-retrospective randomized anti-PD-1 trial or a prospectively designed cohort with a clinically appropriate comparator and rigorous confounding control. The primary analysis must test a prespecified score-by-treatment interaction on a clinically relevant endpoint, with calibration and subgroup uncertainty. A significant score association within only the treated arm is insufficient. Until then, describe the score only as an exploratory post-resection prognostic signature.
- **journal gate:** **FAIL** — N001 importance must rest on a supported conclusion; N002 strength of evidence; supplied rule that retrospective observational evidence cannot establish human treatment benefit.
- **confidence:** `1.00`

## 4. The perturbation does not identify EVA1 as an on-target immune-evasion driver

- **issue_key:** `CAC-04-on-target-immune-mechanism`
- **axis:** `mechanism-evidence`
- **severity:** `BLOCKING`
- **anchor:** Patients and methods, “EVA1 was depleted using one CRISPR guide RNA in Huh7 and Hep3B cells”; “The study did not include a second guide, rescue construct, direct target-engagement assay, or immune-cell co-culture”; Results, “EVA1 depletion reduced 72-hour cell growth by 24% in Huh7 cells and 19% in Hep3B cells. PD-L1 abundance also decreased, while three interferon-response transcripts increased. These findings show that EVA1 directly suppresses anti-tumour immunity.”
- **falsifiable concern:** A single guide cannot separate EVA1 dependence from off-target editing or guide-specific toxicity. The concurrent 19–24% growth defect can change cell state, density, stress responses, interferon transcripts, and PD-L1 without reflecting immune evasion. PD-L1 direction alone is not a functional readout of anti-tumour immunity, and no immune effector is present. The experiment therefore does not establish on-target action, pathway order, or immune consequence.
- **concrete resolution test:** Confirm editing and EVA1 protein depletion; reproduce phenotypes with at least two independent guides and an orthogonal perturbation; restore them with a guide-resistant rescue expressed near endogenous levels. Measure growth-matched or time-resolved effects to separate cell fitness from immune signaling. Then test antigen-specific T-cell or NK-cell recruitment, activation, killing, and exhaustion with suitable controls, plus mechanistic epistasis placing the proposed downstream pathway between EVA1 and the immune phenotype. The causal claim survives only if rescue and epistasis restore both molecular and functional immune endpoints independently of proliferation.
- **journal gate:** **FAIL** — N002 mechanistic strength and supplied strong-causal-completeness requirement.
- **confidence:** `0.99`

## 5. The mouse comparison cannot test sensitization because all animals receive anti-PD-1

- **issue_key:** `CAC-05-missing-treatment-interaction`
- **axis:** `experimental-design`
- **severity:** `BLOCKING`
- **anchor:** Patients and methods, “Ten mice bearing subcutaneous Huh7 xenografts were allocated to control or EVA1-depleted cells, with five animals per group. All mice received anti-PD-1”; Results, “In mice, day-21 tumours were smaller in the EVA1-depleted group (P = 0.048)”; conclusion, “We conclude that EVA1 inhibition sensitizes HCC to anti-PD-1.”
- **falsifiable concern:** The design estimates the effect of EVA1 status in the presence of anti-PD-1, not whether EVA1 status changes the effect of anti-PD-1. Because EVA1 depletion already reduces cell growth in vitro, smaller tumours can arise from baseline fitness loss with no drug interaction. The missing untreated arms make sensitization non-identifiable. Host immune competence, anti-PD-1 species/target compatibility, and engraftment balance are also unreported in the inspected text, so the biological meaning of anti-PD-1 exposure cannot be established.
- **concrete resolution test:** Use a randomized, blinded, adequately powered 2×2 design: control versus validated/rescued EVA1 perturbation crossed with isotype/vehicle versus anti-PD-1. Prespecify a longitudinal model and test the EVA1-by-treatment interaction, not separate within-arm P values. Demonstrate comparable baseline engraftment, sustained EVA1 perturbation, target engagement, host and antibody compatibility, and intratumour immune changes; replicate independently and include rescue. Sensitization requires a reproducible interaction beyond the main effect of EVA1 loss.
- **journal gate:** **FAIL** — N002 experimental identification and supplied causal-completeness/multi-layer-validation gate.
- **confidence:** `1.00`

## 6. No evidence links the mortality score, EVA1 biology, and treatment response into one causal chain

- **issue_key:** `CAC-06-cross-layer-chain`
- **axis:** `causal-vs-correlative`
- **severity:** `BLOCKING`
- **anchor:** Discussion, “The molecular and animal results identify EVA1 as the causal link between the five-gene score and immune escape”; Introduction, “We hypothesized that a tumour-cell immune-evasion programme would predict survival and identify a therapeutic dependency.”
- **falsifiable concern:** Evidence for separate associations does not show that EVA1 mediates the score–survival relationship, that the five-gene score measures the EVA1-dependent state, or that score-high tumours are selectively dependent on EVA1 or responsive to anti-PD-1. The chain can be false even if each marginal association is reproducible. For example, the score may capture stage or liver dysfunction, EVA1 may affect generic proliferation, and anti-PD-1 may be irrelevant.
- **concrete resolution test:** In independent human samples, show that the frozen score maps to the same tumour-cell state and immune spatial phenotype after adjustment for stage, purity, aetiology, and liver function. Test whether EVA1 perturbation specifically shifts the other score components and the inferred state, and use prespecified mediation analyses only where temporal and confounding assumptions are defensible. In treatment models and human immunotherapy cohorts, test whether the frozen score or EVA1 state modifies anti-PD-1 effect. Predefine falsification controls, including unrelated growth perturbations and score-matched EVA1-low/high models. A chain claim requires all directional links to survive these discriminating tests.
- **journal gate:** **FAIL** — N001 conceptual conclusion and N002 strength of evidence; supplied strong causal completeness and independent multi-layer validation.
- **confidence:** `0.98`

## 7. Universal actionability and immediate deployment are unsupported by the sampled population and absent clinical-validation layers

- **issue_key:** `CAC-07-universal-actionability`
- **axis:** `clinical-validity`
- **severity:** `BLOCKING`
- **anchor:** Abstract, “clinically actionable, universally applicable predictor for HCC”; Impact and implications, “immediately deployable biomarker” and “a treatment strategy for all major HCC aetiologies”; Patients and methods, “58 patients with viral hepatitis, 9 with metabolic liver disease, and 5 with other or undocumented aetiologies”; “No external cohort, independent laboratory assay, calibration analysis, or decision-curve analysis was used. Performance was compared only with the five-gene model; BCLC stage and other clinical baselines were not evaluated.”
- **falsifiable concern:** The cohort represents one centre, resected disease, and predominantly viral aetiology. It cannot support transportability to unresectable disease, non-viral populations, different stages or treatments, or all major aetiologies. Without an operational assay, analytical reproducibility, external calibration, clinical comparator, and evidence of decision benefit, “actionable” and “deployable” are not testable clinical properties. Universal claims are especially vulnerable to spectrum and prevalence shifts.
- **concrete resolution test:** Specify intended population, specimen, timing, assay, threshold, and treatment decision. Lock the assay and model, establish analytical validity across laboratories, then externally validate discrimination and calibration in geographically and aetiologically diverse cohorts representing the intended setting. Compare against BCLC and prespecified standard-of-care predictors, quantify incremental and decision-curve utility, and test heterogeneity with adequately powered interaction estimates rather than claiming universality from nonsignificant subgroup tests. Clinical actionability additionally requires prospective evidence that score-guided care improves patient-relevant outcomes.
- **journal gate:** **FAIL** — N001 outstanding and broadly relevant conclusion, N002 evidence strength, and the supplied prohibition on deriving universal clinical actionability from current designs.
- **confidence:** `1.00`

# MAJOR issues

## 8. Three-year AUC is not presently interpretable and is internally inconsistent

- **issue_key:** `CAC-08-three-year-performance`
- **axis:** `statistical-rigor`
- **severity:** `MAJOR`
- **anchor:** Results, “The Results text reports a validation-set 3-year mortality AUC of 0.84. Figure 3 reports an AUC of 0.86, whereas the Abstract reports 0.91. Because median follow-up was 18 months, 3-year outcome status was unavailable for many surviving patients.”
- **falsifiable concern:** The three values cannot all describe the same frozen analysis, and ordinary binary ROC analysis at three years would mishandle censoring. With short follow-up and a small leaked validation subset, the effective number at risk may be inadequate and uncertainty likely large. The claimed magnitude may reflect endpoint coding, subset changes, or an unreported time-dependent AUC method.
- **concrete resolution test:** Freeze one analysis dataset and provide an auditable derivation of a censoring-aware, time-dependent three-year AUC with confidence interval, numbers at risk, censoring distribution, and prespecified handling of patients lacking three-year status. Reconcile every manuscript and figure value from the same output. Report calibration at clinically relevant times and sensitivity to follow-up assumptions. If support at three years is sparse, shorten the horizon or refrain from the estimate.
- **journal gate:** **FAIL** — N002 technical soundness and N006 interpretability/replicability.
- **confidence:** `1.00`

## 9. The survival model lacks the diagnostics and uncertainty needed to exclude a fragile prognostic association

- **issue_key:** `CAC-09-survival-identification`
- **axis:** `statistical-rigor`
- **severity:** `MAJOR`
- **anchor:** Statistical analysis, “The proportional-hazards assumption was not examined. Hazard ratios and P values were reported without confidence intervals”; Study population, “Records with missing values were excluded from each analysis”; Results, “The score remained significant in the selected multivariable model (hazard ratio 2.4, P = 0.04).”
- **falsifiable concern:** A selected P value near 0.05 without a confidence interval, proportional-hazards assessment, transparent missingness flow, or prespecified covariate strategy cannot distinguish a stable prognostic effect from model-selection noise, non-proportionality, complete-case selection, or residual confounding. “Treatment after recurrence” and “recurrence status” also raise potential post-baseline adjustment concerns depending on how they entered the model.
- **concrete resolution test:** Provide a participant flow and missingness table; prespecify baseline covariates using a causal/clinical rationale; use appropriate imputation within resampling; report hazard ratios with 95% confidence intervals, Schoenfeld or time-varying diagnostics, influential observations, functional-form checks, and sensitivity analyses excluding post-baseline variables. Validate absolute risk and calibration in independent data.
- **journal gate:** **FAIL** — N002 strength and reliability of the clinical evidence; N006 sufficient methods.
- **confidence:** `0.98`

## 10. The in vivo estimate is vulnerable to allocation, measurement, multiplicity, and endpoint biases

- **issue_key:** `CAC-10-mouse-internal-validity`
- **axis:** `experimental-design`
- **severity:** `MAJOR`
- **anchor:** Mouse experiment, “Allocation order followed cage order; investigators were aware of group assignment during measurement”; “Tumour volume was compared on day 21 using an unpaired t-test. No independent replicate experiment was performed”; Results, “P = 0.048.”
- **falsifiable concern:** Cage-ordered allocation can confound treatment with cage or time, and unblinded measurement can bias caliper-based tumour volumes. A single endpoint comparison ignores longitudinal dependence and baseline volume, while a marginal P value in ten animals is sensitive to outliers and analytic choices. These weaknesses remain even after adding the missing anti-PD-1 control arms.
- **concrete resolution test:** Conduct a prospectively powered, randomized and allocation-concealed experiment with blinded measurements, balanced cage effects, prespecified exclusions, longitudinal mixed-effects analysis, effect sizes and intervals, and an independent biological replication. Make individual trajectories available and demonstrate robustness to outliers and baseline adjustment.
- **journal gate:** **FAIL** — N002 technical soundness and independent-validation requirement.
- **confidence:** `0.99`

## 11. The unavailable data and code prevent falsification of the proposed chain

- **issue_key:** `CAC-11-reproducibility`
- **axis:** `reproducibility`
- **severity:** `MAJOR`
- **anchor:** Data and code availability, “Raw single-cell data, model code, coefficient values, and the final patient-level analysis dataset are not deposited. Random seeds and software versions were not recorded.”
- **falsifiable concern:** Without raw or suitably controlled-access data, exact coefficients, cutoffs, code, seeds, and environments, an independent analyst cannot reproduce cell assignments, patient-level tests, leakage-free resampling, AUC calculations, or the link between score and outcome. The missing formula also contradicts immediate deployability.
- **concrete resolution test:** Deposit raw and processed single-cell data with patient identifiers appropriately de-identified or controlled; provide the final analysis dataset or a governed access route; release executable code, exact formula, preprocessing and missingness rules, random seeds, package/software versions, and machine-readable provenance. Reproduction by an independent analyst should regenerate all reported primary estimates and figures from raw inputs.
- **journal gate:** **FAIL** — N006 replication and the supplied reproducible-methods expectation.
- **confidence:** `1.00`

# MINOR issues

## 12. The evidence does not discriminate “immune exclusion” from altered immune abundance or tumour composition

- **issue_key:** `CAC-12-exclusion-phenotype`
- **axis:** `mechanism-evidence`
- **severity:** `MINOR`
- **anchor:** Results, “We interpreted this association as evidence that EVA1 excludes T cells from HCC”; Figure 2 legend, “Association between EVA1 expression and the T-cell score in eight tumours.”
- **falsifiable concern:** A bulk or tumour-level T-cell score does not establish the spatial process of exclusion. Lower T-cell abundance could reflect reduced recruitment, increased death, compartmental redistribution, sampling, tumour purity, or technical composition. This is subordinate to the patient-unit flaw but remains necessary if “exclusion” is retained.
- **concrete resolution test:** Use spatially resolved, patient-level measurements to quantify intratumoural versus stromal localization, distances to EVA1-high tumour cells, and relevant chemokine/vascular states, with blinded image analysis and external replication. Perturb EVA1 in a system supporting immune trafficking and test whether localization changes independently of total tumour burden.
- **journal gate:** **FAIL** — N002 mechanistic precision.
- **confidence:** `0.95`

# EDITORIAL issues

## 13. The title and causal verbs prejudge results that the designs do not test

- **issue_key:** `CAC-13-causal-language`
- **axis:** `claim-moderation`
- **severity:** `EDITORIAL`
- **anchor:** Title, “A single-cell-derived immune-evasion signature establishes a universal therapeutic vulnerability in hepatocellular carcinoma”; Abstract, “establish EVA1 as the causal driver”; Discussion, “Future prospective studies may refine, but are not required to establish, clinical utility.”
- **falsifiable concern:** “Establishes,” “causal driver,” “universal,” and “clinically actionable” communicate completed causal and clinical validation despite missing independent discovery, treatment interaction, on-target rescue, and prospective utility evidence. This wording makes the manuscript’s conclusion false under plausible alternatives already compatible with the reported data.
- **concrete resolution test:** Until the blocking tests are passed, revise the title and all summary statements to “exploratory,” “associated with,” or “hypothesis-generating”; explicitly state that clinical utility and predictive treatment benefit require independent prospective validation. Restore stronger verbs only after the corresponding causal or clinical gate is met.
- **journal gate:** **FAIL** — N001 requires the headline conclusion itself to be supported; N002 claim-evidence alignment.
- **confidence:** `1.00`

# Claim-ceiling risks

- **Single-cell ceiling:** With the current analysis, the defensible statement is that EVA1 expression is exploratorily associated with a T-cell score in the sampled tumours. “EVA1 excludes T cells” exceeds the design.
- **Clinical-score ceiling:** With full-cohort feature selection followed by a split, the score is a development-set signal only. “Independent validation” and reported generalization performance are not defensible.
- **Treatment ceiling:** Overall survival after resection supports neither anti-PD-1 benefit prediction nor treatment selection. The score is not yet a predictive biomarker.
- **Perturbation ceiling:** One-guide cell-line results support a provisional EVA1-associated phenotype. They do not establish on-target immune mechanism.
- **Mouse ceiling:** The reported two-group experiment supports, at most, different day-21 tumour volumes between EVA1 states under anti-PD-1 exposure. It does not establish sensitization.
- **Translation ceiling:** No reported evidence supports immediate deployment, all-aetiology applicability, or human benefit from EVA1 inhibition.
- **Integrated-chain ceiling:** Multiple modalities are not equivalent to independent confirmation when each modality tests a different marginal association and no design identifies the links between them.

# Required versus optional additional work

Required to support the manuscript’s present central claims:

1. Re-establish the single-cell signal with patient-level inference, multiplicity control, leave-one-patient-out stability, and independent replication (`CAC-01`).
2. Rebuild and validate the score using a completely leakage-free workflow and a truly external cohort, with clinical comparator, calibration, and uncertainty (`CAC-02`, `CAC-08`, `CAC-09`).
3. Test predictive rather than prognostic value through a prespecified score-by-treatment interaction in an appropriate anti-PD-1 dataset (`CAC-03`).
4. Establish on-target EVA1 biology with independent guides, orthogonal perturbation, rescue, target engagement, growth-matched analyses, immune-effector assays, and pathway epistasis (`CAC-04`).
5. Replace the mouse comparison with a powered, randomized, blinded EVA1-by-anti-PD-1 factorial experiment in a biologically compatible model, with immune readouts and independent replication (`CAC-05`, `CAC-10`).
6. Directly test the cross-layer links among score state, EVA1, immune phenotype, and treatment effect rather than inferring a chain from concordant marginal findings (`CAC-06`).
7. Define intended use and demonstrate analytical validity, external transportability, incremental utility, and ultimately prospective clinical benefit before using “actionable,” “deployable,” or “universal” (`CAC-07`).
8. Release sufficient data, code, formula, and provenance for independent reproduction (`CAC-11`).

Optional if the claims are instead narrowed to an exploratory association report:

- Spatial mapping of EVA1-high tumour cells and T-cell localization would sharpen the exclusion hypothesis but would not, by itself, establish causality (`CAC-12`).
- Broader mechanistic profiling may help identify candidate downstream pathways, provided it follows rather than substitutes for on-target rescue and functional immune tests.
- Additional aetiology-stratified exploration may guide future sampling, but small subgroup comparisons should not be used to claim universality.

# Journal-fit posture

For Nature’s broad flagship standard, the proposed concept could be of interdisciplinary interest if a tumour-cell programme were shown to mechanistically control immune escape and prospectively identify anti-PD-1 benefit. The current manuscript does not meet that posture because every transition in the headline chain is either non-independent, non-causal, or tested with the wrong contrast. The evidence presently supports a preliminary, single-centre hypothesis-generation study, not an outstanding, causally complete advance with clinical actionability. This is a **FAIL** on current Nature fit under N001 and N002, without making a final editorial recommendation.

# NOT ASSESSABLE items

- **Figure-level support:** **NOT ASSESSABLE** because Figures 1–4 were not supplied; only legends were available. Cell distributions, patient contributions, survival curves, ROC construction, individual experimental points, and tumour trajectories cannot be visually audited.
- **Table-level cohort balance and model outputs:** **NOT ASSESSABLE** because no tables were supplied.
- **Numerical reproducibility:** **NOT ASSESSABLE** because raw data, final patient-level data, coefficients, cutoffs, and code were not supplied.
- **Unreported mouse host and reagent details:** **NOT ASSESSABLE** whether the host immune system and anti-PD-1 reagent are biologically compatible with the stated Huh7 xenograft experiment; the manuscript text does not provide the required details.
- **Full-text reference support:** **NOT ASSESSABLE** because the cited papers were not inspected under the frozen-input boundary. The supplied citation titles alone cannot substitute for a full claim-support audit.
- **Unreported protocols and reporting checklists:** **NOT ASSESSABLE** because they were not supplied. This does not establish that no underlying protocols exist.

# Evidence anchors

The causal audit rests principally on the following exact manuscript anchors:

- Patients and methods — Single-cell discovery: “Cells were treated as independent observations” and “no multiple-testing correction was applied.”
- Results — Single-cell discovery: “We interpreted this association as evidence that EVA1 excludes T cells from HCC.”
- Patients and methods — Score construction and validation: “using the entire 72-patient dataset” before “randomly divided 70:30.”
- Patients and methods — Score construction and validation: “No external cohort, independent laboratory assay, calibration analysis, or decision-curve analysis was used.”
- Results — Five-gene score: “0.84,” “0.86,” and “0.91,” with “median follow-up was 18 months.”
- Patients and methods — Functional experiments: “one CRISPR guide RNA” and no “second guide, rescue construct, direct target-engagement assay, or immune-cell co-culture.”
- Patients and methods — Mouse experiment: “All mice received anti-PD-1.”
- Results — Mouse experiment: “P = 0.048” and no immune infiltration, survival, toxicity, or post-implantation EVA1 measurement.
- Discussion: “Future prospective studies may refine, but are not required to establish, clinical utility.”
- Data and code availability: raw data, model code, coefficients, final dataset, seeds, and software versions are unavailable.

# Confidence and reasons

Overall confidence: `0.99`.

Confidence is high because the decisive causal limitations are explicit properties of the reported designs, not inferences from absent supplements: patient-level exposure analyzed with independent-cell tests; full-cohort selection before splitting; a prognostic cohort used for a predictive-treatment claim; one-guide perturbation without rescue or immune effectors; and no untreated mouse arms. These facts logically prevent the stated causal and predictive estimands from being identified. Confidence is lower only for details that could exist outside the manuscript packet—particularly figure appearance, exact computations, mouse host/reagent compatibility, and full reference support—and those are marked **NOT ASSESSABLE** rather than presumed.
