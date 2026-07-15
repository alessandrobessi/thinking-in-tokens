# Chapter 3 — Characters, Words and Tokens

> **Part:** Information · **Concept Level:** Level 1 · **Prerequisites:** Chapter 2 (symbols, computation)
> **New concepts introduced:** Characters, Words, Tokens, Tokenization

---

## 1. Opening Question

> *How does a computer break language into pieces it can actually work with?*

## 2. Real-World Story

Try to teach a child to read, and you don't start with whole words. You
start with letters, then blend them into syllables, then into words. But a
fluent adult reader doesn't process "unbelievable" as u-n-b-e-l-i-e-v-a-b-l-e.
They also don't necessarily process it as one indivisible chunk — most
people can spot "un-," "believe," and "-able" inside it without effort, and
that decomposition helps them guess the meaning of an unfamiliar word like
"unfollowable" the first time they ever see it.

This turns out to be close to the exact problem a computer faces with
language, and close to the exact solution it uses. Chop language into pieces
too small (individual letters) and you lose efficiency — everything takes
forever to process, and the pieces carry very little meaning individually.
Chop it into pieces too large (whole words only) and you're stuck: languages
invent new words constantly, people misspell things, and a system that only
knows a fixed list of whole words breaks the instant it meets one that isn't
on the list.

## 3. Visual Explanation

<svg viewBox="0 0 600 300" width="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#FBF9F6"/>
  <text x="300" y="30" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="15" font-weight="bold" fill="#1B1B2F">Three Ways to Chop "unbelievable"</text>

  <text x="30" y="70" font-family="Helvetica, Arial, sans-serif" font-size="12" fill="#98A6B3">characters</text>
  <g font-family="Helvetica, Arial, sans-serif" font-size="13" fill="#FBF9F6">
    <rect x="30" y="80" width="24" height="28" rx="4" fill="#3D5A80"/><text x="42" y="99" text-anchor="middle">u</text>
    <rect x="58" y="80" width="24" height="28" rx="4" fill="#3D5A80"/><text x="70" y="99" text-anchor="middle">n</text>
    <rect x="86" y="80" width="24" height="28" rx="4" fill="#3D5A80"/><text x="98" y="99" text-anchor="middle">b</text>
    <rect x="114" y="80" width="24" height="28" rx="4" fill="#3D5A80"/><text x="126" y="99" text-anchor="middle">e</text>
    <rect x="142" y="80" width="24" height="28" rx="4" fill="#3D5A80"/><text x="154" y="99" text-anchor="middle">l</text>
    <rect x="170" y="80" width="24" height="28" rx="4" fill="#3D5A80"/><text x="182" y="99" text-anchor="middle">…</text>
  </g>

  <text x="30" y="150" font-family="Helvetica, Arial, sans-serif" font-size="12" fill="#98A6B3">subword tokens</text>
  <g font-family="Helvetica, Arial, sans-serif" font-size="13" fill="#FBF9F6">
    <rect x="30" y="160" width="50" height="28" rx="8" fill="#3D5A80"/><text x="55" y="179" text-anchor="middle">un</text>
    <rect x="86" y="160" width="90" height="28" rx="8" fill="#457B9D"/><text x="131" y="179" text-anchor="middle">believe</text>
    <rect x="182" y="160" width="60" height="28" rx="8" fill="#3D5A80"/><text x="212" y="179" text-anchor="middle">able</text>
  </g>

  <text x="30" y="230" font-family="Helvetica, Arial, sans-serif" font-size="12" fill="#98A6B3">whole word</text>
  <rect x="30" y="240" width="212" height="28" rx="8" fill="#6D597A"/>
  <text x="136" y="259" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="13" fill="#FBF9F6">unbelievable</text>
</svg>

*Takeaway: the same word can be split at three different grain sizes — subword tokens are the middle ground modern models actually use.*

## 4. Core Intuition

A **character** is the smallest unit of written text — a single letter,
digit, or punctuation mark. A **word** is a familiar, larger unit — but
"word" turns out to be a slippery concept computationally, since new words
appear constantly and different languages don't even agree on where one
word ends and another begins.

A **token** is the actual unit a language model works with — a chunk of
text that might be a whole word, a piece of a word, a single character, or
even a punctuation mark, chosen by a process called **tokenization** that
looks at enormous amounts of text in advance and decides which chunks are
common enough to deserve their own reusable piece.

The key design insight: build a fixed-size set of a few tens of thousands of
these chunks, chosen so that common words get their own single token
("the," "is," "cat") while rare or unfamiliar words get broken into
familiar sub-pieces ("un" + "believ" + "able"). This way, the model never
encounters a word it has literally no way to represent — it can always fall
back to smaller, familiar pieces.

## 5. Technical Explanation

The dominant approach, used by essentially every major language model
today, is a family of algorithms broadly called subword tokenization (the
best-known variant is called Byte-Pair Encoding, or BPE). The process
works, conceptually, like this: start with individual characters as the
smallest possible units. Scan a huge amount of text and find the pair of
units that appears together most frequently. Merge that pair into a single
new unit. Repeat this merging process tens of thousands of times. The
result is a fixed vocabulary where extremely common sequences ("ing," "the,"
common whole words) have been merged all the way up into single tokens,
while rare sequences remain split into smaller pieces.

Every token in this final vocabulary is assigned a numerical ID — since,
per Chapter 2, computation ultimately requires everything to be represented
as symbols the machine can manipulate mechanically. A sentence is
tokenized by matching it against this fixed vocabulary and converting it
into a sequence of these numerical IDs, which is the actual input a model
receives — the model never sees letters or words as such, only this
sequence of numbers.

## 6. Common Misconceptions

> **Misconception:** "The model reads text one letter at a time, like sounding out a word."
> **Why it's wrong:** Character-by-character processing is far too slow and loses too much structure for large-scale models; subword tokenization deliberately groups common sequences into single units to avoid this.
> **Correct intuition:** The model reads a sequence of tokens, most of which are whole words or common word-fragments, not individual letters.
> **Analogy:** A fluent reader doesn't sound out "the" letter by letter — they recognize it instantly as a single familiar shape.

> **Misconception:** "A token is always exactly one word."
> **Why it's wrong:** Tokenizers deliberately split rare, long, or unfamiliar words into multiple sub-word tokens, and can also merge very common short words with surrounding punctuation.
> **Correct intuition:** A token is whatever chunk of text the vocabulary happened to assign a single ID to — sometimes a whole word, sometimes a fragment, sometimes less than a word.
> **Analogy:** Postal abbreviations aren't one-per-word either — common words get short codes ("St.," "Ave.") while unusual street names are spelled out in full.

## 7. Practical Implications

This is why AI providers bill by "tokens," not by words or characters — and
why the same sentence can cost a different amount depending on the
language it's written in (some languages tokenize less efficiently than
English in many popular tokenizers). It also explains a famous class of
AI failures: ask a model to count the letters in a word, or reverse a word
letter-by-letter, and it can stumble — because it isn't actually seeing
individual letters, it's seeing tokens, and a token doesn't expose its own
internal letters to the model in an obvious way.

## 8. Canonical Mental-Model Diagram

<svg viewBox="0 0 800 500" width="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#FBF9F6"/>
  <text x="400" y="40" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="20" font-weight="bold" fill="#1B1B2F">Text → Tokens → Numbers</text>

  <text x="400" y="90" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="16" fill="#1B1B2F">"the unbelievable cat"</text>

  <line x1="400" y1="105" x2="400" y2="140" stroke="#98A6B3" stroke-width="2"/>

  <g font-family="Helvetica, Arial, sans-serif" font-size="14" fill="#FBF9F6">
    <rect x="120" y="150" width="70" height="45" rx="8" fill="#3D5A80" stroke="#1B1B2F" stroke-width="2"/><text x="155" y="178" text-anchor="middle">the</text>
    <rect x="200" y="150" width="55" height="45" rx="8" fill="#457B9D" stroke="#1B1B2F" stroke-width="2"/><text x="227" y="178" text-anchor="middle">un</text>
    <rect x="265" y="150" width="95" height="45" rx="8" fill="#457B9D" stroke="#1B1B2F" stroke-width="2"/><text x="312" y="178" text-anchor="middle">believ</text>
    <rect x="370" y="150" width="65" height="45" rx="8" fill="#457B9D" stroke="#1B1B2F" stroke-width="2"/><text x="402" y="178" text-anchor="middle">able</text>
    <rect x="445" y="150" width="70" height="45" rx="8" fill="#3D5A80" stroke="#1B1B2F" stroke-width="2"/><text x="480" y="178" text-anchor="middle">cat</text>
  </g>

  <line x1="400" y1="205" x2="400" y2="240" stroke="#98A6B3" stroke-width="2"/>

  <g font-family="Helvetica, Arial, sans-serif" font-size="13" fill="#1B1B2F">
    <text x="155" y="270" text-anchor="middle">1723</text>
    <text x="227" y="270" text-anchor="middle">312</text>
    <text x="312" y="270" text-anchor="middle">9981</text>
    <text x="402" y="270" text-anchor="middle">88</text>
    <text x="480" y="270" text-anchor="middle">5502</text>
  </g>
  <text x="400" y="320" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="12" fill="#98A6B3">this numeric sequence is what the model actually receives</text>
</svg>

**Takeaway: a language model never sees letters or words — it sees a sequence of token IDs produced by tokenization, some whole words and some fragments.**

## 9. One-Page Summary

- Characters are the smallest text units; words are a familiar but computationally slippery unit; tokens are the actual chunks a model uses.
- Tokenization builds a fixed vocabulary (tens of thousands of tokens) where common sequences become single tokens and rare ones stay split into pieces.
- Byte-Pair Encoding (BPE) is the dominant algorithm: repeatedly merge the most frequent adjacent pair of units to build up the vocabulary.
- Every token is assigned a numeric ID; a model's actual input is a sequence of these IDs, never raw letters or words.
- This design guarantees any input text can be represented, even words the model has never seen whole.
- Token-based billing and letter-counting failures both trace back directly to this chapter's ideas.

## 10. Further Reading

- Search for an interactive "tokenizer visualizer" from any major AI lab to see real tokenization of your own sentences — the companion website for this book will include one directly (see "Living Companion" in the project overview).

## 11. The Next Obvious Question

> *If text becomes a long sequence of small tokens, how does a model deal with the fact that meaning is spread out and repeated across that sequence — and can that sequence be represented more efficiently?*

---

**Glossary terms added this chapter:** Character, Word, Token, Tokenization, Byte-Pair Encoding (BPE) → append to `/glossary.md`
**Misconceptions logged this chapter:** "model reads letter by letter"; "a token is always one word" → append to `/misconceptions.md`
**Concept-graph entries checked off:** Level 1 — Characters, Words, Tokens, Tokenization, all at Ch. 3
