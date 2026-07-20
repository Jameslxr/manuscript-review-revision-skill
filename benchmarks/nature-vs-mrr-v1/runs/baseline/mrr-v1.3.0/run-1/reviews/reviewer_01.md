# Reviewer role

Independent reviewer 01; role_id: `journal-priority`. Functional lens: Nature Article scope, contribution threshold, interdisciplinary interest, and desk-screen risk. I considered technical or validity defects only where they directly determine whether the headline contribution clears that threshold. I do not make or imply the final editorial decision.

# Material inspected and assessment boundary

I inspected only:

- `manuscript.md`, SHA-256 `d51224a5ec717a268dadeee2fe9461a7b9d8c833f5b459be2d522a88d5c0006f`;
- `00_input_inventory.json`;
- `nature-journal-profile.json`, SHA-256 `6f6386d213e195d6ec26d0c177568f27753208425a6a15ce139b1ac2235fd6eb`;
- `02_shared_fact_base.md`, SHA-256 `947b2ed3c744626d5eadc56845b65f223c6b0d4336bd765e3c714acf4ff4a976`.

The packet contains manuscript text and four figure legends, but no figure images, tables, supplementary information, raw data, source code, protocols, reporting checklists, or cover letter. I therefore assess the stated study and reporting, not unprovided underlying materials. Numerical source outputs, figure quality, and full-text reference support remain bounded as stated under “NOT ASSESSABLE items.”

# Journal standard applied

The frozen profile identifies Nature as a broad flagship journal. For an Article at initial submission, I applied requirement N001: original research of outstanding scientific importance that reaches a conclusion of interest to an interdisciplinary readership. I also applied N002 to the strength of evidence, novelty, field importance, and general scientific interest; N006 to methods sufficient for interpretation and replication; and N007 to required initial-submission components. The strictness card additionally requires a major conceptual advance, strong causal completeness, independent multi-layer validation, broad accessibility, and reproducible methods. Observational, retrospective, cell-line, and xenograft evidence alone cannot establish universal clinical actionability or human treatment benefit.

# Overall assessment

The manuscript presents a coherent translational arc from single-cell discovery to a survival score and perturbation experiments. That architecture could support a field-specific hypothesis-generating report. In its present form, however, the conclusions substantially outrun the evidence, and the work does not clear the Nature Article threshold for outstanding importance, causal completeness, or broad generality. Its central model is selected on all 72 patients before the claimed validation split; the cohort is single-centre, retrospective, resection-only, and predominantly viral; no immunotherapy-response cohort is studied; and the mouse experiment cannot test sensitization because every animal receives anti-PD-1. These are contribution-defining limitations rather than refinements.

Critical gates:

| Critical gate | Status | Basis |
|---|---|---|
| Correct target, article type, and stage established | PASS | Frozen profile: Nature; Article; initial submission. |
| Original research contribution present | PASS | The manuscript reports a new five-gene score and EVA1 perturbation experiments. |
| Outstanding scientific importance / major conceptual advance (N001) | FAIL | The universal biomarker and causal-mechanism claims are not supported by independent clinical validation or causally discriminating experiments. |
| Interest to an interdisciplinary scientific readership (N001) | FAIL | The demonstrated result is presently a narrow, single-centre HCC association plus preliminary model-system evidence, not a broadly established principle. |
| Independent multi-layer validation | FAIL | “Five genes were retained after stepwise selection using the entire 72-patient dataset,” followed by a split of “The same 72 patients”; there is no external cohort or independent experiment. |
| Causal completeness for immune escape and anti-PD-1 sensitization | FAIL | One-guide cell-line perturbation lacks rescue or immune-cell testing, and “All mice received anti-PD-1.” |
| Universal clinical actionability or human treatment benefit | FAIL | The cohort contains resected patients and an overall-survival endpoint, not an anti-PD-1 treatment-response comparison or prospective utility test. |
| Reproducible methods and model specification (N006) | FAIL | Model coefficients, code, raw data, final patient-level data, seeds, and software versions are not deposited or reported. |
| Figure-level support | NOT ASSESSABLE | Figure images and source data were not supplied. |
| Full ethics and governance compliance | NOT ASSESSABLE | Committee identifiers, consent procedure, animal protocol, and humane endpoints are not reported; underlying approvals were not supplied. |

# Major strengths

- The manuscript addresses a medically important cancer and attempts to link tumour-cell state, clinical outcome, and perturbational evidence.
- The study states important negative design facts transparently, including use of the full cohort for selection, absence of an external cohort, use of one CRISPR guide, and limitations of the mouse design.
- Two HCC cell lines show directionally concordant growth effects after EVA1 depletion.
- Four display items are proposed, consistent with the frozen profile’s typical Article range, although their content cannot be assessed without images.
- The prose makes the central claims easy to identify, which facilitates a clear test of whether the evidence supports them.

# BLOCKING issues

## JP-01 — The demonstrated contribution does not meet the Nature Article threshold

- **issue_key:** `JP-01-nature-contribution-threshold`
- **axis:** `novelty-significance`
- **severity:** `BLOCKING`
- **anchor:** Title, “establishes a universal therapeutic vulnerability”; Abstract, “clinically actionable, universally applicable predictor”; Discussion, “This study establishes a universal immune-evasion mechanism in HCC and provides a biomarker ready for clinical deployment.”
- **falsifiable concern:** The evidence currently establishes, at most, a single-centre retrospective survival association and preliminary EVA1 dependency in two cell lines and one small xenograft experiment. If a locked score fails independent validation, or if EVA1 perturbation does not alter immune-mediated tumour control across models, the claimed universal vulnerability and major conceptual advance collapse.
- **concrete resolution test:** Demonstrate a pre-specified, locked signature in multiple genuinely independent, adequately powered cohorts spanning major HCC aetiologies and disease settings; show incremental performance over accepted clinical baselines; and establish a reproducible EVA1-centred immune mechanism using orthogonal perturbations, rescue, immune-competent systems, and independent in vivo replication. The combined result must support a general principle beyond one HCC cohort rather than merely improve a disease-specific classifier.
- **journal gate:** `FAIL` — N001 outstanding scientific importance, major conceptual advance, and interdisciplinary interest.
- **confidence:** `0.99`

## JP-02 — The claimed validation is not independent

- **issue_key:** `JP-02-nonindependent-validation`
- **axis:** `statistical-rigor`
- **severity:** `BLOCKING`
- **anchor:** Patients and methods, “Five genes were retained after stepwise selection using the entire 72-patient dataset. Expression cutoffs, coefficient signs, and missing-value rules were also chosen using the full dataset”; then, “The same 72 patients were then randomly divided 70:30 into a training set and a validation set.”
- **falsifiable concern:** Because feature selection and all key model choices used outcomes from the entire cohort, the held-out subset is outcome-informed and cannot provide an unbiased estimate of generalization. A correctly isolated external or fully nested validation may show materially lower discrimination or no stable score.
- **concrete resolution test:** Freeze the complete assay, coefficients, cutoffs, endpoint definition, missing-data rules, and analysis plan without using the validation outcomes, then evaluate once in a sufficiently powered external cohort. Alternatively, use properly nested resampling for development and reserve a truly untouched external cohort for confirmation. Report calibration, uncertainty, clinical-baseline comparison, and all failures as well as successes.
- **journal gate:** `FAIL` — N001 contribution credibility; N002 strength of evidence; strictness-card independent validation.
- **confidence:** `1.00`

## JP-03 — Clinical actionability and universal applicability are not tested

- **issue_key:** `JP-03-clinical-actionability`
- **axis:** `clinical-validity`
- **severity:** `BLOCKING`
- **anchor:** Impact and implications, “used to select anti-PD-1 therapy,” “immediately deployable biomarker,” and “for all major HCC aetiologies”; Study population, “72 adults who underwent resection,” including “58 patients with viral hepatitis”; Score construction and validation, “No external cohort, independent laboratory assay, calibration analysis, or decision-curve analysis was used.”
- **falsifiable concern:** Overall survival after resection is not evidence that a score predicts benefit from anti-PD-1, and a viral-dominant single-centre cohort cannot test applicability across major aetiologies or treatment settings. In a treatment-comparative cohort, the score may be merely prognostic, assay-dependent, or uncalibrated rather than treatment-predictive.
- **concrete resolution test:** Use a locked, analytically validated assay in independent multi-centre cohorts with broad aetiologic representation and actual anti-PD-1 exposure plus an appropriate comparator. Pre-specify and demonstrate a score-by-treatment interaction, calibration, incremental value over BCLC and standard factors, clinically relevant operating thresholds, and prospective decision utility. Until then, replace deployment and universal-selection claims with a hypothesis-generating prognostic claim.
- **journal gate:** `FAIL` — N001 broad importance; N002 strength of evidence; strictness-card prohibition on inferring universal actionability or human benefit from current designs.
- **confidence:** `1.00`

## JP-04 — The experiments do not establish EVA1-mediated immune escape or anti-PD-1 sensitization

- **issue_key:** `JP-04-causal-mechanism`
- **axis:** `causal-vs-correlative`
- **severity:** `BLOCKING`
- **anchor:** Functional experiments, “one CRISPR guide RNA,” with “no second guide, rescue construct, direct target-engagement assay, or immune-cell co-culture”; Mouse experiment, “All mice received anti-PD-1”; Results, “These findings show that EVA1 directly suppresses anti-tumour immunity” and “EVA1 inhibition sensitizes HCC to anti-PD-1.”
- **falsifiable concern:** The cellular phenotype could reflect guide-specific or general growth effects rather than EVA1-specific immune regulation, and the mouse comparison cannot estimate sensitization without anti-PD-1-negative arms. Orthogonal perturbation or factorial treatment could eliminate the apparent immune-specific interpretation.
- **concrete resolution test:** Replicate with multiple independent guides and a distinct perturbation modality; verify target engagement and rescue the phenotype; demonstrate an immune-dependent functional consequence in co-culture or organoid/immune systems; and perform a randomized, blinded, adequately powered factorial in vivo study containing control/EVA1 perturbation × vehicle/anti-PD-1 arms. Show a reproducible interaction, immune infiltration or function, and target persistence in an immune-competent HCC model.
- **journal gate:** `FAIL` — N002 technical soundness and strength of evidence; strictness-card causal completeness.
- **confidence:** `1.00`

## JP-05 — The headline 3-year performance is internally inconsistent and poorly supported by follow-up

- **issue_key:** `JP-05-endpoint-incoherence`
- **axis:** `data-resource-quality`
- **severity:** `BLOCKING`
- **anchor:** Abstract, “AUC of 0.91 for 3-year mortality”; Results, “validation-set 3-year mortality AUC of 0.84”; Figure 3 legend, “validation AUC as 0.86”; Study population, “Median follow-up among surviving patients was 18 months”; Results, “3-year outcome status was unavailable for many surviving patients.”
- **falsifiable concern:** The central performance estimate has three incompatible values, and incomplete 3-year ascertainment may bias a naïve binary AUC. Reanalysis with a pre-specified time-dependent method and adequate follow-up may materially reduce or invalidate the claimed discrimination.
- **concrete resolution test:** Reconcile every reported value to one version-controlled analysis; specify the estimand and censoring method; report numbers at risk, follow-up distribution, confidence intervals, and time-dependent AUC with appropriate censoring adjustment; and confirm the result in an independent cohort with sufficient 3-year outcome information.
- **journal gate:** `FAIL` — N002 strength and coherence of evidence; the manuscript’s headline result is not presently reliable enough to support N001.
- **confidence:** `1.00`

# MAJOR issues

## JP-06 — The single-cell discovery inflates evidence by treating cells as independent

- **issue_key:** `JP-06-single-cell-pseudoreplication`
- **axis:** `experimental-design`
- **severity:** `MAJOR`
- **anchor:** Single-cell discovery, “from eight patients,” “Cells were treated as independent observations,” and “nominal P < 0.05,” with “no multiple-testing correction”; Results, “1,842 nominally significant genes.”
- **falsifiable concern:** The biological unit is the patient, not each of 46,218 cells. Patient-aware analysis with multiplicity control may sharply reduce the discovery set or remove EVA1, weakening both novelty and the proposed mechanism.
- **concrete resolution test:** Reanalyse at the patient level using pseudobulk or a model with patient as the independent unit, apply appropriate genome-wide multiplicity control, report robustness to infiltration definitions, and replicate the EVA1 association in an independent single-cell or spatial cohort.
- **journal gate:** `FAIL` — N002 technical soundness and strength of evidence; directly affects whether the proposed programme is a credible discovery.
- **confidence:** `0.99`

## JP-07 — The survival model is too underpowered and incompletely evaluated for the claimed advance

- **issue_key:** `JP-07-model-overfitting-and-evaluation`
- **axis:** `statistical-rigor`
- **severity:** `MAJOR`
- **anchor:** Study population, “72 adults” and “Thirty-one deaths”; Score construction and validation, “Twenty-seven genes” with “18 available clinical and molecular covariates,” stepwise selection, and “BCLC stage and other clinical baselines were not evaluated”; Statistical analysis, “proportional-hazards assumption was not examined” and results were “reported without confidence intervals.”
- **falsifiable concern:** With 31 events and extensive data-driven selection, estimates may be unstable and the score may offer no incremental value over standard clinical variables. Assumption checks and uncertainty may reveal non-proportional hazards or imprecise effects.
- **concrete resolution test:** Pre-specify an adequately powered analysis; use principled shrinkage or penalization inside a fully nested development process; address missingness without analysis-wise complete-case drift; test proportional hazards; report confidence intervals, calibration, and optimism-corrected performance; and compare against BCLC and accepted clinical models in independent data.
- **journal gate:** `FAIL` — N002 strength of evidence and field importance; without incremental and stable performance, the classifier cannot underpin an outstanding advance.
- **confidence:** `0.99`

## JP-08 — The study is not reproducible from the reported model and data package

- **issue_key:** `JP-08-reproducibility-package`
- **axis:** `reproducibility`
- **severity:** `MAJOR`
- **anchor:** Data and code availability, “Raw single-cell data, model code, coefficient values, and the final patient-level analysis dataset are not deposited. Random seeds and software versions were not recorded”; Score construction and validation, the formula is described as “locked” but its coefficients are not given.
- **falsifiable concern:** An independent group cannot calculate the five-gene score, reproduce the split, reconcile the three AUC values, or audit the discovery/model workflow. Re-execution may not reproduce the reported findings.
- **concrete resolution test:** Deposit de-identified data or a justified controlled-access equivalent, raw/processed single-cell data, executable code, complete coefficient and preprocessing specification, environment versions, seeds, and figure source data; then reproduce all headline outputs from a clean environment.
- **journal gate:** `FAIL` — N006 methods necessary to interpret and replicate results.
- **confidence:** `1.00`

## JP-09 — The novelty and treatment-selection claims are not supported by an adequate literature foundation

- **issue_key:** `JP-09-reference-foundation`
- **axis:** `reference-support`
- **severity:** `MAJOR`
- **anchor:** Introduction, “none provides a universal, mechanistically validated guide to immunotherapy selection” and “the first clinically actionable HCC immune score”; References, only references 1 and 2; final manuscript note, reference 1 is cited for absence of prior clinically useful immune signatures and reference 2 for anti-PD-1 monotherapy benefit selection.
- **falsifiable concern:** The cited works, as described in the packet, do not directly establish the exhaustive novelty claim or validate this score as a selector of anti-PD-1 monotherapy. A complete literature review may identify prior related signatures or show that the treatment citation addresses a different regimen and question.
- **concrete resolution test:** Conduct a systematic, current comparison with prior HCC immune signatures, prognostic models, biomarkers, and treatment-predictive studies; cite primary sources directly matched to each claim; and quantify what conceptual or performance advance remains after comparison. Remove “first” and treatment-selection claims unless directly supported.
- **journal gate:** `FAIL` — N001 novelty/field importance and N002 evidence assessment.
- **confidence:** `0.96`

# MINOR issues

## JP-10 — Broad-audience framing obscures the actual study population and endpoint

- **issue_key:** `JP-10-title-and-summary-framing`
- **axis:** `writing-clarity`
- **severity:** `MINOR`
- **anchor:** Title, “universal therapeutic vulnerability in hepatocellular carcinoma”; Abstract, “3-year mortality”; Study population, “adults who underwent resection”; Impact and implications, “select anti-PD-1 therapy.”
- **falsifiable concern:** A general reader may infer that treatment response and pan-aetiology utility were directly studied, when the clinical endpoint was overall survival in a resected single-centre cohort.
- **concrete resolution test:** Revise the title, summary, and impact text so that they name the retrospective resection cohort, prognostic endpoint, and exploratory preclinical status; confirm that no sentence implies anti-PD-1 benefit selection without treatment-comparative human evidence.
- **journal gate:** `FAIL` — broad accessibility and accurate communication under N001/N002.
- **confidence:** `0.99`

## JP-11 — Limitations are acknowledged but then logically negated

- **issue_key:** `JP-11-limitations-logic`
- **axis:** `claim-moderation`
- **severity:** `MINOR`
- **anchor:** Discussion, “We did not use an external cohort. Nonetheless, the single-cell sample size and mechanistic experiments support application across HCC aetiologies and treatment settings”; and “Future prospective studies may refine, but are not required to establish, clinical utility.”
- **falsifiable concern:** Neither cell count nor preliminary mechanistic concordance substitutes for independent clinical validation; prospective and cross-setting tests could overturn the claimed utility.
- **concrete resolution test:** State the limitations as conclusion-limiting conditions, not caveats overcome by unrelated evidence, and restrict conclusions to association and preclinical hypothesis generation until the tests in JP-01 through JP-04 are passed.
- **journal gate:** `FAIL` — N002 strength-of-evidence communication.
- **confidence:** `1.00`

# EDITORIAL issues

## JP-12 — Initial-submission structure and declarations are incomplete or non-standard

- **issue_key:** `JP-12-submission-components`
- **axis:** `ethical-governance`
- **severity:** `EDITORIAL`
- **anchor:** Ethics, “complied with institutional requirements,” while “The approving committee, protocol number, consent procedure, animal protocol, and humane endpoints are not reported”; manuscript sequence includes “Impact and implications,” but the packet inventory reports no tables, figure images, supplementary information, reporting checklists, or cover letter.
- **falsifiable concern:** The submission may lack information required to verify human and animal oversight and may not yet be assembled in the target journal’s expected initial-submission sequence.
- **concrete resolution test:** Provide the approving bodies, protocol identifiers, consent or waiver basis, animal protocol, humane endpoints, and all required declarations/checklists; assemble the initial file in the journal-specified order and include the figure images. Editorial staff should verify current submission-system requirements against the frozen official profile.
- **journal gate:** `NOT ASSESSABLE` for underlying compliance; `FAIL` for reporting completeness under N007 as supplied.
- **confidence:** `0.98`

# Claim-ceiling risks

- `JP-01`, `JP-03`: The clinical evidence supports only an exploratory, single-centre prognostic association. It does not support “universal,” “immediately deployable,” “clinically actionable,” or anti-PD-1 treatment-selection language.
- `JP-04`: The perturbation evidence supports an EVA1-associated growth phenotype and correlated molecular changes. It does not yet support “causal driver of immune escape,” “sensitizes HCC to anti-PD-1,” or a treatment strategy.
- `JP-02`, `JP-05`, `JP-07`: Until leakage-free independent validation and endpoint reconciliation are completed, even the quantitative prognostic-performance claim should be presented as an internally derived estimate with high risk of optimism.
- `JP-06`: The eight-patient single-cell result should be framed as exploratory because the reported cell-level analysis does not establish patient-level reproducibility.
- `JP-09`: “First” and “none” claims cannot exceed the scope of an adequate, directly supported literature comparison.

# Required versus optional additional work

Required to support the current Nature-level headline:

1. A genuinely independent, multi-centre, adequately powered validation of the fully locked score, with broad aetiologic and clinical-setting coverage.
2. Direct evidence that the score predicts anti-PD-1 benefit rather than prognosis, including an appropriate comparator, treatment-interaction analysis, calibration, and decision utility.
3. Orthogonal, rescue-supported mechanistic work in immune-relevant systems and a factorial in vivo design that can isolate EVA1 × anti-PD-1 interaction.
4. Patient-aware single-cell reanalysis with multiplicity control and independent replication.
5. Reconciliation of the 3-year endpoint and AUC values, full uncertainty reporting, clinical-baseline comparison, and appropriate censoring methods.
6. A reproducible data/code/model package and complete ethics/governance reporting.
7. A current, direct literature comparison sufficient to establish the remaining conceptual novelty.

Optional if claims are narrowed to a field-specific exploratory report:

- Additional spatial localization or multi-omic characterization of EVA1.
- Broader dose-response and toxicity studies before therapeutic-development claims.
- More polished broad-audience framing and graphical synthesis after the evidentiary core is corrected.
- Longer-term clinical endpoints beyond those needed to validate the pre-specified primary claim.

# Journal-fit posture

Current posture: **high desk-screen risk and not competitive as a Nature Article in its present evidentiary form**. The topic is important and the discovery-to-function narrative is readable, but the demonstrated contribution is narrower than the title and conclusions, and several central tests are structurally incapable of supporting the claims made. This is not a request for cosmetic revision. Either the claims must be substantially narrowed for a specialist, exploratory venue, or the required independent clinical and causal evidence must be added before the manuscript can plausibly be judged against Nature’s outstanding-importance standard.

# NOT ASSESSABLE items

- Figure-image integrity, visual readability, exact plotted values, and consistency of panels beyond the legends: figure images and source data were not supplied.
- Table completeness and patient-level descriptive balance: no tables were supplied.
- Numerical reconciliation of AUCs, hazard ratios, P values, cell-level outputs, and tumour volumes: source tables and analysis code were not supplied.
- Existence or adequacy of unreported supplementary experiments and protocols: supplementary information and protocols were not supplied.
- Full-text support from references 1 and 2: only citation metadata and the manuscript’s stated citation usage were supplied; the cited papers were not inspected under the frozen-input boundary.
- Compliance of raw-data sharing with consent or privacy constraints: consent documentation and the dataset were not supplied.
- Whether human and animal approvals actually exist and were adequate: the manuscript gives only a generic compliance statement and omits identifiers and procedures.
- Final submission-system compliance, author information, competing interests, funding, author contributions, and cover-letter positioning: these materials were not supplied.

# Evidence anchors

- **Contribution and claims:** Title; Abstract; Impact and implications; first and second paragraphs of Discussion.
- **Clinical cohort and endpoint:** Patients and methods → Study population; Results → The five-gene score predicts survival.
- **Model leakage and absent comparators:** Patients and methods → Score construction and validation.
- **Single-cell unit of analysis:** Patients and methods → Single-cell discovery; Results → Single-cell discovery identifies an immune-evasion programme.
- **Perturbation limitations:** Patients and methods → Functional experiments; Mouse experiment; Results → EVA1 perturbation supports a therapeutic mechanism.
- **Reproducibility:** Data and code availability.
- **Governance reporting:** Ethics.
- **Figure/AUC conflict:** Results → The five-gene score predicts survival; Figure legend for Figure 3.
- **Reference foundation:** Introduction; References; final paragraph describing how references 1 and 2 are used.
- **Packet boundary:** `00_input_inventory.json`; `02_shared_fact_base.md`.
- **Journal gates:** frozen `nature-journal-profile.json`, especially N001, N002, N006, and N007.

# Confidence and reasons

Overall confidence: **0.99**. The highest-priority conclusions follow from explicit statements in the manuscript rather than inferred absences: selection used the full cohort before splitting; there was no external cohort; all mice received anti-PD-1; one guide was used without rescue or immune co-culture; the AUC values conflict; follow-up is shorter than the headline horizon; and core reproducibility materials are explicitly not deposited. Confidence is lower only for figure-level, source-output, full-reference, and underlying ethics judgments because those materials were not supplied; these have been marked NOT ASSESSABLE rather than presumed defective.
