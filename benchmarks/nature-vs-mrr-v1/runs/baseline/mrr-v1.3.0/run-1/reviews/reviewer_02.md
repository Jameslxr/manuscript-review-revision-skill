# Reviewer role

Independent reviewer 02; role_id: `domain-science`. I assessed HCC biology, tumour immunology, biological interpretation, field-level novelty and significance, and generalizability across HCC aetiologies. I comment on statistical or design defects only where they directly determine whether the biological and clinical claims are interpretable.

# Material inspected and assessment boundary

I inspected only:

- `manuscript.md` (SHA-256 `d51224a5ec717a268dadeee2fe9461a7b9d8c833f5b459be2d522a88d5c0006f`);
- `00_input_inventory.json`;
- `nature-journal-profile.json` (SHA-256 `6f6386d213e195d6ec26d0c177568f27753208425a6a15ce139b1ac2235fd6eb`);
- `02_shared_fact_base.md` (SHA-256 `947b2ed3c744626d5eadc56845b65f223c6b0d4336bd765e3c714acf4ff4a976`).

The manuscript is synthetic. Figure images, tables, supplementary information, raw data, source code, protocols, reporting checklists, and a cover letter were not supplied. I therefore do not infer that an unreported item is absent unless the manuscript explicitly says it was not performed. Numerical reconstruction, image-level assessment, and full-text citation verification are outside the supplied-material boundary.

# Journal standard applied

I applied the frozen Nature Article profile for initial submission. The decisive scientific standard is original research of outstanding scientific importance with a conclusion of interest to an interdisciplinary readership (N001), assessed for technical soundness, evidential strength, novelty, field importance, and general interest (N002). Methods must permit interpretation and replication (N006). For this broad-flagship setting, a universal HCC immune mechanism, a treatment-selection biomarker, and a therapeutic vulnerability require unusually strong causal completeness, independent multi-layer validation, accessibility across disease contexts, and reproducibility. An observational retrospective cohort, tumour-cell cultures, and a small xenograft study cannot alone establish universal clinical actionability or human treatment benefit.

# Overall assessment

The manuscript links a small single-cell discovery set to survival modelling and perturbation experiments, an appealing cross-scale concept. However, the evidence does not establish that EVA1 causes immune escape, that its depletion sensitizes tumours to anti-PD-1, that the five-gene score predicts immunotherapy benefit, or that either result generalizes across HCC aetiologies. The central treatment interaction is not experimentally tested because every mouse received anti-PD-1, and the clinical cohort is a resection-survival cohort rather than an immunotherapy-response cohort. The work is therefore hypothesis-generating, not a universal mechanism or deployable biomarker.

Critical gates:

- Outstanding scientific importance / major conceptual advance: **FAIL** for the claims as written; the proposed advance rests on unresolved causal and validation defects.
- EVA1-specific causal immune-evasion mechanism: **FAIL**.
- Anti-PD-1 sensitization: **FAIL**.
- Anti-PD-1 treatment-selection biomarker: **FAIL**.
- Generalizability across major HCC aetiologies and treatment settings: **FAIL**.
- Independent clinical validation: **FAIL**.
- Exact field-level priority or “first” status: **NOT ASSESSABLE** from two references without a systematic current literature comparison.
- Reproducibility of the biological and modelling results: **FAIL** on the reported data/code and method detail.
- Image-level support for the stated phenotypes: **NOT ASSESSABLE** because figure images were not supplied.

# Major strengths

- The study attempts to connect patient-resolved single-cell observations, clinical outcome, tumour-cell perturbation, and an in-vivo experiment rather than presenting a signature alone.
- Tumour and adjacent tissue were profiled, and tumour-cell calling used both epithelial markers and inferred copy-number patterns, a potentially appropriate starting framework if patient-level validation is shown.
- EVA1 depletion was tested in two HCC cell lines, and the manuscript reports more than one molecular readout (PD-L1 and interferon-response transcripts).
- The manuscript openly reports several important limitations, including the single-centre retrospective cohort, aetiologic imbalance, lack of an external cohort, one-guide perturbation, lack of rescue, and the small non-blinded mouse experiment.

# BLOCKING issues

## DS-B01 — Anti-PD-1 sensitization is not tested

- **issue_key:** `DS-B01_anti-PD1_interaction_absent`
- **axis:** `experimental-design`
- **severity:** `BLOCKING`
- **anchor:** Methods, “Mouse experiment”: “All mice received anti-PD-1.” Results, “EVA1 perturbation supports a therapeutic mechanism”: “We conclude that EVA1 inhibition sensitizes HCC to anti-PD-1”.
- **falsifiable concern:** A comparison of control versus EVA1-depleted tumours when both groups receive anti-PD-1 estimates the effect of EVA1 depletion under one treatment condition. It cannot distinguish intrinsic growth inhibition from an EVA1-by-anti-PD-1 interaction. The reported 19–24% reduction in 72-hour cell growth provides a direct non-immune alternative explanation for smaller xenografts.
- **concrete resolution test:** In an immunologically appropriate HCC model, perform a randomized, blinded factorial experiment containing control/vehicle, control/anti-PD-1, EVA1 perturbation/vehicle, and EVA1 perturbation/anti-PD-1 arms, with prospectively justified sample size, longitudinal tumour kinetics, survival, and a pre-specified interaction test. Demonstrate a reproducible positive interaction beyond the tumour-intrinsic growth effect in an independent model.
- **journal gate:** **FAIL** — N001/N002; the central therapeutic conclusion is not identified by the experiment.
- **confidence:** `0.99`

## DS-B02 — The in-vivo system does not yet support an immune mechanism

- **issue_key:** `DS-B02_xenograft_immune_context_unresolved`
- **axis:** `mechanism-evidence`
- **severity:** `BLOCKING`
- **anchor:** Methods, “Mouse experiment”: “Ten mice bearing subcutaneous Huh7 xenografts”; Results, “EVA1 perturbation supports a therapeutic mechanism”: “The experiment did not measure immune infiltration” and “all mice received anti-PD-1”.
- **falsifiable concern:** Huh7 is a human HCC line, but mouse strain, immune reconstitution, anti-PD-1 reagent/target species, and host immune competence are not reported. Without this information and without tumour immune profiling, a subcutaneous xenograft volume difference cannot be attributed to restored anti-tumour immunity. If the host lacks the relevant functional T-cell/PD-1 axis, the proposed mechanism is biologically untenable in that experiment.
- **concrete resolution test:** Report and verify the host and reagent biology, then reproduce the effect in a model with an intact, targetable PD-1 axis (for example, a justified immunocompetent syngeneic model or rigorously characterized humanized model). Show target engagement and concordant changes in tumour-infiltrating CD8 T cells, activation/exhaustion states, effector function, and tumour-cell antigen-presentation/PD-L1 biology, with appropriate isotype and treatment controls.
- **journal gate:** **FAIL** — N002/N006; the model’s capacity to test the claimed immune mechanism is presently unresolved.
- **confidence:** `0.98`

## DS-B03 — EVA1-specific causality is not established

- **issue_key:** `DS-B03_EVA1_causality_not_established`
- **axis:** `causal-vs-correlative`
- **severity:** `BLOCKING`
- **anchor:** Methods, “Functional experiments”: “one CRISPR guide RNA” and “did not include a second guide, rescue construct, direct target-engagement assay, or immune-cell co-culture”; Results: “These findings show that EVA1 directly suppresses anti-tumour immunity.”
- **falsifiable concern:** A single guide can produce guide-specific or editing-associated effects, while reduced proliferation can secondarily alter PD-L1 and stress/interferon transcripts. The experiments neither establish on-target dependence nor show a functional effect on immune cells. The inverse patient association (“EVA1 was higher in low-infiltration tumours”) is also correlative and does not establish T-cell exclusion.
- **concrete resolution test:** Reproduce the phenotype with at least two independent guides and an orthogonal perturbation; quantify EVA1 editing/protein loss; rescue with guide-resistant EVA1; and test whether perturbation changes T-cell recruitment, activation, killing, or exhaustion in immune-cell co-culture. Define and perturb the intervening pathway, and demonstrate that rescue or pathway epistasis restores both the molecular and immune phenotypes.
- **journal gate:** **FAIL** — N001/N002; a causal mechanism is the principal conceptual claim but is not demonstrated.
- **confidence:** `0.99`

## DS-B04 — The clinical data cannot support immunotherapy selection or universal use

- **issue_key:** `DS-B04_clinical_actionability_universal_claim`
- **axis:** `clinical-validity`
- **severity:** `BLOCKING`
- **anchor:** “Impact and implications”: “used to select anti-PD-1 therapy”, “immediately deployable biomarker”, and “all major HCC aetiologies”; Methods, “Study population”: “72 adults who underwent resection”, including “58 patients with viral hepatitis, 9 with metabolic liver disease, and 5 with other or undocumented aetiologies”; Methods, “Score construction and validation”: “No external cohort, independent laboratory assay, calibration analysis, or decision-curve analysis was used.”
- **falsifiable concern:** Overall survival after resection is not evidence that a biomarker predicts benefit from anti-PD-1. No treated-versus-control clinical interaction is reported. The cohort is overwhelmingly viral, small in non-viral strata, single-centre, and restricted to resectable disease; it cannot establish validity in metabolic, alcohol-associated, or other HCC contexts, nor in advanced disease where checkpoint therapy is used. Analytical deployability is also untested.
- **concrete resolution test:** Validate a fully locked assay and model in independent, multi-centre cohorts spanning major aetiologies, liver-function states, disease stages, and demographic contexts. For treatment selection, use a cohort with anti-PD-1 exposure and an appropriate comparator and pre-specify a treatment-by-score interaction; ideally confirm prospectively. Demonstrate calibration, added value over BCLC/AFP/liver-function and treatment-standard baselines, clinical utility, assay robustness, and aetiology-specific performance with uncertainty.
- **journal gate:** **FAIL** — N001/N002; neither human treatment benefit nor universal applicability is tested.
- **confidence:** `0.99`

# MAJOR issues

## DS-M01 — Patient-level biology is replaced by cell-level replication

- **issue_key:** `DS-M01_single_cell_pseudoreplication`
- **axis:** `statistical-rigor`
- **severity:** `MAJOR`
- **anchor:** Methods, “Single-cell discovery”: “eight patients” and “Cells were treated as independent observations”; Results: “1,842 nominally significant genes” with “no multiple-testing correction”.
- **falsifiable concern:** The biological unit for high- versus low-infiltration tumour comparisons is the patient, not each cell. Treating 46,218 cells as independent inflates effective sample size and can make patient-specific, aetiology-specific, or compositional differences appear to be a conserved tumour programme. With eight tumours and 1,842 nominal hits, EVA1 nomination may be unstable.
- **concrete resolution test:** Reanalyse with patient-aware pseudobulk or a mixed model, predefine infiltration phenotype and cell-state covariates, control false discovery rate, and show leave-one-patient-out stability. Replicate EVA1 direction and the five-gene programme in an independent HCC single-cell cohort with patient-level effect estimates.
- **journal gate:** **FAIL** — N002; the discovery evidence does not presently establish a reproducible HCC programme.
- **confidence:** `0.99`

## DS-M02 — The apparent validation is not independent

- **issue_key:** `DS-M02_validation_leakage`
- **axis:** `experimental-design`
- **severity:** `MAJOR`
- **anchor:** Methods, “Score construction and validation”: “Five genes were retained after stepwise selection using the entire 72-patient dataset” and “Expression cutoffs, coefficient signs, and missing-value rules were also chosen using the full dataset”; Discussion: “validated in an independent subset”.
- **falsifiable concern:** Feature selection, coefficients, cutoffs, and missing-data rules were informed by every patient before the 70:30 split. The held-out subset is therefore not independent, and a 27-gene plus 18-covariate search with 31 deaths is highly vulnerable to optimistic and unstable performance. This undermines the biological assertion that the score captures a conserved immune-evasion state.
- **concrete resolution test:** Freeze the complete assay, preprocessing, coefficients, cutoff, and missing-data policy without using evaluation cases, then test once in an external cohort. Alternatively, report properly nested resampling for internal optimism correction and reserve independent external data for confirmation; benchmark against accepted HCC prognostic variables.
- **journal gate:** **FAIL** — N002; the evidence does not meet the stated independent-validation claim.
- **confidence:** `0.99`

## DS-M03 — Alternative biological explanations are not separated from immune escape

- **issue_key:** `DS-M03_growth_state_confounding`
- **axis:** `mechanism-evidence`
- **severity:** `MAJOR`
- **anchor:** Results, “EVA1 perturbation supports a therapeutic mechanism”: “reduced 72-hour cell growth by 24% in Huh7 cells and 19% in Hep3B cells. PD-L1 abundance also decreased, while three interferon-response transcripts increased.”
- **falsifiable concern:** A generic change in proliferation, viability, stress, or cell-state composition could produce the molecular readouts and the xenograft phenotype without immune-evasion control. Decreased PD-L1 together with increased interferon-response transcripts is not itself a coherent causal pathway, and no receptor signalling, antigen presentation, secreted chemokine, or immune-cell function is measured.
- **concrete resolution test:** Match viable cell number and cell-cycle state, quantify apoptosis and stress, perform time-resolved pathway measurements, and show that the immune phenotype persists independently of growth suppression. Identify the molecular link from EVA1 to PD-L1/interferon signalling and demonstrate functional consequences in immune cells with rescue/epistasis.
- **journal gate:** **FAIL** — N001/N002; the proposed mechanistic interpretation is not distinguished from a tumour-intrinsic fitness effect.
- **confidence:** `0.97`

## DS-M04 — HCC heterogeneity and disease context are insufficiently represented

- **issue_key:** `DS-M04_HCC_context_generalizability`
- **axis:** `data-resource-quality`
- **severity:** `MAJOR`
- **anchor:** Introduction: “HCC arises in diverse liver-disease settings”; Methods, “Study population”: “58 patients with viral hepatitis, 9 with metabolic liver disease, and 5 with other or undocumented aetiologies”; Discussion: “application across HCC aetiologies and treatment settings.”
- **falsifiable concern:** The single-cell subset’s aetiologies, cirrhosis status, tumour stage, prior treatment, and sampling distribution are not reported. Two cell lines and one subcutaneous Huh7 model do not capture the immune and metabolic contexts created by viral hepatitis, steatohepatitis, alcohol-associated liver disease, cirrhosis, or an orthotopic liver microenvironment. The claimed generality could therefore be driven by the dominant viral/resectable subgroup.
- **concrete resolution test:** Report the eight donors’ relevant disease contexts and perform patient-level stratified/sensitivity analyses with interaction estimates. Replicate the programme across independent aetiology-balanced tissue cohorts and mechanistic models that include at least viral and metabolic liver-disease contexts, preferably in the orthotopic liver microenvironment.
- **journal gate:** **FAIL** — N001/N002; a universal HCC conclusion is not supported across the biological settings invoked.
- **confidence:** `0.98`

## DS-M05 — Tumour-cell identity and infiltration phenotype require validation

- **issue_key:** `DS-M05_cell_identity_infiltration_definition`
- **axis:** `data-resource-quality`
- **severity:** `MAJOR`
- **anchor:** Methods, “Single-cell discovery”: “Tumour cells were identified using epithelial markers and inferred copy-number patterns” and “Differential expression between high- and low-infiltration tumours”; Results: “EVA1 excludes T cells from HCC.”
- **falsifiable concern:** The manuscript does not define the infiltration threshold, establish that the comparison is robust to tumour purity and cell recovery, or report patient-level validation of malignant-cell calls. Ambient RNA, epithelial non-malignant cells, clone composition, and sampling region could alter EVA1 expression and apparent T-cell abundance. Correlation across eight tumours does not distinguish exclusion from low recruitment, sampling, or loss of T cells.
- **concrete resolution test:** Provide the pre-specified infiltration definition, donor-level cell counts, malignant-cell calling diagnostics, sensitivity to CNV-calling and tumour purity, and patient-level association plots. Confirm spatially that EVA1-high malignant cells are associated with reduced T-cell proximity/penetration, then perturb EVA1 and demonstrate a change in recruitment or penetration rather than only abundance.
- **journal gate:** **FAIL** — N002/N006; the foundational cell-state-to-immune-architecture link is not adequately established.
- **confidence:** `0.95`

# MINOR issues

## DS-m01 — The relationship between EVA1 and the five-gene score is underdefined

- **issue_key:** `DS-m01_signature_mechanism_bridge`
- **axis:** `writing-clarity`
- **severity:** `MINOR`
- **anchor:** Discussion: “The molecular and animal results identify EVA1 as the causal link between the five-gene score and immune escape.”
- **falsifiable concern:** The manuscript does not show whether EVA1 is necessary for the score’s prognostic association, whether the other four genes mark the same pathway, or whether the score is tumour-cell-specific in bulk clinical samples.
- **concrete resolution test:** Name all five genes and coefficients, show their cell-type localization and covariance, test score performance with and without EVA1, and provide pathway or perturbational evidence linking the five components.
- **journal gate:** **FAIL** — N002/N006 for the claimed mechanistic bridge.
- **confidence:** `0.94`

## DS-m02 — HCC clinical context is not adequately benchmarked

- **issue_key:** `DS-m02_HCC_baseline_comparison`
- **axis:** `clinical-validity`
- **severity:** `MINOR`
- **anchor:** Methods, “Score construction and validation”: “BCLC stage and other clinical baselines were not evaluated.”
- **falsifiable concern:** A survival score can appear informative while adding little beyond tumour burden, vascular invasion, AFP, liver function, recurrence treatment, or established staging. Without these comparisons, its disease-specific value is unclear.
- **concrete resolution test:** Compare the locked score with pre-specified HCC baselines, quantify incremental discrimination and calibration, and report whether associations persist after clinically justified adjustment without data-driven selection.
- **journal gate:** **FAIL** — N002 for clinical importance as presently claimed.
- **confidence:** `0.97`

# EDITORIAL issues

## DS-E01 — Mechanistic and clinical verbs should be aligned with the evidence

- **issue_key:** `DS-E01_overstated_verbs`
- **axis:** `claim-moderation`
- **severity:** `EDITORIAL`
- **anchor:** Title: “establishes a universal therapeutic vulnerability”; Abstract: “causal driver”, “clinically actionable”, and “universally applicable”; Introduction: “first clinically actionable”; Discussion: “ready for clinical deployment”.
- **falsifiable concern:** Readers will interpret these formulations as demonstrated causal immunity, treatment interaction, validated clinical utility, universality, and established priority, none of which is shown by the reported experiments.
- **concrete resolution test:** Until the required evidence exists, revise the title and text to “candidate”, “associated with”, “hypothesis-generating”, and “requires external and treatment-specific validation”; remove “first”, “universal”, “causal”, “actionable”, “immediately deployable”, and “ready” unless each is directly substantiated.
- **journal gate:** **FAIL** — N002; the current language exceeds the evidence.
- **confidence:** `0.99`

# Claim-ceiling risks

- “EVA1 excludes T cells from HCC” is bounded by an inverse association across eight tumours; the defensible ceiling is that EVA1 expression is associated with a lower T-cell score in this discovery set.
- “EVA1 directly suppresses anti-tumour immunity” is bounded by one-guide tumour-cell perturbation without immune cells; the defensible ceiling is that EVA1 depletion is associated with altered tumour-cell growth, PD-L1 abundance, and three interferon-response transcripts.
- “sensitizes HCC to anti-PD-1” is not estimable because there is no anti-PD-1-negative arm; the defensible ceiling is that EVA1-depleted xenografts were smaller than control xenografts when both groups received anti-PD-1.
- “predicts” three-year mortality is constrained by data reuse, limited follow-up, and inconsistent AUCs; the defensible ceiling is an internally derived prognostic association requiring corrected internal and external validation.
- “used to select anti-PD-1 therapy” has no treated-versus-comparator human evidence; it must not be stated.
- “universal” and “all major HCC aetiologies” exceed the viral-dominant, resected, single-centre cohort and incompletely described eight-patient discovery set.
- “first” is **NOT ASSESSABLE** without a systematic, current field comparison; the supplied references cannot establish priority.

# Required versus optional additional work

Required to retain the current causal, therapeutic, clinical-actionability, and universal claims:

1. Establish EVA1-specific causality using multiple independent perturbations, quantitative target engagement, rescue, pathway epistasis, and immune-cell functional assays.
2. Use an immunologically valid in-vivo HCC system and a randomized factorial EVA1-by-anti-PD-1 design, with immune profiling, longitudinal outcomes, toxicity, blinding, sample-size justification, and independent replication.
3. Redo single-cell inference with patient as the biological unit, false-discovery control, robust malignant-cell annotation, spatial or orthogonal validation of T-cell exclusion, and independent-cohort replication.
4. Freeze and externally validate the complete five-gene assay/model without information leakage, including calibration, uncertainty, missing-data rules, and comparison with HCC clinical standards.
5. For treatment selection, demonstrate a score-by-treatment interaction in appropriate human data and confirm clinically meaningful utility; prognosis alone is insufficient.
6. Validate across adequately represented aetiologies, disease stages, liver-function states, centres, and relevant treatment contexts.

If these studies are not available, the required alternative is substantial claim reduction: present the work as exploratory discovery of a candidate EVA1-associated programme and internally derived prognostic score, without causal immunity, sensitization, clinical deployment, treatment selection, priority, or universality claims.

Optional but valuable after the above gates are met:

- orthotopic spatial profiling of tumour margin versus core and longitudinal on-treatment biopsies;
- patient-derived organoid/immune co-culture or ex-vivo slice validation;
- assessment of combination partners and resistance mechanisms;
- formal comparison of etiologic subgroups’ pathway states rather than a single pooled estimate.

# Journal-fit posture

For Nature as an Article, the present manuscript is **not scientifically ready**. The cross-scale question could become important, but the submitted evidence supports neither the declared causal mechanism nor the clinical and universal conclusions. Even after claim moderation, the current package would read as an early HCC biomarker/mechanism study rather than an outstanding, broadly consequential conceptual advance. This is a scientific-fit assessment, not an editorial decision.

# NOT ASSESSABLE items

- Exact novelty, “first” status, and superiority to the full HCC immune-signature literature: no systematic literature corpus was supplied, browsing was prohibited, and only two references are present.
- Figure-level morphology, gating, distributions, outliers, image integrity, and concordance between plots and text: figure images were not supplied.
- Numerical reconciliation of AUCs, hazard models, single-cell results, or mouse measurements: source tables and code were not supplied.
- The full identity of the five genes, coefficient values, assay implementation, and patient-level score distribution: not reported/supplied.
- Mouse strain, sex, immune status/humanization, anti-PD-1 reagent and cross-reactivity, and implantation details: not reported.
- Whether the clinical cohort received immune-checkpoint therapy and, if so, timing and regimen: not reported; the described analysis does not provide a treatment-effect comparison.
- Full-text support from references 1 and 2: the cited papers were not inspected under the frozen-input boundary.
- Ethics and animal-welfare compliance beyond the manuscript’s statement: approving bodies, protocol numbers, consent, animal protocol, and humane endpoints are not reported.

# Evidence anchors

- Abstract: “eight resected HCCs”, “retrospective clinical cohort of 72 patients”, “causal driver”, and “clinically actionable, universally applicable predictor”.
- Impact and implications: “used to select anti-PD-1 therapy”, “immediately deployable biomarker”, and “all major HCC aetiologies”.
- Methods, “Study population”: 72 resected patients, 58 viral, 9 metabolic, 5 other/undocumented, 31 deaths, median survivor follow-up 18 months.
- Methods, “Single-cell discovery”: eight patients; cell-level Wilcoxon testing; cells treated as independent; nominal P < 0.05; no multiple-testing correction.
- Methods, “Score construction and validation”: full-cohort selection of genes, coefficients/cutoffs/rules before a 70:30 split; no external cohort or assay validation; no clinical baseline comparison.
- Methods, “Functional experiments”: one guide in Huh7 and Hep3B; no second guide, rescue, target-engagement assay, or immune-cell co-culture.
- Methods, “Mouse experiment”: ten subcutaneous Huh7 xenografts, five per group, all receiving anti-PD-1, cage-order allocation, unblinded measurement, no independent replicate.
- Results: inverse EVA1/T-cell-score association interpreted as exclusion; growth reduction plus PD-L1/interferon readouts interpreted as direct immune suppression; mouse volume interpreted as anti-PD-1 sensitization.
- Discussion: universal mechanism, independent validation, immediate use, and cross-aetiology applicability claims.
- Data and code availability: raw data, model code, coefficients, analysis dataset, random seeds, and software versions are unavailable/not recorded.

# Confidence and reasons

Overall confidence: `0.98`. The central conclusions and the decisive counterevidence are stated explicitly in the manuscript, including the absence of a treatment-control arm, use of one CRISPR guide without rescue, lack of immune-cell assays, full-dataset model selection, no external validation, and strong aetiologic imbalance. Confidence is lower for any inference about the exact in-vivo immune defect because mouse strain and reagent details are not reported; I therefore frame that system as unresolved and specify a falsifiable validation test rather than presuming a particular host.
