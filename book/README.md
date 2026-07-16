# The Architecture of Intelligence

*A Mental Model for Modern AI Systems*

This is the manuscript, organized by Part and Chapter following the concept
dependency graph in [`../blueprint.md`](../blueprint.md). Chapters are
numbered globally (01–30) and must be read in order — each chapter's
vocabulary is a prerequisite for the next.

The manuscript teaches entirely through prose — no diagrams. Every chapter
pairs an opening story with a second, fully-written worked example, and
ends on one bolded, memorable key-takeaway sentence instead of an
illustration (see `../blueprint.md`'s "No Diagrams" section for why).

Supporting project files: [`../style-guide.md`](../style-guide.md) (voice,
analogy registry), [`../glossary.md`](../glossary.md),
[`../misconceptions.md`](../misconceptions.md), [`../concept-graph.md`](../concept-graph.md).

**Status:** The full manuscript, Parts I–VI (Chapters 1–30), is written.

---

## Part I — Information

1. [Why AI Suddenly Changed](part-1-information/01-why-ai-suddenly-changed.md)
   — *Why did AI suddenly get so good, seemingly overnight?*
2. [What Is Information?](part-1-information/02-what-is-information.md)
   — *What does it actually mean for a computer to "know" or "read" something?*
3. [Characters, Words and Tokens](part-1-information/03-characters-words-tokens.md)
   — *How does a computer break language into pieces it can actually work with?*
4. [Compressing Language](part-1-information/04-compressing-language.md)
   — *Why can a short sentence carry so much meaning, and how do computers exploit that?*
5. [Meaning as Geometry](part-1-information/05-meaning-as-geometry.md)
   — *How can a computer represent the meaning of a word, not just the word itself?*

## Part II — Prediction

6. [Predicting the Next Token](part-2-prediction/06-predicting-the-next-token.md)
   — *Now that a computer can represent meaning as a location in space, how can it use that to predict what comes next?*
7. [Why Counting Is Not Enough](part-2-prediction/07-why-counting-is-not-enough.md)
   — *Why not just count how often one word follows another in a giant table, instead of building something as complicated as a neural network?*
8. [Neural Networks Without Mathematics](part-2-prediction/08-neural-networks-without-mathematics.md)
   — *What is a neural network, actually — without the math?*
9. [Learning From Examples](part-2-prediction/09-learning-from-examples.md)
   — *How does a neural network actually learn the right values for its billions of adjustable parameters?*
10. [Scaling Laws](part-2-prediction/10-scaling-laws.md)
    — *Is there a predictable relationship between how big a model is and how good it becomes — and does scaling ever stop paying off?*

## Part III — The Transformer

11. [The Attention Revolution](part-3-the-transformer/11-the-attention-revolution.md)
    — *How does a model decide which earlier words matter most when predicting the next one?*
12. [Building a Transformer](part-3-the-transformer/12-building-a-transformer.md)
    — *Once a model can weigh relevance across an entire passage, how do you actually assemble that mechanism into a full working system?*
13. [From Transformer to ChatGPT](part-3-the-transformer/13-from-transformer-to-chatgpt.md)
    — *The transformer architecture existed since 2017 — why did it take years before something like ChatGPT appeared?*
14. [Inference and Text Generation](part-3-the-transformer/14-inference-and-text-generation.md)
    — *Once a model has all this training baked in, what actually happens, step by step, when it generates a response to your prompt?*
15. [Why Models Hallucinate](part-3-the-transformer/15-why-models-hallucinate.md)
    — *If the model is just sampling plausible-sounding tokens, what happens when "plausible-sounding" and "actually true" come apart?*

## Part IV — Building Useful AI

16. [Context Windows and Memory](part-4-building-useful-ai/16-context-windows-and-memory.md)
    — *If a model's own trained-in knowledge can run out or go stale, how can it be given a bigger, more reliable memory to draw from?*
17. [Semantic Retrieval and Vector Databases](part-4-building-useful-ai/17-semantic-retrieval-and-vector-databases.md)
    — *If a context window can't hold everything, how can a model still pull in specific relevant information exactly when it's needed?*
18. [Retrieval-Augmented Generation](part-4-building-useful-ai/18-retrieval-augmented-generation.md)
    — *Once relevant documents can be retrieved this way, how does a model actually combine that with its own generation process to produce a grounded answer?*
19. [Fine-Tuning and Alignment](part-4-building-useful-ai/19-fine-tuning-and-alignment.md)
    — *How does additional training after pretraining actually work, and how does a model get pointed toward being safe and aligned with what people actually want?*
20. [Quantization and Efficient Models](part-4-building-useful-ai/20-quantization-and-efficient-models.md)
    — *Can a trained model be made to run cheaper and faster, without retraining it from scratch or changing what it fundamentally knows?*

## Part V — AI Systems

Chapters here are named for the durable question they answer, not for the
specific standard implementing today's answer. MCP, for instance, is taught
inside Chapter 21 as "today's connection standard," not given its own
chapter — so the chapter stays true even after the standard changes.

21. [How Models Reach Into the World](part-5-ai-systems/21-how-models-reach-into-the-world.md)
    — *How does a model actually reach outside itself and take an action in the real world?*
22. [From Single Calls to Agents](part-5-ai-systems/22-from-single-calls-to-agents.md)
    — *What happens when a model is allowed to chain many tool requests together on its own, deciding after each result what to do next?*
23. [Thinking Longer, Not Just Faster](part-5-ai-systems/23-thinking-longer-not-just-faster.md)
    — *What happens when a model is specifically trained to spend more of its own generated text working through a problem before committing to a final answer?*
24. [One Model, Many Senses](part-5-ai-systems/24-one-model-many-senses.md)
    — *How does a model built entirely around predicting the next token learn to also make sense of an image or a sound?*
25. [Many Experts, One Model](part-5-ai-systems/25-many-experts-one-model.md)
    — *Is there a way to build an enormous model without paying the full computational cost of using all of it on every request?*

## Part VI — The Future

26. [Evaluating AI Systems](part-6-the-future/26-evaluating-ai-systems.md)
    — *How does anyone actually know, in a rigorous way, whether a given AI system is good?*
27. [AI Engineering and Observability](part-6-the-future/27-ai-engineering-and-observability.md)
    — *Once a system is live, handling real, unpredictable user requests, how do you know it's still working correctly?*
28. [Security and Safety](part-6-the-future/28-security-and-safety.md)
    — *What happens when someone is deliberately trying to make the system fail, leak information, or behave in ways it wasn't meant to?*
29. [Where AI Is Going](part-6-the-future/29-where-ai-is-going.md)
    — *Given everything covered so far, where does this technology actually go from here?*
30. [How to Keep Learning](part-6-the-future/30-how-to-keep-learning.md)
    — *Now that this mental model exists, how does a reader actually keep it current as the field keeps moving?*
