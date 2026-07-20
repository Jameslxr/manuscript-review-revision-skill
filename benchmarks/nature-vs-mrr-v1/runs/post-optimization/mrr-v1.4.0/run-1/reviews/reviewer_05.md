# Reviewer role

Role `claim-evidence-reference` (CORE). Owned axes reviewed: figures-and-tables, writing-clarity, claim-moderation, and reference-support. All concerns are `PRIMARY`; no independently blocking crossover was identified.

# Material inspected and assessment boundary

I inspected only the frozen manuscript, Nature profile, inventory, and fact base. The supplied hashes matched. This is scientific review of a Nature Article at initial submission. Figures, tables, supplements, raw data, code, cited full texts, and external bibliographic verification were unavailable and are not inferred.

# Journal standard applied

Nature’s supplied profile requires original research of outstanding importance with conclusions supported strongly enough for an interdisciplinary readership (N001–N002), and Methods sufficient to interpret and replicate results (N006). I applied a strict claim-evidence ceiling without making an editorial decision.

# Overall assessment

The coherent discovery-to-perturbation narrative repeatedly converts association or preliminary perturbation evidence into universal, causal, treatment-predictive, and deployment-ready conclusions. Internal AUC disagreement and unavailable source displays prevent numerical closure. Central claims require major recalibration or materially stronger evidence.

# Major strengths

- Cohort composition, model-building sequence, controls, and important limitations are stated directly.
- Results provide concrete effect directions and selected magnitudes, enabling claim-to-evidence comparison.
- The legends identify the intended four-figure narrative and expose the Figure 3 AUC conflict.

# BLOCKING issues

None.

# MAJOR issues

## CE-01

- **concern_id:** CE-01
- **proposed issue_key:** `auc-three-way-conflict-and-outcome-closure`
- **axis:** figures-and-tables
- **role_scope:** `PRIMARY`
- **severity:** `MAJOR`
- **exact claim_pointer:** Abstract, “AUC of 0.91 for 3-year mortality”; Results, “validation-set…AUC of 0.84”; Figure 3 legend, “Panel C…0.86.”
- **exact evidence_pointer/unavailable reason:** The three supplied locations disagree; Results also state median follow-up was 18 months and 3-year status was unavailable for many survivors. Figure image, patient-level outcomes, code, and source table were not supplied.
- **evidence_status:** `LOCATED`
- **falsifiable concern:** At least two reported AUC values are incorrect or refer to analyses that are not distinguished; the evaluable 3-year set is undefined.
- **concrete resolution_test:** Reconcile one prespecified estimand and value across all text/display locations; report analysis set, event/censoring handling, horizon method, and uncertainty; reproduce it from supplied source outputs.
- **journal_gate:** Nature exact-evidence and interpretable-results gate (N001, N002, N006).
- **confidence:** 0.99

## CE-02

- **concern_id:** CE-02
- **proposed issue_key:** `independent-validation-mischaracterization`
- **axis:** claim-moderation
- **role_scope:** `PRIMARY`
- **severity:** `MAJOR`
- **exact claim_pointer:** Discussion, “validated in an independent subset” and “overcomes…single-centre signatures.”
- **exact evidence_pointer/unavailable reason:** Methods state gene selection, cutoffs, coefficient signs, and missing-value rules used the entire 72-patient dataset before that same cohort was split 70:30; no external cohort was used.
- **evidence_status:** `LOCATED`
- **falsifiable concern:** The described validation subset is not independent of model development.
- **concrete resolution_test:** Replace “independent” and the claimed consequence with a technically accurate internal-evaluation description, or demonstrate a fully untouched cohort/sample set never used in any selection or tuning.
- **journal_gate:** Nature strength-of-evidence gate (N002).
- **confidence:** 0.99

## CE-03

- **concern_id:** CE-03
- **proposed issue_key:** `eva1-causal-immune-escape-overclaim`
- **axis:** claim-moderation
- **role_scope:** `PRIMARY`
- **severity:** `MAJOR`
- **exact claim_pointer:** Title/Abstract/Introduction/Results/Discussion claims that EVA1 is “the causal driver,” “directly controls,” or “directly suppresses anti-tumour immunity.”
- **exact evidence_pointer/unavailable reason:** Reported evidence is tumour-level correlation plus one-guide depletion in two cell lines with growth, PD-L1, and three transcript readouts; no immune-cell co-culture, second guide, rescue, or direct target-engagement assay is reported.
- **evidence_status:** `LOCATED`
- **falsifiable concern:** The supplied evidence supports association and perturbation-linked molecular/growth changes, not the stated causal immune-escape mechanism.
- **concrete resolution_test:** Moderate all causal/immune-control language to the measured endpoints, or provide orthogonal perturbation/rescue and direct immune-function evidence that discriminates the proposed causal path.
- **journal_gate:** Nature conclusion-strength gate (N001–N002).
- **confidence:** 0.98

## CE-04

- **concern_id:** CE-04
- **proposed issue_key:** `anti-pd1-sensitization-without-interaction-evidence`
- **axis:** claim-moderation
- **role_scope:** `PRIMARY`
- **severity:** `MAJOR`
- **exact claim_pointer:** Abstract, Results, and Impact statement claim EVA1 depletion “sensitized” xenografts to anti-PD-1 and establishes an EVA1 treatment strategy.
- **exact evidence_pointer/unavailable reason:** All ten mice received anti-PD-1; only control versus EVA1-depleted cells were compared. No no-anti-PD-1 arm, immune infiltration, target persistence, survival, toxicity, or replicate experiment is reported.
- **evidence_status:** `LOCATED`
- **falsifiable concern:** A depletion effect under anti-PD-1 exposure does not by itself establish sensitization or interaction with anti-PD-1.
- **concrete resolution_test:** Remove sensitization/treatment-strategy claims or demonstrate a replicated factorial comparison testing EVA1 status × anti-PD-1 with relevant immune and target-engagement readouts.
- **journal_gate:** Nature exact-evidence gate (N001–N002).
- **confidence:** 0.99

## CE-05

- **concern_id:** CE-05
- **proposed issue_key:** `universal-actionable-deployment-claim`
- **axis:** claim-moderation
- **role_scope:** `PRIMARY`
- **severity:** `MAJOR`
- **exact claim_pointer:** Title, Abstract, Impact statement, Introduction, and Discussion describe a “universal therapeutic vulnerability,” “universally applicable,” “immediately deployable” biomarker usable to select anti-PD-1 across all major HCC aetiologies.
- **exact evidence_pointer/unavailable reason:** One retrospective resection cohort (72; 58 viral, 9 metabolic, 5 other/undocumented), no external cohort, independent assay, calibration, decision analysis, clinical baseline comparison, or immunotherapy-response cohort is reported.
- **evidence_status:** `LOCATED`
- **falsifiable concern:** The sampled population and reported endpoints do not establish cross-aetiology generalizability, clinical deployability, or treatment-benefit prediction.
- **concrete resolution_test:** Restrict claims to retrospective survival association in the studied setting, or supply external cross-aetiology validation, locked assay/model evaluation, calibration/clinical-comparator evidence, and treatment-interaction validation.
- **journal_gate:** Nature interdisciplinary conclusion and evidence-strength gate (N001–N002).
- **confidence:** 0.99

## CE-06

- **concern_id:** CE-06
- **proposed issue_key:** `reference-2-treatment-support-mismatch`
- **axis:** reference-support
- **role_scope:** `PRIMARY`
- **severity:** `MAJOR`
- **exact claim_pointer:** Discussion citation of reference 2 for the claim that the five-gene score identifies benefit from anti-PD-1 monotherapy.
- **exact evidence_pointer/unavailable reason:** Supplied title is “Atezolizumab plus bevacizumab in unresectable hepatocellular carcinoma,” which names combination therapy and no five-gene score. Full text was unavailable.
- **evidence_status:** `LOCATED`
- **falsifiable concern:** The visible bibliographic scope does not match the biomarker-specific monotherapy-benefit claim; exact semantic support remains unverified.
- **concrete resolution_test:** Split background treatment-efficacy from biomarker-prediction claims; cite direct evidence for each, or remove the unsupported treatment-benefit attribution. Verify exact support against full text before resubmission.
- **journal_gate:** Nature reference-support and conclusion-strength gate (N001–N002).
- **confidence:** 0.98

# MINOR issues

## CE-07

- **concern_id:** CE-07
- **proposed issue_key:** `reference-1-exhaustive-negative-claim`
- **axis:** reference-support
- **role_scope:** `PRIMARY`
- **severity:** `MINOR`
- **exact claim_pointer:** Introduction citation of reference 1 for “no previous immune signature has clinical utility.”
- **exact evidence_pointer/unavailable reason:** Reference 1’s supplied title concerns comprehensive/integrative genomic characterization, not an exhaustive clinical-utility review. Full text was unavailable.
- **evidence_status:** `LOCATED`
- **falsifiable concern:** One genomic-characterization citation cannot visibly substantiate the field-wide negative claim.
- **concrete resolution_test:** Narrow the statement or support it with an explicit, current evidence synthesis; verify every cited source’s exact semantic support.
- **journal_gate:** Nature clarity/reference-support gate (N001–N002).
- **confidence:** 0.93

## CE-08

- **concern_id:** CE-08
- **proposed issue_key:** `legends-insufficient-for-display-interpretation`
- **axis:** writing-clarity
- **role_scope:** `PRIMARY`
- **severity:** `MINOR`
- **exact claim_pointer:** Figure legends 1–4.
- **exact evidence_pointer/unavailable reason:** Legends name topics but generally omit sample/unit definitions, group sizes, summary/error conventions, statistical tests, and panel-level endpoint descriptions; images are unavailable.
- **evidence_status:** `LOCATED`
- **falsifiable concern:** The supplied legends are not self-contained enough to interpret displays or reconcile them with text.
- **concrete resolution_test:** Expand each legend with panel mapping, biological unit, n, groups, measures, uncertainty, tests, and abbreviation definitions; confirm every numeric/directional text claim against the final figure and source output.
- **journal_gate:** Nature clear interdisciplinary reporting and interpretability gate (N002, N006).
- **confidence:** 0.95

# EDITORIAL issues

None.

# Claim-ceiling risks

Evidence ceilings are: retrospective survival association, not treatment selection; perturbation-associated phenotypes, not a demonstrated immune-escape mechanism; smaller tumours under shared anti-PD-1 exposure, not sensitization; and studied-cohort relevance, not universality.

# Required versus optional additional work

**Required:** reconcile the AUC; correct validation terminology; calibrate causal, sensitization, universality, and deployability claims; repair citation-to-claim alignment; and close final figure-text-source consistency. **Optional if claims are narrowed:** factorial drug-interaction work, orthogonal causal validation, and external clinical validation are not required merely to report preliminary findings, but are required to retain the present strong claims.

# Journal-fit posture

The cross-scale question could interest a broad readership, but the manuscript in its present form does not meet Nature-level claim precision or evidentiary closure. This is a scientific posture, not a recommendation on the final editorial decision.

# NOT APPLICABLE items

No reference-count concern applies (two references are within the supplied guideline). No out-of-role journal-priority, ethics, study-design, or statistical issue is reported because none met the required `BLOCKING_CROSSOVER` threshold.

# NOT ASSESSABLE items

Figure appearance, panel completeness, table reconciliation, numerical source reproduction, raw-data/model-code consistency, and external bibliographic metadata reality are not assessable from the packet. Exact semantic support from either cited paper is also not assessable without full text; CE-06 and CE-07 are based only on mismatches visible in the manuscript’s claim wording and supplied titles.

# Evidence anchors

Anchors are the three AUC statements; full-cohort model construction before splitting; stated experimental omissions; cohort aetiology counts; deployment/universality language; the legends; and stated uses of references 1 and 2.

# Confidence and reasons

Overall confidence is 0.98 for internal claim-evidence inconsistencies because the relevant claims and limitations are explicit in the manuscript. Confidence is lower only for exact citation semantics and display/source fidelity because cited full texts, figures, tables, data, and code were not supplied.
