#!/usr/bin/env python3
"""Check that forward-references like "...reasoning models, Chapter 24"
actually point at the chapter concept-graph.yaml assigns that concept to.

This is deliberately a small, conservative keyword map, not a general NLP
tool: each entry is a phrase specific enough that seeing it next to
"Chapter N" in the same sentence is a real claim about where that concept
lives, not a coincidence. Missing a real cross-reference (false negative)
is an acceptable tradeoff for not flagging noise (false positive).

Add a new keyword -> concept_id pair here whenever a chapter forward-
references a concept by name; that's what makes this check keep pace with
the manuscript instead of going stale.
"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent

KEYWORD_TO_CONCEPT = {
    "reasoning model": "reasoning-models",
    "hallucinat": "hallucinations",
    "fine-tun": "fine-tuning",
    "quantiz": "quantization",
    "efficient inference": "efficient-inference",
    "multimodal": "multimodality",
    "mixture of experts": "mixture-of-experts",
    "vector database": "vector-databases",
    "retrieval-augmented generation": "rag",
    "retrieval augmented generation": "rag",
    "tool calling": "tool-calling",
    "ai agent": "ai-agents",
    "context window": "context-windows",
    "transformer block": "transformer-blocks",
    "positional encoding": "positional-encoding",
    "scaling law": "scaling-laws",
}

CHAPTER_RE = re.compile(r"Chapter\s+(\d+)")
# Maximum character distance between a keyword occurrence and a "Chapter N"
# mention for the two to count as referring to each other. A synthesis
# chapter (e.g. RAG, which legitimately cites several earlier chapters for
# several different concepts in one paragraph) means whole-paragraph
# matching produces false positives -- only the *nearest* chapter mention
# to a given keyword occurrence is a claim about that keyword's concept.
MAX_DISTANCE = 70

# Manually verified false positives: the keyword and chapter number are
# genuinely close together (same sentence), but the chapter number cites a
# *different* concept discussed in that same breath, not a claim about
# where the keyword's own concept lives. Re-verify each entry by hand if
# the surrounding prose ever changes; don't add to this list to silence a
# finding you haven't actually read.
ALLOWLIST = {
    # "Fine-tuning reuses Chapter 9's training loop..." -- Chapter 9 is
    # correctly cited for *training*, not as fine-tuning's home chapter.
    ("13-from-transformer-to-chatgpt.md", "fine-tun", 9),
    # "...embeddings (Chapter 5), attention and refinement through
    # transformer blocks (Chapters 11-12)..." -- Chapter 5 is correctly
    # cited for embeddings, immediately before the transformer-blocks
    # keyword, not a claim about transformer-blocks' own home chapter.
    ("14-inference-and-text-generation.md", "transformer block", 5),
    # "attention (Chapter 11), transformer blocks (Chapter 12), everything
    # built on top of them..." -- Chapter 11 is correctly cited for
    # attention, immediately before the transformer-blocks keyword, not a
    # claim about transformer-blocks' own home chapter (which the very
    # next parenthetical correctly names as Chapter 12).
    ("24-one-model-many-senses.md", "transformer block", 11),
    # "retrieval (Chapters 17-18), tool calling and agents (Chapters
    # 21-22), evaluation (Chapter 26)..." -- the checker's regex only
    # matches singular "Chapter N", not the plural "Chapters N-M" range
    # immediately following "tool calling and agents", so it skips past
    # to the next singular match (Chapter 26, for evaluation) instead.
    ("27-ai-engineering-and-observability.md", "tool calling", 26),
    # "RAG changes nothing about the model's parameters (Chapter 8). It's
    # entirely a matter of what gets placed in the context window..." --
    # Chapter 8 is correctly cited for parameters, immediately before the
    # context-window keyword, not a claim about context-windows' home.
    ("18-retrieval-augmented-generation.md", "context window", 8),
}


def load_chapter_by_concept():
    data = yaml.safe_load((ROOT / "concept-graph.yaml").read_text())
    return {c["id"]: c["introduced_in"] for c in data["concepts"]}


def current_chapter_number(path):
    m = re.match(r"(\d+)-", path.name)
    return int(m.group(1)) if m else None


def check_file(path, chapter_by_concept):
    errors = []
    text = path.read_text()
    this_chapter = current_chapter_number(path)
    # Skip the front-matter block (before the first "---"): its
    # "Prerequisites: Chapter N (concept)" line legitimately cites earlier
    # chapters and isn't a forward-reference claim about the current
    # chapter's own concepts.
    body = text.split("\n---\n", 1)[-1] if "\n---\n" in text else text
    # A markdown list item should never be treated as adjacent to its
    # neighbor, even with no blank line between them (two Further Reading
    # bullets sit right next to each other, on entirely different topics).
    # Mark those boundaries with a sentinel *before* collapsing whitespace,
    # so "nearest" can refuse to cross one even though the raw character
    # distance might otherwise look small.
    boundary_marked = re.sub(r"\n\s*\n|\n(?=-\s)", "\x00", body)
    # Prose here is also hard-wrapped at ~80 columns *within* a paragraph,
    # so a keyword phrase can straddle a line break ("reasoning\nmodels").
    # Normalize remaining whitespace so that doesn't hide it, and so
    # character distances are measured in rendered space, not
    # raw-line-wrapped space. The sentinel is not whitespace, so it survives.
    normalized = re.sub(r"\s+", " ", boundary_marked)
    lowered = normalized.lower()

    chapter_matches = list(CHAPTER_RE.finditer(normalized))
    if not chapter_matches:
        return errors

    for keyword, concept_id in KEYWORD_TO_CONCEPT.items():
        expected = chapter_by_concept.get(concept_id)
        if expected is None or expected == this_chapter:
            # No assignment to check against, or we're already inside this
            # concept's own home chapter, where a nearby "Chapter N" is
            # necessarily citing something else in the same paragraph, not
            # making a claim about where this concept itself lives.
            continue
        for kw_match in re.finditer(re.escape(keyword), lowered):
            # Only consider chapter mentions in the same segment (no list-
            # item/paragraph boundary sentinel between them), and among
            # those, only the nearest one -- not just any mention anywhere
            # in the same segment.
            candidates = [
                m
                for m in chapter_matches
                if "\x00" not in normalized[min(m.start(), kw_match.start()) : max(m.end(), kw_match.end())]
            ]
            if not candidates:
                continue
            nearest = min(
                candidates,
                key=lambda m: min(
                    abs(m.start() - kw_match.end()), abs(kw_match.start() - m.end())
                ),
            )
            distance = min(
                abs(nearest.start() - kw_match.end()), abs(kw_match.start() - nearest.end())
            )
            if distance > MAX_DISTANCE:
                continue
            referenced = int(nearest.group(1))
            if referenced != expected:
                if (path.name, keyword, referenced) in ALLOWLIST:
                    continue
                start = max(0, min(kw_match.start(), nearest.start()) - 20)
                end = min(len(normalized), max(kw_match.end(), nearest.end()) + 20)
                snippet = normalized[start:end].replace("\x00", " ").strip()
                errors.append(
                    f"{path}: mentions '{keyword}' near 'Chapter {referenced}', "
                    f"but concept-graph.yaml assigns {concept_id} to Chapter {expected} "
                    f"-- \"{snippet}\""
                )
    return errors


def main():
    chapter_by_concept = load_chapter_by_concept()
    all_errors = []
    for f in sorted(ROOT.glob("book/**/*.md")):
        if f.name == "README.md":
            continue
        all_errors += check_file(f, chapter_by_concept)

    if all_errors:
        print(f"{len(all_errors)} cross-reference mismatch(es) found:\n")
        for e in all_errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("OK: no cross-reference mismatches found.")


if __name__ == "__main__":
    main()
