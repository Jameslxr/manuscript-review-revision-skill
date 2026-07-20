# Reviewer role

Independent reviewer 05; role_id: `claim-evidence-reference`. This review is restricted to claim ceilings, exact manuscript evidence, citation placement and stated metadata boundaries, contradictory internal evidence, and limitations.

# Material inspected and assessment boundary

I inspected only the following frozen inputs:

- `manuscript.md` (SHA-256 verified: `d51224a5ec717a268dadeee2fe9461a7b9d8c833f5b459be2d522a88d5c0006f`)
- `00_input_inventory.json`
- `nature-journal-profile.json` (SHA-256 verified: `6f6386d213e195d6ec26d0c177568f27753208425a6a15ce139b1ac2235fd6eb`)
- `02_shared_fact_base.md` (SHA-256 verified: `947b2ed3c744626d5eadc56845b65f223c6b0d4336bd765e3c714acf4ff4a976`)

I did not browse, replace the journal profile, inspect cited-paper full text, or inspect any other review or run artifact. Figure images, tables, supplementary information, raw data, source code, protocols, reporting checklists, and cover letter were not supplied. Consequently, numerical source-output reconciliation, visual figure review, and cited-paper full-text support are not assessable. Statements that the manuscript explicitly says were not performed are assessable as reported absences; material merely absent from the packet is not presumed absent from the underlying study.

# Journal standard applied

Target: Nature; Article; initial submission. I applied the frozen profile’s expectations that an Article report original research of outstanding scientific importance and reach a conclusion of interdisciplinary interest (N001), and that review assess technical soundness, strength of evidence, novelty, field importance, and broad interest without claiming the final editorial decision (N002). I also applied N006, requiring methods sufficient to interpret and replicate the results. Under the supplied strictness card, a broad-flagship claim requires strong causal completeness, independent multi-layer validation, broad accessibility, and reproducible methods; observational, retrospective, cell-line, and xenograft evidence alone cannot establish universal clinical actionability or human treatment benefit.

Critical-gate summary:

- Claim moderation: **FAIL**
- Causal versus correlative interpretation: **FAIL**
- Clinical actionability and treatment-benefit inference: **FAIL**
- Internal numerical coherence of the central predictor claim: **FAIL**
- Independent validation: **FAIL**
- Reproducibility of the locked score from the manuscript: **FAIL**
- Cited-paper full-text claim support: **NOT ASSESSABLE**
- Numerical and visual source-output reconciliation: **NOT ASSESSABLE**

# Overall assessment

The manuscript presents a potentially interesting chain from single-cell discovery to a clinical score and EVA1 perturbation, but its conclusions are not bounded by the evidence. The score is derived and selected using all 72 patients before a nominal 70:30 split, the reported three-year AUC conflicts across three manuscript locations, and follow-up is too immature for many stated three-year outcomes. The resected cohort does not establish response to anti-PD-1, while the mouse experiment gives anti-PD-1 to every animal and therefore cannot test sensitization. The evidence also does not establish EVA1 as a causal immune-escape driver: the human association is based on eight tumours, the single-cell test treats cells as independent, the cell-line perturbation uses one guide without rescue or immune-cell co-culture, and the mouse experiment does not measure immunity. These are not wording-only defects; they break the evidentiary bridge to the central title, Abstract, Impact and implications, and Discussion claims.

At the supplied Nature standard, the current claim-evidence package does not support an outstanding, broadly generalizable conceptual advance. Substantial new validation and redesigned causal and clinical analyses would be required; claim moderation alone could make the manuscript more accurate but would not by itself establish Nature-level significance.

# Major strengths

- The manuscript makes its intended evidence chain unusually explicit: single-cell discovery, survival modelling, perturbation in two cell lines, and a mouse experiment.
- Several important weaknesses are disclosed directly, including cell-level independence, lack of multiple-testing correction, full-cohort stepwise selection, absence of external validation, one-guide perturbation, no rescue, five mice per group, cage-order allocation, lack of blinding, and absence of a replicate mouse experiment. This transparency makes the claim ceiling testable.
- Exact contradictions in the central AUC are visible in the manuscript rather than hidden: Abstract `0.91`, Results `0.84`, and Figure 3 legend `0.86`.
- The Discussion acknowledges the retrospective, single-centre, predominantly viral-disease cohort and lack of an external cohort, although it then draws conclusions that are inconsistent with those limitations.

# BLOCKING issues

## R05-01 — Universal clinical actionability and deployment are unsupported

- **issue_key:** `R05-01-universal-clinical-actionability`
- **axis:** clinical-validity
- **severity:** BLOCKING
- **anchor:** Title, “establishes a universal therapeutic vulnerability”; Abstract, “clinically actionable, universally applicable predictor”; Impact and implications, “used to select anti-PD-1 therapy,” “immediately deployable biomarker,” and “for all major HCC aetiologies”; Discussion, “biomarker ready for clinical deployment” and “supports immediate use for selecting anti-PD-1 therapy.”
- **falsifiable concern:** The reported clinical evidence is one retrospective, single-centre cohort of 72 resected patients, with 58 viral-hepatitis cases, no external cohort, no independent assay, no calibration analysis, no decision-curve analysis, and no comparison with BCLC or other clinical baselines. The endpoint is overall survival, not response or benefit under anti-PD-1. Nothing reported tests whether the score changes treatment benefit, works across major HCC aetiologies, transfers across centres or assays, or is ready for deployment. The universal, actionable, and immediate-use claims would be falsified if a locked score failed calibration, added no value to clinical baselines, or showed no score-by-treatment interaction in independent immunotherapy-treated patients.
- **concrete resolution test:** Lock the complete formula, coefficients, cutoffs, assay, preprocessing, and missing-data rules before testing. Validate discrimination with uncertainty, calibration, and added value over established clinical baselines in sufficiently powered, independent, multi-centre cohorts representing major aetiologies. To claim therapy selection, demonstrate a prespecified score-by-treatment interaction or equivalent causal treatment-benefit evidence in an appropriate anti-PD-1 comparison, followed by prospective clinical-utility evaluation. Until those tests pass, remove “universal,” “clinically actionable,” “immediately deployable,” “ready for clinical deployment,” “select anti-PD-1 therapy,” and “all major HCC aetiologies.”
- **journal gate:** **FAIL** — N001 and the supplied broad-flagship clinical-validity standard.
- **confidence:** 0.99

## R05-02 — The score has no independent validation and the three-year performance claim is internally contradictory

- **issue_key:** `R05-02-model-validation-and-auc`
- **axis:** statistical-rigor
- **severity:** BLOCKING
- **anchor:** Methods, Score construction and validation, “Five genes were retained after stepwise selection using the entire 72-patient dataset” and “The same 72 patients were then randomly divided 70:30”; Results, “validation-set 3-year mortality AUC of 0.84”; Figure 3 legend, “validation AUC as 0.86”; Abstract, “AUC of 0.91”; Results, “median follow-up was 18 months” and “3-year outcome status was unavailable for many surviving patients”; Discussion, “validated in an independent subset.”
- **falsifiable concern:** Because gene selection, coefficient signs, expression cutoffs, and missing-value rules were chosen using all 72 patients before the split, the validation subset is not independent and is contaminated by information used for model construction. The effective modelling burden—27 genes plus 18 covariates with 31 deaths—also creates severe overfitting risk. The central AUC is irreconcilable within the manuscript (`0.91`, `0.84`, `0.86`), and the handling of censoring for the three-year endpoint is not stated despite many unavailable three-year outcomes. The performance claim is falsifiable by rerunning a fully specified, leakage-free analysis: materially lower corrected performance or wide uncertainty would invalidate the present language.
- **concrete resolution test:** Reconcile every reported AUC to one versioned output and define the estimand and censoring method. Evaluate the entire feature-selection and tuning pipeline inside resampling or nested validation, with no test-set access; report optimism-corrected time-dependent discrimination, confidence intervals, calibration, event counts, and sensitivity to censoring. Then test the locked model in a genuinely external cohort. Do not call the random subset “independent,” and do not retain a numerical performance claim until manuscript text, legend, tables, and source output agree.
- **journal gate:** **FAIL** — N001/N002 strength-of-evidence standard and the strictness requirement for independent validation.
- **confidence:** 1.00

## R05-03 — Anti-PD-1 sensitization is not tested by the reported mouse design

- **issue_key:** `R05-03-anti-pd1-sensitization`
- **axis:** causal-vs-correlative
- **severity:** BLOCKING
- **anchor:** Abstract, “sensitized xenografts to anti-PD-1 treatment”; Methods, Mouse experiment, “All mice received anti-PD-1”; Results, “We conclude that EVA1 inhibition sensitizes HCC to anti-PD-1”; Discussion, “supports immediate use for selecting anti-PD-1 therapy.”
- **falsifiable concern:** Sensitization is an interaction claim, but the experiment has no no-anti-PD-1 arms. Comparing control versus EVA1-depleted tumours when every mouse receives anti-PD-1 can show, at most, a difference between implanted cell states under one treatment condition; it cannot distinguish a general growth effect from increased anti-PD-1 sensitivity. This alternative is especially live because EVA1 depletion already reduces 72-hour cell growth in both cell lines. The sensitization claim would be falsified if EVA1 depletion produced the same relative growth reduction without anti-PD-1 or if no EVA1-by-treatment interaction were present.
- **concrete resolution test:** Use a prespecified factorial experiment with control/EVA1-perturbed tumours crossed with isotype or no treatment/anti-PD-1, adequate biological replication, randomized allocation, blinded measurement, and a formal interaction test. Include longitudinal tumour growth and relevant immune readouts, and independently replicate the experiment. Until a reproducible interaction is shown, replace “sensitizes” with a description of the observed comparison and remove treatment-selection claims.
- **journal gate:** **FAIL** — N001/N002 causal strength and the supplied requirement for strong causal completeness.
- **confidence:** 1.00

## R05-04 — EVA1 is not established as the causal driver of immune escape

- **issue_key:** `R05-04-eva1-causal-driver`
- **axis:** mechanism-evidence
- **severity:** BLOCKING
- **anchor:** Abstract, “establish EVA1 as the causal driver of immune escape”; Results, Single-cell discovery, “correlated inversely with a T-cell score” and “interpreted this association as evidence that EVA1 excludes T cells”; Results, EVA1 perturbation, “show that EVA1 directly suppresses anti-tumour immunity”; Methods, Functional experiments, “one CRISPR guide RNA” and no “second guide, rescue construct, direct target-engagement assay, or immune-cell co-culture”; Results, mouse experiment, “did not measure immune infiltration.”
- **falsifiable concern:** The human evidence is association across eight tumours, not causal exclusion. The cell experiments measure growth, PD-L1, and three interferon-response transcripts in tumour-cell cultures without immune cells, so they cannot demonstrate suppression of anti-tumour immunity. One guide without rescue leaves on-target specificity unresolved. The xenograft comparison does not measure immune infiltration or post-implantation EVA1 expression and is confounded by a baseline tumour-cell growth phenotype. The causal-driver claim would be falsified by failure of an independent perturbation, rescue of the phenotype, or absence of immune-functional effects after separating tumour growth from immune mechanisms.
- **concrete resolution test:** Reproduce phenotypes with at least two independent perturbations, confirm target engagement, and restore them with an EVA1 rescue construct. Test immune-cell function directly in relevant co-culture and in an immunologically interpretable in vivo model, measuring immune infiltration/activation and tumour-cell-intrinsic growth separately. Use temporal or mediation evidence sufficient to connect EVA1 perturbation to immune escape. Unless these converge, describe EVA1 as an associated candidate with preliminary tumour-cell phenotypes, not “the causal driver.”
- **journal gate:** **FAIL** — N001/N002 and the strictness card’s strong-causal-completeness requirement.
- **confidence:** 0.99

# MAJOR issues

## R05-05 — Cell-level pseudoreplication and nominal screening do not support the discovery claim

- **issue_key:** `R05-05-single-cell-pseudoreplication`
- **axis:** experimental-design
- **severity:** MAJOR
- **anchor:** Methods, Single-cell discovery, “Cells were treated as independent observations,” “nominal P < 0.05,” and “no multiple-testing correction”; Results, “1,842 nominally significant genes”; Figure 1 legend, “Each point in the differential-expression panel represents one cell”; Figure 2 legend, “in eight tumours.”
- **falsifiable concern:** The biological exposure—high versus low infiltration—is defined at the tumour/patient level, but the test uses thousands of cells as independent observations from only eight patients. This inflates the apparent sample size and can make patient-specific effects appear gene-level significant. Screening at nominal P < 0.05 across many genes without multiplicity correction further weakens the 27-gene input set. The reported programme may not persist when patient is the independent unit.
- **concrete resolution test:** Reanalyse at the patient level using pseudobulk or an appropriately specified mixed model with patient/sample as the replication unit, control false discovery rate, report effect sizes and uncertainty, and demonstrate stability to leave-one-patient-out analysis. The discovery claim should be retained only for genes/programmes robust to these tests and independently replicated.
- **journal gate:** **FAIL** — N002 technical soundness and strength of evidence.
- **confidence:** 0.99

## R05-06 — Survival-effect estimates are reported without the diagnostics and uncertainty needed to sustain the prognostic claim

- **issue_key:** `R05-06-survival-inference`
- **axis:** statistical-rigor
- **severity:** MAJOR
- **anchor:** Statistical analysis, “The proportional-hazards assumption was not examined” and “Hazard ratios and P values were reported without confidence intervals”; Study population, “Records with missing values were excluded from each analysis”; Results, “hazard ratio 2.4, P = 0.04.”
- **falsifiable concern:** A Cox hazard ratio without a confidence interval, proportional-hazards assessment, specified covariate set, or complete-case accounting cannot show the precision, stability, or interpretability of the claimed independent prognostic association. Analysis-specific exclusion for missingness may change the cohort and event count without disclosure. The association could become imprecise, non-proportional, or unstable under transparent accounting.
- **concrete resolution test:** Report the exact analysis population and event count, missingness by variable, complete-case flow, all prespecified covariates and coefficients, hazard ratios with 95% confidence intervals, and proportional-hazards diagnostics. Use justified missing-data handling and sensitivity analyses. Recalibrate the language to the resulting uncertainty and avoid “independent” or robust prognostic wording if estimates are unstable.
- **journal gate:** **FAIL** — N002 strength-of-evidence standard.
- **confidence:** 0.97

## R05-07 — The score and central analyses are not reproducible from the manuscript or availability statement

- **issue_key:** `R05-07-score-reproducibility`
- **axis:** reproducibility
- **severity:** MAJOR
- **anchor:** Methods, Score construction and validation, “Expression cutoffs, coefficient signs, and missing-value rules were also chosen using the full dataset”; Data and code availability, “Raw single-cell data, model code, coefficient values, and the final patient-level analysis dataset are not deposited” and “Random seeds and software versions were not recorded.”
- **falsifiable concern:** A reader cannot calculate the five-gene score, reproduce the split, rerun feature selection, or audit the conflicting AUC values without coefficients, preprocessing rules, code, seeds, software versions, and analyzable data. The manuscript calls the biomarker deployable while withholding the minimum specification required to implement it.
- **concrete resolution test:** Provide the complete locked equation, gene identifiers, coefficient signs and values, units/normalization, cutoff derivation and value, missing-data rule, software/package versions, executable analysis code, and deterministic seeds or split identifiers. Deposit de-identified analyzable data and raw single-cell data where ethically permissible, or provide a controlled-access route plus synthetic/test data that reproduce the workflow. An independent party should be able to regenerate the reported cohort sizes, estimates, and figures.
- **journal gate:** **FAIL** — N006 and the supplied reproducible-methods expectation.
- **confidence:** 1.00

## R05-08 — Citation placement does not support the two claims to which the manuscript assigns the references

- **issue_key:** `R05-08-reference-claim-alignment`
- **axis:** reference-support
- **severity:** MAJOR
- **anchor:** References note, “The Introduction cites reference 1 for the statement that no previous immune signature has clinical utility”; reference 1 metadata, “Comprehensive and integrative genomic characterization of hepatocellular carcinoma”; References note, “The Discussion cites reference 2 for the claim that the five-gene score identifies patients who benefit from anti-PD-1 monotherapy”; reference 2 metadata, “Atezolizumab plus bevacizumab in unresectable hepatocellular carcinoma.”
- **falsifiable concern:** The first cited claim is a literature-wide negative assertion, but the stated metadata identifies one genomic-characterization paper; one such citation cannot establish that no prior immune signature has clinical utility. The second claim concerns this manuscript’s five-gene score and benefit from anti-PD-1 monotherapy, whereas the cited paper’s stated metadata concerns atezolizumab plus bevacizumab in unresectable HCC. Moreover, the current manuscript reports neither an anti-PD-1-treated clinical cohort nor a treatment-interaction analysis. Full-text support within either cited paper remains not assessable, but the claim-to-citation placement and treatment-context mismatch are assessable from the manuscript and supplied metadata.
- **concrete resolution test:** For the novelty claim, provide a transparent, current set of directly relevant citations and narrow “none”/“first” language to what the literature review can substantiate. For treatment benefit, cite direct evidence only if a study evaluates the same locked score in an appropriate anti-PD-1 comparison with a treatment-interaction analysis; otherwise delete the benefit claim. Verify all claim-support relationships against cited full texts before resubmission.
- **journal gate:** **FAIL** for current claim placement under N002; cited-paper full-text support remains **NOT ASSESSABLE**.
- **confidence:** 0.96

# MINOR issues

No additional MINOR issue is necessary within this functional lens; the relevant defects materially affect central inference and are classified above.

# EDITORIAL issues

No purely EDITORIAL issue is necessary within this functional lens. The problematic superlatives and causal verbs require evidentiary correction, not cosmetic editing.

# Claim-ceiling risks

- The human single-cell result supports, at most, an association between EVA1 expression and a T-cell score across eight tumours after a patient-level, multiplicity-controlled reanalysis; it does not show that EVA1 “excludes T cells.”
- The cell-line experiments support preliminary tumour-cell-intrinsic growth and molecular-expression effects after one-guide EVA1 depletion; they do not establish suppression of anti-tumour immunity.
- The mouse experiment supports, at most, a day-21 tumour-volume difference between control and EVA1-depleted Huh7 xenografts when both groups receive anti-PD-1; it does not establish sensitization without a treatment interaction.
- The 72-patient analysis is an internally developed, high-risk-of-bias prognostic model, not an independently validated clinical biomarker.
- Overall-survival association in resected patients is not evidence that the score predicts anti-PD-1 response or benefit.
- A cohort dominated by viral hepatitis cannot establish universality across all HCC aetiologies or treatment settings.
- Cross-modal concordance does not, by itself, demonstrate causality, generality, clinical utility, or deployment readiness.
- “First,” “none,” “universal,” “causal driver,” “immediately deployable,” “ready,” and “not required to establish clinical utility” are all above the current evidence ceiling.

# Required versus optional additional work

Required to support the present central claims:

1. A leakage-free reconstruction of the model-development pipeline and reconciliation of the three AUC values.
2. External, multi-centre validation of a fully locked score with clinically relevant comparators, calibration, uncertainty, and representative aetiologies.
3. Direct evidence of treatment prediction, not prognosis alone, using a prespecified treatment-interaction design in an anti-PD-1-relevant clinical setting.
4. A factorial in vivo anti-PD-1 experiment that can test sensitization, with randomization, blinding, adequate replication, interaction analysis, and immune readouts.
5. Orthogonal EVA1 perturbations, rescue, target-engagement confirmation, and direct immune-functional experiments.
6. Patient-level, multiplicity-controlled reanalysis and independent replication of the single-cell discovery.
7. Full reporting of the score, statistical uncertainty, missingness, survival diagnostics, data provenance, code, software versions, and reproducibility materials.
8. Claim-by-claim citation correction after full-text verification of the references.

If the authors do not perform the above, required revisions for an accurate lower-ceiling report are to remove clinical-actionability, treatment-selection, universality, causal-driver, anti-PD-1-sensitization, and deployment claims; present the work as exploratory and hypothesis-generating; call the split internal rather than independent; and state all uncertainty and design limitations without claiming that cross-modal concordance overcomes them.

Optional work:

- Broader pathway and tissue validation may strengthen biological context after the core causal tests pass.
- Additional aetiology-stratified exploratory analyses may guide future validation but cannot substitute for powered external cohorts.
- Longer-term toxicity and survival studies may inform therapeutic development after target specificity and immune mechanism are established.

# Journal-fit posture

The current manuscript is **not ready at the claim-evidence level for a Nature Article**. This is a scientific-fit assessment, not a prediction of the journal’s final editorial decision. The integration of modalities is potentially interesting, but the headline advance depends on non-independent model validation, internally inconsistent performance values, a prognostic-to-predictive leap, an in vivo design incapable of testing anti-PD-1 sensitization, and mechanistic evidence that does not directly test immune escape. Even after honest claim moderation, the remaining evidence would describe preliminary discovery rather than the outstanding, interdisciplinary, causally complete, independently validated advance expected under N001. Nature-level reconsideration would require the substantive required work above, not only rewriting.

# NOT ASSESSABLE items

- Whether the figure images visually support the legends or reveal additional discrepancies: **NOT ASSESSABLE** because figure images were not supplied.
- Whether `0.91`, `0.84`, or `0.86` matches the underlying calculation: **NOT ASSESSABLE** because tables, patient-level outputs, code, and figures were not supplied. The internal textual contradiction itself is assessable and fails.
- Exact numerical reproducibility, raw-data integrity, patient-level censoring, and the results of unreported sensitivity analyses: **NOT ASSESSABLE** from the supplied packet.
- Whether references 1 and 2 contain any passages that support adjacent background statements: **NOT ASSESSABLE** because cited-paper full text was intentionally not inspected. Citation placement and mismatch to the manuscript’s stated metadata and designs remain assessable.
- Whether absent supplementary information, protocols, or reporting checklists contain additional details: **NOT ASSESSABLE** because these materials were not supplied.
- Any evidence not described in the manuscript but potentially present in an underlying study: **NOT ASSESSABLE** and not presumed absent, except where the manuscript explicitly states that an analysis or control was not performed.

# Evidence anchors

- Title: “establishes a universal therapeutic vulnerability.”
- Abstract: “AUC of 0.91”; “causal driver of immune escape”; “clinically actionable, universally applicable.”
- Impact and implications: “used to select anti-PD-1 therapy”; “immediately deployable”; “all major HCC aetiologies.”
- Introduction: “none provides a universal, mechanistically validated guide”; “first clinically actionable”; “directly controls anti-tumour immunity.”
- Methods, Study population: 72 resected patients; 31 deaths; median follow-up 18 months; 58 viral-hepatitis cases.
- Methods, Single-cell discovery: eight patients; cells treated as independent; nominal P < 0.05; no multiple-testing correction.
- Methods, Score construction and validation: full-cohort selection before the 70:30 split; no external cohort, independent assay, calibration, decision curve, or clinical baseline.
- Methods, Functional experiments: one guide; no second guide, rescue, target engagement, or immune-cell co-culture.
- Methods, Mouse experiment: five mice per group; all received anti-PD-1; cage-order allocation; unblinded measurement; no independent replicate.
- Methods, Statistical analysis: no proportional-hazards check; no confidence intervals.
- Results: eight-tumour EVA1/T-cell-score correlation interpreted as exclusion; AUC values `0.84` versus Figure 3 `0.86`; many three-year outcomes unavailable.
- Results: cell-growth decrease after EVA1 depletion; no immune infiltration, survival, toxicity, or post-implantation EVA1 measurement.
- Discussion: “validated in an independent subset”; “immediate use”; “generality”; future prospective studies “are not required.”
- Data and code availability: no deposited raw single-cell data, model code, coefficient values, or patient-level dataset; no recorded seeds or software versions.
- References note: reference 1 assigned to a literature-wide negative utility claim; reference 2 assigned to benefit from anti-PD-1 monotherapy.

# Confidence and reasons

Overall confidence: **0.99**. The principal concerns follow directly from explicit manuscript statements, exact numerical contradictions, and designs that cannot identify the claimed causal or predictive effects. Confidence is highest for data leakage, the three AUC values, the absence of a no-anti-PD-1 arm, and the mismatch between a prognostic resection cohort and a treatment-benefit claim. Confidence is slightly lower for reference support because cited-paper full texts were intentionally outside scope; I therefore restrict that conclusion to citation placement, supplied metadata, treatment context, and the manuscript’s own lack of direct clinical anti-PD-1 evidence.
