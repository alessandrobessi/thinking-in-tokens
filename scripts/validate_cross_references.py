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
# Prose in this manuscript is hard-wrapped at ~80 columns *within* a
# paragraph, so "same line" is too narrow a scope -- but a markdown list
# item should never bleed into its neighbor even with no blank line
# between them. Split on blank lines (paragraph breaks) OR the start of a
# new "- " list item, whichever comes first.
BLOCK_SPLIT_RE = re.compile(r"\n\s*\n|\n(?=-\s)")


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

    for block in BLOCK_SPLIT_RE.split(body):
        # Prose here is hard-wrapped at ~80 columns, so a keyword phrase
        # can straddle a line break ("reasoning\nmodels"). Normalize
        # internal whitespace before matching so that doesn't hide it.
        normalized_block = re.sub(r"\s+", " ", block)
        chapter_matches = list(CHAPTER_RE.finditer(normalized_block))
        if not chapter_matches:
            continue
        lowered_block = normalized_block.lower()
        for keyword, concept_id in KEYWORD_TO_CONCEPT.items():
            if keyword not in lowered_block:
                continue
            expected = chapter_by_concept.get(concept_id)
            if expected is None:
                continue
            if expected == this_chapter:
                # We're already inside this concept's own home chapter --
                # any nearby "Chapter N" mention is citing something else
                # discussed in the same paragraph, not making a claim
                # about where this concept itself lives.
                continue
            for ch_match in chapter_matches:
                referenced = int(ch_match.group(1))
                if referenced != expected:
                    snippet = block.strip().replace("\n", " ")[:160]
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
