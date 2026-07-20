# Reviewer role

`claim-evidence-reference` — atomic claim ceilings, internal evidence alignment, causal-versus-correlative language, contradictions, limitations, and citation-support boundaries.

# Material inspected and assessment boundary

Inspected only:

- `/tmp/manuscript-skill-benchmark-20260720.zGfMWO/shared/manuscript.md` (SHA-256 `d51224a5ec717a268dadeee2fe9461a7b9d8c833f5b459be2d522a88d5c0006f`; hash verified)
- `/tmp/manuscript-skill-benchmark-20260720.zGfMWO/shared/00_input_inventory.json`
- `/tmp/manuscript-skill-benchmark-20260720.zGfMWO/shared/nature-journal-profile.json` (SHA-256 `6f6386d213e195d6ec26d0c177568f27753208425a6a15ce139b1ac2235fd6eb`; hash verified)
- `/tmp/manuscript-skill-benchmark-20260720.zGfMWO/shared/02_shared_fact_base.md` (SHA-256 `947b2ed3c744626d5eadc56845b65f223c6b0d4336bd765e3c714acf4ff4a976`; hash verified)
- The mandated Skill and its routed review references.

This was a read-only scientific review. No manuscript revision, polishing, formatting, external browsing, external citation lookup, or inspection of figures, tables, supplements, raw data, source code, protocols, reporting checklists, or other reviewer outputs was performed. The packet explicitly lacks figure images, tables, supplements, raw data, and analysis code; numerical source reconciliation is therefore `NOT ASSESSABLE`. Absence from the packet is not treated as proof that an item was absent from the underlying study unless the manuscript expressly says so.

# Journal standard applied

Target: **Nature**, Article, initial submission. The supplied frozen profile classifies the journal as a broad flagship and states that an Article should report original research of outstanding scientific importance with a conclusion of interest to an interdisciplinary readership. The assessment applies the supplied requirements for technical soundness, strength of evidence, novelty, field importance, broad interest, and Methods adequate for interpretation and replication. The relevant frozen requirements are N001, N002, and N006.

Strict claim ceilings applied:

- A retrospective single-centre association cannot alone establish universal generalizability or therapeutic-selection utility.
- Reusing the full cohort for model construction before splitting does not establish independent validation.
- A perturbation experiment without a design identifying treatment interaction cannot establish sensitization.
- Association, prediction, mechanism, causation, clinical utility, and universal applicability are distinct evidence levels.

# Overall assessment

The manuscript contains a potentially interesting translational sequence—single-cell discovery, a clinical score, cellular perturbation, and an animal experiment—but the central conclusions repeatedly exceed the designs and reported evidence. The universal predictor, immediately deployable treatment-selection biomarker, causal immune-escape driver, and anti-PD-1 sensitization claims are not established by the stated analyses. The universal claim gate is `FAIL`; the biomarker clinical-validity gate is `FAIL`; the wet-lab mechanism gate is `FAIL`; and the animal treatment-interaction gate is `FAIL`. Exact semantic support from the two cited papers is `NOT ASSESSABLE` because their full text was not supplied and external lookup was prohibited.

For this reviewer lens, the present claim-evidence architecture does not meet the supplied Nature threshold for strength of evidence or a defensible major conceptual advance. Substantial new validation and/or material lowering of the claims is required.

# Major strengths

- The manuscript states several critical design limitations unusually clearly, including cell-level testing, no multiple-testing correction, full-cohort feature selection, absence of external validation, a single CRISPR guide, no rescue, and the absence of a no-anti-PD-1 animal arm.
- The claimed translational chain is explicit enough to audit at the level of atomic assertions.
- The use of two HCC cell lines gives some bounded evidence that EVA1 depletion is associated with reduced short-term cell growth in more than one in-vitro model.
- The manuscript reports a retrospective clinical cohort, single-cell observations, perturbation results, and an animal comparison rather than relying on only one evidence layer.
- The Discussion acknowledges the retrospective, single-centre cohort, aetiologic imbalance, and lack of an external cohort, although it does not respect the inferential consequences of those limitations.

# BLOCKING issues

## CE-01 — The clinical prediction and universal-applicability claims are not supported by independent validation

- **Severity:** `BLOCKING`
- **Controlled axis:** `clinical-validity`
- **Proposed issue_key:** `internal_reuse_not_external_validation`
- **Exact manuscript anchor:** Patients and methods, “Five genes were retained after stepwise selection using the entire 72-patient dataset”; “Expression cutoffs, coefficient signs, and missing-value rules were also chosen using the full dataset”; “The same 72 patients were then randomly divided 70:30 into a training set and a validation set”; Discussion, “The score was validated in an independent subset”; Abstract, “clinically actionable, universally applicable predictor for HCC.”
- **Falsifiable concern:** Because feature selection, coefficients, cutoffs, and missing-value rules were chosen using all 72 patients before the split, the later 70:30 subsets are not independent of model development. Therefore the reported subset performance does not test a locked model on independent data, and a single-centre cohort cannot establish transportability across centres, aetiologies, stages, assays, or treatment settings. The statements “independent subset,” “overcomes the limitations of earlier single-centre signatures,” and “universally applicable” are false relative to the reported workflow.
- **Concrete resolution test:** Either (a) evaluate a completely locked model—including genes, coefficients, cutoff, preprocessing, and missing-data rules—in an external cohort collected independently at an intended-use setting, with prespecified endpoints, uncertainty, calibration, clinical-baseline comparisons, and subgroup/transportability assessment; or (b) reframe all results as exploratory, internally derived associations and remove independent-validation, universal-applicability, deployment, and treatment-selection claims.
- **Journal gate if applicable:** N001, N002; universal claim gate `FAIL`; biomarker validation gate `FAIL`.
- **Confidence:** `0.99`
- **Required-versus-optional classification:** `REQUIRED`

## CE-02 — The manuscript does not test whether the score selects anti-PD-1 treatment

- **Severity:** `BLOCKING`
- **Controlled axis:** `claim-moderation`
- **Proposed issue_key:** `prognosis_not_treatment_selection`
- **Exact manuscript anchor:** Impact and implications, “used to select anti-PD-1 therapy” and “immediately deployable biomarker”; Discussion, “Its high AUC supports immediate use for selecting anti-PD-1 therapy”; Patients and methods, the cohort “underwent resection for HCC”; Results, “predicts survival.”
- **Falsifiable concern:** Overall-survival association in a retrospective resection cohort does not demonstrate predictive treatment benefit, treatment interaction, or clinical utility for anti-PD-1 selection. The manuscript reports no patient-level anti-PD-1 comparison, no randomized or otherwise identified treatment contrast, no score-by-treatment interaction, no prespecified operating threshold, no calibration, no decision-curve analysis, and no comparison with clinical baselines. A prognostic association cannot be promoted to a treatment-selection biomarker.
- **Concrete resolution test:** Demonstrate a prespecified score-by-treatment interaction in an appropriate independent treated-versus-comparator dataset at the intended-use setting, with a locked assay/model, calibration, clinically relevant operating characteristics, incremental value over a prespecified clinical baseline, and decision-relevant utility; otherwise remove every therapy-selection, clinically actionable, immediately deployable, and “used at diagnosis” assertion and explicitly limit the score to exploratory prognostic association.
- **Journal gate if applicable:** N001, N002; clinical-utility gate `FAIL`.
- **Confidence:** `1.00`
- **Required-versus-optional classification:** `REQUIRED`

## CE-03 — EVA1 is not established as a causal driver of immune escape

- **Severity:** `BLOCKING`
- **Controlled axis:** `causal-vs-correlative`
- **Proposed issue_key:** `eva1_causality_not_identified`
- **Exact manuscript anchor:** Results, “EVA1 was higher in low-infiltration tumours and correlated inversely with a T-cell score (Spearman r = −0.41, P = 0.03). We interpreted this association as evidence that EVA1 excludes T cells”; Functional experiments, “one CRISPR guide RNA,” with no “second guide, rescue construct, direct target-engagement assay, or immune-cell co-culture”; Results, “These findings show that EVA1 directly suppresses anti-tumour immunity”; Abstract, “the causal driver of immune escape.”
- **Falsifiable concern:** The patient evidence is correlational, based on eight tumours, and does not identify direction or exclude confounding. The in-vitro perturbation shows changes in cell growth, PD-L1 abundance, and three transcripts in tumour-cell monoculture, but no immune-cell phenotype, immune-mediated killing, direct target engagement, orthogonal perturbation, or rescue. One guide cannot exclude guide-specific or off-target effects. These layers are consistent with a hypothesis but do not establish that EVA1 directly excludes T cells, directly suppresses anti-tumour immunity, or is “the” causal driver of immune escape.
- **Concrete resolution test:** Establish guide-specific on-target causality with at least an orthogonal perturbation and rescue, verify target engagement, quantify immune-relevant phenotypes in an immune-competent context, and show that the proposed EVA1-dependent pathway mediates rather than merely accompanies the phenotype; alternatively replace causal/direct/driver language throughout with a precisely bounded association and perturbation-consistent hypothesis.
- **Journal gate if applicable:** N001, N002; wet-lab mechanism gate `FAIL`.
- **Confidence:** `0.99`
- **Required-versus-optional classification:** `REQUIRED`

## CE-04 — The animal design cannot establish anti-PD-1 sensitization

- **Severity:** `BLOCKING`
- **Controlled axis:** `experimental-design`
- **Proposed issue_key:** `no_treatment_interaction_for_sensitization`
- **Exact manuscript anchor:** Mouse experiment, “All mice received anti-PD-1”; Results, “We conclude that EVA1 inhibition sensitizes HCC to anti-PD-1”; Abstract, “sensitized xenografts to anti-PD-1 treatment”; Figure 4 legend, “Cell growth and xenograft volume following EVA1 depletion.”
- **Falsifiable concern:** With anti-PD-1 given to every mouse, the experiment estimates only the difference between EVA1-depleted and control tumours under one shared treatment condition. It cannot distinguish a general growth effect from an anti-PD-1-specific effect and therefore cannot identify sensitization. The observed in-vitro growth reduction makes this alternative explanation especially plausible. The reported two-group design lacks the untreated/no-antibody conditions required to test an EVA1-status-by-treatment interaction.
- **Concrete resolution test:** Use a prespecified factorial design containing EVA1 control/depletion crossed with anti-PD-1/control treatment, analyse the interaction with appropriate biological replication and uncertainty, and show immune-mediated response evidence; otherwise remove all “sensitizes,” anti-PD-1-specific vulnerability, and therapeutic-development-readiness claims.
- **Journal gate if applicable:** N002; animal/translational treatment-interaction gate `FAIL`.
- **Confidence:** `1.00`
- **Required-versus-optional classification:** `REQUIRED`

## CE-05 — The reported three-year performance is internally contradictory and not interpretable from the supplied follow-up

- **Severity:** `BLOCKING`
- **Controlled axis:** `statistical-rigor`
- **Proposed issue_key:** `three_year_auc_unresolved`
- **Exact manuscript anchor:** Abstract, “AUC of 0.91 for 3-year mortality”; Results, “validation-set 3-year mortality AUC of 0.84”; Figure 3 legend, “Panel C labels the validation AUC as 0.86”; Results, “median follow-up was 18 months” and “3-year outcome status was unavailable for many surviving patients.”
- **Falsifiable concern:** Three different AUC values are assigned to what appears to be the same validation endpoint. Moreover, ordinary binary 3-year status is not observed for many survivors at the reported follow-up, and the manuscript does not specify a censoring-aware time-dependent AUC method. At least two numerical claims must be incorrect or refer to undisclosed analyses, and the endpoint may be biased or undefined under the reported method.
- **Concrete resolution test:** Reconcile the Abstract, Results, and Figure 3 against the same frozen source output; define the exact analysis population, time origin, censoring handling, estimator, uncertainty interval, and number at risk at three years; provide a reproducible censoring-aware analysis; and retain only the verified value. If reliable three-year performance cannot be estimated, remove it.
- **Journal gate if applicable:** N002, N006; technical-soundness gate `FAIL`.
- **Confidence:** `1.00`
- **Required-versus-optional classification:** `REQUIRED`

# MAJOR issues

## CE-06 — Cell-level pseudoreplication and uncorrected discovery do not support a tumour-level programme

- **Severity:** `MAJOR`
- **Controlled axis:** `data-resource-quality`
- **Proposed issue_key:** `single_cell_pseudoreplication`
- **Exact manuscript anchor:** Single-cell discovery, “eight patients,” “Cells were treated as independent observations,” “nominal P < 0.05,” and “no multiple-testing correction”; Results, “1,842 nominally significant genes”; Figure 1 legend, “Each point in the differential-expression panel represents one cell.”
- **Falsifiable concern:** The infiltration contrast is defined at the tumour/patient level, but cells are analysed as independent replicates. This inflates the apparent sample size, ignores within-patient dependence, and can generate overstated significance. Selecting 1,842 genes at nominal P < 0.05 without multiplicity control does not establish a reproducible immune-evasion programme from eight patients.
- **Concrete resolution test:** Reanalyse differential expression using patient/tumour as the biological unit or a model that explicitly handles within-patient dependence and pairing, control multiplicity, report effect sizes and uncertainty, and demonstrate robustness to patient-level resampling or leave-one-patient-out analysis. Claims should remain discovery-level unless independently validated.
- **Journal gate if applicable:** N002, N006; single-cell unit-of-inference gate `FAIL`.
- **Confidence:** `0.99`
- **Required-versus-optional classification:** `REQUIRED`

## CE-07 — Model complexity, complete-case handling, and selective reporting leave the survival association unstable

- **Severity:** `MAJOR`
- **Controlled axis:** `statistical-rigor`
- **Proposed issue_key:** `survival_model_instability`
- **Exact manuscript anchor:** Study population, “72 adults,” “Thirty-one deaths,” and “Records with missing values were excluded from each analysis”; Score construction, “Twenty-seven genes” plus “18 available clinical and molecular covariates” and stepwise selection; Statistical analysis, “proportional-hazards assumption was not examined” and “Hazard ratios and P values were reported without confidence intervals.”
- **Falsifiable concern:** Forty-five candidate features relative to 31 deaths, stepwise selection, data-dependent cutoffs, unspecified per-analysis complete-case populations, no proportional-hazards assessment, and no confidence intervals make the reported hazard ratio and score composition highly susceptible to optimism and instability. The statement that the score “remained significant” does not establish robust independent prognostic information.
- **Concrete resolution test:** Report cohort flow and missingness by variable, define the complete analysis population, use an appropriately constrained prespecified or penalized modelling strategy, quantify internal optimism with resampling that repeats the full selection pipeline, test model assumptions, and report coefficients, effect sizes, and confidence intervals. Compare incremental performance against prespecified clinical baselines.
- **Journal gate if applicable:** N002, N006; prognostic-model technical-validity gate `FAIL`.
- **Confidence:** `0.98`
- **Required-versus-optional classification:** `REQUIRED`

## CE-08 — The aetiology and setting evidence contradicts claims applying to all major HCC contexts

- **Severity:** `MAJOR`
- **Controlled axis:** `claim-moderation`
- **Proposed issue_key:** `population_scope_overgeneralized`
- **Exact manuscript anchor:** Study population, “58 patients with viral hepatitis, 9 with metabolic liver disease, and 5 with other or undocumented aetiologies”; Impact and implications, “all major HCC aetiologies”; Discussion, “application across HCC aetiologies and treatment settings” despite “most patients had viral liver disease” and “We did not use an external cohort.”
- **Falsifiable concern:** The stated sample provides sparse representation of metabolic disease and combines other with undocumented aetiology. It contains one centre and one resection setting. These data do not test performance across major aetiologies, unresectable disease, non-surgical populations, or immunotherapy settings. The limitation paragraph acknowledges the narrow evidence but then asserts the opposite conclusion.
- **Concrete resolution test:** Either provide adequately powered, independently validated performance and heterogeneity analyses across prespecified aetiologic and treatment-setting strata, or limit every population claim to the observed single-centre resection cohort and explicitly state that transportability is unestablished.
- **Journal gate if applicable:** N001, N002; generalizability gate `FAIL`.
- **Confidence:** `0.99`
- **Required-versus-optional classification:** `REQUIRED`

## CE-09 — Methods and availability statements do not permit replication of the score or key analyses

- **Severity:** `MAJOR`
- **Controlled axis:** `reproducibility`
- **Proposed issue_key:** `model_and_analysis_not_reproducible`
- **Exact manuscript anchor:** Data and code availability, “Raw single-cell data, model code, coefficient values, and the final patient-level analysis dataset are not deposited. Random seeds and software versions were not recorded”; Score construction, “locked five-gene formula” without coefficients, cutoffs, or preprocessing details.
- **Falsifiable concern:** A reader cannot calculate the purportedly deployable score, reproduce the split, rerun feature selection, assess the AUC discrepancy, or verify single-cell and survival analyses from the supplied Methods and availability statement. Calling the score “immediately deployable” is directly incompatible with withholding its coefficients and calculation rules.
- **Concrete resolution test:** Report the complete locked formula, coefficient signs and values, expression preprocessing, cutoffs, missing-data rules, software and versions, random seeds, and executable analysis workflow; provide appropriately governed patient-level or auditable derivative data and deposit raw/processed single-cell data where ethically permitted. An independent analyst should be able to regenerate the reported model outputs from the released materials.
- **Journal gate if applicable:** N006 `FAIL`; reproducibility gate `FAIL`.
- **Confidence:** `1.00`
- **Required-versus-optional classification:** `REQUIRED`

## CE-10 — The two citations cannot presently support the atomic novelty and treatment-benefit claims

- **Severity:** `MAJOR`
- **Controlled axis:** `reference-support`
- **Proposed issue_key:** `citation_semantic_support_unverified`
- **Exact manuscript anchor:** References note, “The Introduction cites reference 1 for the statement that no previous immune signature has clinical utility” and “The Discussion cites reference 2 for the claim that the five-gene score identifies patients who benefit from anti-PD-1 monotherapy”; reference 1 title, “Comprehensive and integrative genomic characterization of hepatocellular carcinoma”; reference 2 title, “Atezolizumab plus bevacizumab in unresectable hepatocellular carcinoma.”
- **Falsifiable concern:** The packet provides citation metadata but not cited full text. Exact semantic support is therefore `NOT ASSESSABLE`, not passed. In addition, the atomic claims are substantially more specific than the supplied metadata: an absence-of-prior-utility claim requires a comprehensive and current evidence basis, while a study of atezolizumab plus bevacizumab in unresectable HCC is not, from metadata alone, direct evidence that this newly derived score predicts benefit from anti-PD-1 monotherapy. The manuscript itself reports no such clinical treatment-benefit analysis.
- **Concrete resolution test:** For each atomic claim, inspect the cited full text and document the exact supporting passage, population, regimen, comparator, endpoint, and evidence type. Replace or qualify claims when support is partial, background-only, or mismatched; add appropriately scoped evidence for the novelty claim; and do not cite external treatment evidence as if it validates this score.
- **Journal gate if applicable:** N002; exact semantic-support gate `NOT ASSESSABLE`; affirmative citation-support pass withheld.
- **Confidence:** `0.97` for the support boundary and scope mismatch; exact full-text support remains `NOT ASSESSABLE`.
- **Required-versus-optional classification:** `REQUIRED`

# MINOR issues

## CE-11 — Citation placement is not auditable at the exact clause level

- **Severity:** `MINOR`
- **Controlled axis:** `reference-support`
- **Proposed issue_key:** `citation_placement_not_explicit`
- **Exact manuscript anchor:** Introduction and Discussion contain the relevant assertions without visible numbered citation markers; the post-reference note separately states which reference is intended for each claim.
- **Falsifiable concern:** A narrative note after the reference list does not show whether a citation is placed immediately after the exact clause it is intended to support. Readers cannot distinguish support for background, novelty, treatment regimen, or score-specific benefit.
- **Concrete resolution test:** Place each numbered citation immediately after the atomic clause it supports, ensure numbering follows first appearance, and verify that no citation is made to cover a stronger adjacent claim.
- **Journal gate if applicable:** Reference placement gate `FAIL` in the supplied Markdown; target-format closure otherwise `NOT ASSESSABLE` at this review phase.
- **Confidence:** `0.95`
- **Required-versus-optional classification:** `REQUIRED`

# EDITORIAL issues

No independent presentation-only issue is reported. The dominant wording problems (“establishes,” “causal driver,” “directly,” “sensitizes,” “clinically actionable,” “immediately deployable,” “universally applicable,” “all major,” and “ready for therapeutic development”) are not cosmetic; they encode the blocking scientific overclaims above. Merely polishing those sentences without resolving or lowering the claims would not close the concerns.

# Claim-ceiling risks

| Manuscript assertion | Highest ceiling supported by the stated evidence | Gate |
|---|---|---|
| “universal” and “all major HCC aetiologies” | Exploratory association in one retrospective, predominantly viral-aetiology, single-centre resection cohort | `FAIL` |
| “validated in an independent subset” | Apparent performance in reused internal data after full-cohort model construction | `FAIL` |
| “clinically actionable,” “immediately deployable,” and anti-PD-1 selection | No treatment-selection utility established; at most exploratory prognostic association | `FAIL` |
| “EVA1 excludes T cells” | Inverse tumour-level correlation in eight tumours | `FAIL` for exclusion/causality |
| “directly suppresses anti-tumour immunity” and “causal driver” | Cell-growth and molecular changes after one-guide depletion, consistent with but not establishing an immune mechanism | `FAIL` |
| “sensitizes HCC to anti-PD-1” | Smaller day-21 tumours after EVA1 depletion when all mice received anti-PD-1; treatment interaction unidentified | `FAIL` |
| “ready for therapeutic development” | Preliminary perturbation hypothesis without specificity, immune-mechanism closure, interaction, replication, toxicity, or model breadth | `FAIL` |
| “first” and “none provides” | Novelty/exhaustiveness claim requiring literature-wide support not supplied | `NOT ASSESSABLE` |
| Reference 1 and reference 2 as exact semantic support | Metadata presence only; direct semantic support not inspected | `NOT ASSESSABLE` |

# Required versus optional additional work

**Required to retain the current central claims:**

1. Truly external validation of a fully locked five-gene model at an intended-use setting, with calibration, uncertainty, clinical-baseline comparison, subgroup/transportability evaluation, and reproducible score specification.
2. Direct evidence of treatment-selection utility, including a credible treated-versus-comparator contrast and a prespecified score-by-treatment interaction.
3. A factorial EVA1-status-by-anti-PD-1 animal design that separates a general growth effect from sensitization.
4. Orthogonal, on-target EVA1 perturbation with rescue/target engagement and immune-relevant mechanistic readouts.
5. Patient-level single-cell reanalysis with multiplicity control and sensitivity to the eight biological units.
6. Reconciliation and reproducible estimation of the three-year AUC, including censoring handling and uncertainty.
7. Reproducible reporting and release of the score formula and analysis workflow.
8. Full-text, atomic claim-citation verification or removal/qualification of unsupported novelty and treatment-benefit assertions.

**Alternative required route:** If the additional evidence cannot be supplied, comprehensively narrow the paper to an exploratory, hypothesis-generating study. This requires removal of the causal, direct, universal, independent-validation, treatment-selection, clinical-actionability, immediate-deployment, sensitization, and therapeutic-readiness claims—not merely adding a generic limitations sentence.

**Optional work that would strengthen presentation but would not resolve the central defects:**

- Add a diagram that explicitly distinguishes discovery, model development, internal assessment, external validation, mechanism, and treatment interaction.
- Report a claim-to-evidence table mapping each conclusion to cohort, assay, endpoint, comparator, and validation layer.
- Improve atomic citation placement after semantic support is verified.

# Journal-fit posture

At the supplied Nature Article threshold, the claim-evidence fit is presently poor. The work may contain a potentially valuable exploratory signal, but the manuscript frames preliminary single-centre, internally reused, correlational, and under-controlled evidence as a universal clinical and causal advance. That mismatch affects technical soundness, strength of evidence, breadth, and claimed conceptual consequence rather than style alone. The current submission would require major scientific rework and/or a substantially lower claim ceiling before a defensible Nature-level assessment could be made. This is a reviewer-lens posture, not a prediction of an editorial decision or acceptance.

# NOT ASSESSABLE items

- Exact numerical agreement with source data, tables, code, or figure images, because none were supplied.
- Whether any unreported experiments, protocols, approvals, or analyses exist outside the packet.
- Exact semantic support, contradictions, corrections, retractions, or integrity status for references 1 and 2, because cited full text and external lookup were unavailable.
- Bibliographic verification beyond the metadata printed in the manuscript; DOI resolution and authoritative-index checks were not performed.
- Figure-data-text closure beyond the explicit AUC conflict stated in the manuscript and Figure 3 legend.
- Exact model coefficients, calibration, discrimination uncertainty, decision utility, subgroup performance, and external transportability because relevant outputs were not supplied.
- Mouse strain, immune competence, anti-PD-1 species reactivity, target engagement after implantation, and complete animal-protocol details because these are not reported.
- Ethics and animal-governance compliance beyond the manuscript’s generic statement; the committee, protocol numbers, consent procedure, humane endpoints, and source documents were unavailable.
- Current literature-wide novelty of EVA1 or the five-gene score; the “first” and “none” claims are therefore not verified.

# Evidence anchors

- **Prediction derivation and leakage:** Patients and methods, “Five genes were retained after stepwise selection using the entire 72-patient dataset” and the subsequent 70:30 split.
- **Clinical-utility boundary:** resection cohort endpoint of overall survival versus claims of selecting anti-PD-1 therapy.
- **Generalizability boundary:** 72 patients at one centre, including 58 with viral hepatitis, versus “universally applicable” and “all major HCC aetiologies.”
- **Single-cell inference:** eight tumours; cells treated as independent; nominal P threshold; no multiple-testing correction.
- **Causality boundary:** EVA1–T-cell score correlation in eight tumours; one-guide cell-line depletion; no rescue, target-engagement assay, or immune-cell co-culture.
- **Sensitization boundary:** five mice per group, all receiving anti-PD-1, with no treatment-interaction design.
- **Internal contradiction:** validation AUC 0.91 in Abstract, 0.84 in Results, and 0.86 in Figure 3 legend; median follow-up 18 months for a three-year endpoint.
- **Reproducibility boundary:** no deposited raw single-cell data, model code, coefficients, final patient-level dataset, seeds, or software versions.
- **Reference boundary:** two references are listed with metadata; full text is absent; the intended novelty and treatment-benefit claims exceed what can be certified from titles/metadata.

# Confidence and reasons

**Overall confidence: `0.99` for the internal claim-evidence findings.** The manuscript explicitly reports the design features that determine the principal ceilings: full-cohort selection before splitting, no external cohort, no clinical treatment contrast, one CRISPR guide without rescue, all animals receiving anti-PD-1, inconsistent AUC values, short follow-up, and absent reproducibility materials. These are direct internal anchors rather than external assumptions.

Confidence is deliberately lower for citation semantics: **`NOT ASSESSABLE` for exact full-text support**. Metadata and titles are sufficient to identify scope mismatch risks, but not to certify direct, partial, contradictory, or absent semantic support without inspecting the cited papers.
