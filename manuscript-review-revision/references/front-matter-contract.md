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
page. Treat title, authors, affiliations, correspondence, Abstract, and Keywords
as semantic Word paragraph roles.

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
| Title | left | Times New Roman | 15 pt | bold | single | 0/0 pt |
| Authors | left | Times New Roman | 12 pt | regular | single | 0/0 pt |
| Affiliations | left | Times New Roman | 10.5 pt | regular | single | 0/0 pt |
| Correspondence | left | Times New Roman | 10.5 pt | regular | single | 0/0 pt |
| Abstract/section heading | left | Times New Roman | 12 pt | bold | single | 0/0 pt |
| Body prose | left | Times New Roman | 12 pt | regular | double | 0/0 pt |
| Keywords | left | Times New Roman | 11 pt | regular | single | 0/0 pt |

Additional rules:

- use 1-inch margins and top vertical page alignment;
- order roles as title, authors, affiliations, correspondence, then Abstract;
- use no empty paragraph inside the title/author/affiliation/correspondence block;
- allow exactly one empty paragraph between the block and Abstract in the
  integrated-first-page profile;
- permit a page break before Abstract only when `abstract_start=new-page` is
  resolved by the journal or user;
- do not center or right-align any title-block role in the neutral profile;
- do not use a table, text box, shape, cover-page panel, vertical centering, or
  decorative container for front matter;
- use superscript affiliation markers when multiple affiliations require a map;
- include corresponding-author contact information for an unblinded
  submission-ready file;
- keep the title within 12-16 pt and the title block visually compact;
- place dynamic page numbers in the upper-right header by default;
- keep continuous Word-native line numbering as the user's global invariant.

The exact journal may require a separate title page, different page-number
location, or a different font. Record and apply that as a sourced override.

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
- non-black front-matter text;
- role-order inversion;
- empty paragraphs inside the title block;
- more than one empty paragraph before Abstract;
- front matter stored in a table or text box;
- non-top vertical page alignment;
- PAGE fields outside the resolved location or duplicate PAGE fields.

Run the existing whole-document style audit separately. Neither audit can
replace the other.

## Rendered-page gates

Inspect every rendered page. On page 1 verify:

- the title block begins naturally below the top margin and is not vertically
  centered;
- title, authors, affiliations, and correspondence share one left edge in the
  neutral profile;
- the title is prominent but not publication-banner sized;
- front matter is compact and not surrounded by artificial whitespace;
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
CONTENT-PRESERVATION PASS
JOURNAL PASS or NOT APPLICABLE
RENDER PASS
```

Return `FORMAT RELEASE PASS` only when every applicable gate passes. A generic
neutral profile can be called submission-style or coauthor-ready; call it
journal compliant only when the current source-linked journal gate also passes.
Use `validate_format_release.py` to combine the machine-readable gate results;
`NOT_ASSESSABLE` must never be promoted to pass.
