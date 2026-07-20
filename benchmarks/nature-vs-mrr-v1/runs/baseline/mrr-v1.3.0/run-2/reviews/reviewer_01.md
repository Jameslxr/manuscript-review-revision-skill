# Reviewer role

`journal-priority` — Nature editorial priority, scope, Article-type fit, cross-field significance, and desk-screen risk.

# Material inspected and assessment boundary

I inspected only:

- the frozen manuscript, `/tmp/manuscript-skill-benchmark-20260720.zGfMWO/shared/manuscript.md` (SHA-256 `d51224a5ec717a268dadeee2fe9461a7b9d8c833f5b459be2d522a88d5c0006f`);
- `00_input_inventory.json`;
- the frozen official-source journal profile, `nature-journal-profile.json` (SHA-256 `6f6386d213e195d6ec26d0c177568f27753208425a6a15ce139b1ac2235fd6eb`);
- the factual intake, `02_shared_fact_base.md` (SHA-256 `947b2ed3c744626d5eadc56845b65f223c6b0d4336bd765e3c714acf4ff4a976`); and
- the manuscript-review-revision Skill and its routed review references.

This is a read-only scientific and editorial-priority review for **Nature**, **Article**, **initial submission**. I did not browse, inspect cited full texts, inspect figure images, inspect source data or code, or infer that packet components unavailable to me were absent from the underlying study. Where verification requires such materials, the result is `NOT ASSESSABLE`.

# Journal standard applied

The frozen profile classifies Nature as a broad flagship journal. I applied the following frozen standards:

- `N001`: an Article should report original research of outstanding scientific importance and reach a conclusion of interest to an interdisciplinary readership.
- `N002`: technical soundness, strength of evidence, novelty, field importance, and general-scientific interest must be assessed without predicting the editorial decision.
- `N006`: Methods must contain the elements necessary to interpret and replicate the results.
- `N007`: the initial manuscript should follow the Nature Article element sequence described in the frozen profile.

The strictness ceiling was also applied: a retrospective single-centre association cannot alone establish universal generalizability or treatment-selection utility; reuse or splitting of the same patients after full-data model construction cannot establish external validation; and a perturbation experiment without a design that identifies a treatment interaction cannot establish sensitization.

# Overall assessment

- **Formal subject scope and Article-type plausibility: `PASS`.** HCC immune escape, single-cell discovery, biomarker development, and functional experiments are within the broad subject range of an original biomedical Article.
- **Nature priority and cross-field significance (`N001`): `FAIL`.** The current evidence supports, at most, a preliminary HCC-specific association and perturbation hypothesis. It does not establish the claimed universal biomarker, broadly important immune-evasion mechanism, or treatment strategy.
- **Strength of evidence (`N002`): `FAIL`.** The central clinical and mechanistic claims are not identified by the reported designs.
- **Interpretability and replication (`N006`): `FAIL`.** The score cannot be reconstructed from the manuscript, and the reported computational analysis cannot be independently rerun from the available information.
- **Exact novelty against the current literature: `NOT ASSESSABLE`.** Only two references are supplied and browsing/full-text inspection was prohibited.
- **Figure, source-data, and numerical-output closure: `NOT ASSESSABLE`.** Figure images, tables, source data, and code were not supplied.

The desk-screen risk for Nature is therefore **very high**. The gap is scientific and conceptual, not cosmetic. Language polishing or reformatting would not resolve it.

# Major strengths

1. The study asks an important question: whether a tumour-cell state can connect immune context, prognosis, and therapeutic response in HCC.
2. The intended multi-layer design—single-cell discovery, a clinical cohort, cell-line perturbation, and an in vivo experiment—could be a useful architecture if each inferential link were independently and rigorously established.
3. The manuscript discloses several important limitations, including use of the full cohort for model selection, lack of an external cohort, lack of multiple-testing correction, use of one guide RNA, and the fact that all mice received anti-PD-1. This makes the principal claim-evidence gaps directly assessable.
4. Four main display items are structurally compatible with the typical scale in the frozen Nature profile, although their actual quality is `NOT ASSESSABLE` without the images and source data.

# BLOCKING issues

## JP-B1 — Clinical intended-use claim is not evaluated

- **Severity:** `BLOCKING`
- **Controlled axis:** `clinical-validity`
- **issue_key:** `untreated-cohort-treatment-selection`
- **Exact manuscript anchor:** Abstract, “clinically actionable, universally applicable predictor”; Impact and implications, “used to select anti-PD-1 therapy” and “immediately deployable biomarker”; Patients and methods, Study population, “72 adults who underwent resection”; Discussion, “immediate use for selecting anti-PD-1 therapy.”
- **Falsifiable concern:** The clinical cohort is a retrospective resection cohort analysed for overall survival, not an intended-use cohort receiving anti-PD-1 with a defined response or benefit endpoint. Overall-survival association in this cohort cannot identify differential benefit from anti-PD-1, and the recorded “treatment after recurrence” introduces rather than resolves treatment heterogeneity. The deployability, treatment-selection, and universal-applicability claims would be false if the score is merely prognostic or tracks disease severity.
- **Concrete resolution test:** Either (a) remove all treatment-selection, deployability, clinical-utility, and universal claims and limit the conclusion to a preliminary retrospective prognostic association in this exact cohort, or (b) evaluate a fully locked assay, formula, cutoff, and missing-data rule in an independent intended-use HCC immunotherapy cohort, against prespecified clinical baselines, with calibration, clinically relevant operating characteristics, and a design/analysis capable of distinguishing prognostic association from treatment interaction. For a treatment-selection claim, demonstrate replicated benefit heterogeneity rather than outcome association alone.
- **Journal gate:** `N001 FAIL`; `N002 FAIL`; Nature flagship clinical-consequence threshold.
- **Confidence:** `0.99`
- **Required versus optional:** `REQUIRED`

## JP-B2 — “Independent validation” is invalidated by full-cohort model construction

- **Severity:** `BLOCKING`
- **Controlled axis:** `reproducibility`
- **issue_key:** `full-data-selection-internal-split`
- **Exact manuscript anchor:** Score construction and validation, “Five genes were retained after stepwise selection using the entire 72-patient dataset,” “Expression cutoffs, coefficient signs, and missing-value rules were also chosen using the full dataset,” followed by “The same 72 patients were then randomly divided 70:30”; Discussion, “validated in an independent subset.”
- **Falsifiable concern:** The nominal validation subset influenced gene retention, coefficients/signs, cutoffs, and missing-value rules before the split. It is therefore not independent and cannot provide an unbiased estimate of generalization. The apparent performance could materially decrease when every analytic choice is frozen before exposure to an untouched cohort.
- **Concrete resolution test:** Rebuild and lock the complete pipeline using discovery/training data only, including feature selection, coefficients, transformations, cutoffs, and missing-data handling, then evaluate it once in a patient-independent external cohort from a distinct site and preferably a distinct temporal or etiologic setting. Nested resampling may estimate internal optimism but must not be labelled external or independent validation. Recompute all performance with confidence intervals and provide the exact locked model.
- **Journal gate:** `N002 FAIL`; the stated validation basis for `N001` significance is not established.
- **Confidence:** `1.00`
- **Required versus optional:** `REQUIRED`

## JP-B3 — The mouse design cannot establish anti-PD-1 sensitization

- **Severity:** `BLOCKING`
- **Controlled axis:** `causal-vs-correlative`
- **issue_key:** `anti-pd1-interaction-not-identified`
- **Exact manuscript anchor:** Mouse experiment, “All mice received anti-PD-1”; Results, “We conclude that EVA1 inhibition sensitizes HCC to anti-PD-1”; Abstract, “sensitized xenografts to anti-PD-1 treatment.”
- **Falsifiable concern:** With no untreated arm, the reported comparison identifies only the effect of EVA1 depletion among anti-PD-1-treated tumours. Because EVA1 depletion already reduced cell growth in vitro, smaller xenografts can arise from a treatment-independent growth effect. No EVA1-by-anti-PD-1 interaction is estimable, so “sensitization” is not established.
- **Concrete resolution test:** Conduct an adequately powered randomized factorial experiment containing control and EVA1 perturbation crossed with vehicle/isotype and anti-PD-1, with blinded measurement, prespecified exclusions, replicated experiments, verified target engagement, and an interaction contrast with uncertainty. Use an immunologically interpretable model and add immune-response readouts. Alternatively, remove all sensitization and anti-PD-1 therapeutic-development claims.
- **Journal gate:** `N002 FAIL`; the proposed therapeutic consequence and causal advance required by `N001` are unsupported.
- **Confidence:** `1.00`
- **Required versus optional:** `REQUIRED`

## JP-B4 — Outstanding importance and a major cross-field conceptual advance are not substantiated

- **Severity:** `BLOCKING`
- **Controlled axis:** `novelty-significance`
- **issue_key:** `flagship-conceptual-advance-unsubstantiated`
- **Exact manuscript anchor:** Title, “establishes a universal therapeutic vulnerability”; Introduction, “none provides a universal, mechanistically validated guide,” “the first clinically actionable HCC immune score,” and “EVA1 directly controls anti-tumour immunity”; Discussion, “universal immune-evasion mechanism.”
- **Falsifiable concern:** The presented evidence comes from eight single-cell patients, one retrospective single-centre resection cohort, two cell lines, and one ten-mouse experiment. Even if the reported associations are numerically correct, this scale and design do not by themselves demonstrate an outstanding, interdisciplinary conceptual advance. The manuscript also supplies only two references, neither of which is presented as a systematic comparator to prior HCC immune signatures or EVA1 biology. The precise novelty may exist, but it is not established in the submitted text.
- **Concrete resolution test:** Provide a claim-specific comparison with the relevant current literature and show exactly what prior conceptual barrier is overcome. Substantiate broad importance with independent, etiologically diverse human validation and a complete causal chain that links tumour state, immune phenotype, and treatment response. If those data are unavailable, narrow the contribution to a preliminary disease-specific hypothesis and retarget to a venue whose editorial threshold matches that evidence.
- **Journal gate:** `N001 FAIL`; novelty component of `N002 NOT ASSESSABLE` externally but inadequately substantiated internally.
- **Confidence:** `0.96` for the Nature-priority failure; exact novelty itself remains `NOT ASSESSABLE`.
- **Required versus optional:** `REQUIRED`

## JP-B5 — The central score and analysis are not reconstructable

- **Severity:** `BLOCKING`
- **Controlled axis:** `reproducibility`
- **issue_key:** `model-reconstruction-materials-missing`
- **Exact manuscript anchor:** Data and code availability, “Raw single-cell data, model code, coefficient values, and the final patient-level analysis dataset are not deposited. Random seeds and software versions were not recorded”; Score construction and validation, reference to formula, cutoffs, coefficient signs, and missing-value rules without reporting their values.
- **Falsifiable concern:** A reader cannot calculate the claimed biomarker, reproduce feature selection, audit leakage, or regenerate the reported performance from the manuscript and stated availability. An “immediately deployable” score is contradicted by the absence of the formula and assay/processing specification.
- **Concrete resolution test:** Publish the exact five-gene formula, coefficients, transformations, units, assay specification, cutoff, and missing-data rules. Deposit raw and processed single-cell data in an appropriate repository, release executable analysis code with seeds and a captured environment, and provide a deidentified patient-level dataset or a justified controlled-access route plus source data. A clean-environment rerun should reproduce the reported cohort, model, and all displayed values.
- **Journal gate:** `N006 FAIL`; technical-soundness and transparency components of `N002 FAIL`.
- **Confidence:** `0.99`
- **Required versus optional:** `REQUIRED`

# MAJOR issues

## JP-M1 — Single-cell discovery uses cells as independent biological replicates

- **Severity:** `MAJOR`
- **Controlled axis:** `experimental-design`
- **issue_key:** `single-cell-pseudoreplication`
- **Exact manuscript anchor:** Single-cell discovery, “Cells were treated as independent observations,” nominal `P < 0.05`, and “no multiple-testing correction”; Results, “1,842 nominally significant genes.”
- **Falsifiable concern:** The biological contrast is defined across eight tumours, but cell-level testing treats 46,218 correlated cells as independent and applies no multiplicity control. The apparent discovery set may therefore reflect pseudoreplication, unequal cell counts, or patient-specific effects rather than a reproducible tumour programme.
- **Concrete resolution test:** Reanalyse at the patient/sample level using an appropriate pseudobulk or mixed-model framework that preserves pairing and batch structure, reports effect sizes and uncertainty, and controls the false-discovery rate. EVA1 and the 27 modelling candidates must remain supported in patient-level sensitivity analyses.
- **Journal gate:** Evidence-strength component of `N002`; foundation of the claimed `N001` advance.
- **Confidence:** `0.99`
- **Required versus optional:** `REQUIRED`

## JP-M2 — Model complexity and performance reporting do not support a stable prognostic score

- **Severity:** `MAJOR`
- **Controlled axis:** `statistical-rigor`
- **issue_key:** `events-overfitting-no-clinical-baseline`
- **Exact manuscript anchor:** Study population, “Thirty-one deaths”; Score construction, “Twenty-seven genes” plus “18 available clinical and molecular covariates,” stepwise selection on 72 patients; Statistical analysis, no confidence intervals; Score construction, “BCLC stage and other clinical baselines were not evaluated,” and no calibration or decision-curve analysis.
- **Falsifiable concern:** With 31 deaths and extensive data-driven selection, the fitted model is likely unstable and optimistically biased. AUC without uncertainty, calibration, prespecified baseline comparison, or incremental-value analysis does not show that the score is robust or clinically useful.
- **Concrete resolution test:** Prespecify a parsimonious modelling strategy justified by event count; quantify optimism and coefficient stability; report hazard-ratio and performance confidence intervals; test proportional hazards; report time-dependent discrimination and calibration; compare against BCLC and other prespecified clinical baselines; and validate the locked model externally. The score must show reproducible incremental value rather than isolated apparent discrimination.
- **Journal gate:** `N002 FAIL` for the current clinical-performance claim.
- **Confidence:** `0.98`
- **Required versus optional:** `REQUIRED`

## JP-M3 — The three-year AUC is internally inconsistent and poorly supported by follow-up

- **Severity:** `MAJOR`
- **Controlled axis:** `figures-and-tables`
- **issue_key:** `three-year-auc-inconsistent`
- **Exact manuscript anchor:** Abstract, AUC `0.91`; Results, validation-set AUC `0.84`; Figure 3 legend, AUC `0.86`; Study population, median follow-up among survivors `18 months`; Results, “3-year outcome status was unavailable for many surviving patients.”
- **Falsifiable concern:** Three different values are reported for the same apparent endpoint, and the short follow-up raises unresolved censoring and risk-set questions. At least two of the three values cannot be the same analysis result, and a standard binary ROC calculation would be invalid if censored status were treated as known.
- **Concrete resolution test:** Reconcile the value across source output, text, and figure; name the exact estimator; report numbers at risk, events by three years, censoring handling, uncertainty, and the patient subset used; and reproduce the value from released code/source data. If a valid three-year estimate is not supported, remove it and use an endpoint justified by follow-up.
- **Journal gate:** Technical-soundness component of `N002`; numerical figure closure is otherwise `NOT ASSESSABLE`.
- **Confidence:** `1.00`
- **Required versus optional:** `REQUIRED`

## JP-M4 — EVA1 perturbation does not establish a direct immune-evasion mechanism

- **Severity:** `MAJOR`
- **Controlled axis:** `mechanism-evidence`
- **issue_key:** `eva1-causal-chain-incomplete`
- **Exact manuscript anchor:** Functional experiments, “one CRISPR guide RNA,” no second guide, rescue, target-engagement assay, or immune-cell co-culture; Results, “These findings show that EVA1 directly suppresses anti-tumour immunity.”
- **Falsifiable concern:** Reduced cell growth, altered PD-L1, and interferon-response transcripts after one guide are compatible with off-target effects, general growth stress, or indirect pathway changes. Experiments without immune cells do not demonstrate suppression of anti-tumour immunity, and no rescue or orthogonal perturbation establishes EVA1 specificity.
- **Concrete resolution test:** Replicate with at least one independent guide or orthogonal loss-of-function method, verify target engagement, restore the phenotype with a rescue construct, separate growth effects from immune signalling, and demonstrate an EVA1-dependent immune-cell phenotype in an appropriate co-culture and/or immune-competent in vivo model. Directness requires temporal or molecular evidence establishing causal order.
- **Journal gate:** `N002`; the claimed mechanistic advance under `N001` remains unsupported.
- **Confidence:** `0.99`
- **Required versus optional:** `REQUIRED`

## JP-M5 — Animal design and reporting do not support general mechanistic inference

- **Severity:** `MAJOR`
- **Controlled axis:** `experimental-design`
- **issue_key:** `xenograft-rigor-and-interpretability`
- **Exact manuscript anchor:** Mouse experiment, ten subcutaneous Huh7 xenografts, five per group, allocation by cage order, unblinded measurement, day-21 t-test, and no independent replicate; Results, no immune infiltration, survival, toxicity, or post-implantation EVA1 measurement.
- **Falsifiable concern:** Non-random cage-order allocation, unblinded measurement, very small group size, a single terminal comparison, absent target-engagement confirmation, and no replication leave the result vulnerable to allocation, measurement, and model-specific effects. The host immune context and rationale for anti-PD-1 activity in this xenograft system are not reported, preventing interpretation of an immune-evasion claim.
- **Concrete resolution test:** Report model/host details and biological-unit rationale; use randomized allocation, blinded longitudinal measurement, a prespecified sample-size rationale and analysis, target-engagement and immune readouts, transparent exclusions/attrition, and an independent replication. Demonstrate the effect in a model capable of interrogating the claimed immune mechanism.
- **Journal gate:** `N002`; interpretability requirement under `N006`.
- **Confidence:** `0.98`
- **Required versus optional:** `REQUIRED`

## JP-M6 — Human and animal governance cannot be verified from the manuscript

- **Severity:** `MAJOR`
- **Controlled axis:** `ethical-governance`
- **issue_key:** `ethics-reporting-incomplete`
- **Exact manuscript anchor:** Ethics, “complied with institutional requirements,” with approving committee, protocol number, consent procedure, animal protocol, and humane endpoints not reported.
- **Falsifiable concern:** The manuscript does not provide the identifiers and procedures needed to verify human-subject approval/consent and animal oversight. This is a reporting failure; whether approvals and consent actually existed is `NOT ASSESSABLE`.
- **Concrete resolution test:** Add the named human ethics committee, approval/protocol identifier, consent or waiver basis, and applicable governance details; add the animal oversight committee, protocol identifier, welfare monitoring, humane endpoints, and euthanasia criteria. Editorial documentation should match the manuscript.
- **Journal gate:** Technical and ethical acceptability under `N002`; declarations/package completeness under `N007`.
- **Confidence:** `0.99` for incomplete reporting; `NOT ASSESSABLE` for actual approval status.
- **Required versus optional:** `REQUIRED`

# MINOR issues

No issue is safely classifiable as merely `MINOR` under the present Nature gate. The observable problems either affect the central inference, reproducibility, or mandatory submission reporting.

# EDITORIAL issues

## JP-E1 — Article architecture does not follow the frozen Nature element sequence

- **Severity:** `EDITORIAL`
- **Controlled axis:** `writing-clarity`
- **issue_key:** `nature-article-element-order`
- **Exact manuscript anchor:** Headings “Abstract,” “Impact and implications,” “Patients and methods” before “Results,” and the absence from the supplied manuscript of visible author/affiliation and required-declaration sections.
- **Falsifiable concern:** The current architecture resembles a specialty-journal format rather than the element order in frozen requirement `N007`. This may create an avoidable initial-submission compliance problem, although author/declaration materials may exist outside the supplied packet.
- **Concrete resolution test:** At package preparation, map the manuscript to the frozen Nature sequence—title, authors, affiliations, summary paragraph, main text, references, tables/legends, Methods, data/code availability, and required declarations—and remove or relocate the journal-mismatched “Impact and implications” element if not requested by Nature. Confirm any separately supplied authorship/declaration materials before calling the gate complete.
- **Journal gate:** `N007`; currently `NOT ASSESSABLE` for materials outside the packet and `FAIL` for the visible section order.
- **Confidence:** `0.91`
- **Required versus optional:** `REQUIRED` for a Nature submission package, but downstream of the scientific blockers.

# Claim-ceiling risks

1. **Five-gene score:** The supported ceiling is a preliminary retrospective prognostic association in this single-centre resection cohort, not a universally applicable or clinically deployable predictor.
2. **Validation:** The supported ceiling is internal apparent performance after full-data model development, not independent or external validation.
3. **Treatment selection:** No clinical treatment-selection inference is supported because the cohort does not evaluate anti-PD-1 benefit.
4. **EVA1 and T cells:** The inverse correlation across eight tumours is an association; it does not establish T-cell exclusion.
5. **EVA1 perturbation:** One-guide effects on growth, PD-L1, and transcripts are consistent with EVA1 involvement but do not establish a direct immune-evasion mechanism.
6. **Anti-PD-1 sensitization:** No sensitization claim is supported without an untreated arm and an EVA1-by-treatment interaction.
7. **Universality:** The reported cohort composition, two cell lines, and one mouse model do not support “all major HCC aetiologies,” all treatment settings, or universal generalizability.
8. **Therapeutic readiness:** The evidence nominates a hypothesis for further study; it does not establish readiness for therapeutic development.

# Required versus optional additional work

## Required to establish the current central claims

- Rebuild the single-cell discovery at the patient/sample level with multiplicity control.
- Develop and lock the model without leakage; report the complete formula and assay specification.
- Obtain independent external validation in the intended-use population, with clinical baselines, calibration, uncertainty, and decision-relevant evaluation.
- For anti-PD-1 selection, use a clinical or experimental design that distinguishes prognostic association from treatment interaction.
- Establish perturbation specificity, target engagement, rescue, immune consequence, and treatment interaction in appropriate models.
- Reconcile every AUC and survival output against source data and code.
- Provide a reproducible data/code package and complete ethics/animal-governance reporting.
- Replace universal, causal, actionable, sensitization, and deployment language unless and until the corresponding resolution tests pass.

## Optional strengthening that cannot substitute for required work

- Improve the cross-field explanation of why the biological concept matters beyond HCC.
- Refine figure sequencing and narrative accessibility for a general scientific audience after the analyses are valid.
- Add an etiologic subgroup exploration only if sample size and multiplicity permit; such exploration would not itself establish universality.
- Conform the final package to Nature’s element order after the scientific architecture is stable.

# Journal-fit posture

**Current Nature posture: do not submit in the present form.** Formal scope is plausible, but the manuscript does not meet the frozen Nature threshold for outstanding scientific importance, a major interdisciplinary conceptual advance, strength of evidence, or replication. The dominant desk-screen risks are explicit in the title and summary: “universal,” “clinically actionable,” “sensitized,” and “causal driver” are all beyond the reported designs.

Substantial new evidence—not wording changes alone—would be required for a credible Nature-level reconsideration. If the authors instead narrow the claims to preliminary cohort-specific association and hypothesis-generating perturbation, the work may become assessable for a specialty venue after rigorous reanalysis and reproducibility closure; selection of a specific alternative journal is outside this reviewer seat.

# NOT ASSESSABLE items

- Exact novelty and priority relative to the current literature, because browsing and cited-paper inspection were not performed.
- Whether references 1 and 2 semantically support the specific novelty and anti-PD-1-selection claims; only manuscript-supplied metadata and citation descriptions were available.
- Actual figure quality, image integrity, labels, visual statistics, and agreement with source values because figure images were not supplied.
- Table-level cohort characteristics, attrition, missingness, model outputs, and subgroup balance because tables were not supplied.
- Numerical reproducibility and source-data closure because raw data, patient-level data, and code were not supplied.
- Whether unreported human approval, consent, animal approval, humane endpoints, reporting checklists, declarations, cover letter, and authorship materials exist elsewhere in the underlying study/package.
- Whether the Huh7 xenograft host/model has an interpretable anti-PD-1-responsive immune compartment, because the necessary host details are not reported.
- Acceptance likelihood or final editorial decision; this review assesses evidence and journal fit only.

# Evidence anchors

- Title: “establishes a universal therapeutic vulnerability.”
- Abstract: eight resected HCCs, 72-patient retrospective cohort, AUC `0.91`, “causal driver,” “clinically actionable,” and “universally applicable.”
- Impact and implications: “used to select anti-PD-1 therapy,” “immediately deployable,” and “all major HCC aetiologies.”
- Study population: single centre, 72 resected patients, 31 deaths, median survivor follow-up 18 months, and per-analysis exclusion of missing values.
- Single-cell discovery: eight patients, cell-level Wilcoxon testing, cells treated as independent, nominal threshold, and no multiple-testing correction.
- Score construction: feature/model/cutoff choices made in all 72 patients before the 70:30 split; no external cohort, assay validation, calibration, decision curve, or clinical baseline.
- Functional experiments: one guide, no rescue, no target-engagement assay, and no immune-cell co-culture.
- Mouse experiment: five animals per group, all treated with anti-PD-1, cage-order allocation, unblinded measurement, single day-21 comparison, and no replicate.
- Results: AUC `0.84` versus Figure 3 legend `0.86` versus Abstract `0.91`; many three-year outcomes unavailable.
- Data and code availability: no deposited raw single-cell data, model code, coefficients, patient-level analysis dataset, seeds, or software versions.
- Ethics: oversight bodies, protocol identifiers, consent procedure, animal protocol, and humane endpoints not reported.

# Confidence and reasons

**Overall confidence: `0.99`** for the conclusion that the current manuscript fails the Nature priority/evidence gate. The decisive concerns are stated directly in the manuscript and do not depend on unavailable source data: the same full cohort was used before splitting; the clinical cohort does not evaluate anti-PD-1 benefit; all mice received anti-PD-1; the mechanistic perturbation lacks specificity/rescue and immune testing; and the score formula and computational materials are unavailable.

Confidence is lower for exact novelty, figure integrity, reference support, and underlying governance because those require materials or external inspection outside this blinded reviewer boundary. Those domains remain `NOT ASSESSABLE`, not `FAIL`, except where the manuscript itself explicitly documents the missing analysis or incomplete reporting.
