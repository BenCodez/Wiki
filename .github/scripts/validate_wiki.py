#!/usr/bin/env python3
"""Check Wiki.js navigation, page metadata and local Markdown links.

Use --base to validate only Markdown changed by a PR while checking all
navigation targets. --all validates the entire source for a deeper audit.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

LINK = re.compile(r"!?\[[^\]\n]*\]\((?P<target><[^>]+>|[^)\s]+)(?:\s+['\"][^'\"]+['\"])?\)")
FENCE = re.compile(r"^\s*((?:\x60){3,}|~{3,})")
INLINE_CODE = re.compile(r"(?<!\\)(`+)(.*?)\1", re.DOTALL)
REFERENCE_DEFINITION = re.compile(r"(?m)^[ \t]{0,3}\[([^\]\n]+)\]:[ \t]*(?:<([^>\n]+)>|([^\s]+))")
FRONT = re.compile(r"\A---\r?\n(?P<fields>.*?)\r?\n---\r?\n", re.DOTALL)


def resolve_link(root: Path, source: Path, raw: str) -> Path | None:
    raw = raw.strip().strip("<>")
    if raw.startswith(("#", "mailto:", "tel:", "data:")):
        return None
    url = urlsplit(raw)
    if url.scheme or url.netloc or not url.path:
        return None
    name = unquote(url.path)
    if name.startswith("/en/"):
        name = name[3:]
    if name == "/":
        return root / "home.md"
    candidate = root / name.lstrip("/") if name.startswith("/") else source.parent / name
    candidate = candidate.resolve()
    if not candidate.is_relative_to(root):
        raise ValueError("link escapes repository: " + raw)
    return candidate


def exists(path: Path) -> bool:
    return (path.is_file() or (not path.suffix and path.with_suffix(".md").is_file())
            or (path.is_dir() and (path / "index.md").is_file()))


def without_fences(content: str) -> str:
    out = []
    open_marker = ""
    for line in content.splitlines(keepends=True):
        match = FENCE.match(line)
        if match and not open_marker:
            open_marker = match.group(1)[0]
            out.append("\n")
        elif match and open_marker and match.group(1)[0] == open_marker:
            open_marker = ""
            out.append("\n")
        else:
            out.append("\n" if open_marker else line)
    return "".join(out)


def check_page(root: Path, path: Path) -> list[str]:
    problems = []
    relative = path.relative_to(root).as_posix()
    content = path.read_text(encoding="utf-8")
    if relative != "README.md":
        match = FRONT.match(content)
        if not match:
            problems.append(relative + ": missing YAML front matter")
        else:
            fields = match.group("fields").splitlines()
            for key in ("title:", "published:", "editor:"):
                if not any(line.startswith(key) for line in fields):
                    problems.append(relative + ": missing field " + key)
    rendered = INLINE_CODE.sub(lambda match: " " * len(match.group(0)), without_fences(content))
    # Reference links use [label][id] plus [id]: destination. Check every
    # definition (including images) even when it is currently unused.
    references = [match.group(2) or match.group(3) for match in REFERENCE_DEFINITION.finditer(rendered)]
    inline = [match.group("target") for match in LINK.finditer(rendered)]
    for target in inline + references:
        try:
            path_ref = resolve_link(root, path, target)
        except ValueError as exc:
            problems.append(relative + ": " + str(exc))
            continue
        if path_ref is not None and not exists(path_ref):
            problems.append(relative + ": broken internal link " + target)
    return problems


def check_nav(root: Path) -> list[str]:
    nav_path = root / ".wikijs" / "navigation.json"
    if not nav_path.is_file():
        return ["missing .wikijs/navigation.json"]
    try:
        data = json.loads(nav_path.read_text(encoding="utf-8"))
    except (ValueError, OSError) as exc:
        return ["invalid navigation JSON: " + str(exc)]
    errors = []
    seen_ids = set()
    for locale in data.get("locales", []):
        for item in locale.get("items", []):
            ident = item.get("id")
            if not ident or ident in seen_ids:
                errors.append("empty or duplicate navigation ID: " + str(ident))
            seen_ids.add(ident)
            if item.get("targetType") != "page":
                continue
            target = item.get("target")
            if not isinstance(target, str) or not target.startswith("/"):
                errors.append("invalid page target: " + str(target))
                continue
            try:
                location = resolve_link(root, root / "home.md", target)
            except ValueError as exc:
                errors.append(str(exc))
                continue
            if location is None or not exists(location):
                errors.append("missing navigation page: " + target)
    return errors


def changed_pages(root: Path, base: str) -> list[Path]:
    proc = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=ACMR", base + "...HEAD"],
        cwd=root, check=True, capture_output=True, text=True,
    )
    paths = []
    for name in proc.stdout.splitlines():
        if not name.endswith(".md"):
            continue
        path = (root / name).resolve()
        if path.is_relative_to(root) and path.is_file():
            paths.append(path)
    return paths


def validate(root: Path, pages: list[Path]) -> list[str]:
    errors = check_nav(root)
    for page in pages:
        errors.extend(check_page(root, page))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    scope = parser.add_mutually_exclusive_group(required=True)
    scope.add_argument("--base", help="Base commit SHA")
    scope.add_argument("--all", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        pages = (sorted(p for p in root.rglob("*.md")
                        if ".git" not in p.parts and "docs" not in p.relative_to(root).parts)
                 if args.all else changed_pages(root, args.base))
        problems = validate(root, pages)
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print("Validator error: " + str(exc), file=sys.stderr)
        return 2
    for problem in problems:
        print("ERROR: " + problem, file=sys.stderr)
    print("Checked " + str(len(pages)) + " Markdown page(s) and all navigation targets.")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
