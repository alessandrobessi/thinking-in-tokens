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
