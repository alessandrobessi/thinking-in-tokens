# AI Engineering and Observability

**Part:** AI in the Real World

**Concept Level:** Level 8

**Prerequisites:** Chapter 18 (RAG), Chapter 22 (AI agents), Chapter 26 (evaluation)

**New concepts introduced:** Observability, AI engineering, Idempotency

---

## Opening Question

*Evaluation tells you how a system performs on a fixed set of test cases before deployment. But once a system is actually live, handling real, unpredictable user requests every day, how do you know it's still working correctly?*

## Real-World Story

A pilot completes a thorough pre-flight checklist before takeoff —
verifying fuel, controls, and instruments are all in order. But she
doesn't file that checklist away and fly blind for the next six hours.
Throughout the flight, a bank of live instruments — altimeter, fuel
gauge, radar, weather updates — continuously reports exactly what's
happening right now, because conditions in the air change in ways no
pre-flight checklist could ever have anticipated. If the fuel gauge
suddenly drops faster than expected, she needs to know immediately, not
discover it only after landing.

A thorough pre-flight checklist and continuous in-flight instruments
aren't redundant with each other. One verifies the aircraft is fit to
fly before departure; the other tells you, moment to moment, whether
everything is still actually going as expected once real conditions —
weather, traffic, mechanical wear — start happening.

## Worked Example

A company deploys an agent (Chapter 22) that handles refund requests by
calling a "check order status" tool and then a "process refund" tool. It
passed every case in its offline evaluation suite (Chapter 26) before
launch. Two weeks later, refund processing times start climbing, and a
handful of customers report being charged twice.

Without any visibility into the live system, the team has no way to find
out why. With it, logs show that the "check order status" tool started
timing out intermittently for a specific subset of order IDs — a
downstream API was having a partial outage — which pushed the agent's
loop (Chapter 22) into retrying the whole sequence, occasionally calling
"process refund" more than once for the same order before the timeout
resolved. Reconstructing the exact sequence of tool calls and results for
the affected requests is what actually revealed the bug. Nothing in the
original evaluation suite had ever tested for a downstream timeout hitting
mid-loop — because nobody had thought to write that specific case in
advance.

Observability found the bug; it isn't what should have prevented it. The
actual fix is making the "process refund" tool **idempotent** — designed
so that calling it twice for the same order has the same effect as
calling it once, typically by having it check first whether that specific
order was already refunded. That's a property engineered into the tool
itself, independent of whether anyone happens to be watching the logs
when a retry occurs. Observability and this kind of safe-by-design
tool behavior work together: one limits the damage an unexpected retry
can do in the first place, the other is how the team finds out a retry
happened at all and confirms the fix worked.

## Core Intuition

**Observability** is the practice of instrumenting a live AI system —
logging what it actually did, tracing multi-step tool-call and agent
sequences (Chapters 21–22) step by step, and tracking metrics like
latency, cost, and error rate — so a team can see what's really happening
in production and diagnose failures after the fact, not just how the
system performed on a fixed evaluation set before launch. **AI
engineering** is the broader discipline of actually building and
operating production systems on top of foundation models — combining
retrieval (Chapters 17–18), tool calling and agents (Chapters 21–22),
evaluation (Chapter 26), and observability into ongoing practical work —
distinct from the comparatively rare specialty of training a foundation
model from scratch (Chapter 9).

## Technical Explanation

Real user traffic is far more varied and unpredictable than any fixed
evaluation set (Chapter 26) could anticipate, which is precisely why
evaluation run once before deployment isn't sufficient on its own. A
production AI system typically needs three things working together.
**Logging**: recording inputs, outputs, and every intermediate step —
each tool call and result inside an agent loop (Chapter 22) — so a
specific failing request can be reconstructed and inspected after the
fact. Logging everything by default isn't automatically safe: a
system's prompts and outputs can carry personal, confidential, or
regulated information, so real logging needs redaction, access controls,
retention limits, and clear data-governance rules alongside it — a
diagnosis tool that itself becomes a privacy liability has just traded
one problem for another. **Tracing**: connecting every step of one
multi-step tool-call or
agent sequence into a single reviewable timeline, rather than a scattered
pile of disconnected log lines, so a team can see exactly which step in
the chain actually produced a failure. And **metrics** tracked
continuously over time — latency, cost per request (Chapter 14, Chapter
20), error rates, and, where feasible, ongoing lightweight evaluation
(Chapter 26's LLM-as-judge approach applied continuously to a sample of
live traffic, not just a fixed test set) — to catch quality regressions
that only surface under real usage patterns nobody wrote a test case for.

None of this changes anything about the model itself; training (Chapter
9) is entirely untouched. It's entirely about the surrounding system's
ability to see and diagnose what the model-plus-tools combination is
actually doing once real, unpredictable requests start arriving. This
surrounding practice — retrieval, tool calling, evaluation, and
observability, stacked together into a working production system — is
what "AI engineering" describes: a genuinely distinct discipline from
training models, drawing on system design, monitoring, and debugging
distributed multi-step behavior rather than the model-training work
covered in Chapters 6 through 10.

## Common Misconceptions

### *"If a system passed its evaluation suite before launch, it's been fully verified and doesn't need further monitoring."*

**Why it's wrong:** Offline evaluation only tests a fixed, necessarily limited set of cases. Real production traffic routinely surfaces failure patterns — edge cases, downstream outages, unusual input combinations — that no evaluation set anticipated, which is exactly why observability is a separate, ongoing practice, not a redundant afterthought to evaluation.

**Correct intuition:** A passing evaluation score verifies the system against the cases someone thought to test in advance; observability is what tells you whether it's still working on the cases nobody thought to test.

**Analogy:** The pre-flight checklist verifies the aircraft is fit to fly — it says nothing about the weather the plane will actually fly through six hours later.

### *"AI engineering means training or fine-tuning models."*

**Why it's wrong:** Most people working under this title never train a foundation model from scratch — an expensive, specialized undertaking covered in Chapters 9 and 10. The day-to-day work centers on building and operating the surrounding system — retrieval, tool calling, agents, evaluation, monitoring — around an existing, already-pretrained model; fine-tuning (Chapter 19) can be one tool in that system-building work, but it isn't the discipline's defining activity.

**Correct intuition:** AI engineering is primarily a systems-and-integration discipline built around a model, not the discipline of producing the model itself — though it can include fine-tuning an existing model as one technique among several.

**Analogy:** Building and maintaining an airline's flight operations is a different job from designing the aircraft's engine — both matter, but they draw on entirely different skills.

### *"A single error or customer complaint means the whole system is broken and needs to be pulled."*

**Why it's wrong:** Observability's whole point is distinguishing an isolated, one-off failure from a systemic pattern — a specific downstream outage affecting a narrow subset of requests, as in the worked example, looks very different in aggregated metrics and traces than a genuine, widespread failure does. But frequency isn't the only axis that matters: one ordinary complaint may say little on its own, while a single severe incident — a privacy exposure, an unauthorized payment — can justify immediate action even without a second occurrence to confirm a pattern.

**Correct intuition:** Aggregated metrics and tracing across many requests are what let a team tell an isolated incident apart from a systemic problem — but severity and frequency are separate questions, and a single high-severity incident doesn't need to repeat before it warrants a response.

**Analogy:** One passenger reporting a bumpy patch of air isn't the same signal as the instruments showing a genuine, sustained loss of altitude — a pilot needs the instruments to know which one she's actually dealing with.

## Practical Implications

This is why production AI teams invest specifically in logging, tracing, and dashboard infrastructure built around LLM and agent calls — a growing category of dedicated "LLM observability" tooling exists for exactly this reason. It also explains why a system can look flawless in testing and still fail unpredictably once real users start using it, without that being a contradiction: the two are answering different questions, on different distributions of input, at different points in time. And it's a direct reason evaluation (Chapter 26) and observability are usually treated as connected, ongoing practices rather than a one-time gate a system passes through once before launch.

## Key Takeaway

**Passing an evaluation suite tells you a system worked on the cases you thought to test — observability is what tells you, continuously, whether it's actually working on the far more varied cases real users are sending it right now.**

## One-Page Summary

- Observability is instrumenting a live AI system — logging, tracing multi-step tool-call/agent sequences, and tracking metrics — to see what it's actually doing in production.
- Real user traffic is far more varied than any fixed evaluation set, which is why evaluation alone, run once before launch, isn't sufficient.
- Logging records individual steps for later reconstruction, but needs redaction, access controls, and retention limits — logging everything by default can itself create a privacy problem; tracing connects steps into one reviewable timeline; metrics track latency, cost, and error rate continuously over time.
- Observability diagnoses a bug after the fact; preventing its effects (e.g. making a tool idempotent, so a retry can't double-charge someone) is a separate, complementary engineering practice.
- AI engineering is the broader discipline of building and operating production systems on top of foundation models — retrieval, tool calling, agents, evaluation, and observability combined — distinct from training a model from scratch, though it can include fine-tuning as one technique among several.
- Most AI engineering work doesn't involve training a foundation model from scratch.
- Aggregated metrics and tracing distinguish an isolated failure from a systemic pattern — but severity and frequency are separate axes; a single severe incident can warrant immediate action without needing to repeat first.

## Further Reading

- Search for "LLM observability" or "AI agent tracing" for concrete, current examples of the instrumentation practices described in §5.
- Search for "AI engineering" for broader discussion of the discipline described in §4, distinct from ML/model-training roles.

## The Next Obvious Question

*Watching a live system closely enough to catch ordinary failures is one thing. What happens when someone is deliberately trying to make the system fail, leak information, or behave in ways it wasn't meant to?*

---

**Glossary terms added this chapter:** Observability, Logging (AI systems), Tracing (AI systems), AI engineering, Idempotency → append to `/glossary.md`

**Misconceptions logged this chapter:** "passing evaluation means no further monitoring needed"; "AI engineering means training or fine-tuning models"; "a single error means the whole system is broken" → append to `/misconceptions.md`

**Concept-graph entries checked off:** Level 8 — Observability, AI engineering, both at Ch. 27
