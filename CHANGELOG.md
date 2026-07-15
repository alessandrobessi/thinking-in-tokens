# Changelog

## 2026-07-15

- Initial commit: project infrastructure (style guide, chapter template,
  glossary, misconception graph, concept dependency tracker, icon set) and
  the full Part I manuscript (chapters 1–5, "Information").
- Added root `README.md`, `LICENSE` (provisional, all-rights-reserved),
  `CONTRIBUTING.md`, `ROADMAP.md`, this changelog, GitHub issue templates,
  and a `references/` bibliography system.
- Amended `blueprint.md`: the Standard Chapter Template is now explicitly
  an editorial checklist rather than a mandatory set of reader-facing
  headings; Part V's table of contents was restructured around durable
  questions instead of named standards (Tool Calling and MCP merged into
  one chapter, "How Models Reach Into the World," with MCP taught inside it
  as the current connection standard). Total chapter count: 31 → 30.
- Chapter 1: softened claims about scale being "the" dominant driver of
  progress and added a note on the ongoing debate over measuring emergent
  abilities.
- Chapter 5: added an explicit distinction between a token's static,
  starting embedding (this chapter) and its contextual, attention-revised
  representation (Chapter 11), plus a new misconception entry, and reframed
  the country/capital geometry example as an illustrative pattern rather
  than a universal law.
- Added `concept-graph.yaml` as the machine-readable source of truth behind
  `concept-graph.md`.
- Added Part II manuscript (chapters 6–10, "Prediction"), with matching
  glossary/misconception/concept-graph/reference updates.
- Second review round: Chapter 8 now draws an explicit boundary between the
  generic layered network it describes and the transformer architecture
  Part III builds on top of it. Chapter 10 clarifies that the scaling-law
  "straight line" requires both axes scaled in equal ratios (not literal
  linear loss decay) and introduces "irreducible loss." Chapter 5 gained a
  "try it yourself" thought experiment (hot/cold/sandwich) reinforcing the
  similarity-vs-synonymy misconception. `style-guide.md`'s chapter-mechanics
  section was reworded to stop contradicting blueprint.md's amended
  template language. Added `testing/` — a ready-to-run reader-validation
  protocol and per-chapter question bank (comprehension, transfer,
  misconception resistance, retention), covering Milestone 3 of
  `ROADMAP.md`.
- **Fixed a rendering bug affecting every diagram in the manuscript.**
  Every embedded `<svg>` contained internal blank lines (used to visually
  separate element groups while authoring). GitHub's Markdown parser treats
  `<svg>` as a generic HTML block that ends at the first blank line — so
  every diagram was silently truncated mid-markup, with the remainder
  (including the closing `</svg>` tag) rendered as literal garbled text
  instead of a diagram. Stripped all internal blank lines from all 20
  diagrams across chapters 1–10; added `scripts/check_svg_bounds.py` and a
  hard rule in `style-guide.md` §3.0 to catch this and a related bug
  (`<text>` labels overflowing their `viewBox`, found and fixed in
  Chapters 1 and 4) before it recurs.
- **Corrected the diagram architecture after confirming diagrams still
  didn't render on GitHub even after the blank-line fix.** Root cause: the
  earlier premise was wrong — GitHub's Markdown sanitizer strips raw
  `<svg>` content wherever it's embedded directly in a `.md` file,
  regardless of formatting; inline SVG in Markdown was never going to
  render on GitHub. Extracted all 20 diagrams (chapters 1–10) to standalone
  files under `assets/diagrams/`, referenced via `<img>` — the same pattern
  already used for the root README's preview image. Verified all 20 render
  correctly via local rendering (macOS QuickLook thumbnailing). Updated
  `templates/chapter-template.md`, `style-guide.md` §3, and
  `scripts/check_svg_bounds.py` (now also fails the build if any chapter
  file contains a literal `<svg` tag again) so future chapters follow the
  corrected pattern by default.
