# Nature-style reviewer assessment

## Review setup

- **Input scope:** Full synthetic benchmark manuscript presented as a Nature Article at initial submission. The supplied file includes title, abstract, impact statement, introduction, methods, results, discussion, data/code availability, ethics statement, figure legends and two references.
- **Assessment boundary:** This is a reviewer-style assessment, not an editorial decision or an author rebuttal. It is grounded only in the supplied manuscript and the local Nature reviewer source basis. The actual figures, supplementary material, protocols, patient-level data, model code and raw single-cell data were not supplied; figure-level visual quality and analyses not described in the text are therefore not assessable.
- **Shared manuscript claim summary:** The manuscript claims that a five-gene score derived from single-cell data is a universally applicable, clinically actionable predictor for HCC and that EVA1 is a causal immune-evasion driver whose inhibition sensitizes HCC to anti-PD-1 therapy.
- **Visible evidence base:** Single-cell RNA sequencing of tumour and adjacent tissue from eight patients; a retrospective single-centre cohort of 72 resected patients with 31 deaths; full-dataset model selection followed by a 70:30 split; one-guide EVA1 depletion in two HCC cell lines; and one ten-mouse, two-group xenograft experiment in which all animals received anti-PD-1.
- **Missing materials affecting confidence:** Actual figures and source data; an independent external cohort; a locked model specification and coefficients; assay validation; patient-level treatment-response data; factorial treatment controls in the mouse study; additional perturbation specificity experiments; detailed ethics approvals; and deposited data/code.

## Reviewer 1

**Emphasis:** Technical validity and technical failings.

### Overall assessment

The manuscript addresses an important connection between tumour-cell state, immune escape and treatment selection, and its attempt to link single-cell discovery, clinical outcomes and perturbation experiments is potentially valuable. The visible analyses and experiments, however, do not establish the principal predictive, causal or therapeutic claims. The most consequential problems are patient-level pseudoreplication and uncorrected screening in discovery, information leakage in score construction, an inadequately supported three-year endpoint, non-specific perturbation evidence, and a mouse design that cannot test sensitization to anti-PD-1.

### Who would be interested in the results, and why

Researchers studying tumour–immune interactions, HCC heterogeneity, prognostic biomarkers and therapy response would be interested in a rigorously validated link between a tumour-cell programme and immune exclusion. The present evidence is most directly relevant to those communities; broader interest would depend on demonstrating a reliable causal mechanism and a genuinely predictive, rather than merely prognostic, clinical application.

### Major strengths

- The manuscript poses a coherent question spanning molecular state, patient outcome and intervention.
- It reports key design limitations explicitly, including lack of multiple-testing correction, whole-dataset feature selection, absence of external validation, single-guide perturbation and unblinded mouse measurements.
- The use of two cell lines provides a limited form of cross-model replication for the growth phenotype.

### Major concerns

**R1-M1 — [experimental-design; issue key: single-cell-pseudoreplication-multiplicity]**  
**Claim pointer:** The single-cell comparison identifies an HCC immune-evasion programme and supports the inference that EVA1 excludes T cells.  
**Evidence pointer:** “Single-cell discovery” (lines 61–67); “Single-cell discovery identifies an immune-evasion programme” (lines 109–115); Figure 1 legend (lines 171–172).  
**Concern:** Cells from only eight patients were treated as independent observations, and 1,842 genes were selected at nominal \(P<0.05\) without multiplicity correction. The biological contrast is between tumours/patients, not 46,218 independent patient-level units. The reported EVA1–T-cell-score correlation is also based on eight tumours and is associative. This discovery procedure does not establish a robust programme or T-cell exclusion.  
**Resolution test:** Reanalyse with the patient as the biological replicate using a patient-aware model or pseudobulk strategy, control the gene-level false-discovery rate, report uncertainty and sensitivity analyses, and restrict “excludes T cells” to an association unless discriminating evidence is supplied.

**R1-M2 — [statistical-rigor; issue key: model-development-validation-leakage]**  
**Claim pointer:** The five-gene formula was independently validated by evaluating it in the held-out 30% subset.  
**Evidence pointer:** “Score construction and validation” (lines 69–81); “The five-gene score predicts survival” (lines 116–123); Discussion (lines 139–143).  
**Concern:** Gene selection, stepwise modelling, cutoffs, coefficient signs and missing-value rules were all chosen using the complete 72-patient dataset before the split. The nominal validation subset therefore influenced the model and is not independent. Twenty-seven genes plus 18 covariates were considered with only 31 deaths, further increasing optimism and selection instability.  
**Resolution test:** Repeat the complete development pipeline strictly within training data, quantify optimism with appropriate resampling or nested validation, provide the locked formula, and test it in an external cohort that had no role in any selection or tuning. Until then, describe the 30% subset as an internal split rather than independent validation.

**R1-M3 — [clinical-validity; issue key: three-year-performance-not-established]**  
**Claim pointer:** The score achieves high validation performance for three-year mortality.  
**Evidence pointer:** Abstract (lines 10–18); study population (lines 47–57); Results (lines 118–123); Figure 3 legend (lines 177–178).  
**Concern:** Median follow-up among survivors is 18 months, while three-year outcome status was unavailable for many survivors. The manuscript does not state how censoring was handled in the time-dependent performance estimate. In addition, the AUC is reported as 0.91 in the Abstract, 0.84 in the Results and 0.86 in Figure 3. These discrepancies and the immature follow-up prevent evaluation of the headline performance claim.  
**Resolution test:** Define the time-dependent AUC estimand and censoring method, report the number at risk and events at three years with confidence intervals, reconcile all AUC values to one verified analysis, and moderate the endpoint claim if follow-up cannot support it.

**R1-M4 — [mechanism-evidence; issue key: eva1-perturbation-specificity]**  
**Claim pointer:** EVA1 directly suppresses antitumour immunity and is the causal driver of immune escape.  
**Evidence pointer:** “Functional experiments” (lines 83–89); Results (lines 125–130); Discussion (lines 145–149).  
**Concern:** One CRISPR guide, without a second guide, rescue experiment or direct target-engagement assessment, cannot separate EVA1-specific effects from guide-related or other perturbation effects. Growth, PD-L1 and three interferon-response transcripts in tumour-cell monocultures do not directly measure immune escape.  
**Resolution test:** Demonstrate on-target specificity with independent perturbations and rescue, verify EVA1 depletion, and use an experimental system that measures a relevant tumour–immune interaction. Alternatively, narrow the conclusion to the observed cell-autonomous associations.

**R1-M5 — [experimental-design; issue key: anti-pd1-sensitization-not-tested]**  
**Claim pointer:** EVA1 depletion sensitizes HCC xenografts to anti-PD-1.  
**Evidence pointer:** “Mouse experiment” (lines 91–97); Results (lines 132–135); Figure 4 legend (line 180).  
**Concern:** All mice received anti-PD-1, and the study compared only control versus EVA1-depleted cells. Without treatment/no-treatment groups for each EVA1 condition, there is no test of an EVA1-by-anti-PD-1 interaction; smaller tumours could reflect the growth phenotype already seen in vitro rather than sensitization.  
**Resolution test:** Use a design that estimates the interaction between EVA1 perturbation and anti-PD-1, with appropriate controls and prespecified analysis, or remove the sensitization claim.

**R1-M6 — [experimental-design; issue key: mouse-bias-and-replication]**  
**Claim pointer:** The mouse experiment provides generalizable in vivo therapeutic evidence.  
**Evidence pointer:** “Mouse experiment” (lines 91–97); Results (lines 132–135).  
**Concern:** Five animals per group, cage-order allocation, unblinded measurement, a single day-21 comparison and no independent replicate create substantial bias and imprecision. No immune infiltration, survival, toxicity or post-implantation EVA1 measurement was obtained, so the experiment cannot establish an immune mechanism or development readiness.  
**Resolution test:** Provide a justified sample size, randomized allocation, blinded outcome measurement, longitudinal analysis with uncertainty, target verification and relevant mechanistic outcomes, with independent replication; otherwise present the result as preliminary.

### Technical failings that need to be addressed before the case is established

The case requires a patient-aware and multiplicity-controlled single-cell analysis (R1-M1), leakage-free model development with credible validation (R1-M2), a coherent and supportable survival-performance estimate (R1-M3), perturbation-specific and immune-relevant causal evidence (R1-M4), a design that actually tests anti-PD-1 sensitization (R1-M5), and bias-controlled in vivo replication (R1-M6).

### Assessment against Nature-style criteria

- **Originality:** A validated connection between an HCC tumour-cell state, treatment response and a tractable driver could be original, but originality is not technically demonstrated by the present discovery and validation chain.
- **Scientific importance:** The clinical and mechanistic questions are important; the visible evidence supports an exploratory signal, not the asserted universal therapeutic vulnerability.
- **Interdisciplinary readership:** The topic could interest cancer biology, immunology, genomics and biomarker audiences, but the present implications remain field-local and preliminary.
- **Technical soundness:** The principal claims are not established for the reasons detailed above.
- **Readability for nonspecialists:** The overall narrative is easy to follow, but it does not explain the distinctions between association and causation, prognostic and treatment-predictive performance, or internal splitting and independent validation.

### Recommendation posture

Currently not established from the provided evidence. A substantially redesigned validation and mechanistic evidence package would be needed before the central claims could be supported; this is a reviewer assessment, not a final editorial judgment.

## Reviewer 2

**Emphasis:** Originality and scientific importance.

### Overall assessment

The proposed advance is framed as both a universal mechanism and an immediately deployable clinical tool. Those are potentially far-reaching claims, but the manuscript does not distinguish the score convincingly from prior immune signatures, does not test treatment benefit in patients, and does not validate the score outside the dataset used to construct it. The experiments suggest hypotheses about EVA1 and tumour growth, but they do not yet supply the mechanistic novelty or therapeutic effect needed to support the stated level of significance.

### Who would be interested in the results, and why

The immediate audience includes HCC researchers, biomarker developers and investigators of cancer immune evasion. A broadly validated predictor of immunotherapy benefit or a causal, targetable immune-evasion mechanism could also interest translational oncology, immunology and precision-medicine readers. The present study has not yet demonstrated those wider implications.

### Major strengths

- The manuscript aims to connect an observational molecular signature to an experimentally tractable candidate rather than stopping at a prognostic association.
- It considers clinically relevant covariates and reports both molecular and in vivo observations.
- The question of whether tumour-cell programmes influence immune treatment response has potentially broad conceptual relevance.

### Major concerns

**R2-M1 — [novelty-significance; issue key: novelty-positioning-unsupported]**  
**Claim pointer:** This is the first clinically actionable HCC immune score, and no previous immune signature provides a universal, mechanistically validated guide to immunotherapy selection.  
**Evidence pointer:** Introduction (lines 30–41); References note (lines 191–194).  
**Concern:** The manuscript provides only two references and does not compare the score, its constituent genes, the EVA1 hypothesis or its performance with prior immune signatures. The manuscript itself states that reference 1 is used to support the absence of previous clinical utility, but no evidence in the supplied text establishes that broad literature claim. Originality relative to prior work is therefore not assessable from the provided material.  
**Resolution test:** Supply a balanced, directly relevant account of prior HCC immune signatures and EVA1-related work, define the precise new conceptual and technical contribution, and temper “first” and “none” claims unless supported by an adequate literature comparison.

**R2-M2 — [clinical-validity; issue key: prognostic-to-treatment-predictive-mismatch]**  
**Claim pointer:** The score can be used at diagnosis to select anti-PD-1 therapy and is immediately deployable.  
**Evidence pointer:** Abstract (lines 10–18); “Impact and implications” (lines 20–26); study population (lines 47–57); Discussion (lines 139–149).  
**Concern:** The clinical cohort consists of patients undergoing resection, and the reported endpoint is overall survival. The manuscript does not report a cohort treated with anti-PD-1, a treatment-by-score interaction, or response endpoints. A prognostic survival association cannot establish that the score predicts benefit from anti-PD-1 or can select therapy.  
**Resolution test:** Evaluate a prespecified locked score in an appropriate treated cohort with a design and comparator that can distinguish treatment-predictive from prognostic value, and demonstrate analytical and clinical validity and utility. Otherwise remove therapy-selection and deployment claims.

**R2-M3 — [statistical-rigor; issue key: model-development-validation-leakage]**  
**Claim pointer:** Independent subset validation overcomes limitations of earlier single-centre signatures.  
**Evidence pointer:** “Score construction and validation” (lines 69–81); Discussion (lines 139–143).  
**Concern:** The full cohort determined feature inclusion, model structure, cutoffs, coefficient signs and missing-value rules before splitting. Consequently, the validation subset is neither independent nor untouched, and it cannot demonstrate transportability beyond this single centre. This directly undermines the claimed advance over previous signatures.  
**Resolution test:** Establish performance for a fully locked model in data entirely external to development and report discrimination, calibration, clinical baselines and uncertainty.

**R2-M4 — [clinical-validity; issue key: universal-generalizability-unsupported]**  
**Claim pointer:** The score and EVA1 strategy apply across all major HCC aetiologies and treatment settings.  
**Evidence pointer:** “Impact and implications” (lines 20–26); study population (lines 47–51); Discussion (lines 151–154).  
**Concern:** The cohort is single-centre, predominantly viral-hepatitis associated (58 of 72), with only nine metabolic-disease cases and five other or undocumented cases. No aetiology-specific performance, interaction, transportability assessment or external cohort is reported. The two cell lines and one xenograft experiment do not establish clinical generality.  
**Resolution test:** Validate the locked claims in sufficiently represented, independently sampled aetiological and treatment strata, quantify heterogeneity and uncertainty, and narrow “universal” language to the populations actually studied unless generality is demonstrated.

**R2-M5 — [mechanism-evidence; issue key: eva1-perturbation-specificity]**  
**Claim pointer:** EVA1 is the causal link between the score and immune escape.  
**Evidence pointer:** Functional methods (lines 83–89); Results (lines 125–135); Discussion (lines 145–149).  
**Concern:** The single-guide tumour-cell perturbation provides no specificity rescue and no direct immune-cell assay, while the mouse comparison does not measure immune infiltration or establish that EVA1 mediates the five-gene score. Concordance among correlation, growth, transcript and tumour-volume observations does not by itself demonstrate the asserted causal chain.  
**Resolution test:** Establish perturbation specificity, link EVA1 experimentally to the score-defined state, and demonstrate an immune-mediated phenotype with discriminating controls; otherwise describe EVA1 as a candidate associated with the observed programme.

**R2-M6 — [novelty-significance; issue key: far-reaching-impact-not-demonstrated]**  
**Claim pointer:** The work provides an immediately deployable biomarker and a treatment strategy with immediate and far-reaching implications.  
**Evidence pointer:** Abstract (lines 16–18); “Impact and implications” (lines 20–26); Discussion (lines 139–154).  
**Concern:** The manuscript supplies neither independent clinical validation nor evidence of treatment selection, analytical assay readiness, prospective utility or a validated therapeutic effect. The importance currently demonstrated is an exploratory single-centre association plus preliminary perturbation observations, which is narrower than the impact claimed.  
**Resolution test:** Either provide a validation and intervention package commensurate with the broad translational claims or reframe the work as hypothesis-generating and articulate the narrower contribution without deployment language.

### Technical failings that need to be addressed before the case is established

The significance claim depends on evidence-based novelty positioning (R2-M1), direct clinical support for treatment prediction (R2-M2), genuinely independent validation (R2-M3), demonstrated rather than asserted generalizability (R2-M4), and a specific causal chain linking EVA1 to immune escape (R2-M5). Without these, the far-reaching-impact claim in R2-M6 is not supported.

### Assessment against Nature-style criteria

- **Originality:** Potentially interesting, but the distinction from prior immune signatures and prior EVA1 knowledge is not assessable from the sparse literature positioning.
- **Scientific importance:** The question is important, but outstanding importance and immediate impact are asserted beyond the visible evidence.
- **Interdisciplinary readership:** A predictive immunotherapy biomarker or general immune-evasion mechanism could attract broad readership; an internally derived prognostic score with preliminary perturbation data is more specialist.
- **Technical soundness:** Model leakage, endpoint mismatch and insufficient causal evidence prevent the main case from being established.
- **Readability for nonspecialists:** The prose is generally direct, but labels such as “validation,” “actionable,” “causal” and “universal” are used without explaining the evidentiary thresholds those terms imply.

### Recommendation posture

Promising question, but the originality, significance and broad-interest case is currently not established from the provided evidence. The final judgment of journal fit belongs to editors.

## Reviewer 3

**Emphasis:** Interdisciplinary readership and readability for nonspecialists.

### Overall assessment

The manuscript has a simple, potentially accessible arc: discover a tumour-cell state, associate it with outcome, perturb a candidate, and test it in vivo. For a broad readership, however, that arc currently compresses several non-equivalent inferences. Association is presented as immune exclusion, prognostic modelling as treatment selection, an internally reused subset as independent validation, and reduced tumour growth as sensitization. The resulting narrative is readable at the sentence level but not reliable at the conceptual level.

### Who would be interested in the results, and why

Cancer biologists and HCC biomarker researchers would recognize the immediate question. Immunologists, quantitative biologists and clinicians could also be interested if the study clearly demonstrated how a tumour-cell state controls immune response and changes therapeutic benefit. At present, the work does not yet provide enough mechanism or clinical validation to make that broader conclusion secure.

### Major strengths

- The manuscript states its central hypothesis plainly and maintains a recognizable discovery-to-translation narrative.
- Sample counts, major exclusions and several missing controls are disclosed in the methods, allowing readers to identify important limitations.
- The multimodal intent could support a clear nonspecialist explanation if the evidentiary transitions were made explicit.

### Major concerns

**R3-M1 — [claim-moderation; issue key: narrative-inference-overreach]**  
**Claim pointer:** The combined observations establish a universal immune-evasion mechanism, a clinically actionable predictor and a therapy ready for development.  
**Evidence pointer:** Title (line 1); Abstract (lines 6–18); “Impact and implications” (lines 20–26); Discussion (lines 137–154).  
**Concern:** The headline and summary sections present the strongest interpretation without communicating that the underlying evidence is retrospective, single-centre, internally reused for model development, correlative at discovery and preliminary in perturbation. This obscures the actual level of support for readers outside the immediate field.  
**Resolution test:** Align the title, abstract, impact statement and discussion with the study design; distinguish exploratory association, prognostic performance, causal mechanism and therapeutic prediction; and reserve “universal,” “actionable,” “causal” and “ready” for evidence that directly tests those propositions.

**R3-M2 — [writing-clarity; issue key: three-year-performance-not-established]**  
**Claim pointer:** The manuscript reports a high AUC for validation-set three-year mortality.  
**Evidence pointer:** Abstract (lines 10–18); Results (lines 118–123); Figure 3 legend (lines 177–178).  
**Concern:** Three different AUC values (0.91, 0.84 and 0.86) are reported for what appears to be the headline performance result, while the text acknowledges incomplete three-year status. A broad reader cannot determine which estimate is intended, how it was obtained or what it means under censoring.  
**Resolution test:** Reconcile the numerical result across all sections and the figure, define the endpoint and censoring analysis in accessible language, and display uncertainty and follow-up support.

**R3-M3 — [clinical-validity; issue key: prognostic-to-treatment-predictive-mismatch]**  
**Claim pointer:** A diagnosis-time score can select anti-PD-1 therapy.  
**Evidence pointer:** “Impact and implications” (lines 20–26); study population and available variables (lines 47–57); Discussion (lines 139–149).  
**Concern:** The manuscript does not explain to nonspecialist readers that an overall-survival association after resection is not evidence that a patient will benefit from anti-PD-1. No anti-PD-1-treated clinical cohort or treatment interaction is presented. This missing distinction is both a technical and communication failure central to the claimed broad impact.  
**Resolution test:** Provide treatment-predictive clinical evidence or explicitly state that the score is presently prognostic and cannot be used to select anti-PD-1.

**R3-M4 — [reproducibility; issue key: data-code-model-unavailable]**  
**Claim pointer:** The five-gene score is deployable and the analyses can support independent scrutiny.  
**Evidence pointer:** “Score construction and validation” (lines 69–81); “Data and code availability” (lines 156–161).  
**Concern:** Coefficient values, model code, final patient-level data, raw single-cell data, random seeds and software versions are unavailable. Even the proposed score cannot be independently calculated from the supplied reporting. This sharply limits scrutiny, replication and any claim of deployment readiness.  
**Resolution test:** Provide the complete locked formula and preprocessing rules, sufficiently detailed methods, code and versions, and access to data at a level consistent with ethical constraints; state any justified access restrictions transparently.

**R3-M5 — [ethical-governance; issue key: ethics-reporting-incomplete]**  
**Claim pointer:** Human and animal work complied with institutional requirements.  
**Evidence pointer:** Ethics (lines 163–167).  
**Concern:** The approving committee, protocol number, consent procedure, animal protocol and humane endpoints are not reported. The supplied statement is insufficient for readers to verify governance of the human and animal work.  
**Resolution test:** Report the relevant approving bodies and identifiers, consent or waiver basis, animal approval and humane endpoints, or explicitly identify information that cannot be supplied and why.

**R3-M6 — [writing-clarity; issue key: causal-chain-not-explained]**  
**Claim pointer:** Correlation with a T-cell score, altered tumour-cell measurements and smaller xenografts together show that EVA1 directly controls antitumour immunity.  
**Evidence pointer:** Results (lines 109–135); Discussion (lines 145–149).  
**Concern:** The manuscript does not provide a clear explanation of which observation supports each link in the proposed chain or what alternative interpretations remain. The cell cultures do not contain an immune-cell assay, and the mouse experiment reports no immune measurements. For nonspecialists, “concordance across data types” substitutes for a demonstrated mechanistic bridge.  
**Resolution test:** Map each mechanistic claim to a direct test, report immune-relevant evidence where claimed, and explain remaining alternatives; otherwise use language limited to association and candidate function.

### Technical failings that need to be addressed before the case is established

The broad-reader case requires claim calibration across the title and summaries (R3-M1), one coherent and interpretable performance result (R3-M2), a correct separation of prognostic and treatment-predictive evidence (R3-M3), reproducible reporting (R3-M4), complete governance information (R3-M5), and an explicit evidence chain for the mechanistic conclusion (R3-M6).

### Assessment against Nature-style criteria

- **Originality:** The manuscript states an original universal mechanism and first actionable score, but the supplied literature context is insufficient to let a broad reader verify those distinctions.
- **Scientific importance:** The problem is important; the demonstrated result is narrower than the claimed immediate therapeutic and clinical impact.
- **Interdisciplinary readership:** The question could cross oncology, immunology, genomics and quantitative medicine, but the present conclusions depend on distinctions that the manuscript blurs.
- **Technical soundness:** Contradictory performance reporting, absence of treatment-predictive evidence, lack of reproducibility materials and incomplete mechanistic linkage weaken the case.
- **Readability for nonspecialists:** Sentence-level readability is good. Conceptual readability is poor because key technical terms and inference transitions are not explained accurately.

### Recommendation posture

Potentially interesting to several communities, but the broad-interest conclusion and its evidentiary basis are currently underdeveloped. This assessment does not determine the editor’s decision.

## Cross-review synthesis

### Consensus strengths

- All three reports recognize an important question at the intersection of HCC biology, tumour immunity, prognostic modelling and therapeutic response.
- All three view the attempt to combine single-cell discovery, a patient cohort and perturbation experiments as potentially useful in principle.
- The manuscript’s explicit disclosure of many design limitations is a positive foundation for a more evidence-calibrated presentation.

### Consensus technical risks

- **Model-development/validation leakage:** Reviewers 1 and 2 agree that whole-cohort model selection before the split makes the “validation” subset non-independent and renders performance optimistic.
- **Three-year performance is not established:** Reviewers 1 and 3 agree that immature follow-up, an undefined censoring approach and mutually inconsistent AUC values prevent evaluation of the headline endpoint.
- **Prognostic evidence is presented as treatment-predictive evidence:** Reviewers 2 and 3 agree that overall survival in a resection cohort cannot support anti-PD-1 selection without treated-cohort and interaction evidence.
- **EVA1 causality is not established:** Reviewers 1 and 2 agree that a one-guide perturbation without rescue or an immune-relevant assay does not establish EVA1 as the causal driver of immune escape.

### Where emphasis differs across reviewers

- Reviewer 1 places greatest weight on discovery pseudoreplication, multiplicity, perturbation specificity, the missing anti-PD-1 interaction design and mouse-study bias.
- Reviewer 2 places greatest weight on unsupported novelty positioning, absence of evidence for universality and the gap between exploratory evidence and the asserted far-reaching importance.
- Reviewer 3 places greatest weight on conceptual readability, unreproducible score reporting, ethics/governance omissions and the way the abstract and discussion obscure inferential boundaries.

Pairwise concern overlap is limited to the genuinely shared issues above; the remaining concerns reflect different weighting of the same supplied fact base rather than different reviewer identities or invented evidence.

### Broad-interest / significance readout

A robust demonstration that an HCC tumour-cell programme causally controls immune escape and predicts benefit from immunotherapy could have interdisciplinary interest and substantial scientific importance. The supplied manuscript demonstrates neither element at that level. It currently supports an exploratory association between a candidate programme and survival plus preliminary EVA1 perturbation phenotypes. Whether the work is sufficiently broad for Nature is an editorial judgment; these reports identify the technical and significance gaps that presently limit that case.

### Most important issues to resolve before a strong Nature-style case is established

1. Rebuild and evaluate the score without information leakage, then validate the locked model externally with appropriate clinical comparators, calibration, uncertainty and mature follow-up.
2. Test the treatment-predictive claim in data capable of distinguishing prognosis from anti-PD-1 benefit.
3. Reanalyse single-cell discovery using patient-level replication and multiplicity control.
4. Establish EVA1 perturbation specificity and directly test the immune mechanism and the EVA1-by-anti-PD-1 interaction.
5. Moderate universal, causal, actionable and development-ready language unless direct evidence closes these gaps.
6. Make the analysis reproducible and complete human/animal governance reporting.

## Risk / unsupported claims

- **Unsupported novelty:** “First clinically actionable” and “none [of the prior signatures]” are not established by the two-reference context (R2-M1). **Not assessable from provided material** without adequate prior-work comparison.
- **Unsupported clinical actionability:** Immediate deployment and anti-PD-1 selection are not supported by the retrospective overall-survival cohort (R2-M2; R3-M3).
- **Unsupported universality:** Application across all aetiologies and treatment settings is not supported by the single-centre, predominantly viral cohort or the limited experimental models (R2-M4).
- **Unsupported causality:** T-cell exclusion, direct suppression of antitumour immunity and EVA1 as the causal driver exceed the correlative and one-guide evidence (R1-M1; R1-M4; R2-M5; R3-M6).
- **Unsupported therapeutic sensitization:** Because every mouse received anti-PD-1, the experiment does not test sensitization (R1-M5).
- **Unsupported performance:** The three-year AUC is internally inconsistent and its validity under incomplete follow-up is not established (R1-M3; R3-M2).
- **Missing validation and comparisons:** No genuinely independent cohort, assay validation, calibration, decision-curve analysis or comparison with BCLC/other clinical baselines is reported.
- **Missing reproducibility and governance:** Essential model, data, code, software and ethics details are absent (R3-M4; R3-M5).
- **Figures not assessable:** Only figure legends were supplied. Visual encodings, denominators, uncertainty displays and agreement between plotted data and text are **not assessable from provided material**.
