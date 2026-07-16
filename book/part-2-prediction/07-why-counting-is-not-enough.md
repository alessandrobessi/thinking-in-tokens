# Why Counting Is Not Enough

**Part:** Prediction

**Concept Level:** motivational (no new formal concept — motivates Level 3's neural networks)

**Prerequisites:** Chapter 6 (prediction)

**New concepts introduced:** none (informally previews why counting-based methods fail; formal treatment of neural networks starts Chapter 8)

---

## Opening Question

*Why not just count how often one word follows another in a giant table, instead of building something as complicated as a neural network?*

## Real-World Story

In the 1980s, a Usenet poster calling himself "Mark V. Shaney" became
locally famous for posts that were grammatically fluent but subtly,
hilariously deranged — sentences that flowed perfectly and meant almost
nothing. Mark V. Shaney wasn't a person. He was a simple program: scan a
body of real text, record which word tends to follow which pair of words,
and then generate new text by repeatedly picking a plausible next word from
that table of recorded counts.

It worked, in a narrow sense — the output was locally fluent, two or three
words at a time. But it fell apart at any distance. A sentence could start
about gardening and, a few words later, drift into a non sequitur about
philosophy, because the program only ever looked at the previous couple of
words. It had no way to remember what the sentence had been about ten words
earlier, and no way to handle a combination of words it hadn't seen during
counting. This is the ceiling every purely count-based approach runs into.

## Worked Example

Imagine the counting table has seen "the cat sat" 412 times, so it
confidently predicts what comes next. Now ask it about "the kitten
pirouetted" — a sentence that means almost the same thing, just with two
words swapped for close synonyms. If the table has seen that exact phrase
zero times, it has nothing to say: no count, no prediction, no fallback.

It cannot notice that "kitten" behaves like "cat" or that "pirouetted"
behaves like "sat" in this context, because it has no representation of
word similarity at all — only exact-match history. A sentence that means
almost the same thing produces a completely different, and completely
empty, lookup.

## Core Intuition

Counting how often word B follows word A (or word A, B follows word C) is
the simplest imaginable way to predict text, and for very short, very
common patterns, it actually works reasonably well. The approach fails for
two related reasons, both structural, not just a matter of not counting
enough.

First: the number of distinct possible word sequences grows explosively
with length. Even a modest vocabulary produces more possible five-word
sequences than could ever be observed, let alone counted, in all the text
humanity has ever written. Any sequence you actually need to predict is
overwhelmingly likely to be one the table has never seen.

Second, and more fundamental: a counting table treats every word as a
completely separate symbol with no relationship to any other word. It has
no notion, the way Chapter 5's embeddings do, that "cat" and "kitten" are
similar — so it can't use what it learned about one to make a good guess
about the other. It can only report exact matches.

## Technical Explanation

This first problem — the explosive growth of possible sequences — is
sometimes called the curse of dimensionality: as you consider longer
contexts (more preceding words), the number of distinct contexts you'd need
to have counted grows exponentially, quickly exceeding what any realistic
amount of text could ever cover. A model restricted to short contexts (like
Mark V. Shaney's two-word window) avoids this explosion but pays for it
with a very short memory — it genuinely cannot use information from
earlier in a sentence or paragraph.

To feel the scale of this: English has tens of thousands of common words,
so counting every possible three-word sequence already means tracking
billions of distinct combinations. Push to five- or ten-word sequences —
still a short paragraph — and the count of possibilities climbs so high
that even the entire indexed internet doesn't contain enough text to have
seen more than a sliver of them. A counting table's coverage gets thinner,
not thicker, the longer the context it tries to consider.

The second problem is a failure to generalize. A counting-based model has
no internal representation of similarity between words — "cat" and
"kitten" are, to it, as unrelated as "cat" and "spreadsheet." This is
precisely the gap embeddings were built to close: by placing tokens as
points in a space where closeness reflects similarity of meaning and use
(Chapter 5), a system can make a reasonable prediction even for a sequence
it has never seen exactly, by reasoning from nearby points it has seen.
What's still missing is a mechanism that can actually learn and use that
geometric structure to make predictions — which is exactly what a neural
network provides.

## Common Misconceptions

### *"A big enough counting table would eventually solve this — it's just a matter of collecting more data."*

**Why it's wrong:** The space of possible word sequences grows so explosively with length that no realistic amount of counting closes the gap — most sequences a system needs to handle will always be ones it has never exactly seen.

**Correct intuition:** The problem isn't insufficient data — it's that counting exact matches can never generalize to new-but-similar cases, no matter how much data you have.

**Analogy:** No matter how many recipes a cookbook contains, it can never contain the exact recipe for every possible combination of ingredients in your kitchen — you need to actually understand cooking principles, not just look up matches.

### *"Modern AI is just a much bigger version of this same counting approach."*

**Why it's wrong:** The core mechanism is different in kind, not just in scale: a counting table only ever reports exact historical frequencies, while a neural network (Chapter 8) learns a general-purpose function that can generalize to sequences it has never encountered.

**Correct intuition:** Scale alone doesn't fix a counting table's fundamental inability to generalize — a different mechanism was required, and finding it is what Chapter 8 covers.

**Analogy:** A phrasebook that's ten times longer is still just a phrasebook — it still can't handle a sentence nobody thought to include.

## Practical Implications

This history explains why "more data" was never, by itself, the answer to
better language models — it took a change in mechanism (neural networks
that learn generalizable patterns, not tables that memorize exact
sequences) before more data could actually help. It's a useful check when
reading about any AI approach: ask whether it can generalize to genuinely
new inputs, or whether it's fundamentally just matching against what it's
already seen.

## Key Takeaway

**A counting table can only report what it's already seen; a system built on geometric similarity can generalize to what it hasn't.**

## One-Page Summary

- Counting how often one word follows another is the simplest possible prediction method, and it fails at scale for two structural reasons.
- The number of possible word sequences grows explosively with length, so most sequences a system must handle were never observed during counting.
- A counting table treats every word as unrelated to every other word — it cannot generalize using similarity, unlike embeddings.
- More data alone doesn't fix this; it took a different mechanism — one that could learn and exploit geometric similarity — to make real progress.
- This mechanism is the neural network, covered starting in Chapter 8.

## Further Reading

- Search for "n-gram language model" for the formal name of the counting-based approach described here, and "curse of dimensionality" for the general problem of sequence-space explosion.

## The Next Obvious Question

*If we need something that can generalize using geometry rather than simply counting exact matches, what is the actual mechanism that learns this geometry and makes predictions from it?*

---

**Glossary terms added this chapter:** N-gram model, Curse of dimensionality → append to `/glossary.md`

**Misconceptions logged this chapter:** "a bigger counting table would eventually work"; "modern AI is just a bigger counting table" → append to `/misconceptions.md`

**Concept-graph entries checked off:** none (motivational chapter, motivates Level 3's neural-networks concept introduced in Ch. 8)
