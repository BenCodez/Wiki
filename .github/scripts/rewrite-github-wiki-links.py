#!/usr/bin/env python3
"""Rewrite staged Wiki.js root links for the GitHub Wiki mirror."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


MARKDOWN_LINK = re.compile(r"(?P<prefix>!?\[[^\]]*\]\()(?P<target><[^>]+>|[^)\s]+)(?P<suffix>\))")


def rewrite_link(match: re.Match[str], source: Path, root: Path) -> str:
    target = match.group("target")
    if target.startswith("<") and target.endswith(">"):
        return match.group(0)

    path, marker, remainder = target.partition("#")
    path, query_marker, query = path.partition("?")
    if not path.startswith("/"):
        return match.group(0)

    candidate = (root / path.lstrip("/")).resolve()
    try:
        candidate.relative_to(root)
    except ValueError:
        return match.group(0)

    page = candidate.with_suffix(".md")
    if not candidate.suffix and page.is_file():
        # GitHub Wiki page URLs are flat and use the Markdown filename.
        rewritten = page.stem
    elif candidate.is_file():
        # GitHub Wiki page URLs are also flat, so assets are relative to the
        # /wiki/ route rather than to the Markdown file's repository folder.
        rewritten = candidate.relative_to(root).as_posix()
    else:
        return match.group(0)

    if query_marker:
        rewritten += query_marker + query
    if marker:
        rewritten += marker + remainder
    return match.group("prefix") + rewritten + match.group("suffix")


def rewrite_file(path: Path, root: Path) -> int:
    original = path.read_text(encoding="utf-8")
    count = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal count
        rewritten = rewrite_link(match, path, root)
        if rewritten != match.group(0):
            count += 1
        return rewritten

    rewritten = MARKDOWN_LINK.sub(replace, original)
    if rewritten != original:
        path.write_text(rewritten, encoding="utf-8")
    return count


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Rewrite staged Wiki.js links for the GitHub Wiki mirror."
    )
    parser.add_argument("root", type=Path, help="Staged GitHub Wiki directory")
    args = parser.parse_args()
    root = args.root.resolve()

    if not root.is_dir():
        parser.error(f"not a directory: {root}")

    files_changed = 0
    links_rewritten = 0
    for path in sorted(root.rglob("*.md")):
        count = rewrite_file(path, root)
        if count:
            files_changed += 1
            links_rewritten += count

    print(
        f"Rewrote {links_rewritten} staged Markdown link(s) "
        f"in {files_changed} file(s) for GitHub Wiki."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
