# From Single Calls to Agents

**Part:** AI Systems

**Concept Level:** Level 6

**Prerequisites:** Chapter 16 (memory), Chapter 21 (tool calling)

**New concepts introduced:** AI agents

---

## Opening Question

*Once a model can request a single tool and read back a single result, what happens when it's allowed to chain many such requests together on its own — deciding, after each result, what to do next — in order to accomplish a goal that takes more than one step?*

## Real-World Story

A manager asks a new employee to "get the numbers ready for the board
meeting." That's the entire instruction. The employee isn't handed a
numbered checklist. She opens the shared drive, notices last quarter's
folder is missing a file, emails finance to ask for it, waits, receives
it, drops it into the spreadsheet, spots a formula that's pulling from
the wrong column, fixes it, double-checks the totals against last
quarter's report, and sends the finished file back — all without
returning to the manager for permission at every step.

Nobody scripted that exact sequence in advance, because nobody could have.
The specific missing file, the specific broken formula — none of that was
knowable until the employee actually started looking. What made this work
wasn't more knowledge or a smarter employee. It was the freedom to decide
the next step herself, based on what she'd just found, and to keep going
until the goal — not any single predetermined step — was actually met.

## Worked Example

Consider a coding assistant asked to fix a failing test. Step one: it
requests the test suite be run (a tool call, Chapter 21) and reads back a
failure message pointing at a specific file. Step two: based on that
result — not on anything decided in advance — it requests to read that
specific file, and reads back its contents. Step three: it identifies the
likely bug and requests an edit to one line. Step four: it requests the
test suite be run again. If the tests now pass, it stops and reports
success. If they still fail, it reads the new failure message and tries
again, informed by what just happened.

Every one of those four steps was, on its own, exactly the request-then-
result pattern from Chapter 21 — nothing new there. What's new is that
nobody manually re-prompted the model between steps two, three, and four.
The choice of what to request next came from the model itself, reading
the result of its own previous request, in a loop that kept running until
the model judged the goal met. Remove that loop, and you'd have four
separate, disconnected tool calls a human had to manually chain together
one at a time. With it, you have something that looks like it's pursuing
a goal.

## Core Intuition

This book uses **AI agent** for a model operating inside a loop: read the
current context (including the results of any tool calls made so far) →
decide the single next action, which may be another tool call (Chapter
21) or a final answer → execute it → append the result back into context
→ repeat — continuing until the loop's stopping condition is met, whether
that's the model itself judging the goal satisfied, a separate verifier
or controller making that call, or an external limit stopping things
regardless. Nothing about the model *has to* change between "a model
making one tool call" and "a model acting as an agent" — the same model
can do both. (Real agent systems sometimes do use a model specifically
fine-tuned for this kind of extended, tool-using behavior, but that's an
optional refinement, not a requirement of the mechanism itself.) What
changes at minimum is that the
deciding-what-to-do-next step, normally done once, now happens
repeatedly, each time conditioned on everything that's happened so far in
that loop. (The word "agent" is used more loosely elsewhere — sometimes
for systems built around a fixed planner, an external controller, or a
verifier standing outside the model — this chapter's definition is the
specific, mechanism-level case that pattern most commonly takes.)

## Technical Explanation

The mechanism underneath an agent is exactly Chapter 21's tool-calling
loop, run more than once without a human manually re-prompting in
between. A piece of surrounding code keeps the loop turning: it takes
whatever the model just produced, executes any requested tool call, adds
the result to the context window (Chapter 16) as new text, and calls the
model again on that updated context — over and over. The property that
actually earns the word "agent" is specifically this: the choice of what
to do at each step is made by the model itself, conditioned on the
results of its own prior steps, not hard-coded in advance by whoever
built the system. A fixed sequence of tool calls set up ahead of time —
"always look up the weather, then always send an email" — isn't agentic
in this sense, no matter how many steps it has; a single step where the
model itself decides whether another tool call is warranted, based on
what the last one returned, already is.

This depends directly on memory (Chapter 16): everything tried and
learned earlier in the same loop has to remain available to the model
when it decides its next step, or it has no way to build on prior
results, avoid repeating itself, or recognize that the goal has actually
been reached. That doesn't require every earlier step to sit untouched in
the context window — a real system might summarize older steps to save
space, store the full history externally and pull back only what's
relevant, or reconstruct state from a structured record rather than raw
transcript — but whatever form it takes, the model's next decision has to
be conditioned on that accumulated history, not just the original task.

Because nothing in the mechanism itself guarantees the loop will
recognize success and stop cleanly — a model can misjudge whether the
goal is met, or get stuck retrying a step that keeps failing the same way
— real systems typically don't leave termination to the model's own
judgment alone. A separate verifier can check whether the actual goal
condition is met, an external controller can decide the loop is done
independent of what the model itself claims, or hard limits — a maximum
number of steps, a budget, a required human-approval checkpoint — can cut
things off regardless of what the model thinks. "Autonomous" here means
specifically that the model picks its own next step without a human
re-prompting between steps — not that it has goals, preferences, or
persistence beyond the task and context it was given.

## Common Misconceptions

### *"An agent is a fundamentally different, more advanced kind of AI model."*

**Why it's wrong:** An agent uses the exact same underlying model and the exact same generation and tool-calling mechanism from Chapters 6, 14, and 21. "Agent" describes the surrounding loop that repeatedly calls the model and feeds results back in — not a new kind of model or a new architecture.

**Correct intuition:** The same model can act as a single-turn assistant in one product and as part of an agent loop in another — the difference is entirely in the surrounding system, not in the model itself.

**Analogy:** The new employee and a colleague who only answers one question and stops could be equally capable people — the difference is whether the surrounding situation calls for one exchange or a self-directed sequence of them.

### *"An agent has genuine autonomy or goals of its own, independent of what it was asked to do."*

**Why it's wrong:** At each step, the model is still doing exactly what it always does: predicting the most useful next output given everything currently in its context — including the original task. It has no persistent desires that outlive that context, and nothing resembling a goal it holds onto between separate sessions.

**Correct intuition:** "Autonomous" describes the loop making its own sequential decisions without a human re-prompting between steps — not independent will or self-generated objectives that exist apart from the task it was given.

**Analogy:** The new employee's initiative is bounded by the manager's actual request — she isn't pursuing a personal agenda, just working out, unsupervised, how to satisfy the one goal she was actually given.

### *"Because an agent can check its own work across multiple steps, it's reliably more accurate than a single response."*

**Why it's wrong:** Looping doesn't change how any individual step is generated — each one is still produced the same fallible way covered in Chapter 15, and a wrong turn early in the loop can compound across later steps just as easily as it can get corrected.

**Correct intuition:** More steps mean more opportunities to catch and fix a mistake, but also more opportunities to introduce or compound one — which is exactly why real systems add external limits and, often, human checkpoints rather than trusting the loop to self-correct indefinitely.

**Analogy:** Giving the new employee more time to keep working unsupervised can lead to a better report — or to her confidently going further down the wrong path, unless someone checks in before it goes too far.

## Practical Implications

This is the mechanism behind "AI agent," "agentic workflow," and "autonomous coding agent" branding across current products — all names for the loop this chapter just described, wrapped around Chapter 21's tool calling. It's also why agent products are typically shipped with visible safeguards: a maximum number of steps, a spending cap, or an explicit approval gate before a consequential action — because nothing about the mechanism itself guarantees the loop stays on track or stops at the right time. And it explains why an agent given a vague goal can take a wildly different path than a person would have expected: it's genuinely deciding its own sequence of steps, not following a script anyone reviewed in advance.

## Key Takeaway

**An AI agent isn't a smarter model — it's the same inference-and-tool-calling loop from Chapter 21, run repeatedly, with the model deciding after each result what to do next, until the loop's stopping condition — its own judgment, a separate verifier, or a hard limit — says otherwise.**

## One-Page Summary

- An AI agent is a model operating inside a loop: read context, decide the next action, execute it (often a tool call), append the result, repeat.
- The mechanism is identical to Chapter 21's single tool call — what's new is that the model itself decides whether another step is needed, without a human re-prompting in between.
- A fixed, pre-scripted sequence of tool calls isn't agentic; a model choosing its own next step based on the result of its last one is.
- This depends on memory (Chapter 16): earlier steps in the same loop must stay available to the model when deciding its next step — as raw context, a summary, or externally stored state.
- Nothing guarantees the loop terminates cleanly on its own — real systems typically don't leave that to the model's own judgment alone, adding a separate verifier, an external controller, or hard limits (max steps, budgets, human approval gates).
- "Autonomous" means the loop makes its own sequential decisions without human intervention between steps — not independent goals or persistent desires.
- Looping doesn't guarantee correctness; each step is still generated the same fallible way, and errors can compound across steps as easily as they can get caught.

## Further Reading

- Search for "AI agents" or "agentic workflows" from any major model provider for concrete, current examples of the loop described in §5.
- Search for "ReAct" (reason + act) for an early, influential description of interleaving a model's own reasoning with tool calls in a loop.

## The Next Obvious Question

*So far, a model produces one predicted step at a time, whether working alone or looping through an agent. What happens when a model is specifically trained to spend more of its own generated text working through a problem before committing to a final answer?*

---

**Glossary terms added this chapter:** AI agent, Agent loop → append to `/glossary.md`

**Misconceptions logged this chapter:** "an agent is a fundamentally different, more advanced model"; "an agent has genuine autonomy/goals of its own"; "an agent looping means it's reliably more accurate" → append to `/misconceptions.md`

**Concept-graph entries checked off:** Level 6 — AI agents, at Ch. 22 (closes Level 6)
