# Misconception Graph

A running index of the misconception graph described in blueprint.md. Each
row mirrors a "Common Misconceptions" block from a chapter — this table
exists so a later chapter never re-introduces the same misconception under a
different analogy without noticing. The `ID` column is the stable key
referenced by `concept-graph.yaml`'s `misconception_ids`.

| ID | Concept | Misconception | Correct Intuition | Analogy | Chapter |
|---|---|---|---|---|---|
| `ai-consciousness-overnight` | Modern AI's origin | AI became conscious / started truly understanding overnight. | Public *access* crossed a threshold after years of steady, gradual improvement. | A pot of water doesn't decide to boil — it crosses 100°C after a steady rise. | Ch. 1 |
| `ai-vs-bigger-chatbot` | Modern AI vs. chatbots | This is just a bigger version of old scripted chatbots. | The shift is from matching input to a pre-written script, to generating plausible text word by word. | A phrasebook vs. a fluent speaker. | Ch. 1 |
| `computation-implies-understanding` | Computation | A computer that processes information understands what it means. | Computation requires only mechanical rule-following, not comprehension. | A vending machine processes coins without knowing what money is. | Ch. 2 |
| `more-data-equals-more-information` | Information | More information means more data / a longer message. | Information measures reduction of uncertainty, not length. | A 100-page forecast saying "same as always" tells you almost nothing. | Ch. 2 |
| `model-reads-letter-by-letter` | Tokenization | The model reads text one letter at a time. | The model reads a sequence of tokens, mostly whole words or common fragments. | A fluent reader recognizes "the" instantly, not letter by letter. | Ch. 3 |
| `token-always-one-word` | Tokens | A token is always exactly one word. | A token is whatever chunk got assigned a single ID — word, fragment, or less. | Postal abbreviations: common words get short codes, rare ones spelled out. | Ch. 3 |
| `compression-loses-meaning` | Compression | Compressing language loses quality/meaning, like a blurry photo. | Compression removes what's predictable; what remains is the informative core. | Telegram-speak drops "I will be" but keeps "Tuesday." | Ch. 4 |
| `context-is-just-topic` | Context | Context just means the general topic being discussed. | Context is the exact surrounding token sequence used to resolve ambiguity. | Knowing the topic is a river; knowing the prior sentence tells you which "bank" is meant. | Ch. 4 |
| `embeddings-store-definitions` | Embeddings | The model stores dictionary definitions. | The model learns locations in a geometric space. | Cities on a map. | Ch. 5 |
| `similarity-means-synonym` | Similarity | Similarity just means "these words are synonyms." | Closeness reflects similarity of use/context, a broader relationship than synonymy. | Rival neighboring capitals sit close on a culture/economy map despite being opposites. | Ch. 5 |
| `embedding-is-permanent-meaning` | Embeddings (static vs. contextual) | An embedding is a word's one true, permanent representation of meaning. | This chapter's embedding is a token's starting location; attention (Ch. 11) revises it per-sentence into a contextual representation. | A home address is fixed; where the person actually is right now changes throughout the day. | Ch. 5 |
