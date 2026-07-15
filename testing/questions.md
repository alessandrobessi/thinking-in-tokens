# Reader-Testing Question Bank — Chapters 1–20

See `README.md` in this directory for how to run a session, the scoring
rubric, and the pre-test step. Misconception-resistance prompts are paired
with the `ID` from `misconceptions.md` so a scoring gap can be traced
directly back to a specific chapter passage.

Misconception-resistance prompts are phrased as **scenarios**, not
yes/no questions — "is X true?" can be answered correctly by guessing the
social cue instead of understanding the mechanism. "Someone claims X, how
do you respond?" forces the reader to produce the actual explanation, which
is what gets scored (see README.md's 0/1/2 rubric).

## Chapter 1 — Why AI Suddenly Changed

- **Comprehension:** "In your own words, why did AI chatbots suddenly get
  so much better around 2022?"
- **Transfer:** "A headline claims a new AI breakthrough happened because
  of 'a completely new kind of chip.' What would you want to know before
  deciding whether that explains it?"
- **Misconception resistance** (`ai-consciousness-overnight`): "A colleague
  says ChatGPT's 2022 release proves machines suddenly became conscious.
  How would you respond, and what alternative explanation would you give?"
- **Misconception resistance** (`ai-vs-bigger-chatbot`): "A friend says
  'modern chatbots are just bigger versions of the 2016 customer-service
  bots.' Do you agree? Explain the actual difference."

## Chapter 2 — What Is Information?

- **Comprehension:** "What does it actually mean for a computer to 'know'
  or 'read' something?"
- **Transfer:** "A friend says a 100-page report gave them 'a lot of
  information.' Is that necessarily true?"
- **Misconception resistance** (`computation-implies-understanding`):
  "Someone says 'the model must understand what my message means —
  otherwise how could it respond so well?' How would you explain what's
  actually happening?" Follow-up: "Is a thermostat deciding to turn on the
  heat any different, in kind, from a computer processing your message?"
- **Misconception resistance** (`more-data-equals-more-information`): "A
  colleague says a 100-page quarterly report contains 'a lot of
  information' just because of its length. Do you agree? Explain why or
  why not."
- **Transfer (chapter's own thought experiment):** "Which carries more
  information — 'it will rain sometime this century' or 'it will rain
  tomorrow at 3pm'?" (Correct answer: the second, shorter sentence — it
  commits to something far less probable, so it reduces more uncertainty.
  If the reader picks the first because it's a "bigger claim" or focuses
  on sentence length, that's the more-data-equals-more-information
  misconception surfacing under a new label.)

## Chapter 3 — Characters, Words and Tokens

- **Comprehension:** "What is a 'token,' and how is it different from a
  word?"
- **Transfer:** "Why might an AI company charge a different price for the
  exact same sentence written in English versus another language?"
- **Misconception resistance** (`model-reads-letter-by-letter`): "Someone
  claims a language model reads text 'one letter at a time, like sounding
  out a word.' Is that accurate? Explain what actually happens."
- **Misconception resistance** (`token-always-one-word`): "A colleague
  says 'a token is basically just a word.' Explain why that's not quite
  right."
- **Transfer (chapter's own thought experiment):** "How do you think a
  tokenizer would handle the word 'quokka' — real, but rare?" (Correct
  answer: broken into two or three familiar sub-word pieces, not rejected
  and not necessarily a single dedicated token. If the reader assumes the
  model would simply fail or substitute a placeholder, that's the
  token-always-one-word misconception surfacing under a new label.)

## Chapter 4 — Compressing Language

- **Comprehension:** "Why can a short sentence carry a lot of meaning?"
- **Transfer:** "Here's an old telegram: 'ARRIVE TUES STOP.' Explain why
  the missing words don't hurt understanding."
- **Misconception resistance** (`compression-loses-meaning`): "Someone
  says compressing language 'always loses some meaning, like a blurry
  photo loses detail.' Do you agree? Explain."
- **Misconception resistance** (`context-is-just-topic`): "A friend says
  'context just means what the conversation is generally about.' Is that
  the full picture? Explain."

## Chapter 5 — Meaning as Geometry

- **Comprehension:** "What is an embedding?"
- **Transfer:** "Would 'physician' and 'doctor' end up close together or
  far apart on this map? Why?"
- **Transfer (chapter's own thought experiment):** "Would 'hot' be closer
  to 'cold,' or closer to 'sandwich'? Why?" (Correct answer: closer to
  "cold" — same grammatical slot, i.e. similar *use*, not similar
  *meaning*. If the reader says "sandwich," they're reasoning about
  meaning-as-agreement, not meaning-as-use — flag as a live
  misconception-resistance failure even though it's phrased as transfer.)
- **Misconception resistance** (`embeddings-store-definitions`): "Someone
  says 'the model must have something like a dictionary stored inside it,
  since it clearly knows what words mean.' How would you respond?"
- **Misconception resistance** (`embedding-is-permanent-meaning`): "A
  colleague says 'the embedding for a word is fixed — it's the same
  wherever the word shows up.' Is that accurate? Explain."

## Chapter 6 — Predicting the Next Token

- **Comprehension:** "How does a model decide what word to write next?"
- **Misconception resistance** (`model-plans-whole-sentence`,
  `prediction-is-lookup`): "Someone tells you: 'the model must plan out
  its whole answer in advance, since the response is so coherent — and
  besides, it's probably just looking up something similar it read
  before.' Address both claims."
- **Transfer (chapter's own thought experiment):** "Given 'The opposite of
  hot is ___,' rank 'cold,' 'freezing,' and 'a banana' by how likely each
  one is to come next." (Correct answer: cold first by a wide margin,
  freezing a distant second, banana essentially zero — the point is that
  the reader can do this ranking instantly and intuitively, which is the
  same operation the model performs computationally over its whole
  vocabulary.)

## Chapter 7 — Why Counting Is Not Enough

- **Comprehension:** "Why doesn't a simple word-counting table work as
  well as a neural network?"
- **Misconception resistance** (`bigger-counting-table-works`,
  `ai-is-bigger-counting-table`): "A colleague says 'if we just collected
  100x more text, a simple counting-based approach would eventually work
  as well as a neural network — it's basically the same idea, just
  bigger.' How would you respond?"

## Chapter 8 — Neural Networks Without Mathematics

- **Comprehension:** "What is a neural network, in your own words?"
- **Misconception resistance** (`nn-simulates-brain`): "Someone says 'a
  neural network is basically a simulation of a human brain.' Explain
  what's accurate and what's misleading about that claim."
- **Misconception resistance** (`more-parameters-more-understanding`): "A
  colleague says 'Model A has ten times more parameters than Model B, so
  Model A must be better.' Is that a safe conclusion? Explain."
- **New probe (post-review addition):** "Someone says 'this is basically
  how ChatGPT is built — just a big stack of these identical layers.'
  What would you tell them?" — correct answer should reference the
  chapter's boundary paragraph distinguishing this generic network from
  the transformer (Part III).

## Chapter 9 — Learning From Examples

- **Comprehension:** "How does a neural network learn the right values for
  its parameters?"
- **Misconception resistance** (`training-is-memorization`): "A friend
  says 'training a model on the internet just means it memorizes all that
  text, like a giant database.' How would you respond?"
- **Misconception resistance** (`lower-loss-is-more-intelligence`): "A
  colleague says 'if the training loss keeps going down, the model must
  be getting smarter in every sense.' Explain why that's not quite right."

## Chapter 10 — Scaling Laws

- **Comprehension:** "What's a scaling law, in your own words?"
- **Misconception resistance** (`scaling-laws-unlimited`): "Someone says
  'these scaling laws mean you can just keep scaling models up forever
  and they'll keep getting better with no limit.' Explain what's wrong
  with that."
- **Misconception resistance** (`bigger-model-always-better`): "A
  colleague says 'we should always use the biggest available model for
  every task, since bigger is better.' Do you agree? Explain."
- **New probe (post-review addition):** "Someone says 'the loss-vs-compute
  chart being a straight line means loss drops by the same fixed amount
  every time you double the compute.' Is that right? Explain what the
  chart actually shows." — correct answer should reflect that both axes
  are scaled in multiples of ten, not that loss falls linearly on an
  ordinary chart.

## Chapter 11 — The Attention Revolution

- **Comprehension:** "What does 'attention' let a model do, in your own
  words?"
- **Misconception resistance** (`attention-reads-sequentially`): "A
  colleague says a model 'reads' a sentence one word at a time in order,
  the way a person does. How would you respond?"
- **Misconception resistance** (`attention-sees-future-tokens`): "A
  colleague says 'since attention weighs every token's relevance, the
  model can look at the whole sentence, including words that come later —
  the same way a person reading the whole thing at once can.' Is that
  right? Explain."
- **Misconception resistance** (`positional-encoding-teaches-grammar`):
  "Someone says positional encoding gives the model an understanding of
  grammar. Explain what it actually does."

## Chapter 12 — Building a Transformer

- **Comprehension:** "What is a transformer block, and what does
  'stacking' many of them actually buy you?"
- **Misconception resistance** (`every-transformer-layer-same`): "A
  friend says 'all the layers in a transformer are doing the same thing,
  just repeated.' How would you respond?"
- **Misconception resistance** (`more-layers-just-slower`): "Someone says
  'adding more layers just makes the model slower — it doesn't change
  what it can do.' Explain why that's not quite right."

## Chapter 13 — From Transformer to ChatGPT

- **Comprehension:** "Why did it take more than just the transformer
  architecture to get something like ChatGPT?"
- **Misconception resistance** (`chatgpt-is-base-model-with-interface`):
  "A colleague says 'ChatGPT is just GPT-3 with a chat window slapped on
  it.' How would you respond?"
- **Misconception resistance** (`transformer-paper-alone-explains-quality`):
  "Someone says 'the 2017 transformer paper alone explains why chatbots
  suddenly got so good.' Is that the whole story? Explain."

## Chapter 14 — Inference and Text Generation

- **Comprehension:** "What's the difference between training and
  inference?"
- **Misconception resistance** (`model-learns-during-conversation`): "A
  friend says 'the model is learning and getting smarter as I chat with
  it.' Explain what's actually happening."
- **Misconception resistance** (`same-prompt-same-answer-always`):
  "Someone says 'since it's the same model and the same prompt, it should
  always give the exact same answer.' Is that true? Explain."
- **New probe (post-review addition):** "A colleague says 'temperature
  and top-k don't change the model's predictions — they just change which
  one gets picked.' Is that accurate? Explain what's actually happening."
  (Correct answer: these controls reshape the distribution actually
  sampled from — rescaling or truncating and renormalizing it — not just
  the selection rule applied to an untouched distribution.)

## Chapter 15 — Why Models Hallucinate

- **Comprehension:** "Why do models 'hallucinate' — what's actually
  happening?"
- **Misconception resistance** (`hallucination-is-rare-bug`): "Someone
  says 'hallucination is just a rare bug that will get fixed as models
  improve.' How would you respond?"
- **Misconception resistance** (`model-knows-its-making-things-up`): "A
  colleague says 'the model knows when it's making something up — it's
  just choosing to deceive us.' Explain what's actually happening."

## Chapter 16 — Context Windows and Memory

- **Comprehension:** "What's the difference between a model's trained
  knowledge and its context window?"
- **Misconception resistance** (`context-window-is-trained-knowledge`):
  "Someone says 'the context window is basically the model's memory, same
  as what it learned in training.' Explain the difference."
- **Misconception resistance** (`model-remembers-fuzzily-like-person`): "A
  friend says 'the model forgets things from earlier in a long
  conversation, kind of like a person does.' Is that an accurate
  description? Explain."

## Chapter 17 — Semantic Retrieval and Vector Databases

- **Comprehension:** "How does semantic retrieval find relevant documents
  without matching exact words?"
- **Misconception resistance** (`retrieval-is-smarter-keyword-search`):
  "A colleague says 'semantic retrieval is really just keyword search
  with some AI sprinkled on.' How would you respond?"
- **Misconception resistance** (`vector-db-is-regular-db-with-search`):
  "Someone says 'a vector database is just a normal database with a
  search feature bolted on.' Explain what's actually different."

## Chapter 18 — Retrieval-Augmented Generation

- **Comprehension:** "What does RAG actually do, step by step?"
- **Misconception resistance** (`rag-means-retrained-on-documents`): "A
  friend says 'if a chatbot uses RAG, it must have been retrained on
  those documents.' Is that right? Explain."
- **Misconception resistance** (`rag-eliminates-hallucination-entirely`):
  "Someone says 'RAG completely solves hallucination, since the model now
  has real sources.' How would you respond?"

## Chapter 19 — Fine-Tuning and Alignment

- **Comprehension:** "What's the difference between fine-tuning and
  pretraining?"
- **Misconception resistance**
  (`finetuning-pretraining-fundamentally-different`): "A colleague says
  'fine-tuning is a totally different process from pretraining.' Explain
  why that's not quite right."
- **Misconception resistance**
  (`aligned-model-genuinely-understands-values`): "Someone says 'an
  aligned model genuinely understands and agrees with human values.' Is
  that an accurate claim? Explain."

## Chapter 20 — Quantization and Efficient Models

- **Comprehension:** "What is quantization, and why doesn't it usually
  hurt a model's behavior much?"
- **Misconception resistance** (`quantization-makes-model-dumber`): "A
  friend says 'a quantized model is obviously going to be noticeably
  worse.' How would you respond?"
- **Misconception resistance**
  (`efficient-model-is-different-smaller-model`): "Someone says 'an
  efficient or quantized version of a model is basically a different,
  smaller model.' Explain what's actually the same and what's different."
