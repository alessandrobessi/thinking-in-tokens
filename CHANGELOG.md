# Changelog

## 2026-07-15

- Reformatted all 20 written chapters to match an updated
  `templates/chapter-template.md`: front matter (Part / Concept Level /
  Prerequisites / New concepts introduced), the Opening Question, the
  Next Obvious Question, each Common Misconceptions block, and the footer
  summary lines all moved from cramped blockquote formatting to plain
  bold paragraphs separated by blank lines — easier to scan and edit,
  same content. Purely mechanical (verified via script + diff review, all
  20 chapters still at 11 sections each, all three validators clean).
- Sixth review round, addressed directly — a precision pass on top of the
  fifth round's causal-masking fix:
  - Chapter 11: added a paragraph explicitly ruling out the misreading
    that a causal model retroactively rewrites an earlier token's
    representation once later context arrives (it doesn't — resolution
    happens at the later position, not backward into the earlier one).
    Fixed query/key/value to note that only the first block derives them
    from raw embeddings — later blocks derive them from the previous
    block's output. Fixed "every earlier token" to "itself and every
    earlier token" in the Technical Explanation, Key Takeaway, and
    Summary, since causal self-attention includes the current position.
  - Chapter 12: same "itself and every earlier token" precision fix in
    the Core Intuition and Summary, which had drifted from Chapter 11's
    corrected framing.
  - Chapter 13: fixed a real contradiction with Chapter 19 — "none of
    these change what the base model fundamentally knows" and "the
    architecture doing the predicting never changes" are both overstated
    given Chapter 19's fuller treatment (fine-tuning can shift facts and
    capabilities; adapter methods add components; DPO skips the reward
    model). Reworded both passages to point to Chapter 19 instead of
    contradicting it, while keeping Chapter 13's preview framing simple.
  - Chapter 15: fixed a residual overstatement — "the model still must
    produce *some* continuation" read as if declining or expressing
    uncertainty weren't valid token choices. Reworded to make clear
    stopping/declining are themselves selectable continuations, and that
    what actually happens depends on training, not sampling mechanics.
  - Chapter 20: the worked example's "errors tend to wash out" framing
    was more reassuring than the Technical Explanation's (already
    correct) calibrated-quantization framing next to it — reworded so
    both sections tell the same story.
  - Fixed a real inconsistency in `concept-graph.yaml`: `rag`'s
    prerequisites listed `vector-databases`, contradicting Chapter 18's
    (correctly) broadened definition of RAG as not requiring vector-based
    retrieval specifically. Removed it from the dependency list. Also
    fixed a stale header comment claiming `concept-graph.md` still needed
    manual regeneration, though the generator script has existed since
    the previous round.
  - Fixed `README.md`'s embedding preview quote, which had drifted from
    Chapter 5's actual (already-corrected) Key Takeaway wording.
  - Added two more citations: `mata2023avianca` (the real court case
    behind Chapter 15's fabricated-citations story) and
    `ji2023hallucination` (a general hallucination survey), closing out
    Chapter 15's previously-flagged citation gaps.
  - Verified several other review claims against the live repo and found
    them stale: `testing/questions.md` already covered Chapters 1–20 (the
    review was reading a version from before the previous commit), and
    the GitHub repo description already read "A Mental Model for Modern
    AI Systems," not the older subtitle the review cited.
- Fifth review round, addressed directly — the most substantial technical
  correctness pass so far, focused on Chapters 11–20:
  - **Causal masking**, the central fix: Chapter 11's Winograd worked
    example and story implicitly described bidirectional (BERT-style)
    resolution of a pronoun, contradicting the book's own established
    framing of generative, decoder-only, autoregressive transformers.
    Rewrote the worked example, story, Core Intuition, and Technical
    Explanation around the fact that attention only looks back across
    earlier tokens, never forward, and added causal masking as a new,
    explicitly named concept with its own misconception
    (`attention-sees-future-tokens`) and detective analogy. Propagated the
    same correction to Chapter 12's story and worked example, which also
    implied full-sentence attention. Added `causal-masking` and
    `attention-heads` to `concept-graph.yaml`.
  - Broadened positional encoding's description beyond "a fixed
    mathematical pattern" to mention learned and RoPE-style alternatives
    (Ch.11), and added a paragraph on multi-head attention.
  - Fixed Chapter 14's sampling explanation: temperature and top-k/nucleus
    sampling were described as merely restricting which token gets
    *picked*; corrected to describe them as *reshaping the distribution
    itself* (rescaling, or truncating and renormalizing).
  - Softened Chapter 15's hallucination framing so it no longer requires
    "confident" phrasing, and softened the "no distinct certainty signal"
    misconception to acknowledge research on internal states correlating
    with uncertainty without being reliably surfaced.
  - Chapter 16: distinguished a token's raw presence in the context window
    (binary) from the model's reliable use of it ("lost in the middle"),
    and qualified the quadratic-cost claim as applying to standard, dense
    attention specifically.
  - Chapters 17/18: broadened RAG so it no longer requires vector-database
    retrieval specifically (keyword search, a direct query, or web search
    can fill the same role), and clarified that RAG's "no parameter
    update" property describes the simplest, most common deployment
    pattern, not every RAG variant.
  - Chapters 13/19: broadened alignment's definition from "what designers
    and users want" (a single, unified target) to "some set of intended
    goals," acknowledging objectives can conflict across designers,
    evaluators, and users. Added Direct Preference Optimization (DPO) as
    an alternative to RLHF, and noted fine-tuning can shift facts and
    capabilities, not only style, and that adapter-based methods exist.
  - Chapter 20: fixed a real factual error — the "same knowledge and
    parameters as the original model" framing for quantization is wrong,
    since quantization does change parameter values; corrected to "same
    architecture, same learned pattern, approximated at lower precision."
    Replaced a generic, hand-wavy "caching" paragraph with a proper
    explanation of KV caching (reusing each token's computed key/value
    instead of recomputing attention from scratch) and prefix caching.
    Also fixed the naive-rounding framing to acknowledge calibrated
    methods (GPTQ-style) use real data, not just independent rounding.
  - Fixed `scripts/validate_concept_graph.py`: the key-takeaway check
    previously only verified that the target file existed, not that the
    anchor was a real heading in it — silently passing a broken anchor.
    Added a GitHub heading-slug approximation and check; verified against
    a synthetically broken anchor that it now genuinely fails.
  - Extended `testing/questions.md` from Chapters 1–10 to 1–20: added
    Comprehension and scenario-based Misconception Resistance questions
    for Chapters 11–20, tied to this round's new and revised
    misconception IDs.
  - Added `levesque2012winograd`, `holtzman2019degeneration`,
    `rafailov2023dpo`, and `frantar2022gptq` to `bibliography.md`, cited
    from the relevant chapter reference files.
  - Verified several other review claims (a GitHub repo-description claim,
    a template-rigidity concern already addressed by the template's
    "editorial checklist, not fixed headings" framing) against the live
    repo; the repo-description claim was stale, as in previous rounds.
- Fourth review round, addressed directly:
  - Fixed Ch.6's "Chapter 24" -> "Chapter 23" reasoning-models
    cross-reference (verified as a real bug before fixing), plus softened
    "geometric neighborhood of a token" and "genuinely undetermined."
  - Reworded Ch.5's Key Takeaway and added a scope note distinguishing
    classic word-level embeddings from modern token/passage embeddings.
  - Fixed a stale concept-graph.yaml comment (Level 6 mislabeled "Part V"
    after retrieval/vector-databases moved to Part IV).
  - concept-graph.md is now GENERATED from concept-graph.yaml
    (`scripts/generate_concept_graph_md.py`), surfacing prerequisites,
    misconception counts, and key-takeaway links per concept instead of a
    bare checkbox — it can no longer drift out of sync by hand-editing.
  - Added `scripts/validate_cross_references.py`, catching exactly the
    "Chapter 24 vs 23" bug class; iterated through several false-positive
    rounds (whole-sentence matching, then paragraph-scoped, then
    nearest-match with list/paragraph boundary awareness) before landing
    on a version clean against the real manuscript that still catches the
    original bug when synthetically reintroduced.
  - Added `requirements.txt` (PyYAML) and `.github/workflows/validate.yml`,
    running all three validators plus a check that `concept-graph.md` is
    actually regenerated and committed alongside any YAML change.
  - Verified several other review claims (a duplicate Ch.7 file, stale
    README/blueprint links, missing pre-test) against the live repo and
    found them false — already fixed in earlier commits; the review was
    reading a stale/cached copy.
- **Added Part III — The Transformer (chapters 11–15)** and **Part IV —
  Building Useful AI (chapters 16–20)**, at the same depth and structure
  as Parts I–II: attention, transformer blocks, the pretraining-to-chatbot
  gap, inference/sampling, hallucination, context windows/memory,
  semantic retrieval/vector databases, RAG, fine-tuning/alignment, and
  quantization/efficient inference. All 10 chapters verified: 11 sections
  each, narrative handoffs intact end to end from Chapter 10 through
  Chapter 20, all three validators clean. Updated glossary, misconception
  graph, concept-graph.yaml (written status, key-takeaways, misconception
  IDs), the style-guide analogy registry (including two deliberately
  linked analogy pairs: the exam analogy spanning Ch.14/18, and the
  medical-school/residency analogy spanning Ch.13/19), both READMEs,
  ROADMAP.md, and `references/chapter-11.md` through `chapter-20.md`.
- Third review round: verified each claim against the live repository
  rather than assuming the review was current. Most of the "urgent" items
  (a duplicate Chapter 7 file, stale links/titles in `book/README.md` and
  `blueprint.md`, unresolved Ch.2/3/4 technical passages, a testing
  protocol missing its pre-test, a stale GitHub repo description) were
  already fixed as of the previous commit — the review was almost
  certainly reading a cached copy (raw.githubusercontent.com and rendered
  GitHub pages can lag behind `git push` by several minutes). Confirmed
  via `git log`, direct file reads, and a direct GitHub API call for the
  repo description, rather than trusting the review's citations.
- Two genuinely new, valid issues fixed: Chapter 5's first definition of
  "embedding" said "words with similar meanings," contradicting the
  chapter's own later, more careful "similar contexts of use" framing —
  reworded, and mirrored in `glossary.md`'s embedding entry (which also
  now reflects the static/contextual distinction). Chapter 3's Key
  Takeaway said a model "never sees letters," technically false for a
  token that happens to be a single character — reworded to "doesn't
  receive text as human-recognized words."
- Added `scripts/validate_manuscript_index.py`: checks exactly one file
  per chapter number (catches a rename that left the old file behind),
  and that every `book/README.md` link resolves and its title matches the
  target file's actual heading. Both this and
  `scripts/validate_concept_graph.py` pass clean.

- **Dropped diagrams as a teaching device entirely** (a deliberate
  reversal, not a deferral — see `blueprint.md`'s new "No Diagrams"
  section). Subtitle changed from "A Visual Guide to Modern AI Systems" to
  "A Conceptual Guide to Modern AI Systems." The chapter template's
  diagram-shaped sections ("Visual Explanation," "Canonical Mental-Model
  Diagram") became text-only sections ("Worked Example" — a second,
  fully-written concrete example — and "Key Takeaway" — one bolded
  sentence) that do the same job with words instead of an illustration.
  Rewrote all 10 written chapters to the new structure. Deleted
  `assets/diagrams/` (20 SVGs), `assets/icons/` (6 SVGs), and
  `scripts/check_svg_bounds.py` — all fully recoverable from git history.
  Amended `blueprint.md`'s Vision, Core Design Principles, Misconception
  Graph example, Standard Chapter Template, and Living Companion sections;
  removed its "Visual Language" section outright. Rewrote
  `style-guide.md` and `templates/chapter-template.md` to match. Renamed
  `concept-graph.yaml`'s `diagram` field to `key_takeaway`, pointing at
  each chapter's §8 anchor instead of a now-deleted diagram file. Updated
  both READMEs and `ROADMAP.md` accordingly.
- Added a second reinforcing example or analogy to every concept across
  all 10 written chapters, so ideas get more than one grounding before
  moving on (per direct feedback that chapters felt compressed): a
  counterfactual thought experiment (Ch. 1, "swap out one of the three
  ingredients"), a thermostat analogy + a reader "try it yourself" for
  information-vs-length (Ch. 2), a rare-word tokenization example (Ch. 3,
  "quokka"), a slang-based context example (Ch. 4, "sick"), a second
  semantic-geometry relationship (Ch. 5, gender offset), a reader
  prediction-ranking exercise (Ch. 6, "opposite of hot"), a concrete sense
  of combinatorial scale (Ch. 7), a hiring-committee analogy (Ch. 8), a
  recipe-adjusting-by-taste analogy (Ch. 9), and a fertilizer/diminishing-
  returns analogy (Ch. 10). All logged in `style-guide.md`'s Analogy
  Registry; the three new reader-facing "try it yourself" prompts (Ch. 2,
  3, 6) were also added to `testing/questions.md` so the reader-validation
  protocol stays in sync with the manuscript.
- Fixed Chapter 3, §10 (Further Reading): removed a reference to "the
  companion website for this book," which doesn't exist yet (an unstarted
  item in `ROADMAP.md`'s Milestone 5) — replaced with a pointer to real,
  already-existing tokenizer visualizer tools.
- Initial commit: project infrastructure (style guide, chapter template,
  glossary, misconception graph, concept dependency tracker, icon set) and
  the full Part I manuscript (chapters 1–5, "Information").
- Added root `README.md`, `LICENSE` (provisional, all-rights-reserved),
  `CONTRIBUTING.md`, `ROADMAP.md`, this changelog, GitHub issue templates,
  and a `references/` bibliography system.
- Amended `blueprint.md`: the Standard Chapter Template is now explicitly
  an editorial checklist rather than a mandatory set of reader-facing
  headings; Part V's table of contents was restructured around durable
  questions instead of named standards (Tool Calling and MCP merged into
  one chapter, "How Models Reach Into the World," with MCP taught inside it
  as the current connection standard). Total chapter count: 31 → 30.
- Chapter 1: softened claims about scale being "the" dominant driver of
  progress and added a note on the ongoing debate over measuring emergent
  abilities.
- Chapter 5: added an explicit distinction between a token's static,
  starting embedding (this chapter) and its contextual, attention-revised
  representation (Chapter 11), plus a new misconception entry, and reframed
  the country/capital geometry example as an illustrative pattern rather
  than a universal law.
- Added `concept-graph.yaml` as the machine-readable source of truth behind
  `concept-graph.md`.
- Added Part II manuscript (chapters 6–10, "Prediction"), with matching
  glossary/misconception/concept-graph/reference updates.
- Second review round: Chapter 8 now draws an explicit boundary between the
  generic layered network it describes and the transformer architecture
  Part III builds on top of it. Chapter 10 clarifies that the scaling-law
  "straight line" requires both axes scaled in equal ratios (not literal
  linear loss decay) and introduces "irreducible loss." Chapter 5 gained a
  "try it yourself" thought experiment (hot/cold/sandwich) reinforcing the
  similarity-vs-synonymy misconception. `style-guide.md`'s chapter-mechanics
  section was reworded to stop contradicting blueprint.md's amended
  template language. Added `testing/` — a ready-to-run reader-validation
  protocol and per-chapter question bank (comprehension, transfer,
  misconception resistance, retention), covering Milestone 3 of
  `ROADMAP.md`.
- **Fixed a rendering bug affecting every diagram in the manuscript.**
  Every embedded `<svg>` contained internal blank lines (used to visually
  separate element groups while authoring). GitHub's Markdown parser treats
  `<svg>` as a generic HTML block that ends at the first blank line — so
  every diagram was silently truncated mid-markup, with the remainder
  (including the closing `</svg>` tag) rendered as literal garbled text
  instead of a diagram. Stripped all internal blank lines from all 20
  diagrams across chapters 1–10; added `scripts/check_svg_bounds.py` and a
  hard rule in `style-guide.md` §3.0 to catch this and a related bug
  (`<text>` labels overflowing their `viewBox`, found and fixed in
  Chapters 1 and 4) before it recurs.
- **Corrected the diagram architecture after confirming diagrams still
  didn't render on GitHub even after the blank-line fix.** Root cause: the
  earlier premise was wrong — GitHub's Markdown sanitizer strips raw
  `<svg>` content wherever it's embedded directly in a `.md` file,
  regardless of formatting; inline SVG in Markdown was never going to
  render on GitHub. Extracted all 20 diagrams (chapters 1–10) to standalone
  files under `assets/diagrams/`, referenced via `<img>` — the same pattern
  already used for the root README's preview image. Verified all 20 render
  correctly via local rendering (macOS QuickLook thumbnailing). Updated
  `templates/chapter-template.md`, `style-guide.md` §3, and
  `scripts/check_svg_bounds.py` (now also fails the build if any chapter
  file contains a literal `<svg` tag again) so future chapters follow the
  corrected pattern by default.
