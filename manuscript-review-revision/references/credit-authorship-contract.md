# CRediT authorship contribution contract

## Authority and scope

Use CRediT to describe contributor roles truthfully and consistently; do not
use it to decide who qualifies for authorship. Apply this precedence:

1. exact current journal submission fields or template
2. current official journal author instructions
3. author-confirmed role assignments
4. the journal-neutral display profile below

The corresponding author should coordinate the assignments, and every
contributor must have an opportunity to review and confirm them. Never infer a
role from author order, affiliation, seniority, or manuscript prose.

Primary standards:

- [NISO CRediT contributor roles](https://credit.niso.org/contributor-roles/)
- [NISO implementation guidance](https://credit.niso.org/implementing-credit/)
- [Elsevier sample CRediT author statement](https://www.elsevier.com/en-gb/researcher/author/policies-and-guidelines/credit-author-statement)

## Controlled role vocabulary

Use the 14 official role labels:

- Conceptualization
- Data curation
- Formal analysis
- Funding acquisition
- Investigation
- Methodology
- Project administration
- Resources
- Software
- Supervision
- Validation
- Visualization
- Writing – original draft
- Writing – review & editing

An individual may have several roles, and one role may be assigned to several
contributors. Optional contribution degrees such as lead, equal, or supporting
may be used only when the submission system supports them and the authors have
confirmed them.

## Journal-neutral display profile

Use `CRediT authorship contribution statement` as the neutral heading unless
the exact journal specifies another label. Format it as a bold body-sized
heading using the manuscript-wide line-spacing token and `0/0 pt` paragraph
spacing.

Prefer one compact author-centric paragraph when authoring a new statement:

```text
CRediT authorship contribution statement¶
Author A: Conceptualization, Methodology, Writing – original draft. Author B: Formal analysis, Visualization, Writing – review & editing.¶
```

For a supplied statement that already uses one paragraph per author, preserve
the paragraph boundaries and text but keep the entry paragraphs consecutive:

```text
CRediT authorship contribution statement¶
Author A: Conceptualization, Methodology, Writing – original draft.¶
Author B: Formal analysis, Visualization, Writing – review & editing.¶
```

Enforce all of the following:

- exactly one real empty paragraph before the CRediT block unless it follows a
  consecutive heading;
- no empty paragraph between the heading and the first entry;
- no empty paragraph between consecutive author-entry paragraphs;
- one manuscript-wide font size and line-spacing token across the heading,
  entries, authors, affiliations, headings, and body text;
- `0 pt` before/after spacing with automatic Word spacing disabled;
- CRediT remains separate from acknowledgements, funding, conflicts, and any AI
  use declaration.

Do not insert an empty paragraph after every author. Do not rewrite supplied
role assignments during format-only work. If a CRediT-labelled statement lacks
any recognized official role, fail the semantic audit and request
author-confirmed correction instead of inventing content.

## Verification

Require the semantic-rhythm audit to verify:

- a CRediT heading has a following statement entry;
- inline or block statements contain recognized official role vocabulary;
- consecutive entries contain zero structurally empty paragraphs between them;
- labels, entries, and separators use the resolved typography and spacing.

Rendered inspection must confirm that the block is compact, readable, and not
visually confused with the next declaration.
