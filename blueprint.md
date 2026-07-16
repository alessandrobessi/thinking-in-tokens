# The Architecture of Intelligence

## A Mental Model for Modern AI Systems

> **Mission**
>
> Build the definitive conceptual introduction to modern AI systems.
> Readers should finish the journey with a durable mental model of how
> modern AI works---from tokens to autonomous agents---without requiring
> mathematics, programming, or prior machine learning knowledge.

------------------------------------------------------------------------

# Vision

This project is **not just a book**.

It is a **knowledge architecture** whose primary artifact is a book, but
whose long-term ecosystem includes:

-   A professionally published book
-   An interactive companion website
-   A concept dependency graph
-   A misconception graph
-   A living glossary
-   Conceptual exercises
-   Teaching material
-   A video course

The ambition is to become for AI what **SICP** became for computer
science and what **The Feynman Lectures** became for physics: a timeless
resource that teaches readers how to think rather than what to memorize.

------------------------------------------------------------------------

# Audience

This book is written for curious professionals:

-   managers
-   consultants
-   product leaders
-   founders
-   sales professionals
-   executives
-   students
-   lifelong learners

Readers are assumed to be intelligent and curious---not technical.

No mathematics or programming background is required.

------------------------------------------------------------------------

# Promise to the Reader

After completing the book, readers should be able to:

-   Explain how LLMs generate text.
-   Understand tokens, embeddings, attention, transformers, inference,
    and training.
-   Explain why hallucinations happen.
-   Understand RAG, vector databases, context windows, tool calling,
    MCP, AI agents, multimodal models, reasoning models, quantization,
    and Mixture of Experts.
-   Read engineering blogs and product announcements with confidence.
-   Distinguish genuine advances from marketing hype.
-   Build a coherent mental model that continues to scale as AI evolves.

------------------------------------------------------------------------

# Teaching Philosophy

Inspired by **Richard Feynman**

-   Explain difficult ideas without sacrificing correctness.
-   Simplify by revealing the essential idea---not by hiding complexity.

Inspired by **SICP**

-   Build knowledge incrementally.
-   Every chapter becomes a prerequisite for the next.
-   The reader constructs a complete mental model rather than
    accumulating isolated facts.

------------------------------------------------------------------------

# Core Design Principles

1.  Intuition before terminology.
2.  One important question per chapter.
3.  One genuinely new idea per page.
4.  Stories before abstractions.
5.  Multiple concrete examples before generalizing a rule --- an idea
    isn't done until it's been turned around and looked at from a second
    angle, not just stated once.
6.  Technical rigor without implementation details.
7.  Reuse analogies consistently.
8.  Every explanation should pass the "Feynman test".
9.  Every chapter ends with:
    -   one memorable, one-sentence key takeaway
    -   "The next obvious question..." leading naturally into the
        following chapter.

------------------------------------------------------------------------

# Concept Dependency Graph

The manuscript is generated from a dependency graph---not written
sequentially.

Level 0 - Information - Symbols - Computation - Probability (intuition)

↓

Level 1 - Characters - Words - Tokens - Tokenization - Compression -
Context

↓

Level 2 - Embeddings - Vector spaces - Similarity - Semantic geometry

↓

Level 3 - Prediction - Neural networks - Parameters - Learning -
Training - Loss - Scaling laws

↓

Level 4 - Attention - Positional encoding - Transformer blocks -
Inference - Sampling

↓

Level 5 - Hallucinations - Fine-tuning - Alignment - Context windows -
Memory

↓

Level 6 - Retrieval - Vector databases - RAG - Tool calling - Model
Context Protocol (MCP) - AI agents

↓

Level 7 - Reasoning models - Multimodality - Mixture of Experts -
Quantization - Efficient inference

↓

Level 8 - Evaluation - Observability - Security - Safety - AI
engineering

**Non-negotiable rule**

Never introduce a concept before all of its prerequisites have been
established.

If a dependency is violated, the table of contents changes---not the
explanation.

------------------------------------------------------------------------

# Misconception Graph

Every important concept includes:

-   motivating question
-   common misconception
-   correct intuition
-   analogy
-   technical explanation
-   practical implications

Example

Concept: Embeddings

Misconception: "The model stores dictionary definitions."

Correct intuition: "The model learns locations in a geometric space."

Analogy: Cities on a map.

------------------------------------------------------------------------

# Narrative Graph

The book is organized around questions rather than technologies.

1.  How can a computer read?
2.  How can it represent meaning?
3.  How can it learn?
4.  How can it predict?
5.  How can it remember?
6.  How can it use external knowledge?
7.  How can it use tools?
8.  How can it act?
9.  How can it reason?
10. Where is AI going?

Every answer should naturally create the next question.

------------------------------------------------------------------------

# Expanded Table of Contents

## Part I --- Information

1.  Why AI Suddenly Changed
2.  What Is Information?
3.  Characters, Words and Tokens
4.  Compressing Language
5.  Meaning as Geometry

## Part II --- Prediction

6.  Predicting the Next Token
7.  Why Counting Is Not Enough
8.  Neural Networks Without Mathematics
9.  Learning From Examples
10. Scaling Laws

## Part III --- The Transformer

11. The Attention Revolution
12. Building a Transformer
13. From Transformer to ChatGPT
14. Inference and Text Generation
15. Why Models Hallucinate

## Part IV --- Building Useful AI

16. Context Windows and Memory
17. Semantic Retrieval and Vector Databases
18. Retrieval-Augmented Generation
19. Fine-Tuning and Alignment
20. Quantization and Efficient Models

## Part V --- AI Systems

Chapter titles here name the durable question each chapter answers, not
the specific standard or product implementing today's answer to it. Where
a current standard is genuinely important (e.g. MCP), it is taught inside
the relevant question-chapter as "the current answer," not given its own
chapter --- so the chapter stays true even after the standard changes.

21. How Models Reach Into the World (tool calling, including MCP as
    today's connection standard)
22. From Single Calls to Agents (AI agents)
23. Thinking Longer, Not Just Faster (reasoning models)
24. One Model, Many Senses (multimodal models)
25. Many Experts, One Model (Mixture of Experts)

## Part VI --- AI in the Real World

26. Evaluating AI Systems
27. AI Engineering and Observability
28. Security and Safety
29. How to Judge What Comes Next
30. How to Keep Learning

------------------------------------------------------------------------

# Standard Chapter Template

This template is an **editorial checklist**, not a mandatory set of
reader-facing headings. Every chapter must substantively cover all eleven
elements before it is considered complete --- but a chapter's actual prose
may blend, reorder, or dissolve these elements into its own rhythm rather
than exposing eleven literal section breaks. A chapter may open with a
thought experiment instead of a story, build its worked example directly
into the surrounding prose instead of setting it apart, or weave a
misconception into the surrounding prose instead of setting it apart in
its own block. The obligation is completeness; the presentation is free.

The eleven elements every chapter must cover:

1.  Opening question
2.  Real-world story
3.  Worked example --- a second, fully-written-out concrete example that
    reinforces the same idea from a different angle than the opening
    story (never a diagram; see "No Diagrams" below)
4.  Core intuition
5.  Technical explanation
6.  Common misconceptions
7.  Practical implications
8.  Key takeaway --- one bolded, memorable sentence that crystallizes the
    chapter's single most important idea
9.  One-page summary
10. Further reading
11. "The next obvious question..."

The manuscript's working draft may still use these as literal section
headers during drafting, precisely because that makes the checklist
trivial to verify chapter by chapter. Loosening the *reader-facing*
presentation is a later editorial pass, not a requirement of the first
draft.

------------------------------------------------------------------------

# No Diagrams

Earlier drafts of this project treated illustration as a primary teaching
device --- a "canonical mental-model diagram" per chapter, a fixed visual
language, an eventual editable SVG library. In practice, across Parts I
and II, the diagrams did not earn their place: they mostly re-illustrated
what the prose already said, added production overhead (a whole SVG
authoring/rendering system, twice rebuilt after platform rendering
failures) disproportionate to their teaching value, and the effort spent
on them competed directly with the effort available for prose depth.

This project now teaches entirely through prose: stories, worked examples,
analogies, and precise technical explanation. Every concept gets **at
least two** concrete groundings (the real-world story plus the worked
example, at minimum) instead of one narrative plus one picture. Where a
chapter previously ended on a diagram, it now ends on one sharply-written
sentence (the "key takeaway" in the template above) that does the same
job --- giving the reader one crystallized image to carry forward --- with
words instead of an illustration.

This is a deliberate reversal, not a deferral. Do not reintroduce diagrams,
an icon vocabulary, or a "visual language" system without revisiting this
decision explicitly.

------------------------------------------------------------------------

# Living Companion

The website extends---not duplicates---the book.

Features:

-   Quizzes
-   Updated references
-   A searchable glossary
-   A text-based concept explorer (browse/search the concept dependency
    graph directly, per level and per prerequisite)

------------------------------------------------------------------------

# Success Criteria

The reader should be able to:

-   understand AI announcements
-   read engineering blogs
-   explain AI concepts to colleagues
-   discuss architectures with engineers
-   recognize hype
-   continue learning independently

The ultimate measure of success is not memorizing terminology.

It is acquiring a durable mental model of modern AI that remains useful
as the technology evolves.
