# One Model, Many Senses

**Part:** AI Systems

**Concept Level:** Level 7

**Prerequisites:** Chapter 3 (tokens), Chapter 5 (embeddings), Chapter 12 (transformer blocks)

**New concepts introduced:** Multimodality, Projector, Cross-attention bridge, Unified early-fusion tokens

---

## Opening Question

*So far, every model in this book has read and written nothing but text. How does a model built entirely around predicting the next token learn to also make sense of an image or a sound?*

## Real-World Story

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

## Worked Example

Here's one concrete way a bridge like this gets built — not the only
way, but a common and easy-to-follow one, in two stages. Recall Chapter
5's map: words get positioned as points in a high-dimensional space,
where nearby points reflect similar meaning or use. Now take a photo of
a golden retriever running on a beach, and the caption "a golden
retriever running on a beach." An image encoder converts the *whole
photo* into a single vector; a matching text encoder converts the
*whole caption* into a single vector, both landing in a space built the
same way Chapter 5's word-embedding space was built.

Trained on enormous numbers of matched photo/caption pairs like this
one, the two encoders learn to pull a genuinely matching pair's
whole-image and whole-caption vectors toward each other, and push
mismatched pairs — this same photo paired with an unrelated caption
about a city skyline — apart. The result: a photo and its true caption
land as neighboring points in a jointly learned multimodal space — built
on the same geometric principle as Chapter 5's word-embedding map
(nearby points reflect similarity), but its own separately-learned
space, not literally the same map the language model's own word tokens
live on. Notice what this alone does and doesn't buy you: it's enough to
tell
whether a photo and a caption match, which is genuinely useful for
search and retrieval, but nothing here has taught any individual word to
attend to any individual patch of the photo — the alignment happened at
the level of the whole image and the whole caption, not piece by piece.

Getting to word-by-word, patch-by-patch interaction — letting a language
model's attention actually work over the image the way it works over
text — takes a second stage, covered in §5 as the encoder-plus-projector
pattern: reusing an encoder like this one, but now keeping its
finer-grained, per-patch features instead of collapsing them into one
vector, and training a separate small network to translate those patch
features into the language model's own token space.

## Core Intuition

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

## Technical Explanation

Three broad patterns cover most real multimodal systems, though the exact
engineering varies system to system.

**Encoder plus projector.** A separate, often independently pretrained
encoder converts an image or audio clip into a set of feature vectors —
one per patch, rather than one pooled vector for the whole image. That
encoder is often one whose overall sense of similarity was shaped the
way §3's worked example described, but producing per-patch features and
translating them for a language model is a distinct second stage, not
the same step. A small additional network, the **projector**, is trained
to translate those patch features into the representation format the
language model's own token embeddings already use — commonly in more than
one stage: an initial pass often trains just the projector, with the
encoder and language model held frozen, purely to align the translated
features to the language model's existing space; a later pass then
fine-tunes on instruction-following examples, sometimes updating parts
of the language model too. Either stage reuses the same next-token-
prediction objective from Chapters 6 and 9, not §3's contrastive
matching objective — this is the LLaVA-style recipe specifically, one
concrete way to train a projector bridge, not the only one possible.
Once translated, the language model's
existing attention mechanism (Chapter 11) can treat them like any other
token in the sequence — it doesn't need to know they originated as
pixels rather than words.

**Cross-attention bridge.** Instead of translating image features into
the main token sequence at all, some systems give the language model
extra, dedicated attention layers built specifically to look up relevant
information from the other modality while generating text. The image is
never merged into one shared sequence with the words — it stays a
separate pool of information the model selectively consults through this
dedicated channel, rather than something sitting directly alongside the
words it attends over. This bridge is what actually gets trained; the
pretrained vision and language components on either side of it can often
stay frozen throughout, with only the new cross-attention layers learning
from scratch.

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
a trained outcome, not a given — though the specific training objective
differs by pattern. An encoder's initial sense of similarity is often
shaped by training on enormous numbers of matched pairs — an image with
its caption, audio with its transcript — using an objective that pulls a
true match's representations together and pushes mismatches apart,
exactly like §3's worked example; this extends Chapter 9's core
predict/measure-error/adjust loop to a cross-modal matching goal. But
the bridge itself — a projector, a cross-attention layer, or a unified
system's joint training — is commonly trained a different way: on
instruction-following or next-token-prediction examples (Chapters 6, 9,
19), the same core mechanism as ordinary language-model training, just
now including non-text tokens or features in what it learns to predict
from. Both are extensions of the same underlying training loop; they
just target different things.

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

## Common Misconceptions

### *"A multimodal model is really two separate models — one for vision, one for language — glued together, only exchanging a final summary."*

**Why it's wrong:** Each modality does usually need some dedicated input representation process — an encoder, tokenizer, or codec — to perform the initial conversion into features, and that step genuinely is modality-specific. But depending on the pattern (§5), what happens next isn't two independently-reasoning systems handing off a finished conclusion: an encoder-plus-projector or unified-token system feeds the converted representation directly into the same reasoning process as the text; a cross-attention system integrates the other modality through a dedicated, trained bridge, consulting it step by step during generation rather than reading one final report — even when the pretrained vision and language backbones on either side of that bridge stay frozen and only the bridge itself trains.

**Correct intuition:** The specialization lives in how a modality is first converted or connected — not in running two fully separate, independently-trained systems that only talk to each other through a finished summary.

**Analogy:** The local doesn't run a separate "photo brain" and "language brain" that trade a finished note — he converts what he's shown, photo or words, into an understanding of which street is meant, consulting whichever source is relevant as he works it out, not reading a pre-written conclusion from someone else.

### *"A model that processes images 'sees' the way a human visually perceives the world."*

**Why it's wrong:** The model has no visual experience or perception. Whichever bridging pattern it uses (§5), it converts pixels into a learned, pattern-based representation and reasons over that representation the same statistical way it reasons over word embeddings.

**Correct intuition:** "Seeing," for a model, means "converted or connected into a representation the model can reason over" — a mechanical conversion process, not a claim about visual experience.

**Analogy:** The local recognizing the street in a photo isn't the same kind of event as him standing on that street and perceiving it directly — one is a comparison of representations, the other is lived experience.

### *"All multimodal models bridge image and text the same underlying way — the specific method doesn't really matter."*

**Why it's wrong:** As §5 covers, real systems use meaningfully different patterns — an encoder-plus-projector approach, a cross-attention bridge, or unified early-fusion tokens — and these have real practical differences: whether a system can be extended to a new modality without retraining the whole thing, how directly an image and a word can influence each other, and how the components were trained in the first place.

**Correct intuition:** "Multimodal" describes a capability, not a specific architecture — knowing which bridging pattern a given system actually uses says something real about how it works, not just an implementation detail.

**Analogy:** Two bridges can both get you across the same river while being built completely differently — a suspension bridge and a tunnel solve the same problem in structurally different ways, and which one a city has actually built affects what you can and can't do with it.

### *"Since a model can already process images, it can handle any new kind of input automatically, with no additional training."*

**Why it's wrong:** Supporting a new modality requires training that modality's own input representation process and bridge to actually connect to the language model, using the kind of training process described in §5. Nothing about the transformer's core attention mechanism automatically extends to a modality it has never been trained to handle properly.

**Correct intuition:** Each new modality is a genuine engineering and training addition — a new encoder or tokenizer, and a new or retrained bridge — not a capability that falls out of the architecture for free.

**Analogy:** Learning to recognize a friend's face doesn't automatically teach you to recognize their voice on the phone — that's a separate skill, even though both eventually feed into the same understanding of who you're talking to.

## Practical Implications

This is why multimodal AI products list specific supported input types — images, audio, PDFs, video — as a discrete, deliberately trained set rather than an open-ended "handles anything" claim: each one needed its own bridge and its own training data, whichever pattern that bridge uses. It's also why "multimodal" alone doesn't tell you everything about a product: whether it understands images, generates them, or both are separate questions (§5), and which architectural pattern a system uses can affect real, practical things — how directly text and image can influence each other, and how easily a new modality can be added later. And because the underlying generation mechanism hasn't changed in any of these patterns, a model can still "hallucinate" about image or audio content the same way Chapter 15 described for text — confidently describing something in an image that isn't actually there.

## Key Takeaway

**A multimodal model doesn't have one universal architecture — it bridges different formats through a projector, a cross-attention channel, or a shared token vocabulary, and knowing which bridge a system actually uses matters more than assuming every multimodal model works the same way underneath.**

## One-Page Summary

- Multimodality is a model's ability to make sense of — and, with additional components, produce — more than one kind of data: text, images, audio.
- There's no single universal architecture: three broad real patterns are encoder-plus-projector, a cross-attention bridge, and unified early-fusion tokens (§5).
- The worked example (whole-image/whole-caption contrastive alignment, then a separately-trained projector for patch-level attention) illustrates one concrete pattern in two distinct stages, not the definition of multimodality itself.
- An encoder's initial sense of similarity is often shaped by matched-pair training (image/caption, audio/transcript); the bridge that connects it to the language model is commonly trained a different way, via ordinary next-token prediction on instruction-following examples — both are trained outcomes, just with different objectives.
- Understanding a modality (input) and generating it (output) are related but distinct problems; output generation typically needs an additional decoder or generative component this chapter doesn't cover in depth.
- "Seeing" or "hearing," for a model, means "converted or connected into a representation it can reason over" — not visual or auditory experience.
- Supporting a new modality requires real additional training in any pattern; it isn't a free extension of the existing architecture.
- Hallucination (Chapter 15) applies to non-text modalities too, since the underlying generation mechanism is unchanged.

## Further Reading

- Search for "CLIP" or "contrastive image-text pretraining" for the whole-image/whole-caption alignment technique behind §3's worked example's first stage.
- Search for "LLaVA" or "visual instruction tuning" for a concrete encoder-plus-projector system — the second stage of §3's worked example and §5's first pattern.
- Search for "vision transformer" or "ViT" for more on patch-based image tokenization, used in more than one of §5's patterns.
- Search for "Flamingo" for a concrete cross-attention-bridge system, and "Chameleon" or "early fusion multimodal" for a concrete unified-token system — both described conceptually in §5.

## The Next Obvious Question

*So far, every model in this book runs its full set of parameters on every single input, regardless of how simple or complex that input is. Is there a way to build an enormous model without paying the full computational cost of using all of it on every request?*

---

**Glossary terms added this chapter:** Multimodality, Patch embedding, Cross-modal alignment, Projector, Cross-attention bridge, Unified early-fusion tokens → append to `/glossary.md`

**Misconceptions logged this chapter:** "a multimodal model is really two separate models glued together, only exchanging a final summary"; "a model that processes images sees the way a human does"; "a model can handle any new modality automatically, with no additional training"; "all multimodal models bridge image and text the same underlying way" → append to `/misconceptions.md`

**Concept-graph entries checked off:** Level 7 — Multimodality, at Ch. 24
