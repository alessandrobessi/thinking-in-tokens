# The Architecture of Intelligence

### A Mental Model for Modern AI Systems

A conceptual introduction to how modern AI actually works — tokens,
embeddings, attention, transformers, training, hallucination, retrieval,
tool use, agents, reasoning models — written for curious, intelligent
readers with **no math, no programming, and no prior ML background**.

Most explanations of AI are either marketing ("it's magic") or academic
(equations first, intuition never). This project is inspired by what
*Structure and Interpretation of Computer Programs*
did for computer science and what the *Feynman Lectures* did for
physics: building one durable mental model, incrementally, that keeps
working as the technology changes.

## Who this is for

Managers, consultants, product leaders, founders, sales professionals,
executives, students, and lifelong learners — anyone who wants to read an
AI engineering blog or product announcement and actually evaluate it,
rather than just trust or dismiss it.

## What readers come away with

By the end, a reader should be able to explain how LLMs generate text; why
they hallucinate; what tokens, embeddings, attention, RAG, vector
databases, tool calling, MCP, and AI agents actually are; and — most
importantly — tell a genuine advance apart from a marketing headline.

## A preview

Every chapter builds understanding through a story, a worked example, and
precise technical explanation, then ends with one bolded, memorable
sentence that distills its core idea. From Chapter 5, on embeddings:

> **Embeddings place tokens as points in a high-dimensional space, where
> nearby points often reflect similar usage, and some recurring
> relationships can appear as geometric directions.**

See it in full context, with the story and worked example that build up
to it, in
[`05-meaning-as-geometry.md`](book/part-1-information/05-meaning-as-geometry.md#key-takeaway).

## Status

**The full manuscript, Parts I–VI (chapters 1–30), is written** —
Information, Prediction, The Transformer, Building Useful AI, AI Systems,
and AI in the Real World. The book builds understanding through stories, worked
examples, careful analogies, and precise technical explanation. See
[`book/README.md`](book/README.md) for the full chapter-by-chapter index
and status, and [`ROADMAP.md`](ROADMAP.md) for project-level milestones.
This is a first complete draft, not a finished, fully-validated book — see
"Editorial status and contributions" below.

## How the project is organized

| | |
|---|---|
| [`blueprint.md`](blueprint.md) | The founding design document — mission, audience, teaching philosophy, concept dependency graph, full table of contents. Read this first if you want the "why" behind every other file. |
| [`book/`](book/) | The manuscript itself, one file per chapter. Start at [`book/README.md`](book/README.md). |
| [`style-guide.md`](style-guide.md) | Voice conventions and the analogy registry (so an analogy is never reinvented under a different name in a later chapter). |
| [`templates/chapter-template.md`](templates/chapter-template.md) | The 11-section template every chapter is drafted against. |
| [`glossary.md`](glossary.md) | Running index of every term, in order of first appearance. |
| [`misconceptions.md`](misconceptions.md) | The misconception graph: one row per concept, its common misconception, and the correct intuition. |
| [`concept-graph.md`](concept-graph.md) / [`concept-graph.yaml`](concept-graph.yaml) | Checklist tracker over the blueprint's 9-level concept dependency graph — a concept may never appear in prose before its own level is checked off. The `.yaml` is the machine-readable source of truth (explicit per-concept prerequisites, introduced-in chapter, linked misconceptions); the `.md` is its human-readable mirror. |
| [`references/`](references/) | Lightweight per-chapter citation trail for empirical/historical claims, plus a master `bibliography.md`. |
| [`scripts/validate_concept_graph.py`](scripts/validate_concept_graph.py) / [`scripts/validate_manuscript_index.py`](scripts/validate_manuscript_index.py) | Run before committing changes to the concept graph or the chapter index: checks prerequisite ordering, dependency cycles, misconception-id references, and — separately — that `book/README.md`'s links and titles actually match the manuscript files on disk. |
| [`publish/`](publish/) | A local Quarto book project rendering the manuscript to HTML, EPUB, and PDF. See "Building the book" below. |

## Reading the built book

**[Read it online](https://alessandrobessi.github.io/the-architecture-of-intelligence/)**
— rebuilt automatically on every push to `main`. A PDF and EPUB of the
same build are attached to the repo's
[latest release](../../releases/tag/latest-build), also updated on every
push.

## Building the book locally

Requires [Quarto](https://quarto.org) and [Typst](https://typst.app)
(`brew install --cask quarto && brew install typst`). From the repo
root:

```sh
python3 scripts/prepare_manuscript_for_publish.py
cd publish && quarto render
```

Output lands in `publish/_book/` (an HTML site, an EPUB, and a PDF).
Nothing under `publish/chapters/` or `publish/_book/` is committed —
both are regenerated from `book/` on every run. This is a first complete
draft, not a professionally edited one — see "License" below before
sharing any output further.

## Editorial status and contributions

This is an early-stage, actively-drafted manuscript, not a finished book.
Expect factual claims, framing, and even structure (the chapter template,
the later table of contents) to be revised as the project gets feedback
from real readers. If you spot a technical error, a confusing explanation,
or a broken internal link, please open an issue — see
[`CONTRIBUTING.md`](CONTRIBUTING.md) for what's useful to report right now
and what isn't yet being accepted.

## License

See [`LICENSE`](LICENSE) — currently a provisional, all-rights-reserved
placeholder. Do not assume any reuse rights based on its current state.
