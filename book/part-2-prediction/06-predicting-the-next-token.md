# Predicting the Next Token

**Part:** Prediction

**Concept Level:** Level 3

**Prerequisites:** Chapter 2 (probability), Chapter 5 (embeddings)

**New concepts introduced:** Prediction

---

## Opening Question

*Now that a computer can represent meaning as a location in space, how can it use that to predict what comes next?*

## Real-World Story

Type the start of a text message on almost any phone, and a small row of
suggested words appears above the keyboard: "I'll be there in about..." and
the keyboard offers "5," "10," "an hour." It isn't reading your mind. It's
doing something much narrower: given everything you've typed so far, it's
ranking every word it knows by how likely that word is to come next, and
showing you the top few.

A modern language model does exactly this — just far more capably, and not
just for the next word, but for the word after that, and the word after
that, one at a time, each new prediction taking into account everything
generated so far, including its own previous guesses. A full paragraph
isn't planned in advance and then written down. It's built one token at a
time, the same small act — "what's the most likely next piece?" — repeated
until a stopping point is reached.

## Worked Example

Take the sequence "The capital of France is ___." A model ranks every
token in its vocabulary by how likely it is to fill that blank. "Paris"
gets an overwhelming share of the probability — call it the vast
majority. "Lyon" (a real French city, just not the capital) gets a
sliver. "a" gets an almost-vanishing amount, since it's grammatically
implausible there. "Banana" gets a probability so close to zero it might
as well not exist as an option.

These numbers aren't retrieved from a table of complete, stored answers.
They're computed from the current sequence using the model's learned
parameters (Chapters 8–9) — the geometry of Chapter 5 is where that
computation starts, not the whole of it. Some specific facts or phrasings
can end up memorized during training, a nuance Chapter 9 returns to — but
the computation itself is still performed fresh over the current
sequence every time, not looked up whole.

## Core Intuition

**Prediction**, in this technical sense, means assigning a probability to
every token in the vocabulary (built back in Chapter 3), representing how
likely that token is to come next given everything before it. The model
doesn't pick one "correct" next word out of certainty — it produces an
entire ranked distribution, most of it close to zero probability, with a
handful of genuinely plausible candidates near the top.

Generating text is then just this single step, repeated: predict a
distribution over the next token, choose one (the highest-probability
option, or something close to it — the precise choice mechanism is covered
in Chapter 14), append it to the sequence, and predict again — now with
one more token of context than before. A whole essay is built this way,
one narrow decision at a time, each decision informed by everything decided
before it.

**Try it yourself:** given "The opposite of hot is ___," rank in your head
which continuation feels most likely before reading on — "cold,"
"freezing," or "a banana"? Almost everyone ranks "cold" first, "freezing"
a distant second, and "a banana" at essentially zero. That instant ranking
you just did is exactly the kind of judgment a model makes at every single
step — just spread across its entire vocabulary instead of three options,
and computed freshly rather than felt intuitively.

## Technical Explanation

Formally, a language model computes a probability distribution over its
entire token vocabulary, conditioned on the sequence of tokens seen so far.
The calculation begins with the embeddings from Chapter 5, but the model
transforms those starting representations through its own learned layers
before producing a prediction — contexts that end up with similar internal
representations after that transformation tend to produce similar
predictions. Predicting well means generalizing from that learned
structure, not just recalling an exact token's history — the mechanism
doing the transforming is covered starting in Chapter 8, and in its
specific, modern form in Part III.

This process, where each new token is generated using all previously
generated tokens as its context, is called autoregressive generation. It
means the model never "sees" the future of its own output while generating
the present token — everything downstream simply hasn't been generated or
made available to the current step yet, one narrow step at a time. This
has real consequences: it's part of why a model can occasionally back
itself into an inconsistent corner mid-response, since no single step has
a view of the entire planned answer — a limitation Chapter 23 revisits
when discussing how reasoning models try to work around it.

## Common Misconceptions

### *"The model plans out the entire sentence in advance, then writes it down."*

**Why it's wrong:** The basic generation mechanism doesn't begin with a hidden, fully-written draft sitting somewhere and being read off token by token — each token is predicted using only what's been generated so far. A model can still produce something that looks like a plan (an outline, "step 1, step 2...") — but if it does, that plan is itself just earlier tokens, generated the same way as everything else, not consulted from some separate pre-formed source.

**Correct intuition:** Coherence emerges from consistently good next-token predictions; any "plan" the model appears to follow had to be developed through the visible context, not fetched from an upfront outline written before the first token.

**Analogy:** A jazz musician improvising a solo doesn't have the whole solo pre-written — each note is chosen in light of everything played so far, and the result can still sound coherent, even if the musician settles into a recognizable pattern partway through.

### *"Predicting the next token means looking up the answer in a giant table of memorized sentences."*

**Why it's wrong:** The model computes a fresh probability distribution from the current context every time; it isn't matching against a stored table of full sentences (Chapter 7 explains in detail why a table-based approach doesn't work at this scale).

**Correct intuition:** Prediction is a computation performed by the model's learned parameters over the current context — starting from the geometry of Chapter 5, not ending there — rather than a lookup.

**Analogy:** A weather forecaster doesn't look up "what happened on a day exactly like this one" in a logbook — they compute a forecast from current conditions using a general-purpose model of the atmosphere.

## Practical Implications

Recognizing that generation happens one token at a time, using only what's
already been produced, explains a lot of real, observable model behavior:
why models can contradict something they said two sentences earlier, why
asking a model to "think step by step" tends to improve accuracy on harder
problems (it gives the model intermediate tokens to condition on before
committing to a final answer), and why the very first token of a response
can matter disproportionately to how the rest of the response unfolds.

## Key Takeaway

**Text is generated one token at a time — predict a distribution, choose a token, append it, and predict again with the longer sequence as new context.**

## One-Page Summary

- Prediction means assigning a probability to every token in the vocabulary, given everything before it.
- Text generation is autoregressive: predict, choose, append, repeat — one token at a time.
- Predictions are computed from the current context using the model's learned parameters, starting from the geometry of embeddings (Chapter 5) — not retrieved from a table of stored answers, though specific facts can still be memorized (Chapter 9).
- No step has access to a hidden, pre-formed plan written before the first token — any plan the model follows had to be developed through the visible context, the same way as everything else.
- This explains why models can contradict themselves mid-response, and why "thinking step by step" tends to help on harder problems.

## Further Reading

- Search for "autoregressive language model" for the formal name of the generation process described here.

## The Next Obvious Question

*Why not just count how often one word follows another in a giant table, instead of building something as complicated as this — isn't that simpler?*

---

**Glossary terms added this chapter:** Prediction, Autoregressive generation → append to `/glossary.md`

**Misconceptions logged this chapter:** "the model plans the whole sentence in advance"; "prediction is a lookup in a memorized table" → append to `/misconceptions.md`

**Concept-graph entries checked off:** Level 3 — Prediction, at Ch. 6
