# BenCodez Wiki

This repository contains the Markdown source synchronized with the BenCodez
Wiki and used to publish VotingPlugin documentation to multiple surfaces.

## Published copies

| Surface | Purpose |
|---|---|
| [wiki.bencodez.com](https://wiki.bencodez.com) | Primary Wiki.js documentation |
| [VotingPlugin GitHub Wiki](https://github.com/BenCodez/VotingPlugin/wiki) | GitHub-hosted mirror |
| [wiki-backup.bencodez.com](https://wiki-backup.bencodez.com) | MkDocs/GitHub Pages backup |

Changes reaching `main` trigger both publication workflows:

- `.github/workflows/mirror-to-votingplugin-wiki.yml` prepares the Markdown for
  GitHub Wiki and pushes it to `BenCodez/VotingPlugin.wiki`.
- `.github/workflows/deploy-pages.yml` stages the repository for MkDocs and
  deploys the backup site through GitHub Pages.

## Repository layout

- `home.md` — Wiki.js home content; mirrored as GitHub Wiki `Home.md`
- `.wikijs/navigation.json` — Wiki.js navigation configuration
- `sidebar.md` — GitHub Wiki sidebar source; mirrored as `_Sidebar.md`
- `VotingPlugin/` — VotingPlugin documentation pages
- `assets/` — diagrams and other documentation assets
- `.github/workflows/` — mirror and backup deployment workflows
- `mkdocs.yml` — GitHub Pages backup configuration

## Source-format compatibility

The source pages may contain Wiki.js YAML front matter and attribute-only lines
such as `{.is-info}`. The publication workflows prepare staged copies for their
target renderer; source pages should not be destructively converted merely to
make one mirror work.

When changing links, page names, images, or metadata, consider all three
published copies. Avoid deleting established page names without leaving a
replacement or migration path because external links may rely on the existing
slug.

## Contributing

1. Create a branch from `main`.
2. Keep each pull request focused on one documentation or publication concern.
3. Check configuration names, commands, API signatures, and examples against
   the current VotingPlugin or AdvancedCore source.
4. Preserve Wiki.js front matter unless the page is newly created.
5. Confirm internal links work after the GitHub Wiki and MkDocs staging steps.
6. Describe whether AI assisted with a proposed change.

Repository-maintenance files such as this README are excluded from the
published wiki copies.
