# Nature reviewer versus manuscript-review-revision benchmark

This benchmark compares review behavior, not brand prestige or expected
acceptance. It uses a fully synthetic hepatocellular-carcinoma manuscript so
that no unpublished research, patient information, or private review material
enters the repository.

## Frozen systems

- `nature-reviewer` upstream snapshot:
  `Yuan1z0825/nature-skills@05305ab1a636e7794849181cb97f397b49ed498b`
  (`manifest.yaml` version `1.1.0`)
- `manuscript-review-revision`: repository tag `v1.3.0`

Version 1.3.0 is the frozen baseline. The duplication controls derived from the
comparison are implemented in 1.4.0 and tested in one separate post-optimization
run; the baseline output is not rewritten after optimization.

The locally installed `nature-reviewer` was not used as the primary comparator
because it was an older `0.1.0 Draft`. The upstream snapshot is the fairer
comparison.

## Test design

### Track A: direct head-to-head

Both systems receive:

- the same synthetic full manuscript
- target journal `Nature`
- article type `Article`
- stage `initial submission`
- the same task: review only, do not revise

Run each system twice in fresh contexts. Do not show either system the answer
key, the other system's output, or the expected winner.

### Track B: journal-adaptation stress test

Run `manuscript-review-revision` against `Journal of Hepatology`, Original
Article, using the same manuscript. This track is not scored as a Nature
head-to-head because `nature-reviewer` is intentionally Nature-specific. It
tests whether the journal-aware workflow changes editorial calibration without
lowering scientific-validity standards.

Status: the official Journal of Hepatology profile is frozen as a reusable
fixture, but this iteration completed only the direct Nature head-to-head and
the version-1.4.0 Nature post-optimization run. Track B remains unscored.

## Scoring

Blind the head-to-head outputs as `System A` and `System B`. An independent
evaluator receives only the frozen manuscript, `answer-key.tsv`, the rubric
below, and the blinded outputs.

| Dimension | Points | Rule |
|---|---:|---|
| Ground-truth concern recall | 30 | Weighted detection of answer-key concerns |
| Precision and non-invention | 20 | Penalize unsupported or fabricated defects |
| Claim/evidence traceability | 15 | Stable concern ID plus faithful claim and evidence pointers |
| Resolution-test quality | 10 | Concrete, claim-proportionate closure test |
| Consensus and internal consistency | 10 | No false consensus; no factual drift across reviewers |
| Journal calibration | 10 | Uses the selected journal's actual editorial bar without pretending to be the editor |
| Reproducibility and auditability | 5 | Frozen inputs, distinguishable runs, machine-checkable artifacts |

Total: 100 points.

## Stability comparison

For each system, compare the two replicates using normalized answer-key issue
IDs:

- concern recall difference
- unsupported-concern difference
- overlap of detected answer-key issues
- verdict/posture agreement
- whether severity changes by more than one level

Two runs are a forward-test, not a population estimate. Report observed
variation without claiming a general model-performance statistic.

## Files

- `synthetic-hcc-manuscript.md`: shared manuscript fixture
- `answer-key.tsv`: sealed concern and non-invention rubric
- `nature-journal-profile.json`: frozen official Nature profile
- `joh-journal-profile.json`: frozen official Journal of Hepatology profile
- `runs/`: raw system outputs and selected structured receipts
- `evaluation/`: blinded scoring, revealed summary, and final benchmark report

## Boundaries

- The answer key measures whether a review notices deliberately embedded
  defects. It does not prove that one Skill is universally superior.
- A richer workflow may score higher on auditability while a smaller workflow
  may be faster and easier to read.
- Benchmark artifacts must not be used as reviewer inputs during forward tests.
