# Chapter 24 — One Model, Many Senses

**Part:** AI Systems

**Concept Level:** Level 7

**Prerequisites:** Chapter 3 (tokens), Chapter 5 (embeddings), Chapter 12 (transformer blocks)

**New concepts introduced:** Multimodality

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

That's the whole puzzle a multimodal model has to solve. Its entire
machinery — attention (Chapter 11), transformer blocks (Chapter 12),
everything built on top of them — was designed to weigh relevance across
a sequence of word embeddings. An
image isn't made of words. For a model to make any use of one at all,
something has to turn a photograph and a sentence about that photograph
into the same kind of thing.

## 3. Worked Example

Recall Chapter 5's map: words get positioned as points in a
high-dimensional space, where nearby points reflect similar meaning or
use. Now take a photo of a golden retriever running on a beach, and the
caption "a golden retriever running on a beach." Cut the photo into a
grid of small square patches — like slicing it into postage stamps — and
convert each patch into a vector using a learned encoder, landing it
somewhere in a space built the same way Chapter 5's word-embedding space
was built. Do the same for the caption's words, using the encoding this
book has covered since Chapter 5.

Trained on enormous numbers of matched photo/caption pairs like this one,
the model learns to pull a genuinely matching pair's embeddings toward
each other and push mismatched pairs — this same photo paired with an
unrelated caption about a city skyline — apart. The result: the image's
patch embeddings and the caption's word embeddings end up as neighboring
points on essentially the same map from Chapter 5, not two separate,
unrelated coordinate systems that happen to sit side by side.

## 4. Core Intuition

**Multimodality** is a model's ability to accept or produce more than one
kind of data — text, images, audio — by converting each modality into the
same kind of numeric representation (tokens and embeddings, Chapters 3
and 5) its existing transformer machinery already knows how to process,
rather than building an entirely separate reasoning system per modality.
Once an image patch and a word are both just vectors positioned in a
shared space, attention (Chapter 11) can weigh relevance across them
exactly the way it already weighs relevance across words in a sentence —
the mechanism doesn't need to know, or care, which modality a given
vector originally came from.

## 5. Technical Explanation

For images, a common approach splits the image into a grid of fixed-size
patches and converts each patch into an embedding vector using a learned
encoder — directly analogous to Chapter 3's tokenization, just operating
on an image instead of text: the image becomes a sequence of "patch
tokens" instead of word tokens. Each patch embedding is combined with
positional encoding (Chapter 11) marking where it sits in the image, and
the resulting sequence is fed into transformer blocks alongside or
instead of text tokens. From that point on, the same attention mechanism
covered since Chapter 11 lets any patch or word attend to any other patch
or word based on learned relevance — the caption word "beach" can attend
directly to the specific patches showing sand, the same way one word
attends to another in ordinary text.

Getting image and text embeddings to land in a genuinely comparable space
in the first place is itself a trained outcome, not a given. Models are
trained on enormous numbers of matched pairs — an image with its caption,
audio with its transcript — using a training objective that pulls a true
match's embeddings together and pushes mismatched pairs apart. This
extends Chapter 9's core predict/measure-error/adjust loop to a
cross-modal matching goal; it is not a fundamentally different learning
procedure, just a different target for the same mechanism. Audio works
analogously: a waveform is converted into a sequence of embeddings, often
through an intermediate spectrogram-like representation, that the same
transformer machinery then processes as another kind of token sequence.
Note that each modality still requires its own dedicated encoder to
perform this initial conversion — that first step genuinely is
modality-specific — but once converted, everything downstream is the same
shared reasoning machinery.

## 6. Common Misconceptions

### Misconception
*"A multimodal model is really two separate models — one for vision, one for language — glued together."*

#### Why it's wrong
Each modality does need its own dedicated encoder to perform the initial conversion into embeddings — that specific step genuinely is modality-specific. But once converted, the same shared transformer machinery and the same attention mechanism process every modality's embeddings together, in one unified reasoning process — not two separate systems that only exchange a final summary.

#### Correct intuition:
The specialization lives entirely in the initial conversion step; everything downstream of it is one shared mechanism working over a common representation, not two independent models bolted together at the end.

#### Analogy:
The local doesn't run a separate "photo brain" and "language brain" that trade notes — he converts what he's shown, photo or words, into the same understanding of which street is meant, then reasons from that one shared understanding.

### Misconception
*"A model that processes images 'sees' the way a human visually perceives the world."*

#### Why it's wrong
The model has no visual experience or perception. It converts pixel patches into embeddings using the same kind of learned, pattern-based mapping used for text, and reasons over those embeddings the same statistical way it reasons over word embeddings.

#### Correct intuition:
"Seeing," for a model, means "converted into the shared representation space this chapter describes" — a mechanical conversion and comparison process, not a claim about visual experience.

#### Analogy:
The local recognizing the street in a photo isn't the same kind of event as him standing on that street and perceiving it directly — one is a comparison of representations, the other is lived experience.

### Misconception
*"Since a model can already process images, it can handle any new kind of input automatically, with no additional training."*

#### Why it's wrong
Supporting a new modality requires training that modality's encoder to actually land in the shared representation space, using the matched-pair training process described in §5. Nothing about the transformer's core attention mechanism automatically extends to a modality it has never been trained to embed properly.

#### Correct intuition:
Each new modality is a genuine engineering and training addition — a new encoder, trained on matched examples — not a capability that falls out of the architecture for free.

#### Analogy:
Learning to recognize a friend's face doesn't automatically teach you to recognize their voice on the phone — that's a separate skill, even though both eventually feed into the same understanding of who you're talking to.

## 7. Practical Implications

This is why multimodal AI products list specific supported input types — images, audio, PDFs, video — as a discrete, deliberately trained set rather than an open-ended "handles anything" claim: each one needed its own encoder and its own matched-pair training data. It also explains why feeding a model a photo of a document sometimes works better, and sometimes worse, than feeding it the same content as extracted text — it depends on what the shared embedding space actually captured well during training. And because the underlying generation mechanism hasn't changed, a model can still "hallucinate" about image or audio content the same way Chapter 15 described for text — confidently describing something in an image that isn't actually there.

## 8. Key Takeaway

**A multimodal model doesn't have separate senses bolted together — it converts each modality into the same kind of embedding the model already reasons over, so one shared attention mechanism can weigh relevance across words, image patches, and audio alike.**

## 9. One-Page Summary

- Multimodality is a model's ability to convert different kinds of data — text, images, audio — into the same kind of embedding its existing transformer machinery already processes.
- Images are typically split into patches and embedded much like Chapter 3's tokenization, just applied to pixels instead of text; audio is converted through an intermediate representation into a comparable sequence of embeddings.
- Getting different modalities' embeddings to land in a genuinely shared space is a trained outcome, achieved by training on matched pairs (image/caption, audio/transcript) that pulls true matches together and pushes mismatches apart — an extension of Chapter 9's core training loop.
- Each modality still needs its own dedicated encoder for the initial conversion step — that part is genuinely modality-specific — but everything downstream is one shared attention mechanism, not separate reasoning systems glued together.
- "Seeing" or "hearing," for a model, means "converted into the shared representation space" — not visual or auditory experience.
- Supporting a new modality requires real additional training; it isn't a free extension of the existing architecture.
- Hallucination (Chapter 15) applies to non-text modalities too, since the underlying generation mechanism is unchanged.

## 10. Further Reading

- Search for "CLIP" or "contrastive image-text pretraining" for the specific technique described in §3/§5 for aligning image and text embeddings in a shared space.
- Search for "vision transformer" or "ViT" for more on the patch-based image tokenization approach described in §5.

## 11. The Next Obvious Question

*So far, every model in this book runs its full set of parameters on every single input, regardless of how simple or complex that input is. Is there a way to build an enormous model without paying the full computational cost of using all of it on every request?*

---

**Glossary terms added this chapter:** Multimodality, Patch embedding, Cross-modal alignment → append to `/glossary.md`

**Misconceptions logged this chapter:** "a multimodal model is really two separate models glued together"; "a model that processes images sees the way a human does"; "a model can handle any new modality automatically, with no additional training" → append to `/misconceptions.md`

**Concept-graph entries checked off:** Level 7 — Multimodality, at Ch. 24
