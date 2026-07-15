#!/usr/bin/env python3
"""Checks for this project's diagram files.

1. Every diagram must live as a standalone file under assets/diagrams/ or
   assets/icons/, referenced from chapters via <img src="...">. GitHub's
   Markdown sanitizer strips raw inline <svg> content wherever it appears
   directly in a .md file's rendered HTML (regardless of blank lines or
   anything else) -- it never renders. So this script's first job is a
   regression guard: fail if any book/**/*.md contains a literal <svg tag.

2. Heuristic check for SVG <text> elements that overflow their viewBox.
   Not a real font-metrics engine -- estimates rendered width as
   (char count) * font-size * AVG_CHAR_WIDTH_FACTOR, a reasonable
   approximation for Helvetica/Arial at these sizes. Does not account for
   transform="rotate(...)" -- verify those by hand instead of trusting the
   tool. Flags anything past a small tolerance so near-misses don't drown
   out real bugs.
"""
import re
import sys
from pathlib import Path

AVG_CHAR_WIDTH_FACTOR = 0.55
TOLERANCE_PX = 3

SVG_RE = re.compile(r"<svg\b([^>]*)>(.*?)</svg>", re.DOTALL)
VIEWBOX_RE = re.compile(r'viewBox="([\d.\-]+)\s+([\d.\-]+)\s+([\d.\-]+)\s+([\d.\-]+)"')
TEXT_RE = re.compile(r'<text\b([^>]*)>(.*?)</text>', re.DOTALL)
ATTR_RE = re.compile(r'([a-zA-Z\-:]+)="([^"]*)"')


def get_attrs(attr_str):
    return dict(ATTR_RE.findall(attr_str))


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s).strip()


def check_inline_svg_regression(root):
    """book/**/*.md must never contain a literal <svg> again -- it silently
    fails to render on GitHub. Diagrams belong in assets/diagrams/ as
    standalone files, referenced via <img>."""
    offenders = []
    for f in sorted(root.glob("book/**/*.md")):
        if "<svg" in f.read_text():
            offenders.append(f)
    return offenders


def check_overflow(path):
    text = path.read_text()
    issues = []
    for svg_match in SVG_RE.finditer(text):
        svg_attrs = get_attrs(svg_match.group(1))
        vb = svg_attrs.get("viewBox")
        if not vb:
            continue
        vb_match = VIEWBOX_RE.search(f'viewBox="{vb}"')
        if not vb_match:
            continue
        vb_min_x, vb_min_y, vb_w, vb_h = map(float, vb_match.groups())
        body = svg_match.group(2)
        for t_match in TEXT_RE.finditer(body):
            attrs = get_attrs(t_match.group(1))
            content = strip_tags(t_match.group(2))
            if not content:
                continue
            try:
                x = float(attrs.get("x", "0"))
            except ValueError:
                continue
            font_size = float(re.sub(r"[^\d.]", "", attrs.get("font-size", "13")) or 13)
            anchor = attrs.get("text-anchor", "start")
            width = len(content) * font_size * AVG_CHAR_WIDTH_FACTOR
            if anchor == "middle":
                left, right = x - width / 2, x + width / 2
            elif anchor == "end":
                left, right = x - width, x
            else:
                left, right = x, x + width
            overflow_right = right - (vb_min_x + vb_w)
            overflow_left = vb_min_x - left
            if overflow_right > TOLERANCE_PX or overflow_left > TOLERANCE_PX:
                issues.append(
                    (content, anchor, x, font_size, round(max(overflow_right, overflow_left)), vb_w)
                )
    return issues


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")

    print("=== Regression check: no inline <svg> in book/**/*.md ===")
    offenders = check_inline_svg_regression(root)
    if offenders:
        for f in offenders:
            print(f"  FAIL: {f} still contains an inline <svg> -- it will not render on GitHub.")
    else:
        print("  OK: no inline <svg> found in any chapter file.")

    print("\n=== Overflow check: assets/diagrams/ and assets/icons/ ===")
    files = sorted(root.glob("assets/diagrams/*.svg")) + sorted(root.glob("assets/icons/*.svg"))
    total = 0
    for f in files:
        issues = check_overflow(f)
        if issues:
            print(f"\n{f}")
            for content, anchor, x, font_size, overflow, vb_w in issues:
                print(
                    f'  "{content}" (anchor={anchor}, x={x}, font-size={font_size}) '
                    f"~{overflow:.0f}px past viewBox edge (width={vb_w:.0f})"
                )
            total += len(issues)
    print(f"\n{total} potential overflow(s) found across {len(files)} diagram files.")

    if offenders:
        sys.exit(1)


if __name__ == "__main__":
    main()
