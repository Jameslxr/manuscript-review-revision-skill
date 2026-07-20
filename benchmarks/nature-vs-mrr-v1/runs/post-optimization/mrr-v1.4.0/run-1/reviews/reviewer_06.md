# Reviewer role

Role_id: adversarial-review (OPTIONAL). Owned axis: causal-vs-correlative. Trigger: fragile causal and clinical-utility chain. This review stress-tests only the inferential chain from single-cell association through treatment selection and universality.

# Material inspected and assessment boundary

I inspected only the frozen manuscript, Nature journal profile, input inventory, and shared fact base. The manuscript was read-only. No browsing, revision, polishing, formatting review, or inspection of unsupplied materials was performed.

# Journal standard applied

Nature-level causal completeness, broad consequence, and independent validation were applied under profile criteria N001, N002, and N006. A broad mechanistic or clinical conclusion must be identified by an appropriate counterfactual, not inferred from concordant associations alone.

# Overall assessment

The hypothesis-generating sequence is interesting, but its headline chain is not causally identified. Separate associations link EVA1 with T-cell score, the five-gene score with survival, and EVA1 depletion with cell growth, markers, and tumour size under universal anti-PD-1 exposure. They do not establish T-cell exclusion, survival mediation, sensitization, treatment selection, or universality. The central conclusions require new evidence.

# Major strengths

- The manuscript connects patient observations, survival modelling, tumour-cell perturbation, and an in vivo experiment.
- The Methods disclose missing rescue, immune-cell co-culture, and untreated mouse counterfactuals.
- EVA1 depletion was examined in two cell lines, providing a starting point for specificity testing.

# BLOCKING issues

## AR-01

- concern_id: AR-01
- proposed issue_key: `causal:evasion-reverse-causation`
- axis: causal-vs-correlative
- role_scope: PRIMARY
- severity: BLOCKING
- exact claim_pointer: Results, “We interpreted this association as evidence that EVA1 excludes T cells from HCC”; Abstract, “EVA1 as the causal driver of immune escape.”
- exact evidence_pointer: Results, EVA1 was higher in low-infiltration tumours and inversely correlated with a T-cell score across eight tumours (Spearman r = −0.41, P = 0.03).
- evidence_status: LOCATED
- falsifiable concern: The cross-sectional association cannot distinguish EVA1-driven exclusion from immune pressure inducing EVA1, tumour composition, disease context, or another tumour state causing both measurements; temporal order is absent.
- concrete resolution_test: In an immune-competent HCC model, induce EVA1 depletion only after tumours are established, include an EVA1 rescue, and serially measure spatial/quantitative T-cell entry before divergence in tumour burden. Failure of depletion to increase infiltration, or rescue to reverse it, falsifies the exclusion claim.
- journal_gate: A causal immune-evasion conclusion central to broad importance is not met by cross-sectional association.
- confidence: 0.99

## AR-02

- concern_id: AR-02
- proposed issue_key: `causal:perturbation-specificity-fitness-confounding`
- axis: causal-vs-correlative
- role_scope: PRIMARY
- severity: BLOCKING
- exact claim_pointer: Results, “These findings show that EVA1 directly suppresses anti-tumour immunity.”
- exact evidence_pointer: Functional experiments and Results: one CRISPR guide reduced 72-hour growth in Huh7 and Hep3B, decreased PD-L1, and increased three interferon-response transcripts; no second guide, rescue, target-engagement assay, or immune-cell co-culture.
- evidence_status: LOCATED
- falsifiable concern: A one-guide perturbation coupled to reduced cell fitness does not identify an EVA1-specific immune mechanism; off-target effects or secondary stress/growth changes can explain the molecular readouts, and no anti-tumour immune function was measured.
- concrete resolution_test: Reproduce the phenotype with at least two independent guides and reverse it with guide-resistant EVA1 rescue, then test immune-cell-mediated killing or activation under viability/growth-matched conditions. Lack of concordance or rescue falsifies EVA1 specificity.
- journal_gate: Direct causal control of immunity requires perturbation specificity and a functional immune endpoint.
- confidence: 0.99

## AR-03

- concern_id: AR-03
- proposed issue_key: `causal:anti-pd1-interaction-missing`
- axis: causal-vs-correlative
- role_scope: PRIMARY
- severity: BLOCKING
- exact claim_pointer: Abstract and Results, EVA1 depletion “sensitized” xenografts/HCC to anti-PD-1.
- exact evidence_pointer: Mouse experiment: control versus EVA1-depleted Huh7 xenografts, five mice per group, with all mice receiving anti-PD-1; EVA1 depletion also reduced cell growth in vitro.
- evidence_status: LOCATED
- falsifiable concern: Without no-anti-PD-1 arms, the observed tumour-size difference cannot distinguish sensitization from an anti-PD-1-independent growth effect of EVA1 depletion. The required treatment-by-EVA1 interaction is unidentified.
- concrete resolution_test: Run a prespecified 2×2 experiment (control versus EVA1 perturbation; anti-PD-1 versus matched control) in an immune-competent model, include rescue, and test the interaction term. Absence of a positive interaction falsifies sensitization.
- journal_gate: The therapeutic-sensitization conclusion requires its defining counterfactual and interaction evidence.
- confidence: 1.00

## AR-04

- concern_id: AR-04
- proposed issue_key: `causal:clinical-selection-no-treatment-effect`
- axis: causal-vs-correlative
- role_scope: PRIMARY
- severity: BLOCKING
- exact claim_pointer: Impact and implications, the score “can be measured at diagnosis and used to select anti-PD-1 therapy”; Discussion, “immediate use for selecting anti-PD-1 therapy.”
- exact evidence_pointer: Study population and Score construction: 72 retrospectively studied resected patients, overall survival endpoint, no reported anti-PD-1 comparison; Methods explicitly state no decision-curve analysis or clinical baseline comparison.
- evidence_status: LOCATED
- falsifiable concern: Prognosis under observed care does not identify differential benefit from anti-PD-1. No treated-versus-comparator counterfactual, score-by-treatment interaction, intended-use population, response endpoint, or net-benefit analysis supports treatment selection.
- concrete resolution_test: Externally lock the assay, formula, threshold, and intended-use population, then test the prespecified score-by-treatment interaction in a prospective randomized anti-PD-1-versus-relevant-comparator dataset with a clinically meaningful endpoint. No interaction means the score is not treatment-selective.
- journal_gate: Clinical actionability requires demonstrated treatment utility, not prognostic discrimination.
- confidence: 1.00

# MAJOR issues

## AR-05

- concern_id: AR-05
- proposed issue_key: `causal:score-mechanism-link-unidentified`
- axis: causal-vs-correlative
- role_scope: PRIMARY
- severity: MAJOR
- exact claim_pointer: Discussion, “The molecular and animal results identify EVA1 as the causal link between the five-gene score and immune escape.”
- exact evidence_pointer: Score construction and Results: five genes were selected for survival association; only EVA1 was perturbed, while neither mediation of score–survival association nor causal contribution of the other four genes was tested.
- evidence_status: LOCATED
- falsifiable concern: The evidence does not connect the composite score to the EVA1 perturbation or show that immune escape mediates its survival association; the score may be merely prognostic and EVA1 experiments a parallel observation.
- concrete resolution_test: In an independent cohort with score, EVA1, immune-state, and outcome measurements, prespecify the causal ordering and test mediation, then perturb score components to determine whether the composite immune phenotype depends on EVA1. Failure of the proposed pathway to account for the association breaks the claimed bridge.
- journal_gate: A unified mechanism cannot be assembled by juxtaposing disconnected associations.
- confidence: 0.97

## AR-06

- concern_id: AR-06
- proposed issue_key: `causal:universality-external-validity`
- axis: causal-vs-correlative
- role_scope: PRIMARY
- severity: MAJOR
- exact claim_pointer: Title, “universal therapeutic vulnerability”; Abstract, “universally applicable”; Impact and implications, “all major HCC aetiologies.”
- exact evidence_pointer: Study population: 58 viral, 9 metabolic, and 5 other or undocumented cases at one centre; functional evidence used Huh7 and Hep3B, with one Huh7 xenograft experiment; no external cohort.
- evidence_status: LOCATED
- falsifiable concern: The evidence neither estimates transportability across aetiologies and treatment settings nor tests whether the EVA1 dependency and treatment interaction are invariant across them.
- concrete resolution_test: Independently validate the locked score and the 2×2 EVA1-by-anti-PD-1 interaction in adequately represented aetiology strata and distinct models; prespecify heterogeneity tests. Material loss of performance or interaction in any claimed major stratum falsifies universality.
- journal_gate: Broad consequence and all-aetiology claims require independent, diversity-aware validation.
- confidence: 0.99

# MINOR issues

None on the owned axis.

# EDITORIAL issues

None on the owned axis.

# Claim-ceiling risks

Current evidence supports associations of EVA1 with a tumour-level T-cell score; EVA1 depletion with growth and selected markers in two cell lines; EVA1 depletion with smaller tumours under universal anti-PD-1 exposure; and the score with survival at the derivation centre. “Excludes T cells,” “directly suppresses immunity,” “sensitizes,” “clinically actionable,” and “universal” exceed these ceilings.

# Required versus optional additional work

Required: the temporal/rescue immune-exclusion test; perturbation-specific functional immune validation; the 2×2 anti-PD-1 interaction experiment; and externally locked clinical treatment-effect validation. Required if the unified and universal claims remain: score-to-mechanism mediation/perturbation evidence and aetiology-diverse external validation. Optional: exploratory mapping of downstream EVA1 pathways after these gates are passed.

# Journal-fit posture

In its current form, the work is hypothesis-generating and does not meet a Nature Article’s causal and broad-consequence standard. Passing the causal gates could materially alter that posture; final editorial fit is not adjudicated here.

# NOT APPLICABLE items

Formatting, prose polish, display-item count, reference count, and other non-scientific submission mechanics are outside this scientific causal review. Lower-severity mechanism, design, statistics, claims, and journal-fit crossover concerns were intentionally not reported.

# NOT ASSESSABLE items

Numerical reconciliation, figure-level support, underlying analyses, provenance, code execution, full protocols, and cited-paper support are not assessable because source materials were not supplied. Packet absence was not treated as proof an experiment never occurred unless the manuscript says it was not performed.

# Evidence anchors

Primary anchors were the Abstract; Impact and implications; Patients and methods subsections “Single-cell discovery,” “Score construction and validation,” “Functional experiments,” and “Mouse experiment”; Results subsections on the immune-evasion programme, score, and perturbation; Discussion; and Figures 2–4 legends. The shared fact base and inventory confirmed the supplied-evidence boundary.

# Confidence and reasons

Overall confidence: 0.99. The conclusions follow directly from explicit study structure and explicitly missing counterfactuals. Confidence is slightly below absolute because source outputs and unreported underlying work are unavailable, but those limitations do not restore the causal identifiability absent from the reported design.
