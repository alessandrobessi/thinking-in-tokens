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
