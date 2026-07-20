# Reviewer role

`domain-science` — HCC tumour biology, immune-evasion interpretation, translational plausibility, and novelty-significance.

# Material inspected and assessment boundary

I inspected only the frozen synthetic manuscript (`manuscript.md`; SHA-256 `d51224a5ec717a268dadeee2fe9461a7b9d8c833f5b459be2d522a88d5c0006f`), `00_input_inventory.json`, the frozen Nature journal profile (SHA-256 `6f6386d213e195d6ec26d0c177568f27753208425a6a15ce139b1ac2235fd6eb`), and the shared factual intake (SHA-256 `947b2ed3c744626d5eadc56845b65f223c6b0d4336bd765e3c714acf4ff4a976`), together with the routed review instructions in the mandated Skill. This was a read-only scientific review. Figure images, tables, supplements, raw data, source code, protocols, reporting checklists, and full texts of the cited articles were unavailable. Their contents are not presumed absent from the underlying study unless the manuscript explicitly states that an analysis or control was not performed.

# Journal standard applied

Nature, Article, initial submission; broad-flagship standard. I applied the frozen profile requirements that an Article report original research of outstanding scientific importance with an interdisciplinary conclusion (N001), that review assess technical soundness, evidence strength, novelty, field importance, and general scientific interest (N002), and that Methods permit interpretation and replication (N006). The expected contribution is a major conceptual advance with causal completeness and multi-layer validation, not merely an internally generated prognostic association.

Applicable biomedical gates:

- Universal claim gate — **FAIL** for clinical actionability, universal applicability, causal immune escape, and anti-PD-1 sensitization; **PASS only for the bounded observations** that the reported score is associated with survival in the analysed cohort and EVA1 depletion is associated with reduced short-term growth in the two reported cell lines.
- Clinical/biomarker gate — **FAIL** for intended-use validation, treatment-selection evidence, external validation, and demonstrated clinical utility.
- Wet-lab mechanism gate — **FAIL** for perturbation specificity, rescue, immune-context causality, and sensitization interaction.
- Animal/translational gate — **FAIL** for the claimed anti-PD-1 sensitization design; immune competence, reagent compatibility, target engagement, toxicity, and full animal-governance details are **NOT ASSESSABLE** from the supplied packet.
- Single-cell/omics gate — **FAIL** for patient-level inference from the reported cell-level differential test and for multiple-testing control; several pipeline details remain **NOT ASSESSABLE**.

# Overall assessment

The manuscript has a coherent translational aspiration—linking a tumour-cell state, a survival signature, and a perturbable candidate—but the evidence presently supports three bounded findings rather than the claimed unified mechanism: a discovery association in eight tumours, an internally derived prognostic association in a small retrospective resection cohort, and tumour-intrinsic growth effects after a single-guide perturbation. It does not establish that EVA1 causes immune escape, that EVA1 depletion sensitizes HCC to anti-PD-1, or that the score selects immunotherapy. The treatment-selection population is also mismatched to the studied resection cohort, which is not described as receiving anti-PD-1. These gaps control the biological interpretation and prevent the claimed broad conceptual advance from meeting the Nature Article threshold.

# Major strengths

- The study asks an important HCC question by attempting to connect tumour state, immune context, prognosis, and intervention.
- Tumour and adjacent tissue were sampled, and the perturbation direction was examined in two HCC cell lines rather than one.
- The manuscript reports several design limitations explicitly, including cell-level independence, no multiple-testing correction, full-dataset model selection, absence of an external cohort, use of one guide, absence of rescue and immune-cell co-culture, and the two-arm animal design.
- The reported observations are potentially hypothesis-generating if their claims are narrowed and the underlying measurements are verified.
- Concordant changes in growth, PD-L1 abundance, and interferon-response transcripts could motivate a more discriminating mechanistic study, although they do not themselves establish immune escape.

# BLOCKING issues

## DS-B1

- **Severity:** BLOCKING
- **Controlled axis:** clinical-validity
- **Proposed issue_key:** `treatment-selection-without-treated-cohort`
- **Exact manuscript anchor:** Abstract, “a retrospective clinical cohort of 72 patients treated at one centre”; Impact and implications, “used to select anti-PD-1 therapy”; Patients and methods, “underwent resection for HCC”; Discussion, “immediate use for selecting anti-PD-1 therapy.”
- **Falsifiable concern:** Overall survival after resection in a cohort not reported to have received anti-PD-1 cannot identify response or benefit from anti-PD-1, and no treated-versus-untreated interaction is estimated. The score may be prognostic, but the reported design cannot distinguish prognosis from treatment-effect modification.
- **Concrete resolution test:** Either (a) remove every anti-PD-1 selection, predictive-biomarker, immediate-deployment, and clinical-actionability claim and define the result as internally observed prognostic association, or (b) provide an independent intended-use cohort with documented immunotherapy exposure, prespecified locked score and threshold, clinically relevant endpoints, calibration and incremental-value analyses, and a design estimating a score-by-treatment interaction against an appropriate comparator.
- **Journal gate:** N001 and N002; the clinical conclusion and interdisciplinary significance require evidence at the stated intended-use layer.
- **Confidence:** 0.99
- **Required-versus-optional classification:** Required to sustain any treatment-selection or clinically actionable claim; claim narrowing is the minimum required resolution.

## DS-B2

- **Severity:** BLOCKING
- **Controlled axis:** causal-vs-correlative
- **Proposed issue_key:** `anti-pd1-sensitization-interaction-absent`
- **Exact manuscript anchor:** Mouse experiment, “All mice received anti-PD-1”; Results, “EVA1 inhibition sensitizes HCC to anti-PD-1”; Abstract, “sensitized xenografts to anti-PD-1 treatment.”
- **Falsifiable concern:** A two-group experiment comparing control versus EVA1-depleted tumours when every animal receives anti-PD-1 cannot identify sensitization. The smaller tumours can be explained entirely by the tumour-intrinsic growth reduction already observed in vitro, without any EVA1-by-anti-PD-1 interaction.
- **Concrete resolution test:** Replace the sensitization claim with the bounded observation that EVA1-depleted tumours were smaller under the single tested anti-PD-1 condition, or perform a randomized factorial experiment containing control and EVA1-perturbed tumours with and without anti-PD-1, demonstrate a prespecified interaction with interval estimates, verify persistent EVA1 target engagement, and replicate in an immune-competent HCC-relevant model.
- **Journal gate:** N001, N002, and N006.
- **Confidence:** 1.00
- **Required-versus-optional classification:** Required; no amount of prose or within-arm significance can recover a treatment-interaction claim from the reported design.

## DS-B3

- **Severity:** BLOCKING
- **Controlled axis:** mechanism-evidence
- **Proposed issue_key:** `eva1-immune-escape-causality-unsupported`
- **Exact manuscript anchor:** Results, “We interpreted this association as evidence that EVA1 excludes T cells from HCC”; Functional experiments, “one CRISPR guide RNA,” “did not include a second guide, rescue construct, direct target-engagement assay, or immune-cell co-culture”; Results, “These findings show that EVA1 directly suppresses anti-tumour immunity”; Abstract, “the causal driver of immune escape.”
- **Falsifiable concern:** An inverse tumour-level association in eight tumours, a single-guide perturbation in tumour-only cultures, and changes in growth, PD-L1, and three transcripts do not demonstrate that EVA1 directly excludes T cells or suppresses anti-tumour immunity. Off-target effects, altered proliferation, stress responses, or indirect transcriptional effects remain viable explanations, and no immune-cell phenotype or causal ordering is measured.
- **Concrete resolution test:** Either narrow the conclusion to an association plus a tumour-intrinsic perturbation phenotype, or establish perturbation specificity with independent guides and rescue, quantify target engagement, reproduce the phenotype without conflating it with growth, and demonstrate the predicted immune-cell consequence and causal order using appropriate co-culture and in vivo immune readouts.
- **Journal gate:** N001, N002, and N006.
- **Confidence:** 0.99
- **Required-versus-optional classification:** Required to retain “causal driver,” “directly suppresses anti-tumour immunity,” or “excludes T cells.”

## DS-B4

- **Severity:** BLOCKING
- **Controlled axis:** claim-moderation
- **Proposed issue_key:** `universal-actionable-claim-exceeds-scope`
- **Exact manuscript anchor:** Title, “establishes a universal therapeutic vulnerability”; Impact and implications, “immediately deployable biomarker” and “all major HCC aetiologies”; Discussion, “universal immune-evasion mechanism,” “ready for clinical deployment,” and “Future prospective studies … are not required to establish clinical utility”; Study population, 58 viral, 9 metabolic, and 5 other or undocumented aetiologies at one centre.
- **Falsifiable concern:** A retrospective single-centre cohort enriched for viral disease, with no external cohort and no intended-use assay or immunotherapy-response cohort, cannot establish universality across aetiologies, disease stages, treatment settings, laboratories, or populations. The statement that prospective studies are unnecessary is contradicted by the study design.
- **Concrete resolution test:** Remove “universal,” “all major aetiologies,” “immediately deployable,” “ready for clinical deployment,” and the assertion that prospective studies are unnecessary; explicitly delimit the studied resection population. To restore those claims, externally validate a locked assay and score across prespecified aetiology, stage, geographic, and treatment strata in independent prospective intended-use settings, with calibration, utility, and treatment-interaction evidence.
- **Journal gate:** N001 and N002.
- **Confidence:** 1.00
- **Required-versus-optional classification:** Required; universal and deployable claims are not supportable by internal reuse or single-centre association.

## DS-B5

- **Severity:** BLOCKING
- **Controlled axis:** novelty-significance
- **Proposed issue_key:** `flagship-conceptual-advance-unestablished`
- **Exact manuscript anchor:** Introduction, “none provides a universal, mechanistically validated guide,” “the first clinically actionable HCC immune score,” and “EVA1 directly controls anti-tumour immunity”; References, two entries only, with reference 1 assigned to the no-prior-utility statement.
- **Falsifiable concern:** The claimed first-in-field and major conceptual advance rests on assertions that are not established by the manuscript’s sparse field context, while the key mechanistic and clinical components fail at their respective evidence layers. Even if the bounded associations are reproducible, they would not yet constitute a mechanistically validated universal treatment guide of outstanding cross-field importance.
- **Concrete resolution test:** Provide a systematic, current comparison against the relevant HCC immune-signature, tumour-state, EVA1-family, prognostic-biomarker, and immunotherapy-prediction literature; state precisely what is new; benchmark against prespecified clinical and molecular baselines; and supply evidence that closes the mechanism and intended-use gaps. If those tests are not met, remove priority claims and reposition the work as exploratory hypothesis generation.
- **Journal gate:** N001 and N002.
- **Confidence:** 0.96 for failure of the current manuscript to demonstrate the claimed advance; the absolute literature priority itself is NOT ASSESSABLE without source inspection.
- **Required-versus-optional classification:** Required for Nature positioning and for any “first” claim.

# MAJOR issues

## DS-M1

- **Severity:** MAJOR
- **Controlled axis:** experimental-design
- **Proposed issue_key:** `immune-infiltration-phenotype-underdefined`
- **Exact manuscript anchor:** Single-cell discovery, “Differential expression between high- and low-infiltration tumours”; Results, “correlated inversely with a T-cell score”; Figure 2 legend, “Association between EVA1 expression and the T-cell score in eight tumours.”
- **Falsifiable concern:** The biological phenotype driving discovery is not operationally defined: the immune-cell classes, score genes, threshold, measurement layer, tumour-level aggregation, and handling of aetiology or tumour composition are unspecified. Without these, “immune-evasion programme” may reflect a data-derived dichotomy, tumour purity, or cohort composition rather than tumour-mediated T-cell exclusion.
- **Concrete resolution test:** Define and justify the infiltration measure and cutoff, report tumour-level values for all eight tumours, show sensitivity to alternative definitions and relevant covariates, and demonstrate that EVA1’s association is not explained by tumour purity, aetiology, sampling composition, or one influential tumour.
- **Journal gate:** N002 and N006.
- **Confidence:** 0.96
- **Required-versus-optional classification:** Required for interpreting the discovery phenotype as immune evasion.

## DS-M2

- **Severity:** MAJOR
- **Controlled axis:** statistical-rigor
- **Proposed issue_key:** `cell-level-pseudoreplication-inflates-program`
- **Exact manuscript anchor:** Single-cell discovery, “eight patients,” “Cells were treated as independent observations,” and “no multiple-testing correction”; Results, “1,842 nominally significant genes.”
- **Falsifiable concern:** Treating 46,218 cells as independent when the biological comparison comprises eight tumours inflates precision and does not support population-level inference; retaining nominally significant genes without multiplicity control makes the asserted immune-evasion programme unstable.
- **Concrete resolution test:** Reanalyse at the patient/sample level or with a model that accounts for within-patient dependence, paired tumour/adjacent structure, and relevant covariates; control false discovery; report effect sizes and uncertainty; and show that EVA1 and the score-building candidates survive patient-level sensitivity and leave-one-patient-out analyses.
- **Journal gate:** N002 and N006.
- **Confidence:** 1.00
- **Required-versus-optional classification:** Required for the biological programme and its downstream gene nomination.

## DS-M3

- **Severity:** MAJOR
- **Controlled axis:** mechanism-evidence
- **Proposed issue_key:** `score-to-eva1-mechanistic-bridge-missing`
- **Exact manuscript anchor:** Abstract, “five-gene immune-evasion score”; Functional experiments, “EVA1 was depleted”; Discussion, “EVA1 as the causal link between the five-gene score and immune escape”; Data and code availability, “coefficient values … are not deposited.”
- **Falsifiable concern:** Perturbing only the “highest-ranked” gene does not establish that EVA1 causally explains a multigene score, that the other four genes participate in one pathway, or that the clinical association is mediated by EVA1. The manuscript does not expose the score formula or evidence connecting score values to EVA1-dependent biology.
- **Concrete resolution test:** Report exact gene identities, coefficients, signs, cutoffs, and score distributions; show the relationship among the five genes and EVA1; test whether EVA1 perturbation changes the defined programme; and use a prespecified mediation or mechanistic framework with orthogonal validation. Otherwise remove the claim that EVA1 is the causal link for the score.
- **Journal gate:** N002 and N006.
- **Confidence:** 0.97
- **Required-versus-optional classification:** Required for the unified score-to-mechanism narrative; optional if the score and EVA1 are reframed as separate exploratory observations.

## DS-M4

- **Severity:** MAJOR
- **Controlled axis:** clinical-validity
- **Proposed issue_key:** `prognostic-population-and-endpoint-mismatch`
- **Exact manuscript anchor:** Study population, resection from 2018–2022 with median surviving follow-up of 18 months; Results, “3-year mortality AUC”; Impact and implications, “measured at diagnosis”; Discussion, application across “treatment settings.”
- **Falsifiable concern:** A postsurgical survival association in a resected cohort does not establish performance at diagnosis across HCC stages or treatment settings. With many survivors lacking three-year status, the biological and clinical meaning of the reported three-year mortality discrimination is unclear.
- **Concrete resolution test:** Define the exact prediction time origin, censoring method, eligibility, stage distribution, recurrence/treatment pathways, and intended-use population; report time-dependent performance with uncertainty and adequate follow-up; and restrict claims to the observed setting unless externally validated elsewhere.
- **Journal gate:** N002 and N006.
- **Confidence:** 0.98
- **Required-versus-optional classification:** Required for any prognostic interpretation beyond the analysed resection cohort.

## DS-M5

- **Severity:** MAJOR
- **Controlled axis:** data-resource-quality
- **Proposed issue_key:** `eva1-target-and-assay-identity-ambiguous`
- **Exact manuscript anchor:** Throughout, the target is named only “EVA1”; Functional experiments, “one CRISPR guide RNA”; Data and code availability, only processed summaries are available on request.
- **Falsifiable concern:** Without an unambiguous approved gene symbol/transcript, guide sequence, assay identifiers, antibody details, and target-engagement result, the molecular target and the reported PD-L1/interferon effects cannot be independently interpreted or replicated.
- **Concrete resolution test:** Provide the exact gene and transcript identifiers, guide sequence and genomic target, editing or depletion quantification, assay and antibody identifiers, normalization procedures, and replicate-level results; reconcile the chosen nomenclature throughout.
- **Journal gate:** N006.
- **Confidence:** 0.93
- **Required-versus-optional classification:** Required for mechanistic interpretation and replication.

## DS-M6

- **Severity:** MAJOR
- **Controlled axis:** reference-support
- **Proposed issue_key:** `anti-pd1-literature-support-mismatch`
- **Exact manuscript anchor:** References note, “The Discussion cites reference 2 for the claim that the five-gene score identifies patients who benefit from anti-PD-1 monotherapy”; reference 2 is titled “Atezolizumab plus bevacizumab in unresectable hepatocellular carcinoma.”
- **Falsifiable concern:** The cited study, as identified in the manuscript, concerns an anti-PD-L1 plus anti-VEGF combination, not this five-gene score and not anti-PD-1 monotherapy. It therefore cannot directly establish that the score identifies anti-PD-1 benefit.
- **Concrete resolution test:** Remove the treatment-benefit claim or replace it only with direct evidence that evaluates the locked score as a treatment-effect modifier for the specified anti-PD-1 regimen and intended-use population; separately cite combination-therapy context without conflating PD-1 and PD-L1 regimens.
- **Journal gate:** N002.
- **Confidence:** 0.98 based on the manuscript-supplied title and assigned claim; full-text semantic verification remains NOT ASSESSABLE.
- **Required-versus-optional classification:** Required.

# MINOR issues

## DS-m1

- **Severity:** MINOR
- **Controlled axis:** writing-clarity
- **Proposed issue_key:** `pd-l1-interferon-direction-overinterpreted`
- **Exact manuscript anchor:** Results, “PD-L1 abundance also decreased, while three interferon-response transcripts increased. These findings show that EVA1 directly suppresses anti-tumour immunity.”
- **Falsifiable concern:** The two readout directions do not by themselves define a coherent immune-escape mechanism, because interferon programmes and PD-L1 regulation are context- and time-dependent and were measured in tumour-only cultures.
- **Concrete resolution test:** Name the three transcripts, provide time course and effect sizes, explain a testable pathway model, and revise the sentence to describe the measured molecular changes unless functional immune consequences are demonstrated.
- **Journal gate:** N002 and N006.
- **Confidence:** 0.94
- **Required-versus-optional classification:** Required claim correction; expanded pathway experiments are optional if the direct-immunity claim is removed.

## DS-m2

- **Severity:** MINOR
- **Controlled axis:** claim-moderation
- **Proposed issue_key:** `growth-phenotype-not-therapeutic-dependency`
- **Exact manuscript anchor:** Introduction, “identify a therapeutic dependency”; Results, 24% and 19% lower growth at 72 hours; Results, “ready for therapeutic development.”
- **Falsifiable concern:** Short-term reduced cell growth after genetic depletion does not establish a selective therapeutic dependency, druggability, therapeutic window, or tolerability.
- **Concrete resolution test:** Replace “therapeutic dependency” and “ready for therapeutic development” with a bounded perturbation phenotype, or demonstrate pharmacologically tractable target engagement, selectivity against relevant non-malignant cells, dose-response, durability, and in vivo exposure/toxicity.
- **Journal gate:** N002.
- **Confidence:** 0.98
- **Required-versus-optional classification:** Required terminology correction; translational pharmacology is optional unless development-readiness is claimed.

# EDITORIAL issues

## DS-E1

- **Severity:** EDITORIAL
- **Controlled axis:** writing-clarity
- **Proposed issue_key:** `prognostic-predictive-terminology`
- **Exact manuscript anchor:** Abstract, “predicts three-year mortality”; Impact and implications, “used to select anti-PD-1 therapy”; Discussion, “identifies patients who benefit.”
- **Falsifiable concern:** The manuscript uses “predicts” for both prognosis and treatment benefit, obscuring the distinction between a prognostic association and a predictive treatment-effect modifier.
- **Concrete resolution test:** Reserve “prognostic” for outcome association independent of treatment and “predictive” for a demonstrated treatment interaction; define the intended use consistently in the title, summary, Results, and Discussion.
- **Journal gate:** N002.
- **Confidence:** 1.00
- **Required-versus-optional classification:** Required for accurate interpretation.

## DS-E2

- **Severity:** EDITORIAL
- **Controlled axis:** writing-clarity
- **Proposed issue_key:** `evidence-layer-labeling`
- **Exact manuscript anchor:** Discussion, “concordance across data types demonstrates the generality of the mechanism.”
- **Falsifiable concern:** “Concordance” merges tumour-level association, cell-autonomous perturbation, and an under-specified xenograft comparison as if they were independent demonstrations of one mechanism.
- **Concrete resolution test:** Label each evidence layer separately—human observational association, tumour-cell perturbation phenotype, and in vivo growth comparison—and state which mechanistic links remain untested.
- **Journal gate:** N002.
- **Confidence:** 0.98
- **Required-versus-optional classification:** Required presentation correction.

# Claim-ceiling risks

- **Score:** At most, the supplied text supports an internally derived association with overall survival in this retrospective single-centre resection cohort. It does not support external validity, universal applicability, clinical actionability, or anti-PD-1 selection.
- **Single-cell result:** At most, EVA1 expression is reported to associate inversely with a T-cell score across eight tumours. The reported cell-level analysis does not establish a patient-level immune-evasion programme or T-cell exclusion.
- **Cell-line perturbation:** At most, one guide targeting the stated EVA1 target is associated with reduced 72-hour growth and altered selected molecular readouts in Huh7 and Hep3B. It does not establish specificity, direct immune regulation, or a therapeutic window.
- **Mouse result:** At most, xenografts from EVA1-depleted cells were reported smaller at day 21 under a condition in which all mice received anti-PD-1. It does not establish sensitization, immune mediation, survival benefit, or clinical efficacy.
- **Novelty:** “First,” “universal,” and “major conceptual advance” remain unsupported until a comprehensive current literature comparison and the missing causal and intended-use evidence are supplied.

# Required versus optional additional work

**Required to retain the manuscript’s present central claims:**

1. An independent intended-use validation cohort with a locked assay/score and a design capable of estimating anti-PD-1 treatment interaction.
2. A factorial anti-PD-1 experiment with appropriate untreated controls, randomization, blinding, target engagement, immune readouts, and replication in an immune-competent HCC-relevant system.
3. Orthogonal EVA1 perturbations, rescue, explicit target engagement, and functional immune assays that separate immune effects from growth effects.
4. Patient-level single-cell inference with multiplicity control and robustness to tumour composition, aetiology, and influential samples.
5. Complete definition of the five-gene score, EVA1 target, discovery phenotype, intended use, and relevant clinical/molecular baselines.
6. Claim narrowing wherever the above evidence is not supplied.

**Optional if claims are narrowed to exploratory associations:**

- Additional mechanistic mapping of the interferon/PD-L1 pathway.
- Pharmacologic EVA1 inhibitor development and formal toxicity/exposure studies.
- Broader multi-region or longitudinal sampling to explore intratumour evolution.
- Additional visual explanatory material, provided it does not substitute for the missing evidence.

# Journal-fit posture

**FAIL for the Nature Article standard as submitted.** The clinically actionable, universal, causal, and sensitization claims are not supported by designs that identify those effects, and the manuscript therefore does not currently demonstrate an outstanding, broadly relevant conceptual advance. A defensible Nature posture would require substantial new independent clinical and mechanistic evidence, not solely textual revision. This is a reviewer assessment, not a prediction of the editorial decision.

# NOT ASSESSABLE items

- Accuracy and completeness of all figure panels, numerical values, representative images, error bars, and figure-to-text consistency beyond the supplied legends.
- Mouse strain and immune competence, anti-PD-1 antibody identity/species reactivity, dosing, pharmacokinetics, target engagement, and toxicity.
- Biological-replicate counts, quantitative distributions, and exclusion handling for the cell-line assays.
- Exact five-gene identities, coefficient values, source measurements, and patient-level performance.
- Single-cell raw-data quality, batch structure, doublet/ambient correction, copy-number inference reliability, annotation uncertainty, and processed-to-raw traceability.
- Full novelty against the current HCC immune-signature and EVA1 literature; full-text support of references 1 and 2.
- Ethics approval, consent, animal protocol, humane endpoints, and reporting compliance beyond the manuscript’s generic statement.
- Any absent supplementary protocols, analyses, or controls not explicitly stated as unperformed in the manuscript.

# Evidence anchors

- Abstract: “AUC of 0.91,” “sensitized xenografts,” “causal driver,” “clinically actionable, universally applicable.”
- Impact and implications: “used to select anti-PD-1 therapy,” “immediately deployable,” “all major HCC aetiologies.”
- Study population: 72 single-centre resected patients; 58 viral, 9 metabolic, 5 other/undocumented; 31 deaths; 18-month median follow-up among survivors.
- Single-cell discovery: eight patients; cells treated as independent; nominal P threshold without multiplicity correction.
- Score construction and validation: full-cohort selection and rule choice; subsequent 70:30 split; no external cohort, calibration, decision curve, or clinical baseline.
- Functional experiments: one guide; no second guide, rescue, direct target engagement, or immune-cell co-culture.
- Mouse experiment: five animals per group; all received anti-PD-1; cage-order allocation; unblinded measurement; no independent replicate.
- Results: T-cell association in eight tumours; inconsistent AUC values of 0.84, 0.86, and 0.91; growth effects of 24% and 19%; day-21 tumour-volume P = 0.048.
- Discussion: “prospective studies … are not required to establish clinical utility.”
- Data and code availability: no deposited raw single-cell data, model code, coefficient values, final patient-level dataset, seeds, or software versions.
- Figure legends: figures 1–4 supplied as text only; figure images unavailable.
- References note: reference 1 assigned to an absence-of-prior-utility claim; reference 2 assigned to anti-PD-1 monotherapy benefit despite the cited title describing atezolizumab plus bevacizumab.

# Confidence and reasons

Overall confidence: **0.98**. The principal conclusions follow directly from explicit design statements in the manuscript: a retrospective single-centre resection cohort, internal data reuse, no external validation, one-guide tumour-only perturbation, and a mouse experiment in which all animals received anti-PD-1. These facts make the claim ceilings highly determinate. Confidence is lower for absolute novelty, detailed assay quality, numerical reconciliation, mouse immune context, and citation semantics because the literature, figure images, raw data, code, and full protocols were not supplied; those items are retained as **NOT ASSESSABLE** rather than inferred.
