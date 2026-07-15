# The Architecture of Intelligence

### A Mental Model for Modern AI Systems

A conceptual introduction to how modern AI actually works — tokens,
embeddings, attention, transformers, training, hallucination, retrieval,
tool use, agents, reasoning models — written for curious, intelligent
readers with **no math, no programming, and no prior ML background**.

Most explanations of AI are either marketing ("it's magic") or academic
(equations first, intuition never). This project tries to do what
[SICP](https://mitp-content-server.mit.edu/books/content/sectbyfnid/8090/sicp.zip/index.html)
did for computer science and what the *Feynman Lectures* did for
physics: build one durable mental model, incrementally, that keeps
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

> **Embeddings place words as points in a high-dimensional space, where
> nearby points mean similar usage and consistent directions capture
> consistent relationships.**

See it in full context, with the story and worked example that build up
to it, in
[`05-meaning-as-geometry.md`](book/part-1-information/05-meaning-as-geometry.md#8-key-takeaway).

## Status

**Parts I and II (chapters 1–10, "Information" and "Prediction") are
written.** The book builds understanding through stories, worked examples,
careful analogies, and precise technical explanation. Parts III–VI exist
only as a planned table of contents. See [`book/README.md`](book/README.md)
for the full chapter-by-chapter index and status, and
[`ROADMAP.md`](ROADMAP.md) for project-level milestones.

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
| [`testing/`](testing/) | The reader-validation protocol: methodology, scoring rubric, and a per-chapter question bank (comprehension, transfer, misconception resistance, retention). Ready to run, pending recruiting actual test readers. |

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
