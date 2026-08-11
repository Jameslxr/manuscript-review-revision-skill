# Front-matter contract

## Contents

1. [Purpose and authority](#purpose-and-authority)
2. [Journal-neutral unblinded profile](#journal-neutral-unblinded-profile)
3. [Blinded profile](#blinded-profile)
4. [Journal-template override](#journal-template-override)
5. [Mechanical gates](#mechanical-gates)
6. [Rendered-page gates](#rendered-page-gates)
7. [Release mapping](#release-mapping)

## Purpose and authority

Turn an editable scientific draft into a restrained author-prepared submission
manuscript, not a published-article facsimile, report cover, or designed title
page. Treat Title, Authors, Affiliations, Author notes, Correspondence,
ORCID/identifiers, Abstract, and Keywords as semantic Word paragraph roles.

The journal-neutral profile is the user's house style. It is not a claim that
all journals prohibit centered title blocks. Apply this precedence:

1. direct current editor instruction
2. exact official template for the article type and submission stage
3. current official journal author instructions
4. explicit user instruction
5. journal-neutral profile below

Do not derive author-manuscript alignment from a typeset published PDF. A
published article is calibration evidence, not an editable submission template.

## Journal-neutral unblinded profile

Use these exact defaults when no official source resolves a different token:

| Role | Alignment | Typeface | Size | Weight | Line spacing | Space before/after |
|---|---|---|---:|---|---|---|
| Title | left | Times New Roman | 15 pt | bold | resolved global token | 0/0 pt |
| Authors | left | Times New Roman | 12 pt | regular | resolved global token | 0/0 pt |
| Affiliations | left | Times New Roman | 12 pt | regular | resolved global token | 0/0 pt |
| Author notes | left | Times New Roman | 12 pt | regular | resolved global token | 0/0 pt |
| Correspondence | left | Times New Roman | 12 pt | regular | resolved global token | 0/0 pt |
| ORCID/identifiers | left | Times New Roman | 12 pt | regular | resolved global token | 0/0 pt |
| Abstract/section heading | left | Times New Roman | 12 pt | bold | resolved global token | 0/0 pt |
| Body prose | left | Times New Roman | 12 pt | regular | resolved global token | 0/0 pt |
| Keywords | left | Times New Roman | 12 pt | bold label only | resolved global token | 0/0 pt |
| Declarations/CRediT | left | Times New Roman | 12 pt | bold heading/label only | resolved global token | 0/0 pt |

Additional rules:

- use 1-inch margins and top vertical page alignment;
- order present roles as Title, Authors, Affiliations, optional Author notes,
  Correspondence, optional ORCID/identifiers, then Abstract;
- require exactly one structurally empty Enter-created paragraph between every
  adjacent present semantic block, including the last present identity block
  and Abstract;
- give every separator `0/0 pt`, disable automatic spacing, and apply the
  resolved global line-spacing token;
- keep consecutive paragraphs inside one semantic block compact: multiple
  authors or affiliations have no empty separator until the next role begins;
- permit a page break before Abstract only when `abstract_start=new-page` is
  resolved by the journal or user;
- do not center or right-align any title-block role in the neutral profile;
- do not use a table, text box, shape, cover-page panel, vertical centering, or
  decorative container for front matter;
- use superscript affiliation markers when multiple affiliations require a map;
- include corresponding-author contact information for an unblinded
  submission-ready file;
- require the resolved title size exactly (15 pt fallback) and keep each
  semantic block visually restrained;
- default the resolved global line-spacing token to double and apply it to the
  complete manuscript, including the author block, headings, Keywords, and
  declarations; use 1.5 or another token only when resolved from the current
  journal/template or an explicit user instruction;
- place no empty paragraph before Keywords and exactly one after Keywords;
- place exactly one empty paragraph before each section, subsection, and
  declaration/CRediT block, with none between its heading and first body
  paragraph;
- load [credit-authorship-contract.md](credit-authorship-contract.md) for every
  CRediT-labelled block and prohibit empty paragraphs between author entries;
- place dynamic page numbers in the upper-right header by default;
- keep continuous Word-native line numbering as the user's global invariant.

The exact journal may require a separate title page, different page-number
location, or a different font. Load
[journal-typography-resolution.md](journal-typography-resolution.md) and apply
only a binding/direct sourced override; example-only wording does not replace
the 15/12 pt fallback.

## Blinded profile

For double-anonymized review:

- retain the title;
- remove author-identifying material only with explicit user authorization;
- fail the audit if authors, affiliations, correspondence, acknowledgements,
  headers, file metadata, or self-identifying text remain in a declared blinded
  deliverable;
- never invent replacement identities or institutions;
- keep a separate protected unblinded source/title-page file when required.

Formatting a file as blinded is a privacy-sensitive transformation. The
profile audit may diagnose identity leakage, but the normalizer must not delete
identity content unless the user explicitly requests anonymization.

## Journal-template override

Allow centered or otherwise non-neutral front matter only when the current
format checklist records all of:

- exact journal;
- exact article type;
- exact submission stage;
- official template or rule URL/path;
- access date;
- exact role and token being overridden;
- verification method.

Do not treat a publisher-wide example or a published PDF as sufficient proof.
If alignment is not specified, retain the journal-neutral left alignment.
The exact semantic block-gap matrix is a personal output invariant. An official
template may override alignment, typography, title-page location,
anonymization, or page-number placement, but it does not authorize a compact
block transition. If the template conflicts, record the conflict and do not
claim simultaneous compliance unless the user explicitly changes the
invariant.

## Mechanical gates

Run `audit_docx_front_matter.py` after the normalizer and numbering enforcer.
When several roles share one Word style, resolve them with explicit
`--<role>-paragraph` arguments using one-based top-level paragraph numbers.
The neutral profile must fail on:

- missing or duplicate title;
- missing authors or affiliations in unblinded mode;
- missing correspondence unless explicitly allowed by the journal profile;
- identity material in blinded mode;
- centered, right-aligned, or mixed-alignment title-block roles;
- unresolved, undersized, or oversized front-matter typography;
- any author, affiliation, author-note, correspondence, ORCID/identifier,
  heading, Keywords, or declaration paragraph whose size differs from the
  resolved body size;
- any manuscript role or empty separator whose line spacing differs from the
  resolved global token;
- a non-bold Keywords label, a bold keyword value, or a missing/duplicated
  semantic blank line;
- non-black front-matter text;
- role-order inversion;
- a missing or duplicated real empty paragraph at any adjacent present block
  transition, including the transition to Abstract;
- an empty paragraph within a multi-paragraph Author, Affiliation, Author-note,
  Correspondence, or ORCID/identifier block;
- an unclassified Author-note or ORCID/identifier paragraph;
- front matter stored in a table or text box;
- non-top vertical page alignment;
- PAGE fields outside the resolved location or duplicate PAGE fields.

Run the existing whole-document style audit and semantic-rhythm audit
separately. No one audit replaces the others.

## Rendered-page gates

Inspect every rendered page. On page 1 verify:

- the title block begins naturally below the top margin and is not vertically
  centered;
- all present front-matter roles share one left edge in the neutral profile;
- every adjacent present semantic block is separated by one natural empty line,
  not paragraph before/after spacing;
- the title is prominent but not publication-banner sized;
- paragraphs within each block are compact and block transitions are uniform;
- Abstract begins at a natural transition or the sourced page break;
- author/affiliation markers are readable and map correctly;
- upper-right page numbering and continuous line numbering are visible;
- no clipping, overlap, missing glyphs, or hidden content exists.

Rendered inspection is mandatory because Word wrapping determines the visible
number of title lines and usable page density.

## Release mapping

Report these gates separately:

```text
STRUCTURAL PASS
FRONT-MATTER PASS
SEMANTIC-RHYTHM PASS
CONTENT-PRESERVATION PASS
JOURNAL PASS or NOT APPLICABLE
RENDER PASS
```

Return `FORMAT RELEASE PASS` only when every applicable gate passes. A generic
neutral profile can be called submission-style or coauthor-ready; call it
journal compliant only when the current source-linked journal gate also passes.
Use `validate_format_release.py` to combine the machine-readable gate results;
`NOT_ASSESSABLE` must never be promoted to pass.
