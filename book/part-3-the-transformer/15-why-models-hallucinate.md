# Why Models Hallucinate

**Part:** The Transformer

**Concept Level:** Level 5

**Prerequisites:** Chapter 9 (training), Chapter 14 (inference, sampling)

**New concepts introduced:** Hallucinations

---

## Opening Question

*If the model is just sampling plausible-sounding tokens, what happens when "plausible-sounding" and "actually true" come apart?*

## Real-World Story

In 2023, a lawyer submitted a legal brief citing several past court
cases to support his argument. The citations looked completely
legitimate: proper formatting, plausible party names, plausible courts
and years. The problem was that the cases didn't exist. He had used an AI
chatbot to help research the brief, and it had generated citations that
looked exactly like real legal citations — because it had learned,
extremely well, what real legal citations look like — without those
specific cases ever having existed.

The system wasn't lying, in the sense of intending to deceive. It was
doing precisely what Chapter 6 described: producing a highly plausible
continuation of text, given the patterns in its training data. In this
case, "plausible-sounding legal citation" and "citation of a real case"
had quietly come apart, and nothing in the generation process itself
flagged the difference.

## Worked Example

Ask a model to produce a citation for a specific, narrow legal question.
It has, across enormous amounts of legal text, thoroughly learned the
*pattern* a citation takes: party name, "v.," another party name, court,
year, volume and page number, all in a familiar, recognizable format.
Producing a token sequence that matches this pattern fluently is exactly
what next-token prediction (Chapter 6) is built to do well — it doesn't
require this specific case to be real, only that the sequence be
statistically consistent with what citations generally look like.

Nothing in the training objective from Chapter 9 directly rewards "and
also, verify this specific case actually exists in the real world" as a
separate step. The model was trained to predict likely next tokens given
patterns in text, not to cross-check every generated claim against an
external record of what's real. For extremely common, heavily-repeated
facts, this rarely matters, because the true fact is also the
overwhelmingly likely continuation. For a rare, specific, or nonexistent
case, without specific training aimed at handling exactly this situation
(Chapter 19 covers this), the model has no strong built-in pull toward
stopping, refusing, or flagging uncertainty instead of continuing — so it
commonly fills the gap with a plausible-looking fabrication rather than a
flagged absence.

## Core Intuition

A **hallucination** is generated output that is factually wrong or
unsupported — fabricated, misremembered, or simply unconnected to any
real source — regardless of how confidently it's phrased. Confident,
fluent delivery is the most attention-grabbing case, but a model can
hallucinate while sounding tentative too; confidence of phrasing and
accuracy of content are produced by the same process and aren't reliably
linked. Explaining this behavior doesn't require assuming deception:
next-token prediction (Chapter 6) optimizes for statistical plausibility
given training-data patterns, and the generation process has no reliably
exposed, independent record of factual belief that it consults — no
separate fact-checking step weighing "is this actually true" against the
outside world — before producing each claim.

## Technical Explanation

Connect this directly back to training (Chapter 9): the training
objective rewards predicting the next token accurately *relative to the
training text*, not relative to ground truth about reality. For
well-represented, heavily-repeated facts — "the capital of France is
Paris" — this distinction rarely bites, because the correct fact is also
the overwhelmingly common continuation across virtually all relevant
training text, so statistical plausibility and truth line up.

For rare, obscure, or entirely nonexistent facts — a specific, uncommon
court case, a specific minor historical date, a citation for a paper that
doesn't exist — the alignment between "statistically plausible" and
"actually true" breaks down. Chapter 14's sampling step still has to
select *some* token at each position, but stopping, declining, or flagging
uncertainty are themselves valid tokens to select, not exceptions to the
process. What actually happens depends on training: unless the model has
been specifically trained or aligned (Chapter 13's preview, Chapter 19's
full treatment) to prefer expressing uncertainty or declining to answer in
exactly these situations, sampling has no particular reason to favor
those options over a fluent, confident-sounding fabrication — so, left to
that default, it commonly produces one instead of a flagged absence.

## Common Misconceptions

### *"Hallucination is a rare bug that will simply get fixed as models improve."*

**Why it's wrong:** It's less a discrete defect than a structural risk of generation systems that optimize for a fluent, confident-sounding continuation without reliable grounding or verification against the separate goal of only stating things that are true — a risk arising from how standard next-token generation works, not a simple coding error, and not necessarily one every future system design must share.

**Correct intuition:** Mitigations exist and genuinely help (better alignment, retrieval-augmentation in Chapters 17–18, improved calibration of uncertainty), but treat hallucination as an ongoing tradeoff to manage, not a bug awaiting a final patch.

**Analogy:** A student trained their whole life to always give a confident-sounding answer on every exam question will keep bluffing convincingly on the questions they don't actually know, even after years of additional coaching — the tendency has to be specifically retrained, not merely reduced by getting generally smarter.

### *"The model knows it's making something up and is choosing to deceive."*

**Why it's wrong:** There's no separate module tracking "what I actually know is true" apart from "what token comes next" — it's the same fluent generation process whether the content happens to be accurate or fabricated. Some research suggests a model's internal computations can carry information correlated with how likely a claim is to be wrong, but normal generation doesn't reliably surface that signal as a calibrated statement of uncertainty — so confident phrasing still isn't a dependable indicator of accuracy in practice.

**Correct intuition:** Confident phrasing and factual accuracy are produced by the same process but aren't reliably linked in the final output — one doesn't guarantee the other, even if some trace of "how sure" exists somewhere inside the computation.

**Analogy:** A fluent public speaker can sound equally confident whether reciting a well-verified fact or a half-remembered detail — confidence of delivery and accuracy of content are simply different things.

## Practical Implications

This is precisely why giving a model access to real source documents to
draw from — retrieval-augmented generation, covered in Chapters 17–18 —
is such a widely used mitigation: it gives the model something concrete
to ground its answer in, rather than relying purely on trained-in
patterns for rare or specific facts. It's also the direct reason
practitioners are consistently told to verify AI-generated facts and
citations, especially for anything rare, specific, or high-stakes, and
why hallucination rates differ noticeably between well-represented common
knowledge and obscure or narrow topics.

## Key Takeaway

**Hallucination isn't the model lying — it's next-token prediction continuing exactly as designed, without a reliable fact-checking step, in a case where statistical plausibility and factual truth have quietly come apart.**

## One-Page Summary

- A hallucination is factually wrong or unsupported output — it doesn't require confident phrasing, though confident delivery is the most noticeable case.
- Next-token prediction (Chapter 6) optimizes for statistical plausibility relative to training text, not for truth about the real world.
- For common, heavily-repeated facts, plausibility and truth usually align; for rare or nonexistent facts, they can come apart.
- Standard generation has no reliable, separate mechanism checking "sounds right" against "is actually true," unless a model has been specifically trained to handle exactly this case.
- Retrieval-augmented generation (Chapters 17–18) is a major practical mitigation, giving the model real source material to ground answers in.
- Hallucination is best treated as an ongoing, manageable tradeoff rather than a simple bug awaiting a final fix.

## Further Reading

- Look up *Mata v. Avianca, Inc.* (S.D.N.Y. 2023) for the full documented record of the fabricated-citations incident referenced in this chapter's story, and other real, verifiable examples of this failure mode in practice.
- Search for "survey of hallucination in natural language generation" for a broader treatment of hallucination's causes and mitigations across the field, beyond this chapter's conceptual introduction.

## The Next Obvious Question

*If a model's own trained-in knowledge can run out or go stale, how can it be given a bigger, more reliable memory to draw from?*

---

**Glossary terms added this chapter:** Hallucination → append to `/glossary.md`

**Misconceptions logged this chapter:** "hallucination is a rare bug that will get fixed"; "the model knows it's making things up" → append to `/misconceptions.md`

**Concept-graph entries checked off:** Level 5 — Hallucinations, at Ch. 15 (closes Part III)
