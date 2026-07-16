# Roadmap

High-level milestones for the project described in `blueprint.md`. For the
chapter-by-chapter manuscript status, see `book/README.md`.

## Milestone 1 — Infrastructure + Part I pilot (done)

- [x] Style guide: voice, analogy registry
- [x] Chapter template (11-element editorial checklist)
- [x] Glossary, misconception graph, concept dependency tracker
- [x] Part I — Information (chapters 1–5), full prose
- [x] Root README, LICENSE, CONTRIBUTING, project scaffolding

## Milestone 2 — Part II: Prediction (done)

- [x] Chapters 6–10 (Predicting the Next Token → Scaling Laws)
- [x] Tracking files updated per chapter, not batched

## Milestone 2.5 — Diagrams tried, then dropped entirely (done)

The manuscript went through two diagram architectures in sequence — inline
`<svg>` in Markdown (broke silently: GitHub's sanitizer strips raw `<svg>`
wherever it's embedded directly in rendered Markdown), then standalone SVG
files under `assets/diagrams/` referenced via `<img>` (worked, verified by
local rendering). Diagrams were then judged not to be pulling their weight
— they mostly re-illustrated what the prose already said, and the
production overhead (two rebuilt SVG systems) was disproportionate to
their teaching value — and the objective was dropped entirely, not just
the second implementation.

- [x] Removed all 20 diagrams and the `assets/diagrams/`, `assets/icons/`,
  and `scripts/check_svg_bounds.py` supporting infrastructure.
- [x] Restructured the chapter template: the diagram-shaped sections
  ("Visual Explanation," "Canonical Mental-Model Diagram") became
  text-only sections ("Worked Example," "Key Takeaway") that do the same
  job — a second concrete grounding, and one memorable closing sentence —
  with words instead of an illustration.
- [x] Rewrote all 10 written chapters (1–10) to the new structure, and
  amended `blueprint.md` (new subtitle, "No Diagrams" section, updated
  Core Design Principles) so the reversal is documented, not silent.

## Milestone 3 — Editorial consolidation of Parts I–IV

- [x] Lightweight citation pass on empirical/historical claims (`references/`)
  — added `levesque2012winograd`, `holtzman2019degeneration`,
  `rafailov2023dpo`, `frantar2022gptq`, `mata2023avianca`, and
  `ji2023hallucination` to `bibliography.md`, cited from
  `references/chapter-11.md`, `chapter-14.md`, `chapter-15.md`,
  `chapter-19.md`, and `chapter-20.md`. KV caching (Ch.20) still has no
  single canonical paper cited — flagged in that reference file for a
  future pass if one is wanted.
- [x] Technical precision pass on Chapters 11, 12, 13, 15, and 20 (causal
  masking, RAG's dependency graph, hallucination framing, quantization) —
  see `CHANGELOG.md`.
- [ ] Informal beta read: 2–3 target-audience readers per completed Part,
  asked where they got lost, what felt repetitive, what they can now
  explain that they couldn't before, and which explanation or example
  stuck with them. No formal scoring or per-chapter protocol — the
  previous structured reader-validation system (`testing/`, pre-test/
  transfer/misconception/retention scoring across 5+ readers) was judged
  disproportionate to a book at this stage and dropped; see `CHANGELOG.md`
  for the reasoning. It remains recoverable from git history (see the
  commit that removed it) if a future course or workshop wants it.
- [ ] Technical review: at least one ML practitioner reviewing Parts I–IV
  directly for inaccurate, overconfident, or misleading claims. Already
  partially informed by external review rounds (see `CHANGELOG.md`); a
  dedicated practitioner pass is still open.
- [ ] Cross-theme, cross-chapter consistency pass on analogies and voice

## Milestone 4 — Parts III–VI

- [x] Part III — The Transformer (11–15)
- [x] Part IV — Building Useful AI (16–20)
- [x] Part V — AI Systems (21–25, durable-question framing per blueprint's
      current TOC — see note on Chapter 21/MCP)
- [x] Part VI — AI in the Real World (26–30)

## Milestone 5 — Local publication pipeline (done)

- [x] Quarto book project (`publish/`) rendering the manuscript to HTML,
      EPUB, and PDF (via the Typst engine) from a single `quarto render`.
      `scripts/prepare_manuscript_for_publish.py` strips each chapter's
      authoring scaffolding (front-matter metadata, footer bookkeeping)
      into a gitignored `publish/chapters/` build directory — `book/*.md`
      itself is untouched. Minimal title page and a preface adapted from
      `README.md`.
- [ ] Deciding whether to dissolve the visible 11-section headers into
      flowing prose before a real release — deliberately not done here;
      see `style-guide.md` §2. The pipeline renders the headers as they
      currently are.
- [ ] A real cover; currently a text-only title page.

## Milestone 6 — Beyond the manuscript

Per blueprint.md's "Vision" and "Living Companion" sections — not started:

- [ ] Interactive companion website (quizzes, updated references, a
      searchable glossary, a text-based concept explorer) — deliberately
      text/interaction-based, not visualization-based, consistent with the
      manuscript dropping diagrams
- [ ] Teaching material / video course

## Explicitly deferred, not forgotten

- Professional publishing conversations — blueprint.md names "a
  professionally published book" as the primary artifact; no publisher
  process has started. The local build pipeline (Milestone 5) produces a
  personal-use PDF/EPUB/site only — `LICENSE` is still an all-rights-
  reserved placeholder, so nothing here grants redistribution rights.

## Explicitly reversed, not deferred

- Diagrams as a teaching device. This isn't a "later" item — it was tried
  twice (Milestone 2.5) and dropped as a deliberate editorial decision. Do
  not reintroduce diagrams, an icon vocabulary, or a "visual language"
  system without revisiting `blueprint.md`'s "No Diagrams" section
  explicitly.
