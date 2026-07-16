# Context Windows and Memory

**Part:** Building Useful AI

**Concept Level:** Level 5

**Prerequisites:** Chapter 4 (context), Chapter 14 (inference)

**New concepts introduced:** Context windows, Memory

---

## Opening Question

*If a model's own trained-in knowledge can run out or go stale, how can it be given a bigger, more reliable memory to draw from?*

## Real-World Story

Imagine a research assistant with an outstanding general education —
years of broad, thorough training, exactly like Chapter 9's training loop
— but one strict working rule: they can only keep the most recent twenty
pages of notes from your current conversation spread out on their desk at
any one time. The moment a twenty-first page arrives, the oldest page gets
cleared away to make room. Their general knowledge hasn't changed at all;
it's just that specific, personal details you mentioned early on — your
name, a preference you stated on page one — are no longer physically in
front of them once you're on page twenty-five, unless something brought
that detail back onto the desk more recently.

This isn't the assistant being forgetful in the human sense. Nothing was
misplaced or degraded. The information you gave them on page one simply
isn't part of what's currently visible, because the desk has a fixed,
finite amount of room.

## Worked Example

Trace a long conversation with an assistant that has exactly this kind of
limit. Early on, you mention you're allergic to peanuts. Many exchanges
later — well past the point where that detail would still fit on the
desk — you ask for a recipe recommendation, and the assistant suggests
one containing peanuts.

This isn't the assistant failing to care, or misremembering in a fuzzy,
human way. As far as the *raw* conversation goes, the peanut-allergy
detail is either still physically present in the input the model is
currently working from, or it's entirely absent — there's no fuzzy,
partially-remembered version of the original sentence sitting in between.
If a system built around this assistant wants to avoid this exact
failure, it needs a deliberate strategy for keeping that detail available
even after the raw conversation has grown too long to hold it directly —
which is precisely what "memory," as a system-design idea, is for: not
recovering a lost original, but making sure the important part survives
in some form (even compressed or restated) before it would otherwise fall
off the desk.

## Core Intuition

A **context window** is the maximum number of tokens (Chapter 3) a model
can consider at once — the hard size limit on everything currently "in
view": system instructions, prior conversation, any retrieved documents
(Chapters 17–18 preview), and the current message. Anything beyond this
window simply doesn't exist for the model at that moment, no matter how
recently or clearly it was stated within the same overall conversation.

**Memory**, in the sense this chapter introduces, is not the context
window itself — it's the set of strategies for managing what stays
available despite the window's fixed size as a conversation or task grows
longer than the window can directly hold. Memory doesn't expand the
window; it decides, deliberately, what earns a place inside it.

Being inside the window is necessary for a model to use something, but it
isn't sufficient for the model to use it *well*. Information outside the
window is unavailable unless something deliberately reintroduces it —
that part is genuinely binary. But information sitting inside a long
window is available only "in principle": models often draw on information
near the beginning or end of a long input more reliably than information
buried in the middle, even when every token is technically present the
whole time. Presence in the window is the floor, not a guarantee of equal
use.

## Technical Explanation

Context window size is a genuine architectural property, not an arbitrary
policy choice: because standard, dense attention (Chapter 11) computes a
relevance score between every pair of tokens, its computational cost grows
much faster than the sequence length itself, which is a major reason
context windows have practical size limits — a bigger window costs
disproportionately more compute per step, a tradeoff Chapter 20 returns to
directly. (Some newer architectures restructure attention to reduce this
cost, but standard dense attention is still the dominant baseline this
book describes.) Context window sizes have grown substantially across
model generations as architectures and infrastructure have improved, but
they remain fundamentally bounded, not unlimited.

Several concrete strategies implement "memory" within that constraint. A
simple sliding window just drops the oldest tokens once the limit is
reached — the assistant-with-a-desk story, exactly. Summarization
periodically compresses older conversation into a shorter recap, which is
then kept in the window in place of the original, much longer exchange,
freeing up room while preserving the gist. External memory stores
specific information — like a stated allergy — outside the window
entirely, and deliberately reinserts it into the window only when it
becomes relevant again, which is a direct preview of the retrieval
mechanism covered in Chapter 17.

## Common Misconceptions

### *"The context window is the same thing as the model's trained knowledge or long-term memory."*

**Why it's wrong:** Trained knowledge (Chapter 9) is baked into the model's parameters and persists across every conversation; the context window is a separate, temporary, per-conversation input buffer that typically resets between sessions and has nothing to do with what the model learned during training.

**Correct intuition:** Training gives a model its general knowledge, once, for good (until retrained); the context window is what it can see about this specific conversation, right now.

**Analogy:** A doctor's medical training doesn't reset between patients, but their notes on the patient currently in front of them are specific to that one visit.

### *"A model remembers earlier parts of a long conversation the way a person does, just imperfectly."*

**Why it's wrong:** There's no active human-style recall process happening. Whether raw information is available at all is a clean, binary fact — present as tokens in the current input, or entirely absent, with no fuzzy in-between. But that's not the whole picture: even present information can be used less reliably depending on where it sits in a long input, which is a different phenomenon from human-style forgetting.

**Correct intuition:** "In the window" or "not in the window" is binary; "used well" is a separate, non-binary question about how reliably a model draws on something it technically has access to.

**Analogy:** A photocopier either has a page in the tray or it doesn't — but even with every page present, a reader skimming a thick stack may still absorb the first and last pages more reliably than page two hundred.

## Practical Implications

This is exactly what "context window size" figures in model
announcements refer to — a genuine, load-bearing spec, not a marketing
number — and it explains why very long documents sometimes get truncated
or summarized by AI tools before being processed. It also explains a
common, very real frustration: a long chatbot conversation that appears
to "forget" something said earlier, which is not a bug in the emotional
sense but a direct, predictable consequence of a fixed-size window. This
sets up exactly why retrieval systems (Chapters 17–18) matter in practice.

## Key Takeaway

**A context window is the fixed-size input budget a model can see at any one moment; memory systems are strategies for managing what stays inside that budget as a conversation grows, not an expansion of the window itself.**

## One-Page Summary

- A context window is the maximum number of tokens a model can consider at once — everything beyond it simply isn't visible to the model.
- Context window size is bounded by standard attention's computational cost, which grows faster than sequence length itself.
- Memory is the set of strategies for managing what stays available within that fixed budget, not an expansion of the budget.
- A sliding window, summarization, and external memory (previewing retrieval) are three concrete memory strategies.
- Raw information is either present in the current input or it isn't — no fuzzy in-between — but being present doesn't guarantee equally reliable use; information in the middle of a long input can still be underused.
- This chapter's limitation directly motivates retrieval-augmented approaches, covered next.

## Further Reading

- Search for "context length" or "context window size" comparisons across major model releases to see how this figure has grown, and what tradeoffs providers describe when discussing it.

## The Next Obvious Question

*If a context window can't hold everything, how can a model still pull in specific relevant information — like documents it was never trained on — exactly when it's needed?*

---

**Glossary terms added this chapter:** Context window, Memory (as a system-design strategy) → append to `/glossary.md`

**Misconceptions logged this chapter:** "context window is the same as trained knowledge"; "the model remembers fuzzily, like a person" → append to `/misconceptions.md`

**Concept-graph entries checked off:** Level 5 — Context windows, Memory, both at Ch. 16 (opens Part IV)
