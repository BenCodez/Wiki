#!/usr/bin/env python3
"""Remove Wiki.js attribute-only lines from staged Markdown files."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ATTRIBUTE_LINE = re.compile(
    r"^[ \t]*\{[ \t]*(?:\.[A-Za-z0-9_-]+)"
    r"(?:[ \t]+\.[A-Za-z0-9_-]+)*[ \t]*\}[ \t]*(?:\r?\n)?$"
)


def strip_attributes(path: Path) -> int:
    original = path.read_text(encoding="utf-8")
    lines = original.splitlines(keepends=True)
    kept = [line for line in lines if ATTRIBUTE_LINE.fullmatch(line) is None]
    removed = len(lines) - len(kept)

    if removed:
        path.write_text("".join(kept), encoding="utf-8")

    return removed


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Remove Wiki.js {.class} attribute-only lines from Markdown."
    )
    parser.add_argument("root", type=Path, help="Directory containing staged Markdown")
    args = parser.parse_args()

    if not args.root.is_dir():
        parser.error(f"not a directory: {args.root}")

    files_changed = 0
    lines_removed = 0

    for path in sorted(args.root.rglob("*.md")):
        if not path.is_file():
            continue

        removed = strip_attributes(path)
        if removed:
            files_changed += 1
            lines_removed += removed

    print(
        f"Removed {lines_removed} Wiki.js attribute line(s) "
        f"from {files_changed} Markdown file(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
