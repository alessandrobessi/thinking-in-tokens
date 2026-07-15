# Chapter 7 — Why Statistics Are Not Enough

> **Part:** Prediction · **Concept Level:** motivational (no new formal concept — motivates Level 3's neural networks) · **Prerequisites:** Chapter 6 (prediction)
> **New concepts introduced:** none (informally previews why counting-based methods fail; formal treatment of neural networks starts Chapter 8)

---

## 1. Opening Question

> *Why not just count how often one word follows another in a giant table, instead of building something as complicated as a neural network?*

## 2. Real-World Story

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

## 3. Visual Explanation

<svg viewBox="0 0 600 300" width="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#FBF9F6"/>
  <text x="300" y="30" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="15" font-weight="bold" fill="#1B1B2F">A Counting Table Runs Out of Cells</text>

  <g font-family="Helvetica, Arial, sans-serif" font-size="11" fill="#1B1B2F">
    <text x="30" y="70">"the cat sat" →</text>
    <rect x="150" y="55" width="40" height="20" fill="#3D5A80"/><text x="170" y="70" text-anchor="middle" fill="#FBF9F6">412</text>
    <text x="200" y="70">times seen</text>

    <text x="30" y="100">"the cat danced" →</text>
    <rect x="170" y="85" width="10" height="20" fill="#98A6B3"/><text x="175" y="100" text-anchor="middle" fill="#1B1B2F">2</text>

    <text x="30" y="130">"the kitten pirouetted" →</text>
    <rect x="200" y="115" width="4" height="20" fill="#D7263D"/><text x="215" y="130" fill="#D7263D">never seen — 0</text>
  </g>

  <text x="300" y="200" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="12" fill="#98A6B3">"kitten" and "danced" mean almost the same thing as "cat" and "pirouetted,"</text>
  <text x="300" y="220" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="12" fill="#98A6B3">but a counting table has no way to know that.</text>
</svg>

*Takeaway: a table can only report what it has already seen — it has no way to generalize to something similar-but-new.*

## 4. Core Intuition

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

## 5. Technical Explanation

This first problem — the explosive growth of possible sequences — is
sometimes called the curse of dimensionality: as you consider longer
contexts (more preceding words), the number of distinct contexts you'd need
to have counted grows exponentially, quickly exceeding what any realistic
amount of text could ever cover. A model restricted to short contexts (like
Mark V. Shaney's two-word window) avoids this explosion but pays for it
with a very short memory — it genuinely cannot use information from
earlier in a sentence or paragraph.

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

## 6. Common Misconceptions

> **Misconception:** "A big enough counting table would eventually solve this — it's just a matter of collecting more data."
> **Why it's wrong:** The space of possible word sequences grows so explosively with length that no realistic amount of counting closes the gap — most sequences a system needs to handle will always be ones it has never exactly seen.
> **Correct intuition:** The problem isn't insufficient data — it's that counting exact matches can never generalize to new-but-similar cases, no matter how much data you have.
> **Analogy:** No matter how many recipes a cookbook contains, it can never contain the exact recipe for every possible combination of ingredients in your kitchen — you need to actually understand cooking principles, not just look up matches.

> **Misconception:** "Modern AI is just a much bigger version of this same counting approach."
> **Why it's wrong:** The core mechanism is different in kind, not just in scale: a counting table only ever reports exact historical frequencies, while a neural network (Chapter 8) learns a general-purpose function that can generalize to sequences it has never encountered.
> **Correct intuition:** Scale alone doesn't fix a counting table's fundamental inability to generalize — a different mechanism was required, and finding it is what Chapter 8 covers.
> **Analogy:** A phrasebook that's ten times longer is still just a phrasebook — it still can't handle a sentence nobody thought to include.

## 7. Practical Implications

This history explains why "more data" was never, by itself, the answer to
better language models — it took a change in mechanism (neural networks
that learn generalizable patterns, not tables that memorize exact
sequences) before more data could actually help. It's a useful check when
reading about any AI approach: ask whether it can generalize to genuinely
new inputs, or whether it's fundamentally just matching against what it's
already seen.

## 8. Canonical Mental-Model Diagram

<svg viewBox="0 0 800 500" width="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#FBF9F6"/>
  <text x="400" y="40" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="20" font-weight="bold" fill="#1B1B2F">Counting vs. Generalizing</text>

  <text x="200" y="80" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="15" fill="#1B1B2F">Counting Table</text>
  <g stroke="#98A6B3" stroke-width="1">
    <line x1="60" y1="100" x2="340" y2="100"/><line x1="60" y1="140" x2="340" y2="140"/>
    <line x1="60" y1="180" x2="340" y2="180"/><line x1="60" y1="220" x2="340" y2="220"/>
    <line x1="60" y1="260" x2="340" y2="260"/>
    <line x1="60" y1="100" x2="60" y2="260"/><line x1="130" y1="100" x2="130" y2="260"/>
    <line x1="200" y1="100" x2="200" y2="260"/><line x1="270" y1="100" x2="270" y2="260"/>
    <line x1="340" y1="100" x2="340" y2="260"/>
  </g>
  <text x="95" y="125" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="16" fill="#3D5A80">412</text>
  <text x="165" y="165" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="16" fill="#3D5A80">7</text>
  <text x="305" y="245" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="14" fill="#D7263D">0</text>
  <text x="235" y="205" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="14" fill="#D7263D">0</text>
  <text x="200" y="290" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="12" fill="#98A6B3">mostly empty — new sequences get nothing</text>

  <text x="620" y="80" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="15" fill="#1B1B2F">Geometric Generalization</text>
  <g stroke="#98A6B3" stroke-width="1" stroke-dasharray="2 4">
    <line x1="460" y1="120" x2="780" y2="120"/><line x1="460" y1="180" x2="780" y2="180"/>
    <line x1="460" y1="240" x2="780" y2="240"/>
    <line x1="540" y1="100" x2="540" y2="260"/><line x1="620" y1="100" x2="620" y2="260"/><line x1="700" y1="100" x2="700" y2="260"/>
  </g>
  <circle cx="560" cy="150" r="7" fill="#457B9D"/><text x="560" y="140" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="11" fill="#1B1B2F">cat</text>
  <circle cx="590" cy="170" r="7" fill="#457B9D"/><text x="605" y="185" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="11" fill="#1B1B2F">kitten</text>
  <circle cx="700" cy="210" r="9" fill="#EE964B"/><text x="700" y="235" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="11" fill="#1B1B2F">new sequence</text>
  <text x="620" y="290" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="12" fill="#98A6B3">nearby points fill the gaps a table leaves empty</text>
</svg>

**Takeaway: a counting table can only report what it's already seen; a system built on geometric similarity can generalize to what it hasn't.**

## 9. One-Page Summary

- Counting how often one word follows another is the simplest possible prediction method, and it fails at scale for two structural reasons.
- The number of possible word sequences grows explosively with length, so most sequences a system must handle were never observed during counting.
- A counting table treats every word as unrelated to every other word — it cannot generalize using similarity, unlike embeddings.
- More data alone doesn't fix this; it took a different mechanism — one that could learn and exploit geometric similarity — to make real progress.
- This mechanism is the neural network, covered starting in Chapter 8.

## 10. Further Reading

- Search for "n-gram language model" for the formal name of the counting-based approach described here, and "curse of dimensionality" for the general problem of sequence-space explosion.

## 11. The Next Obvious Question

> *If we need something that can generalize using geometry rather than simply counting exact matches, what is the actual mechanism that learns this geometry and makes predictions from it?*

---

**Glossary terms added this chapter:** N-gram model, Curse of dimensionality → append to `/glossary.md`
**Misconceptions logged this chapter:** "a bigger counting table would eventually work"; "modern AI is just a bigger counting table" → append to `/misconceptions.md`
**Concept-graph entries checked off:** none (motivational chapter, motivates Level 3's neural-networks concept introduced in Ch. 8)
