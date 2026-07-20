# Benchmark report: Nature reviewer versus manuscript-review-revision

## Question

On the same synthetic hepatocellular-carcinoma manuscript, does
`manuscript-review-revision` provide a more complete, stable, and auditable
scientific review than the current upstream `nature-reviewer`, and what should
be improved after observing both systems?

## Frozen comparison

- Comparator: `nature-reviewer` 1.1.0 from
  `Yuan1z0825/nature-skills@05305ab1a636e7794849181cb97f397b49ed498b`.
- Candidate baseline: `manuscript-review-revision` 1.3.0.
- Target: Nature, Article, initial submission.
- Input: the same fully synthetic manuscript and frozen journal profile.
- Replicates: two fresh runs per system.
- Evaluation: identities hidden as System A and System B until scoring ended.
- Ground truth: 18 deliberately embedded concerns with a total weight of 42.

The locally installed `nature-reviewer` 0.1.0 Draft was not used as the main
comparator because the current upstream 1.1.0 is the fairer benchmark.

## Blinded result

| Revealed system | Run 1 | Run 2 | Mean | Detected issues | Unsupported concerns | Issue Jaccard |
|---|---:|---:|---:|---|---:|---:|
| `manuscript-review-revision` 1.3.0 | 98.000 | 98.000 | **98.000** | 18/18; 18/18 | 0; 0 | 1.000 |
| `nature-reviewer` 1.1.0 | 95.000 | 92.857 | **93.928** | 18/18; 16/18 | 0; 0 | 0.889 |

Nature run 2 missed:

- `G16`: absent hazard-ratio confidence intervals and no
  proportional-hazards assessment;
- `G17`: the cell-level display and incomplete legend denominators obscure the
  patient-level biological unit.

Both systems avoided unsupported allegations in this fixture. Nature produced
leaner final prose. The candidate system scored higher because its concern
ledger, frozen-input receipts, report hashes, consensus rules, explicit
non-assessability boundaries, and executable validators made the review more
auditable and stable.

## Baseline cost and failure mode

| System/run | Reviewer reports | Raw review units | Final units | Concern rows | Normalized issues | Maximum pair overlap |
|---|---:|---:|---:|---:|---:|---:|
| Candidate 1.3.0 run 1 | 7 | 27,200 | 766 | 94 | 25 | 88% |
| Candidate 1.3.0 run 2 | 6 | 21,194 | 490 | 74 | 34 | 80% |
| Nature 1.1.0 run 1 | 3 sections | 4,368 total | included | 18 IDs | 18 | not machine-reported |
| Nature 1.1.0 run 2 | 3 sections | 4,233 total | included | 18 IDs | 18 | not machine-reported |

The candidate's weakness was not missed science. Reviewers repeatedly crossed
role boundaries and reproduced the same whole-manuscript critique. The first
run added both figure/reporting and adversarial seats, creating seven reviewers
when one optional specialist would have been enough. The resulting ledger was
accurate but unnecessarily expensive to generate, synthesize, and read.

## Optimization implemented in 1.4.0

Version 1.4.0 keeps the controls responsible for the higher blinded score and
adds enforceable limits:

1. exactly five core reviewers and at most one risk-triggered specialist;
2. one primary owner for each of the 14 internal review axes;
3. no more than eight prioritized concerns per reviewer;
4. no more than 1,800 word-equivalent units per reviewer;
5. out-of-role ledger entries allowed only as `BLOCKING_CROSSOVER`;
6. one matrix row per normalized issue and a machine-validated author-facing
   verdict capped at 900 word-equivalent units;
7. schema 2.1 validators fail a seventh seat, axis-owner mismatch, non-blocking
   crossover, overlong report, or concern-budget overrun.

These changes target duplication without weakening the minimum of five real,
fresh, independent reviewer tasks.

## Post-optimization forward check

A new fresh-context run evaluated version 1.4.0 on the same frozen manuscript.
The reviewers could not inspect the answer key, baseline outputs, comparator
outputs, prior evaluation, or optimization report. A separate evaluator then
scored only the sealed post-run package.

| Metric | 1.3.0 run 1 | 1.3.0 run 2 | 1.4.0 post-run |
|---|---:|---:|---:|
| Answer-key detection | 18/18 | 18/18 | **18/18** |
| Unsupported concerns | 0 | 0 | **0** |
| Raw review units | 27,200 | 21,194 | **8,379** |
| Concern rows | 94 | 74 | **36** |
| Normalized issues | 25 | 34 | **18** |
| Concern-to-issue ratio | 3.76 | 2.18 | **2.00** |
| Maximum pair overlap | 88% | 80% | **75%** |
| Final verdict units | 766 | 490 | **450** |

The post-run preserved all 42/42 weighted issue units and scored 100/100 under
the same rubric. More important than the scalar score, raw review volume fell
69% versus baseline run 1 and 60% versus run 2 while concern recall remained
complete. All six report budgets and all schema 2.1 validators passed.

The remaining limitation is visible rather than hidden: ten reviewer-pair
overlap warnings remain, with a maximum of 75%. Central causal, actionability,
universality, and treatment-interaction failures were independently raised by
several roles. Future reductions should improve navigation or shorten repeated
explanations; they should not delete independent support merely to optimize the
overlap statistic.

## Interpretation boundary

This is one synthetic manuscript with two baseline replicates per system and
one post-optimization run. It demonstrates behavior on known defects and
supports the specific workflow changes above. The post-run is not a stability
estimate. None of these results proves universal superiority, journal
acceptance, or performance on every discipline, article type, host, or model.

## Reproduce

```bash
python3 benchmarks/nature-vs-mrr-v1/score_runs.py \
  benchmarks/nature-vs-mrr-v1/answer-key.tsv \
  benchmarks/nature-vs-mrr-v1/evaluation/run-scores.tsv
```

Raw outputs are under `runs/baseline/`; the 72-row blinded detection map,
run-level scores, evaluator rationale, and revealed score summary are under
`evaluation/`. The post-optimization artifacts are under
`runs/post-optimization/` and `evaluation/post-v1.4.0/`.
