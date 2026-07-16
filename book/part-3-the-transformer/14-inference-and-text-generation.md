# Inference and Text Generation

**Part:** The Transformer

**Concept Level:** Level 4

**Prerequisites:** Chapter 6 (prediction), Chapter 12 (transformer blocks)

**New concepts introduced:** Inference, Sampling

---

## Opening Question

*Once a model has all this training baked in, what actually happens, step by step, when it generates a response to your prompt?*

## Real-World Story

A medical student spends years in school: studying, practicing, getting
things wrong, being corrected, adjusting — precisely the training loop
from Chapter 9, repeated across an enormous number of cases. Then, on the
day of the licensing exam, something changes. The studying is over. The
student can't look anything up, can't revise their underlying knowledge
mid-exam, can't get corrected and try again. They simply apply everything
they've learned, in the moment, to whatever specific questions appear on
the page in front of them.

The knowledge itself is now fixed — nothing about the exam changes what
the student actually knows. What varies, question to question, is only
how that fixed knowledge gets applied to each specific case. A trained
language model works the same way once training ends: its parameters are
frozen, and every response is that fixed knowledge being applied, fresh,
to whatever specific prompt just arrived.

## Worked Example

Take the prompt "The weather today is" and run it through a trained
model three separate times. Chapter 6 already established that the model
computes a probability distribution over every possible next token — but
it did not specify how one specific token actually gets chosen from that
distribution each time.

If the model always took the single highest-probability token, all three
runs would produce the identical continuation — perhaps "The weather
today is nice," every single time, which is accurate but monotonous, and
prone to visibly looping in longer generations ("nice. The weather today
is nice. The weather today is nice..."). Instead, a model can sample
somewhat randomly among the likely candidates, weighted by their
probability — so the three runs might produce "sunny," "cold," and
"perfect for a walk." None of these is wrong. They're three different,
individually reasonable draws from the same underlying distribution.

## Core Intuition

**Inference** is the process of actually running a trained model to
produce output, using its fixed, already-learned parameters — as opposed
to training (Chapter 9), where those parameters are still being adjusted.
Once training ends, the parameters are frozen; inference is simply
computing forward through the network — embeddings (Chapter 5), attention
and refinement through transformer blocks (Chapters 11–12), and a
next-token probability distribution (Chapter 6) — using those fixed
values, one token at a time.

**Sampling** is the specific method used to actually pick one token,
starting from the model's predicted probabilities at each step. The
options range from always taking the single most likely token
(deterministic, and often repetitive) to sampling more broadly among
likely candidates (more varied and natural-feeling, at some risk of an
occasional odd choice) — and, as the next section makes precise, most
practical sampling methods don't just choose from the model's raw
predicted probabilities unmodified; they first reshape that distribution
before drawing from it.

## Technical Explanation

Precisely: none of these controls change the model's parameters, and none
of them rerun training — that much is fixed the moment inference begins.
But they do genuinely reshape the distribution actually sampled from,
rather than leaving the model's raw predictions untouched and merely
changing the selection rule applied to them.

A control commonly called **temperature** rescales the model's raw
predicted scores before they're converted into probabilities, which
changes the resulting distribution's shape. Low temperature sharpens the
distribution, concentrating most of the probability on the single most
likely token or a small handful of top candidates — closer to always
picking the top answer. High temperature flattens the distribution,
spreading probability more evenly across a wider range of candidates,
including some riskier ones, producing more varied but occasionally less
careful output. Related techniques called **top-k** and **nucleus (top-p)
sampling** go further: they truncate the distribution outright, discarding
everything outside the most plausible handful of candidates (top-k), or
outside the smallest set of candidates whose combined probability crosses
a chosen threshold (nucleus sampling), and then renormalize what remains
into a fresh probability distribution before sampling from it.

So the accurate way to put it: the model's underlying parameters and
training (Chapter 9) are completely fixed during inference — that part
never changes. What temperature, top-k, and nucleus sampling change is
the distribution actually used for sampling at each step, computed *from*
the model's raw output, not identical to it.

## Common Misconceptions

### *"The model is still learning or improving while I chat with it."*

**Why it's wrong:** Unless a system is specifically built to retrain on conversations (unusual, and typically a separate process), inference uses frozen parameters — nothing about a conversation changes the model's underlying trained knowledge.

**Correct intuition:** What grows during a conversation is the context available to the model (Chapter 16), not the model's trained parameters themselves.

**Analogy:** A doctor taking your case history during an exam isn't relearning medicine — they're applying fixed training to new, specific information.

### *"Since it's the same model and the same prompt, it should give the exact same answer every time."*

**Why it's wrong:** Unless sampling is explicitly configured to always pick the top choice, controlled randomness is part of the design — repeating the same prompt can, and often does, yield different, still-reasonable responses.

**Correct intuition:** Identical inputs can produce different outputs by design, because sampling deliberately introduces choice among plausible candidates rather than always taking the single most likely one.

**Analogy:** Asking three different (equally excellent) writers to finish the same sentence naturally produces three different, all-reasonable endings.

## Practical Implications

This is exactly what a "temperature" slider or setting in an AI tool or
API controls directly. It also explains a genuine, recurring business and
engineering distinction: training is an enormous, largely one-time cost
per model, while inference is a smaller cost paid again every single time
anyone actually uses the model — a distinction that shows up constantly
in discussions of AI infrastructure costs, and one that becomes
especially important once Chapter 20 covers making inference cheaper and
faster.

## Key Takeaway

**Inference is running a trained, frozen model to produce output; sampling is the deliberately controllable randomness in how a specific token gets chosen from the model's predicted probabilities.**

## One-Page Summary

- Inference is using a trained model's fixed parameters to produce output — as opposed to training, where parameters are still being adjusted.
- Sampling is the method for choosing one actual token from the model's predicted probability distribution at each step.
- Temperature rescales the model's raw predicted scores before sampling, sharpening or flattening the resulting distribution; top-k/nucleus sampling truncates and renormalizes it, discarding implausible candidates outright.
- None of this changes the model's parameters or reruns training — but it does genuinely reshape the distribution actually sampled from, not just the rule for picking from an untouched one.
- Identical prompts can produce different, equally valid outputs by design, because of this controlled randomness.
- Training is a large, mostly one-time cost; inference is a smaller, recurring cost paid every time the model is used.

## Further Reading

- Search for "temperature sampling" and "nucleus sampling" (top-p sampling) for the formal names of the techniques described in this chapter.

## The Next Obvious Question

*If the model is just sampling plausible-sounding tokens, what happens when "plausible-sounding" and "actually true" come apart?*

---

**Glossary terms added this chapter:** Inference, Sampling, Temperature, Top-k / nucleus sampling → append to `/glossary.md`

**Misconceptions logged this chapter:** "the model keeps learning during conversation"; "same prompt should always give the same answer" → append to `/misconceptions.md`

**Concept-graph entries checked off:** Level 4 — Inference, Sampling, both at Ch. 14
