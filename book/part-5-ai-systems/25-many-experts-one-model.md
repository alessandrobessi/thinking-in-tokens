# Many Experts, One Model

**Part:** AI Systems

**Concept Level:** Level 7

**Prerequisites:** Chapter 8 (parameters), Chapter 12 (transformer blocks)

**New concepts introduced:** Mixture of Experts

---

## Opening Question

*So far, every model in this book runs its full set of parameters on every single input, regardless of how simple or complex that input is. Is there a way to build an enormous model without paying the full computational cost of using all of it on every request?*

## Real-World Story

A large hospital employs dozens of specialists: cardiologists,
dermatologists, orthopedists, and many more. A patient walking in with a
broken wrist doesn't consult every specialist on staff — a triage nurse
quickly figures out which one or two specialists this particular case
actually needs, and routes the patient there. The hospital's total
collective expertise is enormous, spread across every specialist it
employs, but the cost of any one visit is bounded by just the handful of
specialists that specific patient actually sees.

Nobody wastes the cardiologist's time reviewing every broken wrist, and
nobody makes the orthopedist sit through every unrelated case either.
The hospital's *capacity* — how much it collectively knows — and the
*cost of one visit* — how much of that capacity gets used for one patient
— are two completely different numbers, and keeping them separate is
exactly what makes a hospital with dozens of specialists practical to run
at all.

## Worked Example

A large law firm has sixteen specialized partners: tax law, patent law,
criminal defense, and thirteen others. A new case arrives, and an intake
coordinator — who doesn't need deep expertise in any one specialty, just
a good sense of which specialty a case belongs to — routes it to exactly
two of the sixteen partners best suited to it. Those two partners do the
actual work. The other fourteen never touch this particular case, though
a different case arriving the same afternoon might get routed to a
completely different pair.

The firm's total expertise is proportional to all sixteen partners'
combined knowledge. But the cost of handling any single case is
proportional to only two partners' worth of work — not sixteen. Take on
more cases of wildly different types across a year, and different pairs
of partners handle each one, drawing on the firm's full sixteen-partner
capacity in aggregate, while no single case ever pays for more than two
partners at a time.

## Core Intuition

**Mixture of Experts (MoE)** is a way of building a model where selected
feed-forward layers each contain many separate "expert" sub-networks
instead of one, and a small router decides, for each individual token,
which small subset of those experts actually processes it. The model's
total parameter count — its total learned capacity — can be far larger
than the computation those layers spend per token, because that cost
scales mainly with however many experts actually get activated, not the
full total sitting in the model.

## Technical Explanation

In a standard, dense transformer block (Chapter 12), the feed-forward
portion of every layer runs every single token through the exact same
one set of parameters (Chapter 8). A Mixture-of-Experts layer replaces
that single feed-forward network with several separate expert networks —
each one itself a smaller feed-forward network, the same basic kind of
thing Chapter 8 already covered — plus a lightweight router: a small
learned component that looks at a token's current representation and
decides which handful of experts, commonly two, are best suited to
process it. That decision is itself learned during training the same way
any other parameter is learned (Chapter 9), not hand-programmed by anyone
who decided in advance what each expert should specialize in. Real
systems commonly apply this only to some of the model's layers — often
alternating MoE layers with ordinary dense ones — rather than converting
every single layer; the other transformer machinery (attention, and any
dense layers) still processes every token the same way Chapter 12
already described.

Only the selected experts' parameters are actually applied to a given
token; the rest of that layer's experts sit unused for it, though a
different token later in the same sequence, or in an entirely different
request, might get routed to a completely different pair. Because
different tokens get routed differently, some rough specialization
across experts tends to emerge over the course of training — but it
emerges from the router and experts training jointly, not from anyone
assigning a topic to each expert in advance. This is why Mixture-of-
Experts models are described using two separate numbers: **total
parameters** (the sum across every expert in every MoE layer, plus the
model's ordinary dense components — the model's total learned capacity)
and **active parameters** (how many parameters actually get used to
process one token). The entire appeal of the approach is making the
first number far larger than the second.

Active parameters is a useful proxy for per-token compute, not the whole
cost of actually running the model. The router itself costs a small
amount of computation to make its decision every token. When a model is
spread across multiple machines, sending each token's representation to
wherever its chosen experts live costs communication time that a dense
model of the same active size doesn't pay. And if tokens don't route
evenly — some experts getting picked far more often than others — the
busiest expert can become a bottleneck the raw active-parameter count
doesn't capture. Active parameters is the right first-order number for
understanding *why* MoE is cheaper than its total size suggests; it isn't
the complete picture of what it costs to serve one well.

## Common Misconceptions

### *"A Mixture-of-Experts model has one expert per topic — a 'math expert,' a 'history expert' — that a person could identify and label."*

**Why it's wrong:** Routing decisions are learned automatically during training, not assigned by a human. While some rough specialization can emerge, individual experts don't cleanly correspond to interpretable human categories, and a single sentence's tokens are often routed across several different, not-obviously-related experts.

**Correct intuition:** Specialization, where it exists, is an emergent side effect of joint training — not a designed division of labor a person laid out in advance.

**Analogy:** The law firm's intake coordinator doesn't route by a clean, textbook category system either — real cases often blend specialties in ways that don't map neatly onto "the tax expert" or "the patent expert."

### *"Since only a couple of experts are used per token, a Mixture-of-Experts model is just as cheap to run as a small dense model of that active size."*

**Why it's wrong:** Every expert's parameters, used or not for a given token, still have to be stored — often across many machines in a serving system — even though compute cost per token only scales with the active subset. MoE reduces compute cost, not memory footprint, and the tension between the two is often the central practical challenge of actually deploying these models.

**Correct intuition:** MoE trades a smaller per-token compute cost for a larger total memory footprint — it isn't simply "cheap," it's cheap along one specific dimension and expensive along another.

**Analogy:** The hospital still has to keep every specialist on payroll and on-site, even on a day when only two of them happen to see patients — maintaining that full roster costs the hospital something, regardless of how light any single day's actual workload is.

### *"Mixture of Experts means the model is literally made of several completely separate smaller models."*

**Why it's wrong:** The router and every expert are trained jointly, inside one architecture and one training run, sharing everything else in the transformer — attention, other layers, the rest of the model. It isn't several independently trained models glued together afterward, the way an ensemble of separately trained models would be.

**Correct intuition:** It's one model with an internal routing mechanism, not several finished models stitched together after the fact.

**Analogy:** The law firm's partners are colleagues who trained together and share the same firm, clients, and case history — not sixteen solo practitioners who happened to rent office space in the same building.

## Practical Implications

This is the mechanism behind headline claims like "this model has N total parameters but only activates M per token" — a real, meaningful distinction readers will encounter directly in technical announcements, not marketing embellishment. It's why a Mixture-of-Experts model can be dramatically cheaper to run per query than a dense model of equivalent total size, while still requiring substantial hardware just to hold the whole model in memory. And it connects directly back to Chapter 10's scaling laws and Chapter 20's efficient inference: alongside quantization and caching, MoE is another lever for the same underlying goal this book keeps returning to — extracting more capability per unit of compute actually spent.

## Key Takeaway

**Mixture of Experts lets a model have an enormous total number of parameters while only activating a small, learned subset of them per token — trading a larger memory footprint for a computational cost much closer to a far smaller model's.**

## One-Page Summary

- Mixture of Experts replaces selected feed-forward layers' single network with several expert sub-networks plus a small router that picks a handful of experts per token — usually applied to some of a model's layers, not necessarily every one.
- Only the selected experts' parameters process a given token; routing is learned during training, not assigned by a human in advance.
- Total parameters (full model capacity) and active parameters (a useful proxy for per-token compute cost) are two distinct, separately meaningful numbers for an MoE model — router overhead, cross-machine communication, and uneven routing mean active parameters isn't the complete cost picture.
- Some specialization across experts can emerge from training, but it isn't clean, human-interpretable topic assignment.
- MoE reduces per-token compute cost, not memory footprint — the full parameter set still has to be stored regardless of how few experts activate on average.
- Router and experts are trained jointly inside one architecture, not stitched together from separately trained models.
- MoE is another lever, alongside quantization (Chapter 20) and scaling laws (Chapter 10), for getting more capability per unit of compute actually spent.

## Further Reading

- Search for "Mixture of Experts" or "sparse MoE transformer" for concrete, current examples of the total-parameters-versus-active-parameters distinction described in §5.
- Search for "Switch Transformer" for an influential, simplified routing scheme (one expert per token) that helped popularize MoE at scale.

## The Next Obvious Question

*This book has now covered how these systems are built and how they act — reading, predicting, retrieving, reasoning, reaching into the world. But how does anyone actually know, in a rigorous way, whether a given system is good: better than another, safe enough to deploy, actually doing what it's supposed to?*

---

**Glossary terms added this chapter:** Mixture of Experts (MoE), Expert, Router, Total parameters, Active parameters → append to `/glossary.md`

**Misconceptions logged this chapter:** "MoE has one expert per topic a person could label"; "MoE is as cheap as a small dense model of the active size"; "MoE is literally several separate smaller models" → append to `/misconceptions.md`

**Concept-graph entries checked off:** Level 7 — Mixture of Experts, at Ch. 25 (closes Part V)
