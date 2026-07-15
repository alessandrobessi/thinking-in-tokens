# Chapter 2 — What Is Information?

> **Part:** Information · **Concept Level:** Level 0 · **Prerequisites:** Chapter 1 (informal notion of data/computation)
> **New concepts introduced:** Information, Symbols, Computation, Probability (intuition)

---

## 1. Opening Question

> *What does it actually mean for a computer to "know" or "read" something?*

## 2. Real-World Story

In the 1830s, Samuel Morse faced a problem: a telegraph wire could only
send one thing — pulses of electricity, short or long, present or absent.
No ink, no paper, no pictures. Yet somehow entire messages, in any language,
had to cross that wire.

His solution was to agree, in advance, on a code: each letter of the
alphabet would be represented by a specific pattern of short and long
pulses ("dots" and "dashes"). "E," the most common letter in English, got
the shortest possible code: a single dot. "Q," a rare letter, got a long,
four-pulse code. Neither the dot nor the wire "means" anything by itself.
The meaning exists only because sender and receiver agreed, beforehand, on
what each pattern would stand for.

This is the entire trick behind every computer that has ever existed. A
computer's circuits can only really do one thing: be in one of two physical
states (a voltage is present, or it isn't). Everything a computer "reads,"
"writes," or "knows" is built, layer by layer, out of agreed-upon patterns
of those two states — exactly like Morse's dots and dashes, just with far
more layers stacked on top.

## 3. Visual Explanation

<svg viewBox="0 0 600 300" width="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#FBF9F6"/>
  <text x="300" y="35" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="16" font-weight="bold" fill="#1B1B2F">A Letter Is Just an Agreed-Upon Pattern</text>

  <text x="90" y="100" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="40" fill="#1B1B2F">E</text>
  <line x1="60" y1="150" x2="75" y2="150" stroke="#3D5A80" stroke-width="6"/>
  <text x="67" y="175" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="11" fill="#1B1B2F">1 dot</text>

  <text x="290" y="100" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="40" fill="#1B1B2F">Q</text>
  <line x1="230" y1="150" x2="250" y2="150" stroke="#3D5A80" stroke-width="6"/>
  <line x1="256" y1="150" x2="276" y2="150" stroke="#3D5A80" stroke-width="6"/>
  <line x1="282" y1="150" x2="292" y2="150" stroke="#3D5A80" stroke-width="6"/>
  <line x1="298" y1="150" x2="318" y2="150" stroke="#3D5A80" stroke-width="6"/>
  <text x="274" y="175" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="11" fill="#1B1B2F">4 pulses</text>

  <text x="490" y="100" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="40" fill="#1B1B2F">0/1</text>
  <rect x="450" y="140" width="20" height="20" fill="#3D5A80"/>
  <rect x="480" y="140" width="20" height="20" fill="none" stroke="#3D5A80" stroke-width="2"/>
  <text x="480" y="175" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="11" fill="#1B1B2F">voltage on/off</text>

  <text x="300" y="230" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="13" fill="#98A6B3">Common letters get shorter codes — this is not an accident.</text>
</svg>

*Takeaway: any symbol can be represented by any physical pattern, as long as sender and receiver agree on the mapping.*

## 4. Core Intuition

Four ideas, in the order you need them:

**A symbol** is something that stands for something else, by agreement, not
by resemblance. The letter "E" doesn't look like the sound it represents —
it's simply the agreed-upon stand-in for it.

**Computation** is the mechanical manipulation of symbols according to
fixed rules, with no need for whatever is doing the manipulating to
understand what the symbols mean. A telegraph relay flips a switch based on
pulses; it has no idea it's spelling a word.

**Information** is not the same thing as data. A message carries
information only to the extent that it *reduces your uncertainty* about
something. If you already knew exactly what a message was going to say,
receiving it tells you nothing new — it carries almost no information, no
matter how many words it contains. A message you couldn't have predicted at
all carries a lot of information.

**Probability**, here, is just a way of putting a number on "how surprised
should I be." Common, predictable things (the letter "E" showing up in
English text) have high probability and carry little information each time
they appear. Rare, unpredictable things (the letter "Q") have low
probability and carry more information when they do appear. This is
precisely why Morse gave "E" the shortest code and "Q" the longest: he was,
without using this language, matching code length to how much information
each letter actually carried.

## 5. Technical Explanation

Formally, information theory (developed by Claude Shannon in 1948) defines
the information content of an event as a function of how unlikely that
event was. An event with probability close to 1 (nearly certain) carries
information close to zero. An event with low probability carries high
information. This is why "the sun rose this morning" tells you almost
nothing, while "there was a solar eclipse this morning" tells you a great
deal — the second event is far less probable, so learning it happened
reduces far more of your uncertainty.

Computation, in the formal sense established by Alan Turing and Alonzo
Church in the 1930s, is any process that transforms an input symbol
sequence into an output symbol sequence by mechanically following a fixed
set of rules, one deterministic step at a time. Crucially, this definition
never requires the process to "understand" the symbols — it only requires
that the rule-following be mechanical and well-defined. This is the
theoretical foundation that lets us say, honestly, that a computer
"computes" without needing to claim it comprehends.

Modern AI systems, as you'll see over the rest of this book, are built
entirely on top of this foundation: they treat language as sequences of
symbols, and they are fundamentally probability machines — at every step,
estimating how likely each possible next symbol is, given everything they've
seen so far.

## 6. Common Misconceptions

> **Misconception:** "A computer that processes information understands what that information means."
> **Why it's wrong:** Computation, by its formal definition, requires only mechanical rule-following — not comprehension. A telegraph relay "processes" Morse code perfectly without understanding English.
> **Correct intuition:** A computer manipulates symbols according to rules; whether or not any "understanding" is happening is a separate, much harder question this book will return to.
> **Analogy:** A vending machine correctly processes coin-shaped-and-weighted metal without knowing what money is.

> **Misconception:** "More information means more data — a longer message always contains more information."
> **Why it's wrong:** Information is a measure of how much a message reduces your uncertainty, not how many words or bytes it contains. A long, entirely predictable message can carry almost no information.
> **Correct intuition:** Information content depends on how surprising the message is, not on its length.
> **Analogy:** A weather forecast that just says "it will be exactly like every other day this month" can be a hundred pages long and still tell you almost nothing you didn't already expect.

## 7. Practical Implications

You'll repeatedly encounter the words "entropy," "surprise," and
"probability" in explanations of how AI models work — including
explanations of why they sometimes produce wrong answers confidently (a
topic in Chapter 15). Recognizing that these are precise, quantifiable
ideas, not vague metaphors, will make those explanations click into place
rather than feeling hand-wavy.

## 8. Canonical Mental-Model Diagram

<svg viewBox="0 0 800 500" width="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#FBF9F6"/>
  <text x="400" y="40" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="20" font-weight="bold" fill="#1B1B2F">From Symbol to Information</text>

  <circle cx="130" cy="140" r="55" fill="none" stroke="#1B1B2F" stroke-width="1"/>
  <text x="130" y="155" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="48" fill="#1B1B2F">E</text>
  <text x="130" y="220" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="13" fill="#1B1B2F">Symbol</text>
  <text x="130" y="238" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="11" fill="#98A6B3">an agreed-upon stand-in</text>

  <line x1="200" y1="140" x2="290" y2="140" stroke="#98A6B3" stroke-width="2"/>

  <rect x="300" y="100" width="150" height="80" rx="8" fill="#3D5A80" stroke="#1B1B2F" stroke-width="2"/>
  <text x="375" y="135" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="14" fill="#FBF9F6">Computation</text>
  <text x="375" y="155" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="11" fill="#FBF9F6">mechanical rule-following</text>

  <line x1="460" y1="140" x2="540" y2="140" stroke="#98A6B3" stroke-width="2"/>

  <path d="M 550 190 Q 590 100 630 60 T 700 190" fill="none" stroke="#EE964B" stroke-width="2"/>
  <text x="625" y="230" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="13" fill="#1B1B2F">Probability</text>
  <text x="625" y="248" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="11" fill="#98A6B3">how surprising is it?</text>

  <rect x="230" y="330" width="340" height="90" rx="8" fill="#F9DC5C" fill-opacity="0.3" stroke="#1B1B2F" stroke-width="2"/>
  <text x="400" y="370" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="18" font-weight="bold" fill="#1B1B2F">Information</text>
  <text x="400" y="395" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="12" fill="#1B1B2F">= how much uncertainty is reduced</text>

  <line x1="375" y1="180" x2="380" y2="330" stroke="#98A6B3" stroke-width="2"/>
  <line x1="625" y1="230" x2="420" y2="330" stroke="#98A6B3" stroke-width="2"/>
</svg>

**Takeaway: information is not the symbols themselves or the act of processing them — it's the reduction in uncertainty that a probable or improbable symbol carries.**

## 9. One-Page Summary

- A symbol stands for something else purely by agreement, not by resemblance.
- Computation is mechanical, rule-based symbol manipulation — it requires no understanding of what the symbols mean.
- Information measures how much a message reduces your uncertainty, not how long or detailed it is.
- Probability quantifies "how surprising" something is; low-probability events carry more information than high-probability ones.
- Morse code's letter-length design (short codes for common letters) is a real-world example of matching code length to information content.
- Modern AI systems are, at their foundation, probability machines operating over symbols — this framing will recur throughout the book.
- None of this requires or implies that a computer "understands" anything — that question is separate and addressed later.

## 10. Further Reading

- Claude Shannon's 1948 paper "A Mathematical Theory of Communication" is the original source for the formal definition of information described here.

## 11. The Next Obvious Question

> *If computers only handle information as symbols, how does something as messy and irregular as human language get turned into symbols a computer can actually work with?*

---

**Glossary terms added this chapter:** Information, Symbol, Computation, Probability (intuition) → append to `/glossary.md`
**Misconceptions logged this chapter:** "computers understand meaning"; "more information = more data volume" → append to `/misconceptions.md`
**Concept-graph entries checked off:** Level 0 — Information, Symbols, Computation, Probability (intuition), all at Ch. 2
