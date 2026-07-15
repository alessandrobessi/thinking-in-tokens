# Roadmap

High-level milestones for the project described in `blueprint.md`. For the
chapter-by-chapter manuscript status, see `book/README.md`.

## Milestone 1 — Infrastructure + Part I pilot (done)

- [x] Style guide: palette, SVG conventions, icon vocabulary, analogy registry
- [x] Chapter template (11-element editorial checklist)
- [x] Glossary, misconception graph, concept dependency tracker
- [x] Part I — Information (chapters 1–5), full prose + canonical diagrams
- [x] Root README, LICENSE, CONTRIBUTING, project scaffolding

## Milestone 2 — Part II: Prediction (in progress)

- [ ] Chapters 6–10 (Predicting the Next Token → Scaling Laws)
- [ ] Tracking files updated per chapter, not batched

## Milestone 3 — Editorial validation of Part I + II

- [ ] Lightweight citation pass on empirical/historical claims (`references/`)
- [ ] External reader test: 5+ target readers (non-technical professionals)
  read Part I and are asked to explain tokens, information, compression,
  context, and embeddings unaided — revise based on actual misunderstandings
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
- [ ] Editable SVG diagram library as a standalone asset (beyond the
      inline-in-chapter diagrams the manuscript uses today)
- [ ] Teaching material / video course

## Explicitly deferred, not forgotten

- A build pipeline (Pandoc/Typst/Quarto → PDF/EPUB/web) — the manuscript
  currently commits to inline SVG-in-markdown for native GitHub rendering;
  a build pipeline is a real future need but is not being taken on now.
- Professional publishing conversations — blueprint.md names "a
  professionally published book" as the primary artifact; no publisher
  process has started.
