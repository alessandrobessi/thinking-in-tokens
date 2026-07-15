# Changelog

## 2026-07-15

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
