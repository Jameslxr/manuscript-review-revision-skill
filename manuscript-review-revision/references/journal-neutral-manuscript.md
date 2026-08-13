# Journal-neutral general manuscript

Use this route only when the author explicitly selects a neutral, general,
journal-independent, portable, or coauthor-ready manuscript. It is a deliberate
working profile, not a placeholder journal and not permission to blend rules
from multiple publishers.

## Intake and artifact

Record `manuscript_route: JOURNAL_NEUTRAL` in `00_input_inventory.json` and
create `01_neutral_manuscript_profile.json` with:

- `schema_version: 1.0`;
- `manuscript_route: JOURNAL_NEUTRAL`;
- article type and review stage, using `unknown` only when they cannot be
  inferred safely;
- `profile_status`: `PASS`, `FAIL`, or `NOT_ASSESSABLE`;
- `review_standard: RIGOROUS_GENERAL_BIOMEDICAL`;
- `journal_compliance: NOT_APPLICABLE`;
- the frozen global DOCX, semantic-list, table, front-matter, line-number, and
  page-number contracts used for this run;
- known portability limits and the exact items that must be reopened after a
  target journal is chosen.

Do not create fake official sources, use `JOURNAL_NEUTRAL` as a journal name in
author-facing prose, or claim that neutral defaults are official requirements.

## Review calibration

Apply the same scientific validity floor, claim-evidence discipline, reporting
guidelines, ethical checks, statistical rigor, reference-integrity gate, and
five independent reviewer receipts used in a targeted review. Replace the
journal-fit seat with a manuscript-portability and architecture seat. Do not
create an acceptance-tolerance card or use recent accepted papers to estimate
acceptability.

Classify findings as fatal flaws, correctable issues, acceptable inherent
limitations, or optional strengthening. A limitation blocks only when honest
claim narrowing and transparent disclosure still leave the central inference
scientifically indefensible.

## Neutral format profile

Use the conservative manuscript defaults unless the user supplies an explicit
non-journal style instruction:

- Times New Roman; 15 pt bold title; 12 pt top-level manuscript text; 10 pt
  table-cell text;
- double spacing outside tables and single spacing inside tables;
- 0/0 pt paragraph spacing plus exactly one genuinely empty paragraph at
  semantic prose and block boundaries;
- no spaces or tabs inside an empty paragraph;
- compact bullet/numbered lists with no empty paragraph between items;
- left-aligned front matter and restrained black styling;
- journal-neutral three-line editable tables under
  [table-formatting.md](table-formatting.md);
- continuous Word-native line numbering and dynamic continuous page numbering;
- full rendered-page inspection and all non-journal release gates.

Report the format result as `NEUTRAL_FORMAT_PASS`, `NEUTRAL_FORMAT_FAIL`, or
`NEUTRAL_FORMAT_NOT_ASSESSABLE`. A pass means the manuscript satisfies the
frozen neutral house profile; it does not establish readiness for any journal.

## Retargeting boundary

When the author later chooses a target journal, freeze the neutral artifacts
as prior work and reopen current official-source research, article type,
submission stage, journal profile, executable format plan, acceptance-tolerance
calibration, journal-fit review, anonymization, limits, references, tables,
figures, declarations, and upload-package requirements. Preserve neutral work
that remains valid, but never promote it to journal compliance without the new
gates.
