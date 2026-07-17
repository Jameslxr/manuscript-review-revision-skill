# Fail-closed release gates

## Required statuses

Use only `PASS`, `FAIL`, or `NOT ASSESSABLE` for critical gates. Missing evidence is not a pass.

## Gate table

Report:

| Gate | Status | Evidence inspected | Blocking defects | Required correction |
|---|---|---|---|---|
| release-candidate integrity |  |  |  |  |
| current journal profile |  |  |  |  |
| five-agent independent review |  |  |  |  |
| scientific claims and evidence |  |  |  |  |
| methods, statistics, reproducibility |  |  |  |  |
| reference reality and integrity |  |  |  |  |
| exact claim-citation support |  |  |  |  |
| figure/table/supplement integration |  |  |  |  |
| reporting, ethics, and declarations |  |  |  |  |
| journal-specific manuscript format |  |  |  |  |
| rendered visual QA |  |  |  |  |
| submission-package completeness |  |  |  |  |
| adversarial post-revision review |  |  |  |  |

## State distinctions

Keep separate:

- `author-readable`
- `coauthor-review-ready`
- `submission-system-ready`
- `production-ready`

A polished DOCX, clean render, complete review report, or successful specialist script cannot alone establish submission readiness.

## Mandatory blockers

Block release when:

- manuscript components are not demonstrably the same version
- official journal rules or article type cannot be verified
- fewer than five independent reviewers completed
- a material scientific claim is unsupported or not assessable
- citation integrity or exact support remains unresolved
- figures, legends, tables, supplements, or source data conflict
- required ethics, reporting, registration, data/code, authorship, funding, or COI material is missing
- the clean manuscript failed structural or rendered visual QA
- a revision changed core claims without re-review

## Final output

Return exactly:

- `RELEASE PASS`
- `RELEASE FAIL`
- `RELEASE NOT ASSESSABLE`

List blocking issues before optional improvements. Do not predict acceptance or call the package journal-ready when a critical gate is unassessed.
