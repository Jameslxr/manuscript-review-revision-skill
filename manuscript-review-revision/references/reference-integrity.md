# Reference and exact-claim integrity

Run three separate gates. Passing one does not pass the others.

## Gate A: bibliographic reality and integrity

Verify each reference through structured metadata and a primary record where possible:

- DOI resolution
- PubMed/PMID or other authoritative index
- publisher article page
- title, authors, journal, year, volume, issue, pages or article number
- preprint versus version of record
- duplicate records
- retraction, expression of concern, correction, or corrigendum

If records disagree, preserve the discrepancy. Never invent a missing DOI, PMID, page range, issue, or author.

## Gate B: target-journal format and manuscript closure

Use the current official journal instructions and template. Check:

- numbered versus author-date citation style
- order of first appearance
- author truncation and journal-title abbreviation
- title, volume, issue, pages/article number, DOI, and punctuation
- orphan references and missing reference-list entries
- duplicate references
- numbering after revision
- linked citation fields when prohibited at the relevant submission stage

## Gate C: exact semantic support

Split compound sentences into atomic claims. Create one ledger row per claim-citation relationship.

Use:

- `DIRECT_SUPPORT`
- `PARTIAL_SUPPORT`
- `BACKGROUND_ONLY`
- `CONTRADICTS_OR_LIMITS`
- `NOT_ASSESSABLE`

Record the evidence basis:

- `RESULTS_SECTION`
- `FULL_TEXT`
- `ABSTRACT`
- `PUBLISHER_PAGE`
- `METADATA_ONLY`
- `UNAVAILABLE`

Rules:

- Topic similarity is not support.
- Association evidence does not support causality.
- A different species, tissue, model, population, endpoint, or direction requires explicit qualification.
- Reviews provide context unless they directly and appropriately support a synthesis claim.
- Several weak citations do not combine into direct support.
- Place a citation after the exact clause or sentence it supports; do not let a citation ambiguously cover a paragraph.
- `DIRECT_SUPPORT` requires verified metadata, a clear integrity state, and inspection beyond metadata/title.
- Strong mechanistic, clinical, diagnostic, prognostic, or safety claims normally require relevant full-text evidence.
- Retractions or expressions of concern block affirmative support unless the manuscript is explicitly discussing the integrity event.

## Ledger schema

Write TSV/CSV columns:

```text
sentence_id
atomic_claim
citation_key
identifier
metadata_status
integrity_status
evidence_basis
support_grade
placement_status
format_status
action
```

Use:

- metadata: `VERIFIED`, `UNVERIFIED`, `CONFLICT`
- integrity: `CLEAR`, `RETRACTED`, `CORRECTED`, `EXPRESSION_OF_CONCERN`, `NOT_CHECKED`
- placement: `PRECISE`, `AMBIGUOUS`, `MISPLACED`, `MISSING`
- format: `PASS`, `FAIL`, `NOT_ASSESSABLE`

Do not grant the citation gate while any material claim is `NOT_ASSESSABLE`, any integrity state is `NOT_CHECKED`, or any direct-support row relies on metadata-only evidence.
