# Chapter 24 — One Model, Many Senses

**Part:** AI Systems

**Concept Level:** Level 7

**Prerequisites:** Chapter 3 (tokens), Chapter 5 (embeddings), Chapter 12 (transformer blocks)

**New concepts introduced:** Multimodality, Projector, Cross-attention bridge, Unified early-fusion tokens

---

## 1. Opening Question

*So far, every model in this book has read and written nothing but text. How does a model built entirely around predicting the next token learn to also make sense of an image or a sound?*

## 2. Real-World Story

A tourist is lost in a foreign city and doesn't speak the language. Rather
than struggling to describe the street she's looking for in words she
doesn't have, she shows a local a photo of it. The local immediately
understands and points the way — not because he "read" the photograph
like a sentence, but because the photo and any spoken description of that
same street both point at the same real place. A photograph and a
sentence are completely different formats, made of completely different
stuff, but they can refer to the exact same thing.

That's the whole puzzle a multimodal model has to solve. Its language
machinery — attention (Chapter 11), transformer blocks (Chapter 12),
everything built on top of them — was designed to work over a sequence
of word embeddings. An image isn't made of words. For a model to make
any use of one at all, something has to bridge a photograph and a
sentence about that photograph into a form the model can actually
connect — and, as this chapter covers, real systems build that bridge in
more than one way.

## 3. Worked Example

Here's one concrete way to build that bridge — not the only way, but a
common and easy-to-follow one. Recall Chapter 5's map: words get
positioned as points in a high-dimensional space, where nearby points
reflect similar meaning or use. Now take a photo of a golden retriever
running on a beach, and the caption "a golden retriever running on a
beach." Cut the photo into a grid of small square patches — like slicing
it into postage stamps — and convert each patch into a vector using a
learned encoder, landing it somewhere in a space built the same way
Chapter 5's word-embedding space was built. Do the same for the
caption's words, using the encoding this book has covered since Chapter
5.

Trained on enormous numbers of matched photo/caption pairs like this one,
the model learns to pull a genuinely matching pair's embeddings toward
each other and push mismatched pairs — this same photo paired with an
unrelated caption about a city skyline — apart. The result: the image's
patch embeddings and the caption's word embeddings end up as neighboring
points on essentially the same map from Chapter 5, not two separate,
unrelated coordinate systems that happen to sit side by side. As §5
covers, this is one instance of a broader pattern — other real systems
bridge image and text differently, without ever placing patches directly
alongside words on one shared map.

## 4. Core Intuition

**Multimodality** is a model's ability to make sense of — and, with
additional components, produce — more than one kind of data: text,
images, audio. Every approach has to solve the same problem the tourist's
photo did: bridging different formats so a shared model can actually use
them together. But there's no single universal way to build that bridge.
It might be a small learned network that translates one modality's
features into the language model's own embedding space (Chapters 3 and
5), a set of dedicated attention layers that let the language model
consult the other modality without merging it into one shared sequence,
or a single shared vocabulary that represents every modality as tokens
from the very start. Different real systems pick different bridges;
knowing that there are several real patterns, not one, is more useful
than assuming every multimodal model works the same way underneath.

## 5. Technical Explanation

Three broad patterns cover most real multimodal systems, though the exact
engineering varies system to system.

**Encoder plus projector.** A separate, often independently pretrained
encoder converts an image or audio clip into a set of feature vectors —
this is what §3's worked example walked through, with patches encoded
via a learned image encoder trained the way that section described, so
its output space is already organized around meaningful similarity, the
way Chapter 5's word embeddings are. A small additional network, the
**projector**, then translates those feature vectors into the same
numeric space the language model's own token embeddings live in. Once
translated, the language model's existing attention mechanism (Chapter
11) can treat them like any other token in the sequence — it doesn't
need to know they originated as pixels rather than words.

**Cross-attention bridge.** Instead of translating image features into
the main token sequence at all, some systems give the language model
extra, dedicated attention layers built specifically to look up relevant
information from the other modality while generating text. The image is
never merged into one shared sequence with the words — it stays a
separate pool of information the model selectively consults through this
dedicated channel, rather than something sitting directly alongside the
words it attends over.

**Unified early-fusion tokens.** A third approach skips building a bridge
on top of an already-trained language model at all: images, audio, and
text are converted into tokens from one shared vocabulary from the very
start, and the whole system — encoder and language model together — is
trained as a single unit on that unified token stream. There's no
separate add-on component translating between formats after the fact,
because every format was designed into the same representation from the
beginning.

Whichever pattern a system uses, getting a non-text modality's
representation to land somewhere the language model can actually use is
a trained outcome, not a given. This commonly involves training on
enormous numbers of matched pairs — an image with its caption, audio
with its transcript — using an objective that pulls a true match's
representations together and pushes mismatches apart, exactly like §3's
worked example. This extends Chapter 9's core predict/measure-error/adjust
loop to a cross-modal matching goal; it is not a fundamentally different
learning procedure, just a different target for the same mechanism.

Everything above covers a model making sense of a non-text *input* —
turning an image or sound into something the model can reason about and
describe. Producing new image or audio *output* is a related but
distinct problem: it typically requires an additional output-side
component — a decoder or dedicated generative model — that converts the
language model's internal representations back into pixels or sound,
separate from the encoders and bridges this chapter has covered for the
understanding direction. A system can be genuinely strong at
understanding images without generating any at all, and vice versa;
"multimodal" alone doesn't specify which direction, or both, a given
system actually supports.

## 6. Common Misconceptions

### Misconception
*"A multimodal model is really two separate models — one for vision, one for language — glued together, only exchanging a final summary."*

**Why it's wrong:** Each modality does typically need its own dedicated encoder to perform the initial conversion into features — that step genuinely is modality-specific. But depending on the pattern (§5), what happens next isn't two independently-reasoning systems handing off a finished conclusion: an encoder-plus-projector or unified-token system feeds the converted representation directly into the same reasoning process as the text; a cross-attention system keeps a dedicated channel to the other modality but trains it jointly with the language model, consulting it step by step rather than reading one final report.

**Correct intuition:** The specialization lives in how a modality is first converted or connected — not in running two fully separate, independently-trained systems that only talk to each other through a finished summary.

**Analogy:** The local doesn't run a separate "photo brain" and "language brain" that trade a finished note — he converts what he's shown, photo or words, into an understanding of which street is meant, consulting whichever source is relevant as he works it out, not reading a pre-written conclusion from someone else.

### Misconception
*"A model that processes images 'sees' the way a human visually perceives the world."*

**Why it's wrong:** The model has no visual experience or perception. Whichever bridging pattern it uses (§5), it converts pixels into a learned, pattern-based representation and reasons over that representation the same statistical way it reasons over word embeddings.

**Correct intuition:** "Seeing," for a model, means "converted or connected into a representation the model can reason over" — a mechanical conversion process, not a claim about visual experience.

**Analogy:** The local recognizing the street in a photo isn't the same kind of event as him standing on that street and perceiving it directly — one is a comparison of representations, the other is lived experience.

### Misconception
*"All multimodal models bridge image and text the same underlying way — the specific method doesn't really matter."*

**Why it's wrong:** As §5 covers, real systems use meaningfully different patterns — an encoder-plus-projector approach, a cross-attention bridge, or unified early-fusion tokens — and these have real practical differences: whether a system can be extended to a new modality without retraining the whole thing, how directly an image and a word can influence each other, and how the components were trained in the first place.

**Correct intuition:** "Multimodal" describes a capability, not a specific architecture — knowing which bridging pattern a given system actually uses says something real about how it works, not just an implementation detail.

**Analogy:** Two bridges can both get you across the same river while being built completely differently — a suspension bridge and a tunnel solve the same problem in structurally different ways, and which one a city has actually built affects what you can and can't do with it.

### Misconception
*"Since a model can already process images, it can handle any new kind of input automatically, with no additional training."*

**Why it's wrong:** Supporting a new modality requires training that modality's encoder to actually land in the shared representation space, using the matched-pair training process described in §5. Nothing about the transformer's core attention mechanism automatically extends to a modality it has never been trained to embed properly.

**Correct intuition:** Each new modality is a genuine engineering and training addition — a new encoder, trained on matched examples — not a capability that falls out of the architecture for free.

**Analogy:** Learning to recognize a friend's face doesn't automatically teach you to recognize their voice on the phone — that's a separate skill, even though both eventually feed into the same understanding of who you're talking to.

## 7. Practical Implications

This is why multimodal AI products list specific supported input types — images, audio, PDFs, video — as a discrete, deliberately trained set rather than an open-ended "handles anything" claim: each one needed its own bridge and its own training data, whichever pattern that bridge uses. It's also why "multimodal" alone doesn't tell you everything about a product: whether it understands images, generates them, or both are separate questions (§5), and which architectural pattern a system uses can affect real, practical things — how directly text and image can influence each other, and how easily a new modality can be added later. And because the underlying generation mechanism hasn't changed in any of these patterns, a model can still "hallucinate" about image or audio content the same way Chapter 15 described for text — confidently describing something in an image that isn't actually there.

## 8. Key Takeaway

**A multimodal model doesn't have one universal architecture — it bridges different formats through a projector, a cross-attention channel, or a shared token vocabulary, and knowing which bridge a system actually uses matters more than assuming every multimodal model works the same way underneath.**

## 9. One-Page Summary

- Multimodality is a model's ability to make sense of — and, with additional components, produce — more than one kind of data: text, images, audio.
- There's no single universal architecture: three broad real patterns are encoder-plus-projector, a cross-attention bridge, and unified early-fusion tokens (§5).
- The worked example (patches encoded, then processed by the same attention as text) is one concrete instance of one pattern, not the definition of multimodality itself.
- Getting a non-text modality's representation to land somewhere the language model can use is a trained outcome in any pattern, commonly via matched-pair training (image/caption, audio/transcript) — an extension of Chapter 9's core training loop.
- Understanding a modality (input) and generating it (output) are related but distinct problems; output generation typically needs an additional decoder or generative component this chapter doesn't cover in depth.
- "Seeing" or "hearing," for a model, means "converted or connected into a representation it can reason over" — not visual or auditory experience.
- Supporting a new modality requires real additional training in any pattern; it isn't a free extension of the existing architecture.
- Hallucination (Chapter 15) applies to non-text modalities too, since the underlying generation mechanism is unchanged.

## 10. Further Reading

- Search for "CLIP" or "contrastive image-text pretraining" for the alignment technique behind §3's worked example and the encoder-plus-projector pattern.
- Search for "vision transformer" or "ViT" for more on patch-based image tokenization, used in more than one of §5's patterns.
- Search for "Flamingo" for a concrete cross-attention-bridge system, and "Chameleon" or "early fusion multimodal" for a concrete unified-token system — both described conceptually in §5.

## 11. The Next Obvious Question

*So far, every model in this book runs its full set of parameters on every single input, regardless of how simple or complex that input is. Is there a way to build an enormous model without paying the full computational cost of using all of it on every request?*

---

**Glossary terms added this chapter:** Multimodality, Patch embedding, Cross-modal alignment, Projector, Cross-attention bridge, Unified early-fusion tokens → append to `/glossary.md`

**Misconceptions logged this chapter:** "a multimodal model is really two separate models glued together, only exchanging a final summary"; "a model that processes images sees the way a human does"; "a model can handle any new modality automatically, with no additional training"; "all multimodal models bridge image and text the same underlying way" → append to `/misconceptions.md`

**Concept-graph entries checked off:** Level 7 — Multimodality, at Ch. 24
