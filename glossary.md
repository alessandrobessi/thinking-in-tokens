# Glossary

A running index of every term introduced in the book, in order of first
appearance. This table is a thin index, not a duplicate of chapter prose —
the real explanation lives in the chapter itself.

| Term | One-line definition | First introduced |
|---|---|---|
| Information | The reduction in uncertainty a message provides — not its length or volume. | Ch. 2 |
| Symbol | Something that stands for something else by agreement, not resemblance. | Ch. 2 |
| Computation | Mechanical, rule-based manipulation of symbols, requiring no understanding of their meaning. | Ch. 2 |
| Probability (intuition) | A measure of how surprising or expected something is. | Ch. 2 |
| Character | The smallest unit of written text — a single letter, digit, or punctuation mark. | Ch. 3 |
| Word | A familiar linguistic unit that is computationally slippery to define precisely. | Ch. 3 |
| Token | The actual chunk of text a language model operates on — a whole word, a fragment, or a character. | Ch. 3 |
| Tokenization | The process of splitting text into tokens using a fixed, pre-built vocabulary. | Ch. 3 |
| Byte-Pair Encoding (BPE) | An algorithm that builds a token vocabulary by repeatedly merging the most frequent adjacent pair of units. | Ch. 3 |
| Compression | Representing information with fewer symbols by exploiting redundancy/predictability. | Ch. 4 |
| Context | The specific surrounding sequence of tokens that disambiguates meaning or aids prediction. | Ch. 4 |
| Embedding | A token's learned starting location (vector) in a high-dimensional space, reflecting patterns of usage; attention (Ch. 11) later revises it into a context-specific representation. | Ch. 5 |
| Vector space | A space with many numeric dimensions in which embeddings are located, generalizing a 2D map. | Ch. 5 |
| Similarity | Geometric closeness between two embeddings, reflecting similarity of meaning/use. | Ch. 5 |
| Semantic geometry | The idea that meaningful relationships between words correspond to consistent directions/distances in vector space. | Ch. 5 |
| Prediction | Assigning a probability to every possible next token, given everything before it. | Ch. 6 |
| Autoregressive generation | Generating text by repeatedly predicting one token at a time, using all previously generated tokens as context. | Ch. 6 |
| N-gram model | A counting-based prediction method: track how often one word follows a short preceding sequence. | Ch. 7 |
| Curse of dimensionality | The exponential growth in distinct possible sequences as context length increases, which defeats pure counting. | Ch. 7 |
| Neural network | A system of many simple, adjustable units connected in layers, whose overall behavior emerges from the pattern of connections. | Ch. 8 |
| Parameter (weight) | An adjustable number attached to a connection between units, controlling how much an input matters. | Ch. 8 |
| Layer (input/hidden/output) | A stage of units in a neural network; hidden layers build on combinations detected by the layer before them. | Ch. 8 |
| Loss | A number measuring how wrong a single prediction was. | Ch. 9 |
| Training | The repeated loop of predicting, measuring loss, and nudging every parameter to reduce it. | Ch. 9 |
| Learning | The useful patterns that emerge from repeated training, not designed directly by anyone. | Ch. 9 |
| Scaling law | The empirical, forecastable relationship between training data/parameters/compute and resulting loss. | Ch. 10 |
| Undertrained (relative to parameter count) | A model with more parameters than its training data can make good use of. | Ch. 10 |
| Irreducible loss | The small remaining part of loss that scale alone doesn't remove; the power-law scaling description applies to the part that does shrink. | Ch. 10 |
| Attention | A mechanism letting a model weigh every other token's relevance when interpreting or predicting from a given token. | Ch. 11 |
| Positional encoding | A position-dependent tag attached to each token so attention can tell where tokens sit, not just which are present. | Ch. 11 |
| Query/key/value | The three per-token quantities attention compares and combines: what a token seeks, what it offers, and what it contributes if selected. | Ch. 11 |
| Transformer block | A combination of an attention step and an individual feed-forward refinement step, stacked repeatedly to form a transformer. | Ch. 12 |
| Feed-forward step | The part of a transformer block that refines each token's representation individually, via a simple neural network (Ch. 8). | Ch. 12 |
| Residual connection | Adding a block's refinement on top of its input rather than replacing it, preserving information across many stacked layers. | Ch. 12 |
| Normalization | A bookkeeping step keeping numeric scale consistent across stacked transformer blocks. | Ch. 12 |
| Pretraining | The large-scale, generic next-token-prediction training phase, as formally contrasted with fine-tuning. | Ch. 13 |
| Base model | A pretrained model with no further behavioral shaping applied. | Ch. 13 |
| Chat/instruct model | A pretrained model further shaped by fine-tuning and human feedback toward helpful, direct behavior. | Ch. 13 |
| RLHF (preview) | Reinforcement Learning from Human Feedback — training a reward model from human preferences, then adjusting the language model against it. | Ch. 13 |
| Inference | Running a trained model with fixed, frozen parameters to produce output. | Ch. 14 |
| Sampling | The method used to choose one actual token from a model's predicted probability distribution at each generation step. | Ch. 14 |
| Temperature | A control that rescales the model's raw predicted scores before sampling, sharpening or flattening the resulting distribution. | Ch. 14 |
| Top-k / nucleus sampling | Sampling techniques that truncate and renormalize the predicted distribution to the most plausible candidates before drawing from it. | Ch. 14 |
| Hallucination | Generated output that is factually wrong or unsupported, with or without confident phrasing, without intent to deceive. | Ch. 15 |
| Context window | The maximum number of tokens a model can consider at once; everything beyond it isn't visible to the model. | Ch. 16 |
| Memory (system-design sense) | Strategies for managing what stays available within a fixed context window as a conversation grows. | Ch. 16 |
| Retrieval | Finding relevant documents or passages using semantic similarity rather than exact keyword matching. | Ch. 17 |
| Vector database | A specialized storage system for huge numbers of embeddings, built for fast nearest-neighbor search. | Ch. 17 |
| Chunking | Splitting documents into passages before embedding them for retrieval. | Ch. 17 |
| Nearest-neighbor search | Finding the stored embeddings closest to a query's embedding in a vector space. | Ch. 17 |
| Retrieval-Augmented Generation (RAG) | Retrieving relevant passages from an external source and inserting them into the context window before generating an answer; the retrieval mechanism (vector search, keyword search, etc.) is an implementation choice, not part of the definition. | Ch. 18 |
| Fine-tuning (formal) | Continuing training on a smaller, curated dataset after pretraining, using the same mechanism as Ch. 9, aimed at a narrower goal. | Ch. 19 |
| Alignment | The goal of making a model's behavior match what people actually want, not just what's statistically plausible. | Ch. 19 |
| Supervised fine-tuning | Fine-tuning directly on curated example input/output pairs showing desired behavior. | Ch. 19 |
| RLHF (formal) | Training a reward model from human preference comparisons, then adjusting the language model against that reward model. | Ch. 19 |
| Reward model | A model trained to predict which of two candidate responses a human would prefer. | Ch. 19 |
| Quantization | Reducing the numerical precision of a model's stored parameters to shrink memory and compute needs. | Ch. 20 |
| Efficient inference | The broader set of techniques (including quantization) for making inference faster and cheaper without retraining. | Ch. 20 |
| KV cache | Reusing each token's already-computed key and value (Chapter 11) instead of recomputing the whole sequence's attention at every generation step. | Ch. 20 |
| Prefix caching | Reusing KV-cached work across separate requests that share an identical starting prompt. | Ch. 20 |
| Tool calling | A model producing a structured request naming an available capability and its arguments, executed by software outside the model, with the result inserted back into context. | Ch. 21 |
| Tool schema | The advance description of an available tool given to a model: its name, what it does, and the exact arguments it accepts. | Ch. 21 |
| Model Context Protocol (MCP) | A standardized protocol for how tools, external resources, and reusable prompt templates describe themselves and connect to model-serving applications, replacing custom per-pairing integration code. | Ch. 21 |
| Orchestration layer | The surrounding software that parses a model's tool-call request, executes the real function, and returns the result to the model's context. | Ch. 21 |
| AI agent | A model operating inside a loop — read context, decide the next action, execute it, append the result, repeat — deciding its own next step until it judges the goal met. | Ch. 22 |
| Agent loop | The surrounding code that repeatedly feeds tool-call results back into a model's context and calls it again, without a human re-prompting between steps. | Ch. 22 |
| Test-time compute | Spending additional computation at inference time, beyond a single one-shot prediction, to improve reliability on a hard problem — via a longer written chain, multiple checked candidates, or search. | Ch. 23 |
| Reasoning model | A model that generates explicit intermediate steps before a final answer, often trained via reinforcement learning to use that space productively on hard problems — the most visible current instance of test-time compute. | Ch. 23 |
| Chain-of-thought | Prompting or training a model to generate intermediate reasoning steps as context before its final answer. | Ch. 23 |
| Multimodality | A model's ability to make sense of, and with additional components produce, more than one kind of data — text, images, audio — by bridging formats via one of several real architectural patterns. | Ch. 24 |
| Patch embedding | An image patch (a small square region of pixels) converted into an embedding vector, analogous to a text token. | Ch. 24 |
| Cross-modal alignment | Training that pulls a genuinely matching pair's embeddings (e.g. image and caption) together and pushes mismatched pairs apart, so different modalities land in a shared, comparable space. | Ch. 24 |
| Projector | A small learned network that translates a non-text encoder's output into the language model's own embedding space, in the encoder-plus-projector multimodal pattern. | Ch. 24 |
| Cross-attention bridge | Dedicated attention layers letting a language model consult another modality's representations without merging them into one shared token sequence. | Ch. 24 |
| Unified early-fusion tokens | A multimodal pattern where every modality is converted into tokens from one shared vocabulary from the start, and the whole system is trained together on that stream. | Ch. 24 |
| Mixture of Experts (MoE) | An architecture where each layer contains several expert sub-networks and a router activates only a small subset per token. | Ch. 25 |
| Expert | One of several sub-networks within a Mixture-of-Experts layer, only some of which process any given token. | Ch. 25 |
| Router | The learned component in a Mixture-of-Experts layer that decides which experts process a given token. | Ch. 25 |
| Total parameters / Active parameters | Total parameters is a model's full learned capacity across every expert; active parameters is how many are actually used to process one token. | Ch. 25 |
| Evaluation | Measuring whether a complete AI system — model plus retrieval, tools, and orchestration — actually performs well under realistic conditions, trustworthy enough to compare versions, catch regressions, and decide deployment readiness. | Ch. 26 |
| Benchmark | A fixed set of test questions or tasks with known correct answers, scored automatically. | Ch. 26 |
| Contamination (evaluation) | A benchmark's exact test questions leaking into a model's training data, inflating its score without genuine capability improvement. | Ch. 26 |
| LLM-as-judge | Using a separate model to score or compare outputs against a rubric, instead of a human doing it directly. | Ch. 26 |
| Observability | Instrumenting a live AI system — logging, tracing, and metrics — to see what it's actually doing in production and diagnose failures after the fact. | Ch. 27 |
| Logging (AI systems) | Recording inputs, outputs, and intermediate steps of a live system so a specific request can be reconstructed and inspected later; needs redaction, access controls, and retention limits given the sensitive content it can capture. | Ch. 27 |
| Tracing (AI systems) | Connecting every step of one multi-step tool-call or agent sequence into a single reviewable timeline. | Ch. 27 |
| AI engineering | The discipline of building and operating production systems on top of foundation models — retrieval, tool calling, agents, evaluation, and observability combined. | Ch. 27 |
| Idempotency | A property of an operation (e.g. a tool call) where repeating it has the same effect as performing it once, preventing an unexpected retry from causing duplicate real-world effects. | Ch. 27 |
| Security (AI systems) | Protecting an AI system against inputs specifically crafted to make it behave in unintended, harmful ways. | Ch. 28 |
| Prompt injection | Instructions hidden inside content a model merely processes (a document, email, webpage) being treated as if they were legitimate commands. | Ch. 28 |
| Safety | Ensuring a system's behavior, including any real-world actions its tools and agency let it take, actually matches human intent and doesn't cause harm — spanning security, alignment, privacy, bias, high-stakes reliability, misuse, and excessive permissions. | Ch. 28 |
