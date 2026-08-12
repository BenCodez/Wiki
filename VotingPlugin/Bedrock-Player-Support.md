---
title: Bedrock Player Support
description: Configure consistent Geyser/Floodgate player names for standalone and proxy voting
published: true
date: 2025-08-31T03:33:53.924Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:17:57.836Z
---

# Bedrock Player Support

VotingPlugin identifies a Bedrock player by the prefix used by Geyser/Floodgate.
The default is a period, so a Bedrock player whose base name is `Example` votes
as `.Example`.

> These instructions describe the latest public release, VotingPlugin 7.1.1.
{.is-info}

## Proxy and backend configuration

Set `BedrockPlayerPrefix` to the prefix actually used for Bedrock player names.
On a standalone server, configure it in `Config.yml`. On a proxy network, use
the same value in the proxy `bungeeconfig.yml` and every backend `Config.yml`:

```yaml
BedrockPlayerPrefix: '.'
```

Restart the affected proxy and servers after changing the value. Players must
enter the complete in-game name, including the prefix, on every voting site.
If a voting site rejects or removes the prefix character, it cannot reliably
address that Bedrock identity.

## Identity safety

Treat the prefixed and unprefixed names as different accounts. For example,
`.Example` (Bedrock) and `Example` (Java) may both exist. Do not remove the
prefix to work around a voting-site form, because the vote could be credited to
the Java identity instead.

Choose the prefix before players begin voting and keep it consistent. Changing
it later can leave existing vote data under the old player name; back up the
VotingPlugin data and plan an identity/data migration before doing so.

## Development-build changes

> **Development only — not in release 7.1.1:** the unreleased
> `7.1.2-SNAPSHOT` line adds strict validation for usernames received from
> Votifier while allowing the configured Bedrock prefix (VotingPlugin commits
> [`935ea656`](https://github.com/BenCodez/VotingPlugin/commit/935ea656d265f2ac2ddea28e8e9fc2f0a2676cc3),
> [`8aaf1eb9`](https://github.com/BenCodez/VotingPlugin/commit/8aaf1eb909e4a6feec1e12e397e5006ee039eab1),
> and [`0a344625`](https://github.com/BenCodez/VotingPlugin/commit/0a3446255be089f70539c99896e793b97ebdafd8)).
> It also preserves an exact known Java identity before trying a prefixed
> Bedrock fallback, preventing a shared base name from redirecting that vote
> (AdvancedCore commit
> [`4e81f7d4`](https://github.com/BenCodez/AdvancedCore/commit/4e81f7d4) and
> VotingPlugin commit
> [`2ac38e81`](https://github.com/BenCodez/VotingPlugin/commit/2ac38e81)).
> Release users do not have these hardening changes yet.
{.is-warning}

## Troubleshooting

- Confirm the player's exact in-game name, including case and prefix.
- Confirm `BedrockPlayerPrefix` is identical on the proxy and all backends.
- Send a test vote and check which username the voting site actually delivers.
- Follow [Votifier Troubleshooting](https://github.com/BenCodez/VotingPlugin/wiki/Votifier-Troubleshooting)
  if the listener does not receive the expected name.
