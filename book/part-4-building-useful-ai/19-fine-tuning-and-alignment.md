# Fine-Tuning and Alignment

**Part:** Building Useful AI

**Concept Level:** Level 5

**Prerequisites:** Chapter 9 (training, parameters), Chapter 13 (preview of fine-tuning/human feedback)

**New concepts introduced:** Fine-tuning, Alignment

---

## Opening Question

*How does additional training after pretraining actually work, and how does a model get pointed toward being safe and aligned with the goals its designers set for it?*

## Real-World Story

A doctor completes medical school — years of broad, general training,
covering an enormous range of conditions and cases. Then they enter a
residency in a specific specialty, say cardiology. The residency doesn't
throw out everything from medical school and start over; it reuses that
same underlying skill (diagnosing, reasoning from evidence, learning from
feedback on real cases) and applies it, intensively, to a much narrower
and more specific set of situations, with much more targeted correction
along the way.

Fine-tuning a language model works the same way. Pretraining (Chapter 9)
is medical school: broad, general, enormous in scope. Fine-tuning is the
residency: the same underlying learning mechanism, applied afterward to a
smaller, much more specifically curated set of examples, aimed at a
particular goal.

## Worked Example

Suppose a model is shown two candidate responses to a sensitive user
request, and a human rater is asked which one they prefer — perhaps one
response is more careful and appropriately cautious, the other more
blunt and less considerate of context. The rater picks the first.

This single preference judgment, multiplied across a huge number of
paired comparisons, becomes training data of a new kind: not "what token
comes next in this training text" (Chapter 9's original signal), but
"which of these two responses do humans actually prefer." That preference
data is used to further adjust the model's parameters — using the exact
same predict/measure-error/nudge loop from Chapter 9 — so that future
responses trend toward the style humans rated more highly.

## Core Intuition

**Fine-tuning** is continuing the training process (Chapter 9) on a new,
typically smaller and more specifically curated dataset, after the
large-scale pretraining phase is already complete. It reuses the exact
same predict/measure-error/adjust loop — nothing about the underlying
mechanism changes — only now it's aimed at a narrower goal, like following
instructions reliably, answering directly, or matching a particular
style, instead of generic text continuation.

**Alignment** is the broader goal fine-tuning (and related techniques) is
used to pursue: making a model's behavior actually match some set of
intended goals — helpful, honest, careful — rather than merely
"statistically plausible given training text," which, as Chapter 15
showed, doesn't automatically mean helpful or truthful. That phrase "some
set of intended goals" is doing real work: alignment is always relative
to particular objectives set by particular designers, evaluators, or
policies, and those can conflict with each other or with what any given
user wants in the moment — "aligned" is not a single, universally-agreed
target.

## Technical Explanation

Several broad techniques are widely used, often in combination.
**Supervised fine-tuning** trains directly on example input/output pairs
written or curated by humans, showing the model the desired style of
response explicitly. **Reinforcement Learning from Human Feedback
(RLHF)**, already previewed in Chapter 13, works differently and in two
steps: humans compare pairs of candidate model outputs and indicate which
they prefer; that preference data trains a separate model — a reward
model — to predict which of two responses a human would favor. The
original language model is then further adjusted, using Chapter 9's core
loss-reduction mechanism, but now using the reward model's predicted
preference as the error signal instead of raw next-token accuracy.

RLHF is an influential approach, but not the only way to use preference
data. Newer methods, broadly grouped under the name **direct preference
optimization**, adjust the language model directly from pairs of
preferred and rejected responses, without training a separate reward
model or running RLHF's full two-stage pipeline. The shared idea across
all of these methods is the same: shift the model toward outputs that
some evaluator — human or otherwise — prefers, using whichever specific
training procedure gets there.

Two more precisions matter. First, fine-tuning doesn't only reshape
surface style — it can also add, sharpen, or shift specific factual
associations and capabilities, not just tone. Second, "the underlying
architecture doesn't change" describes the most common and simplest case,
where every original parameter remains and gets further adjusted; some
fine-tuning methods instead freeze most of the original model and train a
small number of additional parameters (often called adapters) bolted onto
it, which changes the mechanics slightly while keeping the same basic
idea: reuse a pretrained model, adjust it further toward a narrower goal.

It's important to be precise about what this achieves. Alignment
techniques adjust a model's *output tendencies* to match patterns of
behavior that were rated favorably during training — this is a real,
measurable, and useful behavioral shift. It is not evidence that the
model has come to genuinely understand or agree with human values in any
deeper sense; that question echoes Chapter 2's original distinction
between mechanical computation and understanding, and remains
genuinely unresolved. Alignment is also an ongoing, actively researched
effort rather than a solved, one-time fix — a model can still behave in
subtly misaligned ways after this process, which is part of why Chapter
28 revisits safety directly.

## Common Misconceptions

### *"Fine-tuning and pretraining are fundamentally different kinds of processes."*

**Why it's wrong:** Fine-tuning reuses the identical predict/measure-error/adjust loop from Chapter 9 — the only thing that changes is the dataset and the specific goal it's aimed at, not the underlying mechanism.

**Correct intuition:** Fine-tuning is the same training process, applied again, to a different and usually smaller set of examples.

**Analogy:** A medical residency uses the same underlying learning process as medical school — observe, get corrected, adjust — just applied to a narrower set of cases.

### *"An aligned model has been made to genuinely understand and agree with human values."*

**Why it's wrong:** Alignment techniques adjust which outputs the model tends to produce, based on patterns rated favorably during training — a behavioral adjustment, not demonstrated evidence of genuine comprehension or agreement with the values behind those ratings.

**Correct intuition:** Treat "aligned" as a description of trained behavioral tendencies, not a claim about the model's inner understanding — a distinction worth holding onto rather than resolving prematurely.

**Analogy:** A well-trained customer service employee can reliably follow a company's values in every interaction without that proving they personally hold those values — the training shapes behavior either way.

## Practical Implications

This is exactly what "fine-tuned," "instruction-tuned," and "RLHF" mean
in AI product announcements, and it explains why a single company often
offers both a raw "base model" and a separate "chat" or "instruct"
version of the same underlying architecture (Chapter 13). It also
justifies a healthy skepticism toward marketing claims that a model has
been "fully aligned" or is "guaranteed safe" — alignment techniques are
genuinely useful and improving, but they remain an ongoing, imperfect
effort, not a completed guarantee.

## Key Takeaway

**Fine-tuning is Chapter 9's training loop applied again after pretraining, on a narrower goal; alignment is the broader aim that loop is pointed at — matching a model's behavior to some set of intended goals, not just what's statistically plausible.**

## One-Page Summary

- Fine-tuning reuses Chapter 9's core training loop on a smaller, more specifically curated dataset, after pretraining is complete.
- Alignment is the broader goal fine-tuning serves — matching model behavior to particular designers'/evaluators' intended goals, which can themselves conflict, not just statistically plausible continuations.
- Supervised fine-tuning trains directly on curated examples; RLHF trains a reward model from human preferences and adjusts the language model against it; direct preference optimization methods skip the separate reward model and adjust the language model straight from preference pairs.
- Fine-tuning can shift specific facts and capabilities, not just surface style, and some methods add small adapter components rather than adjusting every original parameter.
- Alignment adjusts output tendencies, not necessarily genuine understanding or agreement — a distinction worth holding onto rather than resolving.
- Alignment is an ongoing, imperfect, actively researched effort, not a one-time, completed fix.

## Further Reading

- Search for "InstructGPT" and "RLHF" for the research that formalized much of the fine-tuning and alignment approach described in this chapter, and "Direct Preference Optimization" (DPO) for a widely-used alternative that skips the separate reward model.

## The Next Obvious Question

*If a model can be fine-tuned to behave better, can it also be adjusted to run cheaper and faster, without retraining it from scratch or changing what it fundamentally knows?*

---

**Glossary terms added this chapter:** Fine-tuning (formal), Alignment, Supervised fine-tuning, RLHF (formal), Reward model, Direct preference optimization (DPO), Adapter (fine-tuning) → append to `/glossary.md`

**Misconceptions logged this chapter:** "fine-tuning and pretraining are fundamentally different"; "an aligned model genuinely understands/agrees with human values" → append to `/misconceptions.md`

**Concept-graph entries checked off:** Level 5 — Fine-tuning, Alignment, both at Ch. 19
