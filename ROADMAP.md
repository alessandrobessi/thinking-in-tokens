# Roadmap

High-level milestones for the project described in `blueprint.md`. For the
chapter-by-chapter manuscript status, see `book/README.md`.

## Milestone 1 — Infrastructure + Part I pilot (done)

- [x] Style guide: palette, SVG conventions, icon vocabulary, analogy registry
- [x] Chapter template (11-element editorial checklist)
- [x] Glossary, misconception graph, concept dependency tracker
- [x] Part I — Information (chapters 1–5), full prose + canonical diagrams
- [x] Root README, LICENSE, CONTRIBUTING, project scaffolding

## Milestone 2 — Part II: Prediction (done)

- [x] Chapters 6–10 (Predicting the Next Token → Scaling Laws)
- [x] Tracking files updated per chapter, not batched

## Milestone 2.5 — Diagram architecture correction (done)

- [x] Discovered that inline `<svg>` never rendered on GitHub at all (its
  HTML sanitizer strips raw `<svg>` content wherever it appears directly in
  rendered Markdown) — this invalidated the original "inline SVG for
  native GitHub rendering" premise.
- [x] Extracted all 20 diagrams (chapters 1–10) to standalone files under
  `assets/diagrams/`, referenced via `<img>`. Verified by local rendering.
- [x] Updated `style-guide.md`, `templates/chapter-template.md`, and
  `scripts/check_svg_bounds.py` so every future chapter follows the
  corrected pattern, with a regression guard against inline `<svg>`
  creeping back into `book/**/*.md`.

## Milestone 3 — Editorial validation of Part I + II

- [ ] Lightweight citation pass on empirical/historical claims (`references/`)
- [ ] External reader test: 5+ target readers (non-technical professionals),
  following the structured protocol and question bank in `testing/` —
  comprehension, transfer, misconception resistance, retention, and
  reading-experience notes, per chapter, per reader. Requires actually
  recruiting readers; the protocol itself is ready to run.
- [ ] Cross-theme, cross-chapter consistency pass on analogies and voice

## Milestone 4 — Parts III–VI

- [ ] Part III — The Transformer (11–15)
- [ ] Part IV — Building Useful AI (16–20)
- [ ] Part V — AI Systems (21–25, durable-question framing per blueprint's
      current TOC — see note on Chapter 21/MCP)
- [ ] Part VI — The Future (26–30)

## Milestone 5 — Beyond the manuscript

Per blueprint.md's "Vision" and "Living Companion" sections — not started:

- [ ] Interactive companion website (tokenization explorer, embedding
      playground, attention/transformer animations, RAG simulator, agent
      execution visualizer, quizzes)
- [ ] Editable SVG diagram library as a documented, cataloged asset —
      `assets/diagrams/` already holds every diagram as a standalone,
      editable file (see Milestone 2.5 below); what's missing is an index/
      catalog and any tooling beyond hand-editing
- [ ] Teaching material / video course

## Explicitly deferred, not forgotten

- A build pipeline (Pandoc/Typst/Quarto → PDF/EPUB/web) — the manuscript
  now stores diagrams as standalone files under `assets/diagrams/`
  referenced via `<img>`, which happens to make a future build pipeline
  easier (no HTML-to-extract from Markdown), but one still isn't being
  taken on now.
- Professional publishing conversations — blueprint.md names "a
  professionally published book" as the primary artifact; no publisher
  process has started.
