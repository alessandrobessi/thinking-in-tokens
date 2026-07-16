# Building a Transformer

**Part:** The Transformer

**Concept Level:** Level 4

**Prerequisites:** Chapter 8 (neural networks), Chapter 11 (attention, positional encoding)

**New concepts introduced:** Transformer blocks

---

## Opening Question

*Once a model can weigh relevance across an entire passage, how do you actually assemble that mechanism into a full working system?*

## Real-World Story

Picture a manuscript passed through twenty-four rounds of editing, but
with a constraint: at every point, an editor may only weigh a passage
against everything written *before* it — never against a later section,
even one that already exists on the page, exactly the discipline Chapter
11 described. Each editing pass, working forward through the manuscript,
reconsiders each passage against everything earlier, and makes a focused
round of small, local adjustments: sharpening a sentence here, clarifying
a reference there. Then it moves to the next editor, who does the same
thing again, starting from the previous editor's version.

No single editor rewrites the whole manuscript from scratch. Each one adds
a layer of refinement on top of what came before. After twenty-four
rounds, the manuscript hasn't gotten longer, and no single editorial pass
looks dramatic — but the cumulative result is far more polished and
coherent than any one editor could have produced alone. The transformer
architecture builds a token's understanding of its own context the same
way: not in one shot, but through many repeated rounds of refinement.

## Worked Example

Trace what happens once the model reaches the position of "big" itself,
in Chapter 11's trophy sentence. In the first round, an attention step
(Chapter 11) at this position looks backward across everything already
read — "it," "trophy," "suitcase," and every earlier word — and weighs
"trophy" and "it" heavily, since they're exactly what "big" is
describing. Then a feed-forward step — a small neural network, exactly
like Chapter 8's layered network, applied to each token individually —
further processes that freshly-weighted representation, refining it a
bit further based on patterns it learned during training.

That refined representation, now attached to the position of "big," enters
a second round: attention runs again, this time drawing on the
already-improved representations of "it," "trophy," and every other
earlier position, sharpening the interpretation further. Feed-forward
refines it again. Stack twenty or forty of these rounds, each one
building on the last, and the representation at this position — still
only ever looking backward — ends up carrying a rich, specific
understanding of exactly what "big" is doing in this exact sentence.

## Core Intuition

A **transformer block** combines two sub-steps, applied one after the
other: an attention step (Chapter 11), where every token gathers relevant
information from itself and every earlier token, and a feed-forward step,
where a simple neural network (Chapter 8) further transforms each token's
representation individually, independent of the others. A transformer is
what you get by stacking many of these blocks — modern models use dozens
— each one refining the output of the block before it, the same way each
editor in the story refined the previous editor's draft.

Crucially, each block has its own independently learned parameters
(Chapter 9) — later blocks are not just repeating what earlier blocks did.
Across training, different blocks tend to end up specializing in
different kinds of refinement (earlier blocks often settle into simpler,
more local patterns; later blocks into more abstract ones) — though, as
with everything in this book so far, nobody designs this division of
labor directly. It emerges from what reduces loss most reliably.

## Technical Explanation

Two additional design details make stacking dozens of blocks actually
work in practice, without each round of refinement washing out or
destabilizing everything before it. First, each block typically adds its
refinement on top of the incoming representation rather than replacing it
outright — closer to an editor adding sticky notes and margin comments
than an editor deleting the previous draft and starting over. This keeps
information from earlier blocks from simply vanishing as it passes
through many rounds of processing. Second, a normalization step keeps the
scale of the numbers flowing through the network consistent from block to
block, preventing values from growing or shrinking out of control over
dozens of repeated rounds — bookkeeping, not a conceptual addition.

The final token representations, after passing through every block, feed
directly into the next-token prediction step from Chapter 6 — the same
probability-distribution calculation described there, just computed from
representations that have now been repeatedly refined by attention and
feed-forward processing, rather than from raw, unrefined embeddings.

## Common Misconceptions

### *"Every layer in a transformer does the same thing — it's the same computation repeated identically."*

**Why it's wrong:** Each block has its own independently learned parameters; different blocks tend to specialize in different kinds of patterns as a byproduct of training, not identical, interchangeable copies of one computation.

**Correct intuition:** Stacking blocks is stacking distinct, separately-learned refinements, not repeating one fixed operation.

**Analogy:** Twenty-four editors reading the same manuscript don't make identical changes — each brings a different kind of scrutiny, even though they're all doing "editing."

### *"Adding more layers just makes the same computation take longer, without changing what the model can do."*

**Why it's wrong:** Additional layers give the network more rounds of refinement to build increasingly elaborate representations — similar to how Chapter 8's hidden layers build on patterns detected by the layer before, just now with attention included at every stage.

**Correct intuition:** Depth is a qualitatively different resource from raw speed — more layers change what kinds of patterns the network can represent, not just how long it takes to run.

**Analogy:** Twenty-four rounds of editing don't just take longer than one round — they produce a qualitatively more polished manuscript than one editor working twenty-four times as long alone.

## Practical Implications

This is why model "depth" (the number of stacked blocks) shows up as a
headline architectural detail alongside parameter count (Chapter 8) — it's
a genuinely separate design choice, not just a proxy for size. It also
explains why transformer-based models scale as productively as Chapter 10
described: depth combined with attention gives a network many flexible,
independently-useful places to put additional parameters, rather than
just making one computation bigger.

## Key Takeaway

**A transformer is many stacked blocks, each combining attention and individual refinement — depth is what turns one weighing step into a rich, layered understanding.**

## One-Page Summary

- A transformer block combines an attention step (gathering relevant context from itself and every earlier token) with a feed-forward step (refining each token's representation individually).
- A transformer stacks many such blocks, each with its own independently learned parameters, each refining the output of the one before it.
- Blocks add their refinements on top of incoming representations rather than replacing them, and normalization keeps values stable across many stacked rounds.
- Different blocks tend to specialize in different kinds of patterns as a byproduct of training, not by design.
- The final, repeatedly-refined representations feed into the next-token prediction step from Chapter 6.
- Depth (number of blocks) is a distinct architectural lever from parameter count, and a real contributor to why transformers scale so productively.

## Further Reading

- Look up "residual connections" and "layer normalization" for the formal names of the two stabilizing techniques described in this chapter.

## The Next Obvious Question

*Given this machinery existed conceptually for a while, what specifically made it good enough to power something like ChatGPT?*

---

**Glossary terms added this chapter:** Transformer block, Feed-forward step, Residual connection, Normalization → append to `/glossary.md`

**Misconceptions logged this chapter:** "every transformer layer does the same thing"; "more layers just means slower, not different" → append to `/misconceptions.md`

**Concept-graph entries checked off:** Level 4 — Transformer blocks, at Ch. 12
