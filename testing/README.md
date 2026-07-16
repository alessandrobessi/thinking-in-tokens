# Reader-Testing Protocol

This is the structured version of `ROADMAP.md`'s Milestone 3 ("external
reader test: 5+ target readers"). It exists so that running the test is a
matter of following a script, not designing one from scratch under time
pressure with an actual reader sitting across from you.

**This protocol does not require a build step or code to run.** It's a
methodology document plus a question bank (`questions.md`). What it does
require is you, actually recruiting readers and sitting through the
sessions — that part can't be delegated.

## Two tracks, not one

Pedagogy and technical correctness are different questions, and one
reader pool can't answer both:

**Track A — Pedagogy (5+ non-technical readers).** Matching
`blueprint.md`'s stated audience: managers, consultants, product leaders,
founders, sales professionals, executives, students, lifelong learners.
Deliberately exclude people with an ML/CS background for this track — the
book's entire promise is legibility *without* that background, so testing
on readers who already have it will under-detect real confusion. Run the
full protocol below with this group.

**Track B — Technical correctness (1–2 ML practitioners).** Their job is
different: not "did this land," but "is this actually true, and does it
stay true as stated." Give them the chapter text directly (not the
question bank) and ask them to flag any claim that's wrong, overstated, or
will need walking back in a later chapter. Cross-check their findings
against `references/` and log any fix the same way as any other
correction (see `CHANGELOG.md`). This track doesn't use the scoring rubric
below at all — it's a review, not a test.

## Pre-test, before any chapter

Before a Track A reader reads chapter N for the first time, ask the
comprehension question for chapter N *cold* — no reading yet — and note
whatever they say. This is what makes retention and comprehension scores
meaningful: without it, you can't tell whether a good post-reading answer
came from the chapter or from something the reader already knew going in.
Score the pre-test 0–2 with the same rubric as everything else; the
number you actually care about is the *increase* from pre-test to
post-reading, not the raw post-reading score.

## What to measure, per chapter, per reader (Track A)

Four scored dimensions plus one unscored note. Use this rubric for all of
them unless a question specifies otherwise:

- **0 — Repeats the misconception, or cannot explain.** The reader either
  restates the wrong belief as fact, or has no account at all beyond "I'm
  not sure."
- **1 — Reaches the right conclusion, but the explanation is weak,
  circular, or borrowed from your own phrasing.** E.g. "no, it's not
  conscious, it's just... not conscious" — a correct verdict with no
  mechanism behind it. This is the score that most needs the *scenario*
  phrasing in `questions.md` to catch — a direct yes/no question lets a
  reader land here by guessing your intent rather than reasoning it out.
- **2 — Explains the actual mechanism, in their own words, and can apply
  it to a case that isn't the one in the chapter.** This is the bar; don't
  round up a plausible-sounding "1" to a "2" because the vocabulary sounded
  right.

1. **Comprehension** — can they explain the chapter's core concept,
   unaided, right after reading?
2. **Transfer** — can they apply the concept to a *new* example you give
   them, not one from the chapter?
3. **Misconception resistance** — present the scenario prompt from
   `questions.md` (a colleague/friend asserting the misconception as fact)
   and ask how the reader would respond. Scenario framing matters: a bare
   "is X true?" question lets a reader answer correctly by picking up on
   your tone, which is exactly the false-positive Track A exists to avoid.
4. **Retention** — ask the comprehension question again, unprompted, one
   week later, with no re-reading in between.
5. **Reading experience** — not scored; a free-text note on *where*
   attention visibly dropped (a specific paragraph, an example that didn't
   land, a term used before its explanation arrived).

`questions.md` has the exact comprehension/transfer/misconception prompts
for all 20 written chapters (1–20), pulled directly from each chapter's own
logged misconceptions so this protocol stays in sync with the manuscript
rather than drifting into a separate, parallel set of questions.

## How to run a session (Track A)

1. **Pre-test:** ask the comprehension question for the chapter the
   reader is about to read, cold. Score it. Don't explain the answer.
2. Reader reads the chapter, at their own pace, with no help from you.
3. Immediately after: ask the comprehension question again. Don't hint.
   Score it.
4. Ask the transfer question. Score it.
5. Present the misconception-resistance scenario from `questions.md`
   ("a colleague says X — how would you respond?"). Deliver it as a
   genuine scenario, not a quiz question — don't signal by tone that
   you're testing for a specific wrong answer. Score it against the 0/1/2
   rubric above, not just right/wrong.
6. Ask, informally: "was there any point where you felt lost, bored, or
   unsure what a term meant?" Write down whatever they say verbatim — don't
   paraphrase it into your own words yet.
7. Move to the next chapter, or stop for the day — don't run all 10
   chapters in one sitting; fatigue will contaminate the reading-experience
   signal for later chapters.
8. One week later, cold: ask the comprehension question again for every
   chapter they read, with no re-reading allowed beforehand. Score
   retention.

## Scoring sheet template

Copy this table per reader (e.g. `testing/results/reader-1.md` — this
`results/` subfolder is intentionally not created yet; make it when you
have actual sessions to log, so an empty scaffold doesn't imply data that
doesn't exist):

| Chapter | Pre-test | Comprehension | Transfer | Misconception resistance | Retention (1wk) | Reading-experience notes |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| ... | | | | | | |

For Track B, skip the scoring table — log findings as a plain list of
"claim → what's wrong with it → suggested fix," the same shape as the
technical fixes already tracked in `CHANGELOG.md`.

## What to do with the results

- Any concept scoring low on **comprehension** across multiple readers:
  the explanation itself needs rework — likely too fast, or missing an
  intermediate step.
- Low **transfer**, high comprehension: the reader can repeat the chapter's
  own example but hasn't generalized the underlying idea — usually fixed by
  adding a second example or a "predict what happens" prompt (see the one
  already added to Chapter 5, §6, as a template for this pattern).
- Low **misconception resistance** despite the chapter directly addressing
  it: the misconception block isn't landing — consider moving it earlier,
  or strengthening the analogy.
- Low **retention** despite good same-day comprehension: the chapter may be
  memorable in the moment but not sticky — often fixed by a punchier,
  more specific key-takeaway sentence (template §8) or a sharper worked
  example (template §3).
- Recurring "lost/bored" reports at the same *point* across multiple
  readers, independent of chapter: a structural problem (pacing, template
  rigidity) rather than a content problem in that one chapter — cross-check
  against the "chapters feel compressed" and "template rhythm" concerns
  already logged in `ROADMAP.md`.

Feed concrete findings back into the relevant chapter file directly, and
log the revision in `CHANGELOG.md`, the same way any other correction is
tracked.
