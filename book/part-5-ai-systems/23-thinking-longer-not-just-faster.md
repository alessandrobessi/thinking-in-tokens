# Thinking Longer, Not Just Faster

**Part:** AI Systems

**Concept Level:** Level 7

**Prerequisites:** Chapter 6 (prediction), Chapter 14 (sampling), Chapter 19 (fine-tuning)

**New concepts introduced:** Test-time compute, Reasoning models

---

## Opening Question

*So far, a model produces one predicted step at a time, whether working alone or looping through an agent. What happens when a model is specifically trained to spend more of its own generated text working through a problem before committing to a final answer?*

## Real-World Story

Two students face the same hard word problem in a math competition. The
first reads it and writes down an answer almost immediately — pattern
recognition, gut instinct, first thing that looks right. On genuinely
multi-step problems, this student is wrong more often than not, because
one small early slip carries through to the end unnoticed.

The second student works it out on scratch paper. She writes each step
out: what she knows, what she's computing next, and why. Partway through,
she sometimes catches herself — "wait, that's not right, let me redo this
part" — and corrects course before continuing. Only after laying out the
full chain does she commit to a final answer. Both students eventually
write down one number as their answer. But the second student's scratch
paper isn't just showing her work for the grader's benefit — it's the
actual process that got her to a reliable answer in the first place.

## Worked Example

Ask a model: "A store has 120 apples. It sells one third of them on
Monday, then one quarter of what's left on Tuesday. How many apples
remain?"

Asked to answer in one uninterrupted burst, a model predicting token by
token (Chapter 6) has to reach the final number without ever making an
intermediate result — like "80 apples remain after Monday" — available
as reusable context for later tokens; whatever internal computation gets
it there stays invisible and unchecked, and on a problem with more than
one dependent step, that raises the odds of a slip going unnoticed. Asked
instead to work through it step by step, the model might generate
something like: "Monday: 120 ÷ 3 = 40 sold, so 80 remain. Tuesday: 80 ÷ 4
= 20 sold, so 60 remain." Then it states the final answer: 60.

Nothing about the model's underlying mechanism changed between these two
attempts. What changed is that the second attempt made "80 apples remain
after Monday" into actual generated text — text that becomes part of the
context (Chapter 16) available when predicting the Tuesday step. The
second step is now a much easier, narrower prediction — "80 ÷ 4"— instead
of a single unbroken leap from the full question to a final number.

## Core Intuition

**Test-time compute** is spending additional computation at inference
time — beyond a single, one-shot prediction — to improve the odds of a
correct answer on a hard problem, trading more time and cost (Chapter 14,
Chapter 20) for more reliability. **Reasoning models** are the most
visible current way of doing this: models that generate explicit
intermediate reasoning text before a final answer, often specifically
trained to make good, extensive use of that reasoning space on genuinely
hard problems, rather than merely producing it because a prompt asked
nicely. Writing a longer chain of steps is one way to spend that extra
computation, but not the only one — generating several independent
attempts and checking them, or searching through alternative solution
paths, spend the same kind of extra computation in a different shape.
This chapter focuses on written, trained reasoning because it's
currently the most common and most product-visible instance of the
broader idea, not because it's the only one.

## Technical Explanation

The effect rests directly on autoregressive generation (Chapter 6): every
token a model generates, including an intermediate reasoning step, joins
the context window (Chapter 16) that every later token conditions on.
Writing "80 apples remain" isn't cosmetic scratch work performed
somewhere else and then transcribed — it's new context that makes the
next prediction narrower and more tractable than trying to solve the
whole problem in one silent internal leap. This is the same underlying
mechanism behind "chain-of-thought" prompting, which produced this
accuracy improvement in ordinary models simply by asking them, in the
prompt, to reason step by step before answering.

Reasoning models take a further step past relying on a prompt asking
nicely, though the exact training recipe varies by model and isn't
always publicly disclosed. Some publicly documented reasoning-optimized
models are trained, building on Chapter 19's fine-tuning and reinforcement-learning
machinery, with an outcome-based signal that reinforces reasoning-plus-
answer trajectories leading to a correct final answer — sometimes
combined with supervised examples of good reasoning, feedback on
intermediate steps rather than only the final answer, or distillation
from a stronger model's own reasoning. Whatever the specific mix, the
model learns, from many practice problems, how to use extra reasoning
tokens productively rather than merely verbosely. This is also why these
models can use noticeably more tokens on a hard problem and far fewer on
an easy one — reasoning length becomes something the model itself
adjusts based on the problem, not a fixed amount fixed by a prompt
template.

Written, trained reasoning isn't the only shape test-time compute takes.
A system can instead generate several independent candidate answers to
the same problem — using the sampling randomness Chapter 14 already
covered, so different attempts genuinely differ — and then select among
them, whether by taking whichever answer the most candidates agree on or
by using a separate check to score and filter them. Alternatively, a
system can search through multiple partial solution paths, using a
verifier to catch a bad step early and try a different continuation
instead of committing to the first path generated all the way through.
Both spend more inference-time computation than a single one-shot
prediction, exactly like a longer written chain does, just distributed
across width (many attempts) or backtracking (checked, revisable paths)
rather than length. None of these require a readable chain of steps at
all — which is exactly why "test-time compute" is the more durable term
for the underlying idea, and "reasoning model" names one popular way of
spending it.

It's worth being precise about what hasn't changed in any of these. A
reasoning model isn't running some different decoding primitive behind
the scenes. Every reasoning token is produced by the identical
next-token-prediction mechanism as every other token this book has
covered — visible reasoning steps included. What's different is that
training has built a strong, specifically reinforced capacity to use
that extra generated text productively, and system design organizes more
inference-time computation around difficult problems — not that a
different underlying generation mechanism has appeared. The same is true
of the wider and
search-based variants: more computation, organized differently, on top of
the same generation mechanism throughout — not a different kind of
system underneath.

## Common Misconceptions

### *"A reasoning model is deliberately thinking behind the scenes, the way a person reflects before speaking."*

**Why it's wrong:** Every reasoning token is generated by the same autoregressive next-token prediction mechanism (Chapter 6) as any other token this book has covered. Mechanically, the "thinking" is the visible (or hidden-but-still-generated) token sequence itself, produced by generation — not a separate process running somewhere else that generation merely reports on.

**Correct intuition:** What's different about a reasoning model isn't a new kind of internal process — it's that generating and reinforcing useful intermediate steps has been specifically trained, changing what gets generated, not how generation fundamentally works.

**Analogy:** The second student isn't running some fundamentally different kind of brain than the first — she's using the same mind to actually write out the steps, and that act of writing is itself what improves the outcome.

### *"Longer reasoning always means a more correct answer."*

**Why it's wrong:** More reasoning tokens increase the chance of catching and fixing an error on a genuinely hard, multi-step problem, but each reasoning step is still produced by the same fallible generation process covered in Chapter 15 — reasoning text can itself state a wrong intermediate step confidently, and excessive reasoning on a simple problem can introduce unnecessary uncertainty rather than resolve it.

**Correct intuition:** More reasoning space raises the odds of a correct answer on hard problems; it doesn't guarantee one, and it isn't free or automatically beneficial on easy ones.

**Analogy:** A student who reasons carefully on a genuinely hard problem does better than one who blurts an answer — but a student who overthinks a trivially simple question can talk themselves into the wrong answer.

### *"The reasoning a model prints out is a transparent, fully accurate window into its actual internal computation."*

**Why it's wrong:** Printed reasoning text is generated the same way as any other output, and it does causally shape the final answer by becoming part of the context (§5) — but that's a different claim from the printed trace being a guaranteed, faithful report of everything actually happening inside the model's computation. The two can diverge.

**Correct intuition:** Visible reasoning genuinely influences the final answer, which is useful and real — but treat it as the model's stated reasoning, not a verified, complete transcript of its internal process.

**Analogy:** A student's scratch paper reliably shapes what she writes next, and is worth reading — but it's her account of her thinking, not a machine readout of every neuron that fired along the way.

## Practical Implications

This is the mechanism behind "reasoning mode," "extended thinking," or "thinking longer" toggles in current AI products — an explicit tradeoff between latency/cost and accuracy on harder problems, directly connected to Chapter 14's and Chapter 20's inference-cost concepts. It's why reasoning models are emphasized specifically for math, coding, and multi-step logic tasks, and are often unnecessary overhead for simple factual lookups a single prediction handles fine. And it's a direct reason not to treat a model's visible reasoning trace as a guaranteed explanation of its behavior when something goes wrong — useful evidence, not proof.

## Key Takeaway

**Spending more inference-time computation — whether as a longer written chain, several checked candidate attempts, or a searched set of paths — trades time and cost for a higher chance of getting hard, multi-step problems right; a reasoning model's written chain is the most visible way of doing this, not the only one.**

## One-Page Summary

- Test-time compute is spending additional computation at inference time, beyond a single one-shot prediction, to improve reliability on hard problems.
- Reasoning models generate explicit intermediate steps before a final answer, often trained with some combination of outcome-based reinforcement learning, supervised reasoning examples, process-level feedback, or distillation (building on Chapter 19) to use that space productively — the most visible current instance of test-time compute, not the only one.
- This works because every generated token, including reasoning steps, becomes context for later tokens (Chapter 6, Chapter 16) — writing out a step makes the next prediction narrower and more reliable than one unbroken leap.
- Generating multiple candidate answers and selecting among them, or searching through alternative paths with a verifier, spend the same kind of extra computation in a different shape — wider or checked, rather than longer.
- No different decoding primitive is involved in any of these — every reasoning token is produced by the same next-token prediction mechanism as any other output, with training and system design organizing more inference-time computation around the problem.
- More reasoning tokens raise the odds of a correct answer on hard problems but don't guarantee one, and can be unnecessary or even counterproductive on easy ones.
- A model's printed reasoning trace genuinely shapes its final answer but isn't a guaranteed, fully faithful transcript of its actual internal computation.
- This underlies "reasoning mode" / "extended thinking" toggles — an explicit latency/cost-versus-accuracy tradeoff.

## Further Reading

- Search for "chain-of-thought prompting" for the original prompting-based version of the effect described in §5.
- Search for "chain-of-thought faithfulness" for ongoing research on how closely a model's stated reasoning tracks its actual computation, directly relevant to §6's third misconception.
- Search for "test-time compute scaling" or "best-of-N sampling" for the broader family of techniques — width and search, not just length — described in §5.
- Search for "DeepSeek-R1" for one publicly documented example of outcome-based reinforcement learning on reasoning trajectories — one real recipe among several §5 describes, not the only one.

## The Next Obvious Question

*So far, every model in this book has read and written nothing but text. How does a model built entirely around predicting the next token learn to also make sense of an image or a sound?*

---

**Glossary terms added this chapter:** Test-time compute, Reasoning model, Chain-of-thought → append to `/glossary.md`

**Misconceptions logged this chapter:** "a reasoning model is deliberately thinking behind the scenes"; "longer reasoning always means a more correct answer"; "printed reasoning is a transparent window into internal computation" → append to `/misconceptions.md`

**Concept-graph entries checked off:** Level 7 — Reasoning models, at Ch. 23
