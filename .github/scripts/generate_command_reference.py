#!/usr/bin/env python3
"""Source-only command reference generator. Does not load or modify VotingPlugin."""
import argparse
import json
import re
from pathlib import Path

CONSTRUCTOR = re.compile(r"new\s+(?:Player)?CommandHandler\s*\(")
PERMISSION_VARS = {"adminPerm": "VotingPlugin.Admin", "playerPerm": "VotingPlugin.Player",
                   "modPerm": "VotingPlugin.Mod", "adminPermission": "VotingPlugin.Admin"}


def split_top_level(text):
    result, at, depth, quote, escaped = [], 0, 0, "", False
    for i, ch in enumerate(text):
        if quote:
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == quote:
                quote = ""
        elif ch in ('"', "'"):
            quote = ch
        elif ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth -= 1
        elif ch == "," and depth == 0:
            result.append(text[at:i].strip())
            at = i + 1
    result.append(text[at:].strip())
    return result


def constructor_body(source, start):
    depth, quote, escaped = 0, "", False
    for i in range(start, len(source)):
        ch = source[i]
        if quote:
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == quote:
                quote = ""
        elif ch in ('"', "'"):
            quote = ch
        elif ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0:
                return source[start + 1:i]
    raise ValueError("Unclosed CommandHandler constructor")


def expression(text):
    pieces, dynamic = [], False
    for piece in re.split(r"\s+\+\s+", text.strip()):
        if piece.startswith('"') and piece.endswith('"'):
            try:
                pieces.append(json.loads(piece))
            except ValueError:
                dynamic = True
                pieces.append("<expression>")
        elif piece in PERMISSION_VARS:
            pieces.append(PERMISSION_VARS[piece])
        else:
            dynamic = True
            pieces.append("<" + piece.replace("|", "¦").replace("\n", " ") + ">")
    return "".join(pieces), dynamic


def extract(source, filename, root):
    rows = []
    for match in CONSTRUCTOR.finditer(source):
        fields = split_top_level(constructor_body(source, match.end() - 1))
        if len(fields) < 4 or fields[0] != "plugin":
            raise ValueError("Unexpected constructor in " + filename)
        arg_match = re.fullmatch(r"new\s+String\s*\[\s*\]\s*\{(.*)\}", fields[1], re.DOTALL)
        if arg_match:
            parsed = [expression(item) for item in split_top_level(arg_match.group(1)) if item]
            args = " ".join(item[0].replace("&", "/") for item in parsed)
            dynamic = any(item[1] for item in parsed)
        else:
            args, dynamic = "<configuration-defined arguments>", True
        permission, dyn_permission = expression(fields[2])
        description, dyn_description = expression(fields[3])
        line = source.count("\n", 0, match.start()) + 1
        rows.append({"root": root(match.start()), "args": args, "permission": permission,
                     "description": description, "dynamic": dynamic or dyn_permission or dyn_description,
                     "filename": filename, "line": line})
    return rows


def cell(text):
    return text.replace("|", "\\|").replace("\n", " ").replace(chr(96), "&#96;")


def render(rows):
    """Generate user-facing administrator tables without implementation links."""
    visible = [row for row in rows if not row["dynamic"]]
    omitted = len(rows) - len(visible)
    marker = chr(96)
    lines = [
        "---",
        "title: VotingPlugin Commands & Permissions (Development)",
        "description: Automatically generated command and permission reference for server administrators",
        "published: true",
        "date: 2026-11-09T00:00:00.000Z",
        "tags:",
        "editor: markdown",
        "dateCreated: 2026-11-09T00:00:00.000Z",
        "---",
        "",
        "# Commands & Permissions — Development",
        "",
        "These command tables are automatically maintained from VotingPlugin's development",
        "command definitions. They are intended for **server administrators**, not for",
        "players learning how to vote. The latest stable release may have different commands.",
        "For the released-version reference, see",
        "[Commands & Permissions](/VotingPlugin/Commands-&-Permissions).",
        "",
        "> **Availability:** Some commands depend on server settings, permissions, or",
        "> optional features. Use `/av help`, `/av perms` and `/vote help` on your server",
        "> to confirm what your installed version actually supports.",
        "{.is-info}",
        "",
    ]
    for root, heading in (("/av", "Administrator commands (`/av`)"),
                          ("/vote", "Voting commands (`/vote`)")):
        lines.extend(["## " + heading, "",
                      "| Command | Permission | Description |",
                      "|---|---|---|"])
        entries = sorted((row for row in visible if row["root"] == root),
                         key=lambda row: (row["args"].casefold(), row["permission"].casefold()))
        for row in entries:
            syntax = root + (" " + row["args"] if row["args"] else "")
            lines.append("| " + marker + cell(syntax) + marker
                         + " | " + marker + cell(row["permission"]) + marker
                         + " | " + cell(row["description"]) + " |")
        lines.append("")
    lines.extend([
        "## Optional and dynamically configured commands",
        "",
        "The tables show command names that can be determined directly. This generated",
        "snapshot omits " + str(omitted) + " dynamically constructed command templates",
        "rather than displaying Java expressions as usable commands.",
        "Commands registered through configuration, optional integrations, and",
        "other command dispatchers can also differ from these tables.",
        "",
        "For proxy administration (`/votingpluginproxy`), see",
        "[Proxy Setups](/VotingPlugin/Proxy-Setups).",
        "For command access on a running server, use `/av perms` or",
        "`/av permsplayer <player>`.",
        "",
    ])
    return "\n".join(lines)


def generate(loader, streak):
    boundary = loader.index("private void loadVoteCommand()")
    rows = extract(loader, "CommandLoader.java", lambda i: "/av" if i < boundary else "/vote")
    rows += extract(streak, "VoteStreaksCommand.java", lambda i: "/vote")
    if len(rows) < 100:
        raise ValueError("Source format changed or too few handlers found")
    return render(rows)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--loader", required=True, type=Path)
    parser.add_argument("--streak", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    output = generate(args.loader.read_text(encoding="utf-8"),
                      args.streak.read_text(encoding="utf-8"))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output, encoding="utf-8")


if __name__ == "__main__":
    main()
