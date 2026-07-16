# What Is Information?

**Part:** Information

**Concept Level:** Level 0

**Prerequisites:** Chapter 1 (informal notion of data/computation)

**New concepts introduced:** Information, Symbols, Computation, Probability (intuition)

---

## Opening Question

*What does it actually mean for a computer to "know" or "read" something?*

## Real-World Story

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

## Worked Example

Trace what Morse's code does to one specific word: "FLEE." F is a
moderately common letter (dot-dot-dash-dot). L is common too
(dot-dash-dot-dot). E — the single most common letter in English — gets
the shortest possible code, one dot. The second E repeats that same single
dot. Spelled out, "FLEE" becomes: dot-dot-dash-dot, dot-dash-dot-dot, dot,
dot.

Notice what just happened: the word has four letters, but the two E's
together take no longer to transmit than the single L does. That isn't an
accident of this particular word. It's the direct, designed consequence of
E being the most probable letter in English and therefore carrying the
least information every time it shows up — exactly the relationship the
rest of this chapter makes precise.

## Core Intuition

Four ideas, in the order you need them:

**A symbol** is something that stands for something else, by agreement, not
by resemblance. The letter "E" doesn't look like the sound it represents —
it's simply the agreed-upon stand-in for it.

**Computation** is the mechanical manipulation of symbols according to
fixed rules, with no need for whatever is doing the manipulating to
understand what the symbols mean. A telegraph relay flips a switch based on
pulses; it has no idea it's spelling a word. A thermostat makes the same
point even more plainly: it reads a temperature, compares it to a setpoint,
and mechanically decides whether to turn the heat on — reliably, correctly,
thousands of times — without anything resembling an awareness of what
"cold" feels like. A computer processing language is doing the same kind of
thing, just with vastly more elaborate rules stacked on top of each other.

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

## Technical Explanation

Formally, information theory (developed by Claude Shannon in 1948) defines
the information content of an event as a function of how unlikely that
event was. An event with probability close to 1 (nearly certain) carries
information close to zero. An event with low probability carries high
information. This is why "the sun rose this morning" tells you almost
nothing, while "there was a solar eclipse this morning" tells you a great
deal — the second event is far less probable, so learning it happened
reduces far more of your uncertainty.

**Try it yourself, before reading on:** which carries more information —
"it will rain sometime this century" or "it will rain tomorrow at 3pm"? The
second is much shorter, but it commits to something far less probable if
you were just guessing, so it reduces far more of your uncertainty. It
carries more information despite being the shorter sentence — length was
never the variable that mattered.

Computation, in the formal sense established by Alan Turing and Alonzo
Church in the 1930s, is the mechanical transformation of represented
information according to precisely defined operations. Crucially, this
definition never requires the process to "understand" the symbols — it
only requires that the operations be mechanical and well-defined. That's
compatible with those operations incorporating randomness or probability
along the way (rolling a die is a perfectly mechanical operation too) —
mechanical just means "follows its rules without needing comprehension,"
not "always produces the exact same output from the exact same input."
This is the theoretical foundation that lets us say, honestly, that a
computer "computes" without needing to claim it comprehends.

Modern AI systems, as you'll see over the rest of this book, are built
entirely on top of this foundation: they treat language as sequences of
symbols, and they are fundamentally probability machines — at every step,
estimating how likely each possible next symbol is, given everything
they've seen so far, and often making a deliberately randomized choice
among the likely candidates rather than always picking the single most
probable one (a mechanism Chapter 14 covers in detail).

## Common Misconceptions

### *"A computer that processes information understands what that information means."*

**Why it's wrong:** Computation, by its formal definition, requires only mechanical rule-following — not comprehension. A telegraph relay "processes" Morse code perfectly without understanding English.

**Correct intuition:** A computer manipulates symbols according to rules; whether or not any "understanding" is happening is a separate, much harder question this book will return to.

**Analogy:** A vending machine correctly processes coin-shaped-and-weighted metal without knowing what money is.

### *"More information means more data — a longer message always contains more information."*

**Why it's wrong:** Information is a measure of how much a message reduces your uncertainty, not how many words or bytes it contains. A long, entirely predictable message can carry almost no information.

**Correct intuition:** Information content depends on how surprising the message is, not on its length.

**Analogy:** A weather forecast that just says "it will be exactly like every other day this month" can be a hundred pages long and still tell you almost nothing you didn't already expect.

## Practical Implications

You'll repeatedly encounter the words "entropy," "surprise," and
"probability" in explanations of how AI models work — including
explanations of why they sometimes produce wrong answers confidently (a
topic in Chapter 15). Recognizing that these are precise, quantifiable
ideas, not vague metaphors, will make those explanations click into place
rather than feeling hand-wavy.

## Key Takeaway

**Information is not the symbols themselves or the act of processing them — it's the reduction in uncertainty that a probable or improbable symbol carries.**

## One-Page Summary

- A symbol stands for something else purely by agreement, not by resemblance.
- Computation is mechanical, rule-based symbol manipulation — it requires no understanding of what the symbols mean.
- Information measures how much a message reduces your uncertainty, not how long or detailed it is.
- Probability quantifies "how surprising" something is; low-probability events carry more information than high-probability ones.
- Morse code's letter-length design (short codes for common letters) is a real-world example of matching code length to information content.
- Modern AI systems are, at their foundation, probability machines operating over symbols — this framing will recur throughout the book.
- None of this requires or implies that a computer "understands" anything — that question is separate and addressed later.

## Further Reading

- Claude Shannon's 1948 paper "A Mathematical Theory of Communication" is the original source for the formal definition of information described here.

## The Next Obvious Question

*If computers only handle information as symbols, how does something as messy and irregular as human language get turned into symbols a computer can actually work with?*

---

**Glossary terms added this chapter:** Information, Symbol, Computation, Probability (intuition) → append to `/glossary.md`

**Misconceptions logged this chapter:** "computers understand meaning"; "more information = more data volume" → append to `/misconceptions.md`

**Concept-graph entries checked off:** Level 0 — Information, Symbols, Computation, Probability (intuition), all at Ch. 2
