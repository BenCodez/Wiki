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
    return text.replace("|", "\\|").replace("\n", " ").replace("§", "&#96;")


def render(rows):
    lines = ["---", "title: Commands from VotingPlugin Source",
             "description: Java source-derived command and permission inventory for admins",
             "published: true", "date: 2026-11-09T00:00:00.000Z",
             "tags:", "editor: markdown", "dateCreated: 2026-11-09T00:00:00.000Z",
             "---", "", "# Commands from VotingPlugin source (development)", "",
             "These commands come from Java §CommandHandler§ constructor sites in VotingPlugin's §master§ branch.",
             "This is **static source analysis**, not an in-game registry or a stable-release promise.",
             "See [Commands & Permissions](/VotingPlugin/Commands-&-Permissions) for stable-release guidance.",
             "",
             "> **Dynamic** means the registration contains values created by loops, enums, or configuration.",
             "> Confirm such commands, feature gates, and alternate labels against the relevant source.",
             "{.is-warning}", ""]
    for root in ["/av", "/vote"]:
        lines += ["## " + root + " handlers", "",
                  "| Command or template | Permission expression | Description | Source |",
                  "|---|---|---|---|"]
        entries = sorted((r for r in rows if r["root"] == root),
                         key=lambda r: (r["args"].casefold(), r["line"]))
        for row in entries:
            filename = row["filename"]
            directory = "commands" if filename == "CommandLoader.java" else "streaks"
            url = ("https://github.com/BenCodez/VotingPlugin/blob/master/"
                   "VotingPlugin/src/main/java/com/bencodez/votingplugin/" + directory
                   + "/" + filename + "#L" + str(row["line"]))
            syntax = root + (" " + row["args"] if row["args"] else "")
            lines.append("| §" + cell(syntax) + "§" + (" **Dynamic**" if row["dynamic"] else "")
                         + " | §" + cell(row["permission"]) + "§ | "
                         + cell(row["description"]) + " | [source](" + url + ") |")
        lines.append("")
    lines += ["## Beyond these constructor sites", "",
              "Additional registrations from §DateVoteMilestoneCommands.register§,",
              "§AdvancedCore.command.CommandLoader.getBasicCommands§, and configuration-defined",
              "custom commands are not expanded into concrete entries by this static pass.",
              "Proxy-side §/votingpluginproxy§ commands use a different dispatcher.",
              "",
              "The Wiki workflow can refresh this page whenever upstream source changes.",
              "It opens a documentation PR for review and requires no server runtime changes.", ""]
    return "\n".join(lines).replace("§", chr(96))


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
