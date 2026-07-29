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

Risk-stratify claims before choosing audit depth:

| Tier | Scope | Required audit depth |
|---|---|---|
| `A_MATERIAL` | central causal, quantitative, clinical, diagnostic, prognostic, safety, or decision-relevant claim | audit every claim-citation relationship with relevant full text or results evidence |
| `B_SUPPORTING` | interpretation, synthesis, or supporting evidence that materially shapes the argument | audit every relationship; use the primary report or an authoritative full-text synthesis source appropriate to the claim |
| `C_CONTEXT` | generic background or low-consequence context | verify metadata/integrity and use a documented semantic-support sample; unresolved sampled rows remain advisory unless a known defect is found |

Split compound sentences into atomic claims for tiers A and B. Create one
ledger row per audited claim-citation relationship. Do not manufacture an
exhaustive tier-C ledger merely to increase row count.

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
- Reviews may directly support a synthesis or consensus claim when their scope
  and full text match that claim. They do not replace primary evidence for a
  specific experiment, effect estimate, causal result, or safety outcome.
- Several weak citations do not combine into direct support.
- Place a citation after the exact clause or sentence it supports; do not let a citation ambiguously cover a paragraph.
- `DIRECT_SUPPORT` requires verified metadata, a clear integrity state, and inspection beyond metadata/title.
- Tier-A mechanistic, clinical, diagnostic, prognostic, quantitative, or safety
  claims require relevant full-text or results-section evidence.
- Retractions or expressions of concern block affirmative support unless the manuscript is explicitly discussing the integrity event.

## Ledger schema

Write TSV/CSV columns:

```text
sentence_id
atomic_claim
claim_tier
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

Do not grant the citation gate while any tier-A or tier-B claim is
`NOT_ASSESSABLE`, has unverified metadata or integrity, has unresolved
placement, or relies on metadata-only direct support. A tier-C `NOT_CHECKED` or
`NOT_ASSESSABLE` sampled row produces a visible advisory rather than blocking
the whole citation gate. A known formatting defect, retracted affirmative
support, or expression of concern remains blocking at every tier.
