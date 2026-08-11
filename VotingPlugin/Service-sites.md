---
title: Service-sites
description: 
published: true
date: 2025-08-30T22:18:24.404Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:23.897Z
---

# Service Sites

The service site is the identifier supplied by the voting website through
Votifier. VotingPlugin uses it to decide which entry in `VoteSites.yml` should
process the vote.

Most voting websites use a domain-like value, but the website controls the
actual value. Do not guess it from the public vote URL.

## Find the received value

Send a real or administrative test vote and check the console for messages like:

```text
[VotifierPlus] Debug: Received vote record -> Vote (from:SERVICESITEHERE username:BenCodez ...)
[VotingPlugin] Received a vote from service site 'SERVICESITEHERE' by player 'BenCodez'!
```

You can also run `/av servicesites` after the vote to view service sites that
VotingPlugin has received. Put the value in the applicable `VoteSites.yml`
entry:

```yaml
VoteSites:
  ExampleVoteSite:
    Enabled: true
    ServiceSite: 'SERVICESITEHERE'
```

Matching is case-insensitive, but otherwise the received service-site text
must match the configured value.

## Supported names

> **Availability:** The validation rules and rejection warning in this section
> are available only in development builds containing
> [VotingPlugin PR #1540](https://github.com/BenCodez/VotingPlugin/pull/1540),
> merged after the latest public release, **7.1.1**. Release 7.1.1 supports
> service-site matching and automatic creation but does not apply this new
> validator.
{.is-warning}

Development builds with this validator accept bounded, visible service-site
names, including common domain names, spaces, Unicode letters, and
URL-compatible punctuation such as `:`, `/`, `?`, `=`, `&`, `%`, `+`, and `#`.

A received name is rejected before vote processing when it:

- is empty, whitespace-only, or made only of combining/invisible filler
  characters;
- exceeds 2,048 UTF-16 code units;
- contains square brackets, a single or double quote, a backtick, or a
  backslash; or
- contains control or formatting characters, including tabs and line breaks.

Rejected values produce a bounded warning beginning with
`Rejected vote with invalid service site`. Correct the service-site value at
the voting website; do not create a differently named `VoteSites.yml` entry to
work around the rejection.

## Automatic vote-site creation

With `AutoCreateVoteSites: true`, VotingPlugin attempts to create a missing
`VoteSites.yml` entry from a valid received service site. Dots and whitespace
are converted to underscores for the internal vote-site key, while the
original text is retained as `ServiceSite`.

If automatic creation is disabled or fails, create the site through `/av gui`,
VotingPluginEditor, or `VoteSites.yml`, then retry a vote.

## Enforce the vote delay

`VoteDelay` controls `/vote next`, but it does not reject an early vote unless
`WaitUntilVoteDelay` is enabled for that site:

```yaml
VoteSites:
  ExampleVoteSite:
    ServiceSite: 'SERVICESITEHERE'
    VoteDelay: 24h
    WaitUntilVoteDelay: true
```

Enable this only when the voting website's real voting interval matches the
configured delay. Otherwise a legitimate vote can be discarded without its
normal rewards. `VotingPlugin.BypassWaitUntilVoteDelay` bypasses this check.

> **Development-build availability:** Release **7.1.1** logs and rejects an
> early real vote, but it has no configurable rejection reward. Development
> builds containing
> [VotingPlugin PR #1536](https://github.com/BenCodez/VotingPlugin/pull/1536)
> add the standard reward section `WaitUntilVoteDelayRewards`:
>
> ```yaml
> VoteSites:
>   ExampleVoteSite:
>     WaitUntilVoteDelay: true
>     WaitUntilVoteDelayRewards:
>       Messages:
>         Player: '&cThat vote was too early and was not accepted.'
> ```
>
> It supports `%ServiceSite%`, `%SiteName%`, `%VoteDelay%`, and `%VoteURL%`.
> Proxy-side rejection feedback requires compatible development builds on the
> proxy and receiving backend, `ProcessRewards: true` on the backend, and an
> online player whose current backend is known. An offline proxy rejection is
> still logged but does not send this reward to a backend.
{.is-warning}

If VotingPlugin never logs that it received the vote, follow
[Votifier Troubleshooting](https://github.com/BenCodez/VotingPlugin/wiki/Votifier-Troubleshooting).
Known examples are listed under
[Minecraft Server Lists](https://github.com/BenCodez/VotingPlugin/wiki/Minecraft-Server-Lists).
