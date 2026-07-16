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

# Matches a whole "Chapter(s) N[, M][-P][ and Q]"-style span, e.g.
# "Chapter 9", "Chapters 11-12", "Chapters 17-18", "Chapters 13 and 19".
# The whole span is treated as *one* mention covering a set of chapter
# numbers (see find_chapter_mentions below), not one mention per digit --
# "Chapters 11-12" is a single, legitimate combined citation, and a
# concept whose home is either 11 or 12 is correctly referenced by that
# whole range, not just by whichever digit happens to sit closest to the
# keyword. A plain r"Chapter\s+(\d+)" regex only ever matches the singular
# form and silently skips past any plural range entirely, which used to
# make "nearest chapter mention" skip past a correctly-adjacent range to
# some much farther singular mention instead.
CHAPTER_SPAN_RE = re.compile(r"Chapters?\s+\d+(?:\s*(?:[-–—]|,|and)\s*\d+)*")
NUMBER_RE = re.compile(r"\d+")
# Maximum character distance between a keyword occurrence and a chapter
# mention for the two to count as referring to each other. A synthesis
# chapter (e.g. RAG, which legitimately cites several earlier chapters for
# several different concepts in one paragraph) means whole-paragraph
# matching produces false positives -- only the *nearest* chapter mention
# to a given keyword occurrence is a claim about that keyword's concept.
MAX_DISTANCE = 70


def find_chapter_mentions(text):
    """Return (start, end, {numbers}) for every "Chapter(s) ..." span,
    with every individual chapter number in a plural range grouped into
    that one span's number set -- so "Chapters 21-22" is one mention
    covering {21, 22}, not two independent single-number mentions."""
    mentions = []
    for span in CHAPTER_SPAN_RE.finditer(text):
        numbers = {int(n) for n in NUMBER_RE.findall(span.group(0))}
        mentions.append((span.start(), span.end(), numbers))
    return mentions


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
    # "attention (Chapter 11), transformer blocks (Chapter 12), everything
    # built on top of them..." -- both are singular, adjacent mentions on
    # either side of the keyword with near-identical character distance;
    # "Chapter 11" (correctly cited for attention) wins the nearest-mention
    # tiebreak even though "Chapter 12" (transformer-blocks' actual home)
    # sits right after the keyword too. Not a plural-range parsing issue --
    # a genuine adjacency tie between two correct-but-different citations.
    ("24-one-model-many-senses.md", "transformer block", 11),
    # "RAG changes nothing about the model's parameters (Chapter 8). It's
    # entirely a matter of what gets placed in the context window..." --
    # Chapter 8 is correctly cited for parameters, immediately before the
    # context-window keyword, not a claim about context-windows' home.
    ("18-retrieval-augmented-generation.md", "context window", 8),
    # "combining retrieval (Chapters 17-18), tool calling and agents
    # (Chapters 21-22)..." -- two different, correctly-cited ranges for
    # two different concepts sitting back-to-back in a list; "Chapters
    # 17-18" (correctly cited for retrieval/RAG) wins the nearest-mention
    # tiebreak over "Chapters 21-22" (tool-calling's actual home) despite
    # sitting right before the keyword. Same adjacency-tie pattern as the
    # transformer-blocks entry above, not a range-parsing issue.
    ("27-ai-engineering-and-observability.md", "tool calling", 18),
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

    chapter_matches = find_chapter_mentions(normalized)
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
                cm
                for cm in chapter_matches
                if "\x00" not in normalized[min(cm[0], kw_match.start()) : max(cm[1], kw_match.end())]
            ]
            if not candidates:
                continue
            nearest = min(
                candidates,
                key=lambda cm: min(
                    abs(cm[0] - kw_match.end()), abs(kw_match.start() - cm[1])
                ),
            )
            distance = min(
                abs(nearest[0] - kw_match.end()), abs(kw_match.start() - nearest[1])
            )
            if distance > MAX_DISTANCE:
                continue
            referenced = nearest[2]
            if expected not in referenced:
                shown = min(referenced, key=lambda n: abs(n - expected))
                if (path.name, keyword, shown) in ALLOWLIST:
                    continue
                start = max(0, min(kw_match.start(), nearest[0]) - 20)
                end = min(len(normalized), max(kw_match.end(), nearest[1]) + 20)
                snippet = normalized[start:end].replace("\x00", " ").strip()
                errors.append(
                    f"{path}: mentions '{keyword}' near 'Chapter {shown}', "
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
