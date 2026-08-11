# Journal typography resolution

Use this contract whenever an official source, editor instruction, or template
may change manuscript font or line spacing.

## Read the rule in context

Inspect the complete sentence, its heading, the exact article type, and the
submission stage. Record the official URL, access date, exact source excerpt,
and one rule-strength value:

- `MANDATORY`: uses binding language such as `must`, `required`, or an exact
  template token;
- `EXPLICIT_REQUIREMENT`: uses a direct imperative such as `Use 12-point Times
  New Roman` without presenting the value as an example;
- `EXAMPLE_ONLY`: introduces the value with `e.g.`, `for example`, `for
  instance`, or `such as`;
- `UNSPECIFIED`: the current exact source gives no value;
- `NOT_ASSESSABLE`: the source is inaccessible, contradictory, or stage/type
  scope cannot be resolved.

An `EXAMPLE_ONLY` value is not a journal override. Do not convert `e.g.,
10-point Times Roman` into a mandatory 10 pt body rule. A published article,
search snippet, remembered rule, or publisher-wide example is also not an
editable-manuscript override.

## Resolve tokens

Use an official value only for `MANDATORY` or `EXPLICIT_REQUIREMENT` evidence.
Otherwise apply the manuscript fallback:

- Times New Roman;
- Title: 15 pt bold;
- every other visible manuscript paragraph: 12 pt;
- section and subsection headings: 12 pt bold, preserving supplied wording and
  capitalization unless the official source explicitly requires a case rule;
- table-cell text: 12 pt unless an exact source explicitly resolves another
  table token;
- line spacing: double;
- black text and 0/0 pt paragraph spacing.

If the source explicitly requires 12 pt, use 12 pt. If it explicitly requires
1.5 line spacing, use `1.5`. Keep font and line-spacing decisions independent:
an explicit font rule does not resolve spacing, and an explicit spacing rule
does not resolve font.

## Fail-closed evidence

Record `font_rule_strength`, `font_source_excerpt`,
`line_spacing_rule_strength`, and `line_spacing_source_excerpt` in the format
plan. Use `CONSERVATIVE_FALLBACK` for `EXAMPLE_ONLY` or `UNSPECIFIED` evidence.
Use an official basis only with a binding/direct rule and a listed official
source URL. Mark unresolved conflicts `NOT_ASSESSABLE`; never guess.
