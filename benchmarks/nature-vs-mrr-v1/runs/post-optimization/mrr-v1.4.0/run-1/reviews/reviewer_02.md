# Reviewer role

domain-science (CORE), mechanism-evidence axis only.

# Material inspected and assessment boundary

I inspected the supplied manuscript, Nature journal profile, input inventory, and shared factual fact base. The manuscript was read-only. Assessment is limited to reported mechanistic evidence; absent figure images, tables, protocols, raw data, and code prevent source-level verification.

# Journal standard applied

Nature Article at initial submission: a central causal conclusion must be supported by specific perturbation, appropriate controls, convergent validation, and relevance broad enough for an interdisciplinary flagship claim. Association or expression change alone does not establish pathway dependence.

# Overall assessment

The study offers a coherent hypothesis connecting tumour state, EVA1, and immune escape, but the experiments demonstrate only that a single EVA1-directed perturbation is associated with growth and immune-marker changes. They do not establish on-target EVA1 causality, anti-PD-1 sensitization, or immune-mediated tumour control. The universal mechanistic and therapeutic conclusions therefore exceed the evidence.

# Major strengths

- Human single-cell observations, two in-vitro HCC models, and an in-vivo experiment address the same candidate.
- The manuscript explicitly reports several mechanistically important negative design facts, allowing the causal limits to be assessed.

# BLOCKING issues

## DS-01

- **concern_id:** DS-01
- **proposed issue_key:** eva1-causality-perturbation-specificity
- **axis:** mechanism-evidence
- **role_scope:** PRIMARY
- **severity:** BLOCKING
- **exact claim_pointer:** Abstract, “EVA1 as the causal driver of immune escape”; Results, “EVA1 directly suppresses anti-tumour immunity.”
- **exact evidence_pointer:** Patients and methods, “Functional experiments”: one CRISPR guide in Huh7 and Hep3B, with no second guide, rescue construct, direct target-engagement assay, or immune-cell co-culture; Results, “EVA1 perturbation supports a therapeutic mechanism.”
- **evidence_status:** LOCATED
- **falsifiable concern:** The growth, PD-L1, and interferon-transcript phenotypes could arise from guide-specific off-target effects or secondary cell-state changes rather than loss of EVA1.
- **concrete resolution_test:** Reproduce the phenotype with at least two independent guides and an orthogonal loss-of-function method; quantify EVA1 target engagement; rescue with guide-resistant EVA1; and show that rescue reverses molecular and immune-functional phenotypes.
- **journal_gate:** Required to sustain the central EVA1-specific causal conclusion at Nature.
- **confidence:** 0.99

## DS-02

- **concern_id:** DS-02
- **proposed issue_key:** anti-pd1-sensitization-not-identified
- **axis:** mechanism-evidence
- **role_scope:** PRIMARY
- **severity:** BLOCKING
- **exact claim_pointer:** Abstract, “sensitized xenografts to anti-PD-1 treatment”; Results, “EVA1 inhibition sensitizes HCC to anti-PD-1.”
- **exact evidence_pointer:** Patients and methods, “Mouse experiment”: control and EVA1-depleted tumours were compared, but all mice received anti-PD-1.
- **evidence_status:** LOCATED
- **falsifiable concern:** Without no-antibody/isotype arms, the smaller EVA1-depleted tumours may reflect the reported cell-autonomous growth defect rather than enhanced anti-PD-1 response.
- **concrete resolution_test:** Run an adequately powered, randomized and blinded 2 × 2 study (control versus EVA1 perturbation; anti-PD-1 versus isotype), with a prespecified interaction test, longitudinal growth and survival, and confirmed tumour EVA1 engagement.
- **journal_gate:** A treatment-by-perturbation interaction is required for the claimed sensitization and therapeutic strategy.
- **confidence:** 1.00

## DS-03

- **concern_id:** DS-03
- **proposed issue_key:** xenograft-immune-mechanism-unresolved
- **axis:** mechanism-evidence
- **role_scope:** PRIMARY
- **severity:** BLOCKING
- **exact claim_pointer:** Introduction, “EVA1 directly controls anti-tumour immunity”; Discussion, “universal immune-evasion mechanism.”
- **exact evidence_pointer:** Patients and methods, “Mouse experiment”: subcutaneous Huh7 xenografts; Results states immune infiltration was not measured. Host strain, immune competence, antibody cross-reactivity, and model humanization are not reported.
- **evidence_status:** LOCATION_NOT_PROVIDED
- **falsifiable concern:** The in-vivo phenotype may be tumour-intrinsic and the model may not support the PD-1-dependent immune interaction invoked by the claim.
- **concrete resolution_test:** Specify and validate the host/antibody immune context, then demonstrate EVA1-dependent changes in functional antitumour immune cells and PD-1-pathway response in an immunocompetent matched system or a validated humanized model, with appropriate controls.
- **journal_gate:** Direct immune-mechanism evidence is required to convert tumour-volume concordance into an immune-evasion conclusion.
- **confidence:** 0.98

# MAJOR issues

## DS-04

- **concern_id:** DS-04
- **proposed issue_key:** t-cell-exclusion-inferred-from-association
- **axis:** mechanism-evidence
- **role_scope:** PRIMARY
- **severity:** MAJOR
- **exact claim_pointer:** Results, “We interpreted this association as evidence that EVA1 excludes T cells from HCC.”
- **exact evidence_pointer:** Results, “Single-cell discovery identifies an immune-evasion programme”: EVA1 was higher in low-infiltration tumours and correlated inversely with a T-cell score across eight tumours (r = −0.41, P = 0.03).
- **evidence_status:** LOCATED
- **falsifiable concern:** The association cannot distinguish EVA1-mediated exclusion from tumour composition, aetiology, or another shared cell state.
- **concrete resolution_test:** Combine spatial or histological localization with controlled EVA1 gain/loss experiments measuring T-cell recruitment, activation, cytotoxicity, and tumour-cell killing; test whether EVA1 rescue restores the phenotype.
- **journal_gate:** Required for “excludes T cells”; otherwise revise to “associated with lower T-cell score.”
- **confidence:** 0.99

## DS-05

- **concern_id:** DS-05
- **proposed issue_key:** immune-readouts-confounded-by-growth-state
- **axis:** mechanism-evidence
- **role_scope:** PRIMARY
- **severity:** MAJOR
- **exact claim_pointer:** Results, “PD-L1 abundance also decreased, while three interferon-response transcripts increased. These findings show that EVA1 directly suppresses anti-tumour immunity.”
- **exact evidence_pointer:** Patients and methods, “Functional experiments”: growth and immune readouts were measured in the same 72-hour cultures; Results reports 24% and 19% growth reductions.
- **evidence_status:** LOCATED
- **falsifiable concern:** PD-L1 and transcript changes may be downstream of altered proliferation, viability, stress, or cell-cycle composition rather than a direct immune-regulatory pathway.
- **concrete resolution_test:** Establish dose and time order before growth divergence, control for viable cell number and cell cycle, measure pathway-level intermediates and protein function, and test immune-cell consequences under matched tumour-cell fitness.
- **journal_gate:** Required to claim direct immune regulation rather than a phenotype consistent with it.
- **confidence:** 0.96

## DS-06

- **concern_id:** DS-06
- **proposed issue_key:** universal-mechanism-model-breadth
- **axis:** mechanism-evidence
- **role_scope:** PRIMARY
- **severity:** MAJOR
- **exact claim_pointer:** Title, “universal therapeutic vulnerability”; Impact and implications, “all major HCC aetiologies”; Discussion, “generality of the mechanism.”
- **exact evidence_pointer:** Patients and methods: functional testing used Huh7 and Hep3B, and the sole mouse experiment used Huh7; Study population: 58/72 patients had viral hepatitis. Cell-line provenance, genotype, and aetiologic representation are not reported.
- **evidence_status:** LOCATED
- **falsifiable concern:** The EVA1 phenotype may be restricted to these cell states and need not generalize across molecular or aetiologic HCC diversity.
- **concrete resolution_test:** Validate perturbation specificity and immune function across genomically and aetiologically diverse HCC models, including primary patient-derived systems, with prespecified heterogeneity tests; otherwise narrow the universal/all-aetiology claims.
- **journal_gate:** Nature-level breadth must be demonstrated proportionate to the universal claim or the claim ceiling must be reduced.
- **confidence:** 0.98

# MINOR issues

None within this role.

# EDITORIAL issues

None within this role.

# Claim-ceiling risks

Current evidence supports that an EVA1-directed guide is associated with reduced HCC-cell growth, altered PD-L1/interferon readouts, and smaller anti-PD-1-treated xenografts. It does not support EVA1-specific causality, T-cell exclusion, anti-PD-1 sensitization, a five-gene-score mechanism, therapeutic readiness, or universality.

# Required versus optional additional work

**Required:** on-target replication and rescue; factorial anti-PD-1 testing; a validated immune-competent context with functional immune readouts; separation of immune effects from growth-state effects; and either model-diversity validation or narrowed claims.

**Optional:** deeper downstream pathway mapping after the causal and immune gates pass.

# Journal-fit posture

Not ready for Nature as claimed. The cross-layer concept could become compelling, but the flagship-level causal chain and breadth are presently incomplete.

# NOT APPLICABLE items

Gain/loss symmetry is not independently mandatory if orthogonal loss-of-function, rescue, and immune-functional validation establish specificity; it becomes useful for sufficiency claims.

# NOT ASSESSABLE items

Cell-line authentication and mycoplasma status; CRISPR guide sequence and editing efficiency; biological-replicate counts; antibody identity/cross-reactivity; host strain and immune status; underlying immune-readout data; and figure-level mechanistic evidence.

# Evidence anchors

Primary anchors are the “Functional experiments” and “Mouse experiment” methods, the two mechanistic Results subsections, and the central causal statements in the Abstract, Introduction, Impact and implications, and Discussion.

# Confidence and reasons

High (0.98 overall). The decisive limitations are explicitly stated and map directly onto the manuscript’s central mechanistic claims. Confidence is slightly reduced only where host immune-model details and unsupplied figures/protocols could add context, but they cannot repair the explicitly non-factorial mouse design.
