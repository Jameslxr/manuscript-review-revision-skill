# Review setup

- **Input scope:** Full synthetic manuscript presented as a Nature Article at initial submission, including Abstract, Impact and implications, Introduction, Patients and methods, Results, Discussion, data/code availability, ethics statement, figure legends, and references. No underlying figures, tables, patient-level data, code, protocols, or supplementary information were supplied.
- **Assessment boundary:** This is a reviewer-style assessment of the supplied text only. The review does not independently verify the cited literature, recompute analyses, inspect raw data, or infer experiments and controls that are not reported.
- **Shared manuscript claim summary:** The manuscript claims that a five-gene score derived through single-cell discovery predicts HCC mortality, is ready to guide anti-PD-1 selection, and that EVA1 is a causal, universal immune-evasion driver and therapeutic vulnerability across HCC.
- **Visible evidence base:** Single-cell RNA sequencing of tumour and adjacent tissue from eight patients; a retrospective, single-centre resection cohort of 72 patients with 31 deaths; score construction and random 70:30 splitting within that cohort; one-guide EVA1 depletion in two HCC cell lines; and a single, unblinded, cage-ordered, two-group xenograft experiment with five mice per group, in which all mice received anti-PD-1.
- **Missing materials affecting confidence:** Raw single-cell data, patient-level clinical data, model coefficients and code, time-dependent performance methods, complete multivariable model output, confidence intervals, calibration, clinical comparator analyses, independent validation, underlying figures, replicate-level experimental data, protocol details, and complete human and animal ethics information.

# Reviewer 1

*Emphasis: technical validity and technical failings.*

## Overall assessment

The manuscript attempts an ambitious progression from single-cell discovery to prognostic modelling and experimental perturbation. The multimodal structure is potentially valuable, and the authors disclose several important limitations. However, the central predictive and mechanistic conclusions are not technically established by the analyses described. The score-development procedure contains information leakage and severe overfitting risk; the single-cell analysis treats cells as independent biological replicates; and neither the cell-line nor mouse design identifies EVA1 as a causal immune-evasion mechanism or demonstrates sensitization to anti-PD-1.

## Who would be interested in the results, and why

If validated, the work could interest researchers studying tumour immune states, HCC heterogeneity, translational biomarkers, and therapeutic target discovery because it tries to connect tumour-cell transcriptional state with clinical outcome and perturbational evidence. The present evidence is more likely to interest the immediate HCC biomarker field than a broad interdisciplinary readership because the claimed clinical and mechanistic advance remains unverified.

## Major strengths

- The manuscript integrates patient-derived single-cell observations, clinical outcomes, cell-line perturbation, and an in vivo experiment around a common hypothesis.
- The Methods state several design limitations directly, including lack of multiplicity correction, reuse of the full clinical dataset, missing external validation, use of one guide RNA, absence of rescue, small mouse groups, non-random allocation, lack of blinding, and incomplete data/code deposition.
- The AUC discrepancy is visible in the text and legends rather than concealed, making the reporting problem identifiable.

## Major concerns

### R1-M1 — [clinical-validity]

- **Claim pointer:** The five-gene score was independently validated and is a clinically actionable mortality predictor.
- **Evidence pointer:** Patients and methods, “Score construction and validation”; Discussion, first paragraph.
- **Concern:** The 27 candidate genes, five retained genes, expression cutoffs, coefficient signs, and missing-value rules were all selected using the complete 72-patient dataset before that same dataset was divided into training and validation subsets. The nominal validation subset is therefore not independent of model development. With 31 deaths and 45 clinical and molecular candidate covariates described before stepwise selection, optimism and model instability are major risks. The reported split does not establish out-of-sample validity.
- **Resolution test:** Rebuild the complete pipeline inside resampling or a genuinely development-only cohort, keep all feature selection and preprocessing within each training fold, quantify optimism and uncertainty, and confirm the locked model in an external cohort using a prespecified assay and analysis plan. Until then, describe the result as exploratory model development rather than independent validation.

### R1-M2 — [experimental-design]

- **Claim pointer:** Single-cell analysis identified an immune-evasion programme and EVA1 as a tumour-level correlate of low T-cell infiltration.
- **Evidence pointer:** Patients and methods, “Single-cell discovery”; Results, “Single-cell discovery identifies an immune-evasion programme”; Figures 1 and 2 legends.
- **Concern:** Differential expression was performed at the cell level across cells originating from only eight patients, while treating cells as independent observations. This does not preserve the patient as the biological replication unit. Testing 1,842 nominally significant genes without multiple-testing correction further inflates discovery risk. The inverse EVA1–T-cell-score correlation is reported across eight tumours and cannot by itself show T-cell exclusion.
- **Resolution test:** Reanalyse discovery at the patient/sample level using a method that accounts for within-patient dependence, apply an appropriate multiple-testing procedure, show the robustness of EVA1 prioritization across patients, and describe the correlation as associative unless additional discriminating evidence supports exclusion.

### R1-M3 — [mechanism-evidence]

- **Claim pointer:** EVA1 is the causal driver of immune escape and directly suppresses anti-tumour immunity.
- **Evidence pointer:** Patients and methods, “Functional experiments”; Results, “EVA1 perturbation supports a therapeutic mechanism”; Abstract.
- **Concern:** A single CRISPR guide, without a second independent guide, rescue, or direct target-engagement check, cannot exclude guide-specific or editing-related effects. Reduced growth, altered PD-L1 abundance, and changes in three interferon-response transcripts in tumour-cell monoculture are compatible with several explanations and do not directly measure immune-cell function or immune escape.
- **Resolution test:** Establish perturbation specificity with independent guides and rescue, document target engagement, and use experiments that directly measure the proposed tumour–immune interaction. If these data are not supplied, narrow the conclusion to an association between EVA1 perturbation and tumour-cell growth/signalling phenotypes.

### R1-M4 — [experimental-design]

- **Claim pointer:** EVA1 depletion sensitizes HCC xenografts to anti-PD-1 treatment.
- **Evidence pointer:** Patients and methods, “Mouse experiment”; Results, “EVA1 perturbation supports a therapeutic mechanism”; Figure 4 legend.
- **Concern:** All mice received anti-PD-1, so the two-group experiment estimates the effect of EVA1 depletion under one treatment condition; it cannot test whether EVA1 status modifies the effect of anti-PD-1. Cage-ordered allocation, unblinded measurement, five animals per group, a single day-21 comparison, and no independent replication increase bias and uncertainty. The experiment also did not measure immune infiltration, survival, toxicity, or post-implantation EVA1 expression.
- **Resolution test:** Use an adequately justified factorial design including EVA1 status and anti-PD-1 exposure, prespecify the interaction test and longitudinal analysis, randomize and blind allocation/measurement, verify EVA1 status, measure relevant immune endpoints, and replicate the experiment. Without this evidence, remove the sensitization claim.

### R1-M5 — [statistical-rigor]

- **Claim pointer:** The score has high 3-year mortality discrimination and remains independently associated with overall survival.
- **Evidence pointer:** Patients and methods, “Statistical analysis”; Results, “The five-gene score predicts survival”; Abstract; Figure 3 legend.
- **Concern:** The 3-year AUC is reported as 0.84 in Results, 0.86 in Figure 3, and 0.91 in the Abstract. Median follow-up among survivors was 18 months, leaving 3-year status unavailable for many patients, but the handling of censoring in the AUC is not reported. The proportional-hazards assumption was not checked, hazard ratios lack confidence intervals, multiplicity is not controlled, and per-analysis exclusion of missing records leaves changing denominators unreported.
- **Resolution test:** Reconcile all performance values against one frozen analysis, state the time-dependent ROC method and censoring assumptions, report uncertainty and numbers at risk, test model assumptions, document missingness and analysis denominators, and provide confidence intervals and multiplicity handling appropriate to each inferential family.

### R1-M6 — [reproducibility]

- **Claim pointer:** The reported score and experimental evidence can support independent scrutiny and eventual clinical use.
- **Evidence pointer:** “Data and code availability”; Patients and methods.
- **Concern:** Raw single-cell data, patient-level analysis data, model code, coefficients, seeds, and software versions are unavailable. The five-gene formula therefore cannot be independently reproduced or even applied from the manuscript as supplied.
- **Resolution test:** Deposit de-identified data to the extent ethically permissible, raw/processed single-cell data, complete model coefficients and preprocessing rules, executable analysis code, software versions, and experimental protocols, with controlled-access procedures where required.

## Technical failings that need to be addressed before the case is established

The indispensable technical issues are the non-independent model validation, patient-level replication failure in the single-cell analysis, lack of perturbation-specific mechanistic evidence, absence of an anti-PD-1 interaction design, unresolved survival-performance reporting, and inability to reproduce the score. These are not presentation-only issues; they affect the main predictive and causal conclusions.

## Assessment against Nature-style criteria

- **Originality:** The cross-modal concept may be original, but originality is not established because the manuscript does not adequately distinguish this score or EVA1 mechanism from prior work.
- **Scientific importance:** A validated treatment-selection biomarker and immune-evasion target in HCC would be important. The described evidence currently supports an exploratory signature and perturbation phenotype, not the claimed clinical or therapeutic advance.
- **Interdisciplinary readership:** The topic could reach cancer biology, immunology, genomics, and clinical-methods audiences, but the current conclusions remain too technically insecure to sustain that reach.
- **Technical soundness:** The main case is not established for the reasons above.
- **Readability for nonspecialists:** The manuscript is structurally clear, but categorical causal and clinical language obscures the actual distinction among association, prognosis, prediction, and treatment-effect modification.

## Recommendation posture

Currently not established from the provided evidence. A substantially redesigned and independently validated evidentiary package would be needed before the principal claims could support a strong Nature-style case.

# Reviewer 2

*Emphasis: originality and scientific importance.*

## Overall assessment

The manuscript targets a significant problem and presents a seemingly compelling narrative: single-cell discovery yields a compact score and a tractable target with therapeutic implications. Yet the breadth of the headline claim is generated chiefly by extrapolation. The study is a small, retrospective, single-centre prognostic analysis in resected HCC, supplemented by limited perturbation experiments. It does not show that the score predicts benefit from anti-PD-1, works across HCC aetiologies and settings, is ready for deployment, or represents a clearly distinguished advance over prior signatures.

## Who would be interested in the results, and why

HCC biomarker investigators and tumour-immunology researchers may find EVA1 and the five-gene score useful as hypotheses for further study. Clinicians and broader precision-oncology readers would be interested only if the score added reproducible value over established clinical factors and predicted treatment benefit in the intended-use population.

## Major strengths

- The manuscript asks a clinically relevant question and links molecular discovery to a proposed use case.
- The five-gene endpoint is potentially more deployable than an unwieldy transcriptomic signature if its assay, coefficients, and validity can be established.
- The study exposes enough of its design limitations to permit a clear evaluation of where the significance claim fails.

## Major concerns

### R2-M1 — [clinical-validity]

- **Claim pointer:** Random splitting produced an independent validation that overcomes limitations of earlier single-centre signatures.
- **Evidence pointer:** Patients and methods, “Score construction and validation”; Discussion, first paragraph.
- **Concern:** This is the same underlying model-leakage problem identified in R1-M1. Model and preprocessing choices were fixed using all 72 patients before the split, so the held-out subset was already used in discovery. The manuscript cannot use this split to claim independent validation or superiority over earlier single-centre signatures.
- **Resolution test:** Provide truly independent validation of a completely locked model and assay, or recast the current cohort as development-only and remove claims of independent validation.

### R2-M2 — [clinical-validity]

- **Claim pointer:** The five-gene score can be used at diagnosis to select anti-PD-1 therapy.
- **Evidence pointer:** “Impact and implications”; Discussion, first paragraph; References note concerning reference 2.
- **Concern:** The clinical analysis uses overall survival after resection. The supplied text does not report that cohort members received anti-PD-1 under a design capable of estimating treatment benefit, nor does it compare treated and untreated outcomes or test a score-by-treatment interaction. Prognostic discrimination is not evidence that the score is predictive of anti-PD-1 benefit. The cited anti-PD-L1/bevacizumab trial, as identified in the manuscript, does not by itself validate this five-gene score or anti-PD-1 monotherapy selection.
- **Resolution test:** Define the intended clinical context and demonstrate treatment-effect prediction in an appropriate, independent immunotherapy-treated population with a comparator and prespecified interaction analysis. Otherwise restrict the claim to exploratory prognostic association.

### R2-M3 — [claim-moderation]

- **Claim pointer:** The score and EVA1 vulnerability are universally applicable across all major HCC aetiologies and treatment settings.
- **Evidence pointer:** Abstract; “Impact and implications”; Study population; Discussion, second and third paragraphs.
- **Concern:** The cohort is from one centre, contains 58 of 72 patients with viral hepatitis and only nine with metabolic liver disease, and has five with other or undocumented aetiologies. The single-cell discovery uses eight patients; the experiments use two cell lines and one subcutaneous model. These data do not establish universality across aetiology, disease stage, geography, assay platform, or treatment setting.
- **Resolution test:** Replace universal language with a population-bounded claim and test prespecified transportability across sufficiently powered, independent aetiological and clinical strata before making general claims.

### R2-M4 — [novelty-significance]

- **Claim pointer:** This is the first clinically actionable HCC immune score derived from single-cell data, and no prior immune signature provides a universal mechanistically validated guide.
- **Evidence pointer:** Introduction, first and third paragraphs; References and accompanying citation note.
- **Concern:** The manuscript supplies only two references and assigns the sweeping prior-signature claim to a broad HCC genomic characterization paper. From the provided material, neither priority nor the asserted distinction from prior immune signatures is established. No external literature verification was performed for this review.
- **Resolution test:** Provide a current, focused comparison with the closest single-cell, immune-signature, prognostic, and treatment-selection studies; state the exact incremental conceptual and empirical advance; and moderate priority language if the distinction cannot be documented.

### R2-M5 — [clinical-validity]

- **Claim pointer:** The score is immediately deployable and clinically actionable.
- **Evidence pointer:** Abstract; “Impact and implications”; Patients and methods, “Score construction and validation”; Data and code availability.
- **Concern:** The study lacks external validation, a locked accessible formula, an independent assay, comparison with BCLC stage or other clinical baselines, calibration, decision-curve analysis, and a demonstrated treatment-selection effect. Discrimination alone—even if correctly estimated—does not establish clinical utility or deployability.
- **Resolution test:** Specify the intended-use population and decision, lock and disclose the assay/model, compare it with current clinical standards, validate calibration and discrimination externally, and quantify whether model-guided decisions improve clinically relevant outcomes.

### R2-M6 — [scientific importance / significance]

- **Claim pointer:** Concordance across data types establishes a general immune-evasion mechanism and a treatment strategy ready for therapeutic development.
- **Evidence pointer:** Results, “EVA1 perturbation supports a therapeutic mechanism”; Discussion, second paragraph.
- **Concern:** The single-cell association, tumour-cell growth phenotype, molecular marker changes, and one two-group mouse result are mutually compatible with the hypothesis but do not form independent proof of a universal immune mechanism. Their apparent concordance does not compensate for the non-discriminating designs. Consequently, the broad scientific importance is asserted rather than demonstrated.
- **Resolution test:** Establish a coherent, discriminating mechanistic chain from EVA1 perturbation through immune-cell behaviour to treatment response, with perturbation specificity and replication, or narrow the paper’s significance claim to nomination of an exploratory candidate.

## Technical failings that need to be addressed before the case is established

The manuscript must separate prognostic association from treatment-response prediction, replace the contaminated internal split with genuine validation, establish incremental value and clinical utility, substantiate novelty against the closest work, and bound claims to the populations and models actually studied. Without those elements, the most consequential translational statements are unsupported.

## Assessment against Nature-style criteria

- **Originality:** Potentially interesting, but not assessable with confidence from the sparse and poorly matched prior-work framing.
- **Scientific importance:** The problem is important; the demonstrated advance is presently narrower than the title, Abstract, and Discussion suggest.
- **Interdisciplinary readership:** A robust link among single-cell state, clinical treatment benefit, and causal immune mechanism could have broad reach. The current study does not yet establish that link.
- **Technical soundness:** Model development, validation, and experimental design do not support the principal translational inferences.
- **Readability for nonspecialists:** The prose is direct, but it repeatedly uses “predictor,” “actionable,” “causal,” and “universal” without explaining the distinct evidentiary requirements behind those terms.

## Recommendation posture

Promising as hypothesis-generating work, but the originality, broad importance, and clinical-actionability case remains underdeveloped and is not established by the supplied evidence.

# Reviewer 3

*Emphasis: interdisciplinary readership and readability for nonspecialists.*

## Overall assessment

The manuscript is concise and its broad aim is easy to recognize. However, a nonspecialist reader is likely to leave with a much stronger impression of validation and causality than the methods justify. The narrative collapses four distinct questions—prognosis, immunotherapy-benefit prediction, tumour-cell mechanism, and therapeutic sensitization—into a single “immune-evasion” story. Internal performance inconsistencies, minimal figure legends, and incomplete ethics reporting further reduce confidence.

## Who would be interested in the results, and why

Cancer genomics, tumour-immunology, biomarker, and HCC audiences could be interested in a transparent demonstration that a single-cell-derived tumour state predicts clinically meaningful treatment response and exposes a causal dependency. For readers outside those specialties, the manuscript would need to explain more clearly what the score predicts, how that differs from choosing therapy, and which experiment directly tests immune escape.

## Major strengths

- The manuscript presents a recognizable through-line from discovery to proposed translation.
- Major sections are short and use generally accessible prose.
- The explicit reporting of several negative design features gives readers an opportunity to understand the assessment boundary.

## Major concerns

### R3-M1 — [figures-and-tables]

- **Claim pointer:** The validation-set 3-year mortality AUC demonstrates high predictive performance.
- **Evidence pointer:** Abstract; Results, “The five-gene score predicts survival”; Figure 3 legend.
- **Concern:** This is the same underlying outcome-reporting issue identified in R1-M5. Three different AUC values—0.91, 0.84, and 0.86—are presented for what appears to be the same endpoint and subset. Because median follow-up among survivors is 18 months, the manuscript also needs to explain how censoring and incomplete 3-year observation were handled. A broad reader cannot determine which result is correct or what population and method each value represents.
- **Resolution test:** Reconcile the values; define the endpoint, analysis set, time origin, censoring method, and uncertainty in the text and figure; and ensure every summary reports the same verified result.

### R3-M2 — [causal-vs-correlative]

- **Claim pointer:** A mortality score measured at diagnosis can select anti-PD-1 therapy.
- **Evidence pointer:** “Impact and implications”; Discussion, first paragraph.
- **Concern:** This is the same prognostic-versus-predictive mismatch identified in R2-M2. The manuscript does not explain that association with survival in a resection cohort is different from evidence that biomarker strata experience different benefit from anti-PD-1. The narrative therefore invites a clinically consequential misinterpretation.
- **Resolution test:** State explicitly whether the intended claim is prognostic or treatment-predictive and align the title, summary, figures, and discussion with the actual design. A treatment-selection statement requires an appropriate comparative treatment-effect analysis.

### R3-M3 — [writing-clarity]

- **Claim pointer:** Associations and perturbation phenotypes together show that EVA1 excludes T cells, directly suppresses immunity, and causally links the score to immune escape.
- **Evidence pointer:** Results, “Single-cell discovery identifies an immune-evasion programme” and “EVA1 perturbation supports a therapeutic mechanism”; Discussion, second paragraph.
- **Concern:** The narrative does not distinguish what each experiment observes. The eight-tumour correlation concerns co-variation; the cell-line experiments concern growth, PD-L1, and transcript levels; and the mouse comparison concerns day-21 tumour volume under anti-PD-1. None directly reports T-cell exclusion or immune-cell function. Presenting them as one causal chain makes the manuscript less—not more—readable because the inferential transitions are hidden.
- **Resolution test:** For each claim, state the observation, the inference it permits, and the remaining alternative explanations. Reserve causal immune language for experiments that directly discriminate the proposed mechanism.

### R3-M4 — [figures-and-tables]

- **Claim pointer:** Figures 1–4 transparently support the single-cell, score, cell-growth, and xenograft conclusions.
- **Evidence pointer:** “Figure legends.”
- **Concern:** The supplied legends do not state key denominators, biological versus technical replication, uncertainty displays, statistical tests, adjustment procedures, or—in Figure 4—which subpanels correspond to cell-line and mouse measurements. Figure 1’s statement that each point represents one cell reinforces the risk that readers mistake cellular observations for independent patient replication. The underlying figures were not supplied, so their visual accuracy is not assessable.
- **Resolution test:** Provide self-contained legends with sample sizes at the correct biological level, replicate definitions, statistical methods, uncertainty measures, and panel-specific descriptions; provide the figures for assessment.

### R3-M5 — [readability for nonspecialists]

- **Claim pointer:** The manuscript communicates why a five-gene score and EVA1 change the field for HCC patients.
- **Evidence pointer:** Abstract; “Impact and implications”; Introduction.
- **Concern:** The clinical context is compressed into statements of need and deployability. The text does not explain the intended decision point after resection, why overall survival is an adequate endpoint for anti-PD-1 selection, how the score would be measured in practice, or why EVA1 is prioritized over the other four genes. The result is superficially simple but conceptually incomplete for interdisciplinary readers.
- **Resolution test:** Add a clear, evidence-bounded account of the intended use, comparator, assay, patient pathway, distinction between prognosis and treatment selection, and rationale for EVA1 prioritization, without claiming that unavailable validation has already been completed.

### R3-M6 — [ethical-governance]

- **Claim pointer:** The human and animal work complied with institutional requirements.
- **Evidence pointer:** “Ethics”; Patients and methods, “Study population” and “Mouse experiment.”
- **Concern:** The approving committee, protocol number, consent procedure, animal protocol, and humane endpoints are not reported. The general compliance statement is not sufficient to assess governance of the patient records, tissue use, or animal work from the supplied manuscript.
- **Resolution test:** Report the responsible committees, approval identifiers, consent or waiver basis, animal protocol, welfare monitoring, humane endpoints, and any relevant data-governance conditions.

## Technical failings that need to be addressed before the case is established

The manuscript needs one consistent, fully defined performance result; a clear separation of prognosis from treatment prediction; claim-by-claim alignment between observation and inference; complete figure reporting; and assessable ethics documentation. These changes would improve readability, but most also require substantive evidence or reanalysis rather than prose alone.

## Assessment against Nature-style criteria

- **Originality:** The integrated framing could be distinctive, but novelty is not established from the supplied prior-work discussion.
- **Scientific importance:** The intended clinical and mechanistic implications are substantial; the demonstrated findings are presently exploratory.
- **Interdisciplinary readership:** The disease problem and tumour–immune question are broadly relevant, but the manuscript’s inferential shortcuts make the take-home message unreliable for readers outside the immediate field.
- **Technical soundness:** Conflicting performance reporting and design–claim mismatches prevent the main case from being established.
- **Readability for nonspecialists:** The prose is concise, yet key concepts and inference boundaries are insufficiently explained. The clarity of the sentences should not be mistaken for clarity of the evidence chain.

## Recommendation posture

The broad-readership case is potentially interesting but currently unreliable because the summary language outruns the study design and key reporting is inconsistent or incomplete.

# Cross-review synthesis

## Consensus strengths

- All three reports recognize the potentially valuable attempt to connect single-cell discovery, clinical outcomes, and perturbational evidence around an important HCC problem.
- The manuscript’s concise organization and unusually explicit disclosure of multiple limitations make the core weaknesses identifiable.
- A validated score with a rigorously demonstrated immune mechanism and treatment-selection role could interest HCC, cancer-genomics, immunology, and precision-oncology readers.

## Consensus technical risks

- **Non-independent score validation (`clinical-model-data-leakage-overfitting`; R1-M1 and R2-M1):** Model and preprocessing choices used all 72 patients before the split, so the validation subset does not provide independent confirmation.
- **Unresolved 3-year performance reporting (`outcome-performance-inconsistency-followup`; R1-M5 and R3-M1):** The AUC differs across the Abstract, Results, and Figure 3, while censoring at a horizon longer than median survivor follow-up is unexplained.
- **Prognostic-versus-predictive mismatch (`prognostic-predictive-mismatch`; R2-M2 and R3-M2):** Overall-survival association in a resection cohort does not establish ability to select patients for anti-PD-1 benefit.

## Where emphasis differs across reviewers

- Reviewer 1 gives greatest weight to patient-level replication, statistical validity, perturbation specificity, and the absence of an experimental test of anti-PD-1 sensitization.
- Reviewer 2 gives greatest weight to unsupported priority, clinical utility, universality, and the gap between a potentially important question and the narrower demonstrated advance.
- Reviewer 3 gives greatest weight to how inconsistent metrics, compressed clinical context, incomplete figure legends, hidden inferential transitions, and missing ethics details affect interdisciplinary comprehension and trust.
- Important single-report issues include single-cell pseudoreplication and multiplicity (R1-M2), lack of perturbation specificity (R1-M3), universality across HCC settings (R2-M3), inadequate prior-work distinction (R2-M4), incomplete figure reporting (R3-M4), and incomplete ethics reporting (R3-M6).

## Broad-interest / significance readout

The manuscript addresses a broadly important disease and a question that could have interdisciplinary reach. The evidence shown, however, supports at most an exploratory single-centre prognostic signature, an EVA1-associated tumour state, and preliminary perturbation phenotypes. It does not yet establish an original, clinically deployable anti-PD-1 selection tool, a universal HCC mechanism, or a therapeutic vulnerability ready for development. Final broad-readership fit remains an editorial judgment; this reviewer package finds that the technical and significance case is not currently established.

## Most important issues to resolve before a strong Nature-style case is established

1. Rebuild and externally validate a fully locked score without information leakage, with transparent code, coefficients, assay specifications, uncertainty, calibration, and comparison to clinical baselines.
2. Test the intended clinical claim directly: distinguish prognosis from treatment-effect prediction and provide appropriate evidence for anti-PD-1 selection.
3. Reanalyse single-cell discovery at the patient level with multiplicity control and demonstrate robustness across patients.
4. Establish EVA1 perturbation specificity and directly test the proposed tumour–immune mechanism.
5. Use a randomized, blinded, adequately justified factorial in vivo design capable of testing EVA1-by-anti-PD-1 interaction, with relevant immune endpoints and independent replication.
6. Reconcile all outcome metrics, moderate universal and causal claims, establish the advance relative to the closest prior work, and complete ethics and reproducibility reporting.

# Risk / unsupported claims

- **“Independent validation”: unsupported.** The full cohort informed model and preprocessing choices before splitting.
- **AUC of 0.91 for 3-year mortality: internally inconsistent and not assessable as reported.** Results and Figure 3 give different values, and censoring methods are absent.
- **“Clinically actionable,” “immediately deployable,” and “ready for clinical deployment”: unsupported.** External validation, accessible formula, assay validation, calibration, baseline comparison, decision analysis, and clinical-utility evidence are missing.
- **Anti-PD-1 treatment selection: unsupported.** The clinical study does not report a design that estimates differential treatment benefit.
- **EVA1 excludes T cells and is the causal driver of immune escape: unsupported.** The visible evidence is correlation plus non-specific perturbation phenotypes without direct immune-function testing.
- **EVA1 sensitizes HCC to anti-PD-1: unsupported.** The mouse experiment lacks a no-anti-PD-1 arm and therefore cannot test treatment-effect modification.
- **Universal applicability across HCC aetiologies and settings: unsupported.** The cohort, single-cell sample, cell lines, and mouse experiment are too narrow to establish transportability.
- **First or uniquely mechanistically validated HCC immune score: not assessable from the supplied references.** A focused prior-work comparison is absent, and no external literature verification was performed.
- **Therapeutic readiness: unsupported.** Specificity, mechanism, efficacy interaction, toxicity, replication, and generalizability have not been established.
- **Research governance: not assessable from the provided material.** Human and animal approval and consent details are incomplete.
- **Figure-level validity: not assessable from the provided material.** Only brief legends, not the underlying figures, were supplied.
