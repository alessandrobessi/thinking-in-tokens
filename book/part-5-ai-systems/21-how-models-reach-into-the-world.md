# How Models Reach Into the World

**Part:** AI Systems

**Concept Level:** Level 6

**Prerequisites:** Chapter 14 (inference), Chapter 16 (context windows)

**New concepts introduced:** Tool calling, Tool schema, Model Context Protocol (MCP)

---

## Opening Question

*So far, every capability this book has covered has kept the model's own job the same: read context, produce text. Even Chapter 18's retrieval, which genuinely happens outside the model, only ever hands the model more text to read — it isn't something the model itself does. How does a model actually reach outside itself and take an action in the real world?*

## Real-World Story

A financial analyst is finishing a report and needs one more number: today's
price for a particular stock. She doesn't have it memorized — and even if
she'd memorized yesterday's price, that number would already be stale. So
she doesn't guess. She messages a colleague down on the trading floor with
a precise, structured request: the ticker symbol, nothing else. The
colleague looks up the live number and messages back a single figure. The
analyst drops that figure into her report and keeps writing.

Notice what didn't happen. The analyst didn't walk down to the trading
floor herself. She didn't need to know how the price-lookup system worked
internally. She just knew *that* such a request was possible, exactly how
to phrase it, and that a reliable answer would come back in a form she
could immediately use. Chapter 18 already covered a version of this — RAG
adds retrieved information into a model's context before it generates a
response, and that retrieval step can itself reach live sources, not
only a fixed document collection. What's different here isn't retrieval
versus something else; it's that tool calling is the more general
interface underneath. Retrieval can be implemented as one specific kind
of tool call, but tools aren't limited to fetching information back —
they can run exact computation, or take an action with a real side
effect, like sending a message or updating a record, that has no
equivalent in simply retrieving a passage.

## Worked Example

Ask a language model to multiply 847 by 2,193 using nothing but its own
next-token prediction (Chapter 6), and it will often get a large
multiplication like this at least slightly wrong. That's not simply a
knowledge gap — a model can pick up rough internal patterns for
arithmetic from its training data, and those patterns sometimes get
smaller calculations right, but they're learned approximations, not a
guaranteed, exact procedure. Predicting each digit is still fundamentally
the same operation as predicting a plausible-looking next word in a
sentence (Chapter 7 covered exactly this distinction between
pattern-matching and the operation you actually want), and that operation
comes with no guarantee of exactness the way a calculator's arithmetic
does.

Now give the same model access to a calculator tool. Instead of predicting
digits directly, the model instead predicts a small, structured request:
something like *multiply, 847, 2193*. That request isn't sent through the
model's own token-by-token guessing at all — it's handed to an actual
calculator program, which computes 1,857,471 using ordinary, exact
arithmetic, the same way a spreadsheet would. That exact number is then
inserted back into the model's context window (Chapter 16) as new text,
and the model reads it and reports it back to the user. The model didn't
"get better at math." It got access to something that computes exactly,
every time, instead of predicting a plausible-looking answer that's
usually — but not reliably — correct.

## Core Intuition

**Tool calling** is a model producing a structured request — naming a
specific available capability and the exact arguments it needs — instead
of, or in addition to, producing ordinary prose. That request is executed
by software outside the model itself; the result is then inserted back
into the model's context window as new text, which the model reads and
continues generating from, using the exact same generation mechanism
(Chapter 6, Chapter 14) it always uses. The model doesn't gain a new kind
of ability. It gains a new kind of thing it's allowed to write, and a
system on the other end that knows what to do when it writes that.

## Technical Explanation

A tool call rests on a division of labor that's easy to blur if you only
see the finished product. The model is responsible for exactly one thing:
deciding, based on everything in its context, *whether* calling a tool is
the most useful next output, *which* available tool fits, and *what*
arguments to fill in — all of it produced the normal way, as predicted
text, just text shaped to match a specific expected structure instead of
free-form prose. Everything after that point is not the model's doing. A
surrounding piece of software — often called an orchestration layer —
parses that structured request, actually calls the real function (a
calculator, a weather API, a database query, an email-sending service,
whatever was made available), and inserts the result back into the
context window before generation continues. The model that produces the
next sentence, describing today's weather or confirming an email was
sent, has that information only because it was just handed to it as
freshly appended context — the same mechanism Chapter 18 used for
retrieved documents, now carrying the result of an executed action
instead of a retrieved passage.

This only works because every available tool is described to the model in
advance, typically inserted into its context alongside the conversation
itself, as a **tool schema**: a name, a plain description of what it does,
and the exact arguments it accepts. The model can only request tools that
appear in that schema — it has no way to invent access to a capability
nobody described to it, no matter how plausible a request for one might
sound. Whether a specific fine-tuned or aligned (Chapter 19) model
reliably produces well-formed requests, picks the right tool, and fills in
sensible arguments is itself a trained behavior, not a guarantee that
comes free with the architecture.

That description step is part of what the **Model Context Protocol
(MCP)** standardizes. Before a shared protocol existed, every pairing of a
specific model-serving application and a specific external tool or data
source needed its own custom integration code — a combinatorial problem
that got worse as more tools and more model providers appeared. MCP
defines a common, standardized way for tools, and more broadly for
external resources (documents, records, live data) and reusable prompt
templates, to describe themselves to a model-serving application and be
invoked or retrieved by it — tool calling in this chapter's sense is the
part of MCP most relevant here, but the protocol's scope is broader than
tool schemas alone. MCP removes the need to invent a custom message protocol for every
pairing — an MCP-compatible application can speak to any MCP-compatible
server using the same protocol, rather than a one-off integration built
specifically for that pairing — though a real deployment still needs its
own configuration, authentication, and permission handling on top; the
protocol standardizes the conversation, not everything around it. MCP
doesn't change what tool calling fundamentally is,
and it isn't the only way to implement tool calling — it's one
increasingly adopted open standard for *how the connection itself gets
standardized*, which is why this chapter teaches it as a concrete instance
of the durable idea, not as a separate mechanism.

## Common Misconceptions

### *"When a model 'uses a tool,' it's directly running code or reaching out onto the internet itself."*

**Why it's wrong:** The model only ever produces generated tokens — in this case, a specifically structured piece of output naming a tool and its arguments. It does not execute the requested operation itself; a separate system outside the model parses that output and performs the actual action.

**Correct intuition:** The model requests; surrounding software executes. Those are two different systems with two different jobs, even though the finished conversation makes the boundary invisible.

**Analogy:** The financial analyst doesn't walk onto the trading floor herself — she sends a precise request and waits for someone else to come back with the answer.

### *"Tool calling means the model can use whatever tool it decides it needs, on its own initiative."*

**Why it's wrong:** A model can only request tools that were explicitly described to it in advance, in a tool schema listing exactly what's available and what arguments each one takes. It cannot invent access to a capability nobody exposed to it, regardless of how useful or plausible the request would sound.

**Correct intuition:** Available tools are a fixed, predefined catalog set up by whoever built the surrounding system — not an open-ended set the model can expand on its own.

**Analogy:** The analyst's colleague can look up a stock price because that specific request line exists — he can't suddenly also approve a wire transfer just because the analyst phrases a request for one.

### *"MCP is a fundamentally smarter or more capable kind of AI, not just a connection standard."*

**Why it's wrong:** MCP adds no new reasoning ability to a model at all. It standardizes how a tool or data source describes itself and how a model-serving application connects to it — the same tool-calling mechanism as before, now usable across many tools and providers without custom integration code for every single pairing.

**Correct intuition:** MCP is a shared plug shape, not a new kind of appliance — it changes how easily things connect, not what a model can fundamentally do once connected.

**Analogy:** A standardized electrical outlet doesn't make any appliance more powerful — it just means any compliant appliance can plug into any compliant socket without a custom adapter built for that one pairing.

## Practical Implications

This is what sits underneath the labels "function calling," "tools," "plugins," and "connectors" across different AI products — different names for the same underlying pattern this chapter just walked through. It's also the direct answer to something Chapters 16 and 18 already raised: a model's trained knowledge has a fixed cutoff, and while RAG can reach live sources too, tool calling is the broader interface — retrieval is one kind of tool call, alongside exact computation and actions with a real-world effect (sending a message, updating a record) that don't reduce to fetching a passage at all. And because the available tools are always an explicit, predefined catalog, evaluating any AI product that claims to "use tools" or "connect via MCP" comes down to one practical question: exactly which tools were exposed to it, and by whom — not some open-ended claim about what the model can reach.

## Key Takeaway

**A model doesn't reach into the world itself — it emits a precise, structured request naming a predefined tool and its arguments, and a separate system executes that request and hands the result back as new context for the model to keep reasoning from.**

## One-Page Summary

- Tool calling is a model producing a structured request (a tool name plus arguments) instead of, or alongside, ordinary prose — using the same generation mechanism as always.
- The model never executes anything itself. A surrounding orchestration layer parses the request, runs the real function, and inserts the result back into the context window as new text.
- Available tools form a fixed, predefined catalog described to the model in advance as a tool schema — the model cannot request a tool that was never exposed to it.
- Tool calling is the broader interface: retrieval (Chapter 18) can be implemented as one kind of tool call, alongside exact computation and real-world actions that don't reduce to fetching a passage at all.
- The Model Context Protocol (MCP) standardizes the communication protocol between tools/data sources and model-serving applications, reducing custom, one-off protocol glue — real deployments still need their own configuration, authentication, and permissions, and MCP doesn't add any new reasoning capability.
- Producing well-formed, correctly-targeted tool requests is itself a trained behavior (Chapter 19), not a free guarantee of the architecture.

## Further Reading

- Search for "function calling" or "tool use" from any major model provider for concrete, current examples of the schema and request format described in §5.
- Search for "Model Context Protocol" or "MCP" for the open standard described in §5 and its growing ecosystem of tool servers.

## The Next Obvious Question

*Once a model can request a single tool and read back a single result, what happens when it's allowed to chain many such requests together on its own — deciding, after each result, what to do next — in order to accomplish a goal that takes more than one step?*

---

**Glossary terms added this chapter:** Tool calling, Tool schema, Model Context Protocol (MCP), Orchestration layer → append to `/glossary.md`

**Misconceptions logged this chapter:** "the model directly executes code/reaches the internet itself"; "the model can call whatever tool it decides it needs, on its own initiative"; "MCP is a smarter kind of AI, not just a connection standard" → append to `/misconceptions.md`

**Concept-graph entries checked off:** Level 6 — Tool calling, Model Context Protocol (MCP), both at Ch. 21
