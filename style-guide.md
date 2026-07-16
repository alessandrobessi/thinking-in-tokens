# Style Guide

Shared conventions for prose and voice across every chapter. This file is
written once and reused unchanged across all 30 chapters — do not fork
per-part variants. When Parts III–VI are drafted in later passes, they
follow these exact rules; the only thing that grows is the analogy
registry (§3).

This project does not use diagrams — see blueprint.md's "No Diagrams"
section for why, and don't reintroduce an SVG/icon system without
revisiting that decision explicitly.

---

## 1. Voice

- Write to an intelligent, curious, non-technical reader — a manager, founder,
  consultant, or student. Never assume math, programming, or ML background.
- Intuition before terminology: introduce the idea in plain language, *then*
  attach the technical name to it, never the reverse.
- One genuinely new idea per page. If a paragraph needs a reader to hold two
  new concepts at once, split it.
- Every idea gets at least two concrete groundings before moving on — the
  opening story plus the worked example, at minimum (template §2/§3). One
  telling is a claim; a second telling from a different angle is what
  actually makes it stick. This is what replaced diagrams as the book's
  primary "does this really sink in" mechanism.
- Prefer short, concrete sentences over qualified, abstract ones. Cut hedges.
- A technical explanation must still be *correct* — simplify by revealing the
  essential mechanism, never by stating something false that's "close enough."
- Every explanation should pass the Feynman test: if a curious 12-year-old
  friend asked "wait, why?", does the next sentence already answer it?
- Reuse analogies deliberately (see §3, Analogy Registry). Introducing a new
  analogy for a concept that already has one elsewhere in the book is a bug,
  not a stylistic choice — check the registry before writing one.

## 2. Chapter Mechanics

- Every chapter must substantively cover all 11 elements of
  `templates/chapter-template.md` — completeness is mandatory, but per
  blueprint.md's amended "Standard Chapter Template" section, the
  reader-facing presentation is not. During this drafting phase, every
  chapter still uses the 11 headers verbatim, in order, because that makes
  completeness trivial to verify chapter by chapter. Loosening the visible
  headers into freer prose is a deliberate later editorial pass, not
  something to improvise chapter by chapter now — doing it piecemeal would
  make the 11-point completeness check unreliable across 30 chapters.
- §3 (Worked Example) and §8 (Key Takeaway) are text-only — no images, no
  diagrams. §3 is a second, fully-written concrete example distinct from
  the opening story, not a recap of it. §8 is one bolded sentence, not a
  paragraph.
- Every chapter answers exactly one question from the Narrative Graph
  (blueprint.md, "Narrative Graph" section) and ends by provoking the next.
  §11 of chapter N and §1 of chapter N+1 must express the same question.
- Never introduce a concept before its prerequisites (blueprint.md, "Concept
  Dependency Graph"). The test: does the sentence require the reader to
  already understand *how* the later concept works to parse it correctly?
  If yes, that's a violation, even if the concept's name is never used
  (e.g. Chapter 1 originally said older architectures "process a sentence
  one piece at a time instead of weighing an entire passage at once" to
  explain *why* a 2022-scale comparison failed — using attention's
  mechanism to justify a claim, four chapters before attention exists). A
  bare forward-pointer is fine and is used deliberately elsewhere in the
  book — naming a future concept only to say "that's the subject of
  Chapter N" (see Ch. 5's and Ch. 8's handling of "attention"/"the
  transformer"), with no claim resting on the reader already grasping how
  it works. If a chapter needs more than a bare pointer, cut it instead of
  half-explaining it.
- After finishing a chapter, immediately: add its new terms to `glossary.md`,
  its misconceptions to `misconceptions.md`, check off its concepts in
  `concept-graph.md`, and add any new analogy to the registry below. Do this
  per chapter, not batched — batching is how these files silently drift.

## 3. Analogy Registry

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
| Marathon training's diminishing returns | Scaling laws (predictable but diminishing) | Ch. 10, reused Ch. 29 | Reused in Ch. 29's "AI progress isn't guaranteed to continue at the same pace" misconception — same underlying point (diminishing returns), new context. |
| Counterfactual: swap one of three ingredients out | "All three ingredients are necessary, none sufficient alone" | Ch. 1 | A reusable move, not just an analogy — pair a concept's real example with "what if only two of the N factors were present?" |
| Thermostat mechanically deciding without awareness | Computation without understanding | Ch. 2 | Second grounding alongside the vending-machine misconception analogy — simpler and more universally familiar. |
| Rain forecast: vague-long-term vs. specific-near-term | Information as uncertainty reduction, not length | Ch. 2 | Reader-facing "try it yourself," not just expository — reuse this move (see counterfactual note above) for other counterintuitive quantities later in the book. |
| Rare/invented word ("quokka") tokenized into familiar pieces | Tokenization's graceful fallback on unfamiliar input | Ch. 3 | Reuse for any future chapter discussing out-of-vocabulary or rare-input handling (e.g. multimodal tokenization, Ch. 24). |
| Slang double meaning ("sick" = great vs. ill) | Context disambiguation | Ch. 4 | Second grounding alongside bank/river — deliberately a different generation/register of language. |
| Gender offset (king→queen, actor→actress) | Semantic geometry / consistent relationship directions | Ch. 5 | Second grounding alongside capital-of — keep both equally hedged as "illustrative, not universal." |
| Hiring committee weighing the same facts differently | Neural network units / weighted combination | Ch. 8 | Second grounding alongside the valve factory — a social/business framing for readers who find the mechanical one less intuitive. |
| Adjusting a recipe by taste | Training loop (predict, measure error, nudge, repeat) | Ch. 9 | Second grounding alongside free throws — reuse for fine-tuning (Ch. 19) alongside the free-throw analogy. |
| Fertilizer and crop yield (diminishing returns) | Scaling laws | Ch. 10 | Second grounding alongside marathon training — an economics framing likely to land well with the book's manager/consultant readers. |
| Winograd sentence pair ("too big" / "too small" flips what "it" refers to) | Attention (selective, weighted relevance) | Ch. 11 | A real, well-known linguistic example; concrete and self-contained. |
| Conductor attending to a whole ensemble at once | Attention is parallel weighing, not sequential reading | Ch. 11 | Reuse if a later chapter needs a "whole-picture-at-once" framing distinct from reading metaphors. |
| Manuscript passed through many rounds of editing | Transformer blocks (stacked refinement) | Ch. 12 | Ties naturally to Ch. 9's "loop, industrialized" language — refinement happening repeatedly, each round building on the last. |
| Quiz-list continuation vs. direct answer | Pretraining vs. fine-tuned/aligned behavior | Ch. 13 | Concrete, testable example distinguishing base-model behavior from chat-model behavior. |
| Medical school (pretraining) → residency (fine-tuning) | Fine-tuning as continued training on a narrower goal | Ch. 13, reused Ch. 19 | Deliberately reused across both chapters — same domain, same point, two different depths of treatment. |
| Exam analogy: studying (training) vs. sitting the exam (inference) | Training vs. inference (fixed, frozen parameters) | Ch. 14 | Reuse this exact domain for Ch. 18's "open-book exam" (RAG) — a deliberate, connected pair of analogies across two chapters. |
| Open-book exam (reference pages handed over at the last minute) | RAG (retrieved passages inserted into context) | Ch. 18 | Explicitly built on Ch. 14's exam analogy — don't treat as a fresh, unrelated analogy. |
| Real 2023 case of fabricated legal citations | Hallucination | Ch. 15 | A true, documented incident — treat as a real-world citation, not an invented example; verify details before reuse. |
| Sticky notes / limited desk space | Context window (fixed-size, oldest gets dropped) | Ch. 16 | Reuse if a later chapter needs a "fixed capacity, oldest displaced" framing. |
| Librarian organizing books by meaning, not title | Retrieval / semantic search | Ch. 17 | Directly extends Ch. 5's cities-on-a-map analogy to passage-level embeddings — not a fresh analogy, a continuation of it. |
| RAW photo vs. JPEG | Quantization (coarser precision, barely noticeable loss) | Ch. 20 | Reuse if a later chapter needs a "practical precision vs. fidelity" tradeoff framing. |
| Analyst phoning a trading-floor colleague for a live stock price | Tool calling (structured request, external execution, result returned) | Ch. 21 | Distinguishes tool calling from RAG's static-document retrieval (Ch. 18) — the request can trigger a live lookup or action, not just fetch existing text. |
| Standardized electrical outlet (any compliant appliance, any compliant socket) | MCP (connection standard, not a capability) | Ch. 21 | Reuse if a later chapter needs a "shared plug shape doesn't add power" framing for another standard/protocol. |
| New employee given a goal, not a checklist ("get the numbers ready") | AI agents (self-directed multi-step loop) | Ch. 22 | Distinguishes agentic looping from a fixed, pre-scripted sequence of tool calls — the employee decides her own next step from what she just found. |
| Tourist showing a photo instead of describing a street in words | Multimodality (different formats bridged to the same understanding) | Ch. 24 | General motivating story for the bridging problem itself, kept architecture-agnostic (extends Ch. 5's cities-on-a-map framing without committing to one specific bridge). |
| Suspension bridge vs. tunnel (same river, structurally different crossings) | Multimodality (multiple real architectural patterns, not one universal recipe) | Ch. 24 | Reuse if a later chapter needs a "same capability, genuinely different underlying implementations" framing. |
| Hospital with many specialists; a triage nurse routes each patient to one or two | Mixture of Experts (total capacity vs. per-token active cost) | Ch. 25 | Reuse (law firm, second grounding, same chapter) if a later chapter needs a "large collective capacity, small per-instance cost" framing. |
| Hiring manager whose coding quiz stops predicting job performance once candidates study the quiz itself | Evaluation (proxy vs. target, Goodhart's law) | Ch. 26 | Concrete, relatable grounding for benchmark contamination/overfitting; reuse if a later chapter needs a "measurement stops working once it becomes the target" framing. |
| Pilot's pre-flight checklist vs. continuous in-flight instruments | Observability (one-time evaluation vs. continuous production monitoring) | Ch. 27 | Reused within the chapter (misconceptions §6) for "checklist verifies fitness to fly; instruments track live conditions" — a durable pairing if a later chapter needs a "one-time gate vs. ongoing monitoring" framing. |
| Executive assistant reading mail aloud, tricked by an instruction embedded in a letter | Security / prompt injection (no built-in instruction-vs-content distinction) | Ch. 28 | Concrete, relatable grounding for why a model can't reliably tell trusted instructions from content it's merely processing. |

(Table grows chapter by chapter; append immediately after finishing a chapter
that introduces a new analogy — see §2.)
