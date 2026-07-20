# Reviewer role

`journal-priority` (CORE). Primary axes: `journal-fit`; `novelty-significance`.

# Material inspected and assessment boundary

I inspected only the frozen manuscript, journal profile, input inventory, and shared factual fact base supplied for this review. The hashes matched the stated frozen hashes. Target: Nature; Article; initial submission; scientific review only. I did not inspect external literature, figure images, tables, supplements, raw data, or code. The manuscript remained read-only.

# Journal standard applied

Nature is treated as a broad flagship requiring original research of outstanding scientific importance and a conclusion interesting to an interdisciplinary readership. I assessed strength of the claimed advance, novelty, field importance, general-scientific interest, causal completeness, independent validation, and whether the breadth of consequence is proportionate to the evidence. I do not predict acceptance or an editorial decision.

# Overall assessment

The work addresses an important HCC problem and ambitiously connects single-cell discovery, clinical modelling, perturbation, and an animal experiment. However, the evidence described supports at most an exploratory HCC-specific survival association and preliminary EVA1 perturbation phenotype. The universal, clinically actionable, causal, and therapeutic conclusions that create the claimed Nature-level contribution are not established. Lowering the claims to the design-supported ceiling would materially narrow the contribution and would not, on the supplied evidence, leave a conclusion of demonstrated interdisciplinary importance.

# Major strengths

- The manuscript asks a clinically and biologically consequential question.
- It attempts a multi-layer connection from human tumour profiling to functional perturbation.
- Several limitations relevant to validation and mechanism are stated explicitly, enabling clear claim-ceiling assessment.

# BLOCKING issues

## JP-01

- **concern_id:** JP-01
- **proposed issue_key:** `flagship-breadth-not-demonstrated`
- **axis:** `journal-fit`
- **role_scope:** PRIMARY
- **severity:** BLOCKING
- **exact claim_pointer:** Title, “establishes a universal therapeutic vulnerability”; Abstract, “universally applicable predictor”; Discussion, “establishes a universal immune-evasion mechanism in HCC.”
- **exact evidence_pointer:** Patients and methods—Study population; Single-cell discovery; Functional experiments; Mouse experiment. The reported scope is eight single-cell patients, one 72-patient resection cohort from one centre, two HCC cell lines, and one ten-mouse Huh7 experiment.
- **evidence_status:** LOCATED
- **falsifiable concern:** The supplied evidence does not demonstrate a transferable biological principle or consequence beyond the specific HCC cohort and models; therefore, the central conclusion does not presently meet the supplied Nature criterion of outstanding importance to an interdisciplinary readership.
- **concrete resolution_test:** Either provide independent human and mechanistic validation showing that the central principle generalizes across prespecified HCC aetiologies, treatment settings, and relevant model systems, with a clearly articulated consequence beyond this disease-specific signature, or remove “universal” and broad-interest framing and reassess journal target.
- **journal_gate:** N001 outstanding scientific importance and interdisciplinary interest; N002 field importance and general-scientific interest.
- **confidence:** 0.97

## JP-02

- **concern_id:** JP-02
- **proposed issue_key:** `clinical-actionability-and-treatment-selection-unestablished`
- **axis:** `novelty-significance`
- **role_scope:** PRIMARY
- **severity:** BLOCKING
- **exact claim_pointer:** Impact and implications, “used to select anti-PD-1 therapy” and “immediately deployable biomarker”; Discussion, “immediate use for selecting anti-PD-1 therapy.”
- **exact evidence_pointer:** Score construction and validation states that the model and all rules were selected using the full 72-patient dataset before a 70:30 split; no external cohort, independent assay, calibration, decision-curve analysis, or clinical-baseline comparison was used. Study population reports overall survival after resection, not response or benefit under an anti-PD-1 treatment-selection design.
- **evidence_status:** LOCATED
- **falsifiable concern:** A retrospective overall-survival association in a reused single-centre dataset cannot establish that the score predicts anti-PD-1 benefit, improves treatment selection, is deployable, or has clinical utility; these unsupported consequences constitute much of the claimed significance.
- **concrete resolution_test:** Demonstrate a locked score in an independent intended-use cohort receiving clinically relevant alternatives, test treatment-by-score interaction or an appropriate predictive-benefit endpoint, compare against prespecified clinical baselines, and report calibration and decision utility; otherwise lower the conclusion to an exploratory survival association and remove actionability, treatment-selection, deployment, and universal-use claims.
- **journal_gate:** N001 outstanding scientific importance; N002 strength of evidence, novelty, and field importance.
- **confidence:** 0.99

## JP-03

- **concern_id:** JP-03
- **proposed issue_key:** `causal-therapeutic-advance-unestablished`
- **axis:** `novelty-significance`
- **role_scope:** PRIMARY
- **severity:** BLOCKING
- **exact claim_pointer:** Abstract, “EVA1 as the causal driver of immune escape”; Results, “directly suppresses anti-tumour immunity” and “sensitizes HCC to anti-PD-1”; Discussion, “causal link” and “therapeutic development.”
- **exact evidence_pointer:** Functional experiments used one guide, with no second guide, rescue, direct target-engagement assay, or immune-cell co-culture. In the mouse experiment, all animals received anti-PD-1, no untreated comparator arm was included, and immune infiltration and post-implantation EVA1 expression were not measured.
- **evidence_status:** LOCATED
- **falsifiable concern:** The reported growth, PD-L1, transcript, and tumour-volume changes do not distinguish EVA1-specific immune causality from perturbation-associated growth effects, and the all-anti-PD-1 mouse design cannot establish sensitization as an interaction. Thus the claimed causal therapeutic advance—the main conceptual novelty—is not demonstrated.
- **concrete resolution_test:** Establish EVA1-specific causality with independent perturbations, rescue and target engagement in an immune-relevant system, then demonstrate a prespecified EVA1-perturbation-by-anti-PD-1 interaction with appropriate control arms and immune readouts in a relevant replicated model; otherwise lower the claims to preliminary depletion-associated phenotypes.
- **journal_gate:** N002 strength of evidence, novelty, and field importance.
- **confidence:** 0.99

# MAJOR issues

## JP-04

- **concern_id:** JP-04
- **proposed issue_key:** `priority-claim-not-substantiated`
- **axis:** `novelty-significance`
- **role_scope:** PRIMARY
- **severity:** MAJOR
- **exact claim_pointer:** Introduction, “none provides a universal, mechanistically validated guide” and “the first clinically actionable HCC immune score derived from single-cell data.”
- **exact evidence_pointer:** Unavailable for a field-wide priority determination: the packet supplies only two references, external literature and cited-paper full texts were not supplied, and browsing was prohibited.
- **evidence_status:** NOT_ASSESSABLE
- **falsifiable concern:** The “none” and “first” priority claims are not established by the supplied evidence, so the degree of originality relative to prior HCC immune signatures cannot be judged.
- **concrete resolution_test:** Provide a current, claim-specific literature comparison covering prior single-cell-derived HCC signatures, immune-evasion mechanisms, clinical validation, and treatment-predictive studies; retain priority wording only if direct comparison supports it, otherwise replace it with a bounded contribution statement.
- **journal_gate:** N002 novelty and field importance.
- **confidence:** 0.98

# MINOR issues

None within the assigned axes.

# EDITORIAL issues

None within the assigned axes.

# Claim-ceiling risks

The defensible ceiling from the supplied design is an exploratory, single-centre HCC survival signature plus preliminary EVA1 depletion-associated growth and molecular phenotypes. “Predicts anti-PD-1 benefit,” “clinically actionable,” “immediately deployable,” “causal driver,” “sensitizes,” “universal,” and “all major HCC aetiologies” require the resolution tests in JP-01–JP-03 or must be removed.

# Required versus optional additional work

Required for the stated contribution: close JP-01–JP-03 with independent, intended-use human validation and causal, interaction-capable mechanistic evidence, and close JP-04 with a direct novelty comparison. If those designs are not feasible, claim lowering and retargeting are required. Optional only after those gates close: broader etiologic sampling or additional model systems that extend, rather than substitute for, the core validation.

# Journal-fit posture

`RETARGET_RECOMMENDED` on the supplied evidence unless the central evidence architecture is substantially expanded. This is a scientific fit assessment, not an acceptance prediction or editorial decision.

# NOT APPLICABLE items

None among the two assigned axes.

# NOT ASSESSABLE items

Exact field-wide priority and originality are not assessable without the relevant literature corpus or permission to inspect it (JP-04). Final editorial outcome is outside this review and is not predicted.

# Evidence anchors

Primary anchors are the quoted Title, Abstract, Impact and implications, Introduction, Score construction and validation, Functional experiments, Mouse experiment, Results, Discussion, References, and the inventory’s list of unavailable materials.

# Confidence and reasons

Overall confidence: 0.98. The headline claims and the limitations controlling their ceilings are stated explicitly, and the journal profile supplies the applicable flagship criteria. Confidence is lower only for field-wide novelty because the required external literature evidence was unavailable by design.
