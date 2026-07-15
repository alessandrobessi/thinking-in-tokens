# Style Guide

Shared conventions for prose, voice, and diagrams across every chapter. This
file is written once and reused unchanged across all 31 chapters — do not fork
per-part variants. When Parts II–VI are drafted in later passes, they follow
these exact rules; the only thing that grows is the icon vocabulary (§3) and
the analogy registry (§5).

---

## 1. Voice

- Write to an intelligent, curious, non-technical reader — a manager, founder,
  consultant, or student. Never assume math, programming, or ML background.
- Intuition before terminology: introduce the idea in plain language, *then*
  attach the technical name to it, never the reverse.
- One genuinely new idea per page. If a paragraph needs a reader to hold two
  new concepts at once, split it.
- Prefer short, concrete sentences over qualified, abstract ones. Cut hedges.
- A technical explanation must still be *correct* — simplify by revealing the
  essential mechanism, never by stating something false that's "close enough."
- Every explanation should pass the Feynman test: if a curious 12-year-old
  friend asked "wait, why?", does the next sentence already answer it?
- Reuse analogies deliberately (see §5, Analogy Registry). Introducing a new
  analogy for a concept that already has one elsewhere in the book is a bug,
  not a stylistic choice — check the registry before writing one.

## 2. Chapter Mechanics

- Every chapter must substantively cover all 11 elements of
  `templates/chapter-template.md` — completeness is mandatory, but per
  blueprint.md's amended "Standard Chapter Template" section, the
  reader-facing presentation is not. During this drafting phase, every
  chapter still uses the 11 headers verbatim, in order, because that makes
  completeness trivial to verify chapter by chapter (see the verification
  steps in this project's plan history). Loosening the visible headers
  into freer prose is a deliberate later editorial pass, not something to
  improvise chapter by chapter now — doing it piecemeal would make the
  11-point completeness check unreliable across 30 chapters.
- Every chapter answers exactly one question from the Narrative Graph
  (blueprint.md, "Narrative Graph" section) and ends by provoking the next.
  §11 of chapter N and §1 of chapter N+1 must express the same question.
- Never introduce a concept before its prerequisites (blueprint.md, "Concept
  Dependency Graph"). If a chapter needs a concept from a later level to make
  an aside, cut the aside — don't forward-reference.
- After finishing a chapter, immediately: add its new terms to `glossary.md`,
  its misconceptions to `misconceptions.md`, check off its concepts in
  `concept-graph.md`, and add any new analogy to the registry below. Do this
  per chapter, not batched — batching is how these files silently drift.

## 3. SVG Diagram System

All diagrams are hand-authored SVG, stored as **standalone files** under
`assets/diagrams/` (one file per figure — `chNN-fig1-slug.svg` for the
Visual Explanation figure, `chNN-fig2-slug.svg` for the Canonical
Mental-Model Diagram), referenced from the chapter file with a plain
`<img>` tag:

```html
<p align="center">
  <img src="../../assets/diagrams/chNN-fig1-slug.svg" alt="..." width="640"/>
</p>
```

`assets/icons/*.svg` follows the same standalone-file pattern and is
treated as reference snippets to copy and adapt by hand when building a new
diagram, not as an include mechanism.

### 3.0 Never paste a raw `<svg>` directly into a chapter's markdown

This is a hard rule, not a style preference — it has already broken every
diagram in the manuscript once (see `CHANGELOG.md`). `<svg>` is not
rendered by GitHub when it appears inline inside a `.md` file's content:
GitHub's HTML sanitizer strips raw `<svg>` markup wherever it's embedded
directly in rendered Markdown, full stop, regardless of formatting. (An
earlier, *different* bug — inline SVGs breaking at internal blank lines
per CommonMark's HTML-block rules — was fixed first and turned out not to
be the real blocker; moving to standalone files sidesteps both problems at
once, since a real `.svg` file is fetched and rendered by the browser as an
ordinary image, never parsed as part of the page's Markdown/HTML at all.)

Concretely: every diagram is a real file under `assets/diagrams/`,
referenced via `<img src="...">`. If you ever see a literal `<svg` inside
a `book/**/*.md` file, that's a regression — extract it to its own file
immediately.

Before committing any new or edited diagram, run the checker:

```
python3 scripts/check_svg_bounds.py .
```

It does two things: (1) fails if any `book/**/*.md` file contains a literal
`<svg` tag (the regression above), and (2) heuristically estimates whether
any `<text>` element in `assets/diagrams/*.svg` or `assets/icons/*.svg`
would run past its `viewBox`'s edge (a second, unrelated failure mode —
text positioned assuming a short label that turns out to be longer, e.g.
"compute" vs. "architecture (2017)" sharing one x-position). The width
estimate is a rough character-count heuristic, not real font metrics, and
it does not account for `transform="rotate(...)"` — treat its output as
"check this by hand," not as ground truth, especially for rotated labels.
Since standalone SVG files aren't parsed by Markdown at all, blank lines
inside them are harmless — feel free to use them for readability while
authoring.

### 3.1 Canvas

Every SVG's **first child** must be an explicit background rect, so the
diagram stays legible regardless of the reader's light/dark theme:

```xml
<rect width="100%" height="100%" fill="#FBF9F6"/>
```

### 3.2 Fixed viewBoxes

| Use | viewBox | width attr |
|---|---|---|
| Canonical mental-model diagram (template §8) | `0 0 800 500` | `100%` |
| Supporting figures (template §3) | `0 0 600 300` | `100%` |

Never use a fixed pixel width — always `width="100%"` so the SVG scales
responsively while the viewBox fixes the aspect ratio.

### 3.3 Palette (fixed hex values — semantic roles, not decoration)

| Role | Hex | Meaning |
|---|---|---|
| Ink / text / default stroke | `#1B1B2F` | all body text, default line color |
| Canvas background | `#FBF9F6` | background rect, every SVG |
| Primary structure | `#3D5A80` | tokens, blocks, containers |
| Secondary / neutral | `#98A6B3` | connector lines, inactive elements |
| Attention / relationship | `#EE964B` | weighted arrows, relationship lines |
| Context highlight (wash, ~30% opacity) | `#F9DC5C` | context-window / "active" bands |
| Misconception — **reserved** | `#D7263D` | "Common Misconceptions" callouts only |
| Correct intuition — **reserved** | `#2A9D8F` | "correct intuition" callouts only |

Categorical extension (only to distinguish multiple instances of the *same*
icon type — e.g. several embedding clusters — never for the two reserved
roles above): `#457B9D`, `#6D597A`, `#B56576`, `#84A98C`.

### 3.4 Line and shape conventions

- Three stroke weights only: `2` for container/icon outlines, `2` for
  connecting/attention lines (color-coded per §3.3), `1` for fine annotation.
- Token rectangles: `rx="8"`, always.
- Embedding points: filled circles, `r="6"` default, `r="9"` emphasized/example.
- Type: `font-family="Helvetica, Arial, sans-serif"`. Sizes: 18–20px bold for
  in-diagram titles, 14–16px regular for labels, 11–12px for fine annotations.

### 3.5 ID namespacing

Now that every diagram is its own standalone file loaded as an `<img>`, its
`<defs>`/`<marker>` ids are scoped to that file alone — no cross-diagram
collision is possible any more. Keep prefixing local ids with chapter and
figure number anyway (`id="ch03-fig1-arrowhead"`, not a bare
`id="arrowhead"`): it costs nothing, and it's what makes `grep`-ing for a
specific diagram's markup across `assets/diagrams/` unambiguous.

### 3.6 Takeaways

Every figure (supporting or canonical) is followed by a one-sentence italic
takeaway. The canonical diagram's takeaway is bolded, not italic, to mark it
as the chapter's single load-bearing sentence.

## 4. Icon Vocabulary

**Official (from blueprint.md, "Visual Language")** — fixed meaning, never
repurposed:

| Concept | Icon | First needed |
|---|---|---|
| Tokens | rounded rectangles (`rx="8"`) | Ch. 3 |
| Embeddings | colored points (filled circles) | Ch. 5 |
| Attention | weighted arrows | Ch. 11 |
| Transformer | stacked blocks | Ch. 12 |
| Context | highlighted sequence | Ch. 4, Ch. 16 |
| Memory | notebook | Ch. 16 |
| Retrieval | library | Ch. 17 |
| Tool | wrench | Ch. 21 |
| Agent | planning loop | Ch. 22 |
| Vector database | constellation | Ch. 18 |
| External world | white canvas | Ch. 21+ |

**Supplementary (invented for concepts below the blueprint's official
vocabulary, i.e. Level 0–2, needed starting in Part I)**:

| Concept | Icon | First needed |
|---|---|---|
| Symbol / character | a bare glyph inside a thin circle | Ch. 2, Ch. 3 |
| Probability | a small distribution curve (low hump → high hump) | Ch. 2 |
| Compression | a block visually "squeezed" narrower, with a shrink arrow | Ch. 4 |
| Vector-space backdrop | a faint dotted grid or axes, used behind embedding points | Ch. 5 |

Reserve names now for icons Parts II–V will need, drawn only when first used:
`attention-arrow.svg`, `transformer-block.svg`, `context-highlight.svg`,
`memory-notebook.svg`, `retrieval-library.svg`, `tool-wrench.svg`,
`agent-loop.svg`, `vector-db-constellation.svg`.

Canonical snippets for each icon live in `assets/icons/<name>.svg` — copy the
markup into a chapter's diagram and adapt coordinates/labels rather than
redrawing the icon from scratch, so the same concept always looks the same
across chapters.

## 5. Analogy Registry

One analogy per concept, reused everywhere that concept reappears. Check this
table before writing a new analogy — if the concept already has one, reuse it.

| Analogy | Used for concept | First used in | Notes |
|---|---|---|---|
| Cities on a map (re-drawn by similarity, not geography) | Embeddings / semantic geometry | Ch. 5 | From blueprint.md's own worked example — canonical, do not replace. |
| Morse code letter-length (common letters get shorter codes) | Information / probability / compression | Ch. 2, reused Ch. 4 | Ties information theory directly to compression — keep reusing rather than inventing a new one. |
| Telegram/text-speak ("ARRIVE TUESDAY STOP") | Compression via redundancy removal | Ch. 4 | Good source of a second, non-technical grounding for compression alongside Morse. |
| Fluent reader recognizing whole words/fragments, not sounding out letters | Tokenization | Ch. 3 | Reuse if attention/reading-speed analogies are needed again in Part III. |
| Phone keyboard's next-word suggestions | Prediction / autoregressive generation | Ch. 6 | Concrete, universally familiar; reuse before introducing sampling (Ch. 14). |
| Jazz musician improvising note by note | Autoregressive generation (no pre-formed plan) | Ch. 6 | Pairs well with the phone-keyboard analogy above. |
| Mark V. Shaney (1980s Usenet statistical text bot) | N-gram models and their failure to generalize | Ch. 7 | Real historical example; reuse if a later chapter needs a cautionary "looks fluent, isn't grounded" case. |
| Factory floor of simple, adjustable valves | Neural networks / parameters | Ch. 8 | Deliberately not the brain analogy — keeps a clean mechanical intuition free of biological over-claiming. |
| Learning free throws via miss-and-adjust feedback | Loss / training / learning | Ch. 9 | Reuse for fine-tuning (Ch. 19), which is the same loop applied after initial training. |
| Marathon training's diminishing returns | Scaling laws (predictable but diminishing) | Ch. 10 | Reuse if quantization/efficient-inference (Ch. 20) needs a "more isn't always the answer" callback. |

(Table grows chapter by chapter; append immediately after finishing a chapter
that introduces a new analogy — see §2.)
