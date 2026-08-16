---
title: Votifier Troubleshooting
description: Diagnose listener, service-site, and proxy vote delivery
published: true
date: 2026-08-14T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2025-08-30T22:18:29.993Z
---

# Votifier Troubleshooting

## Verify the listener path

A healthy real or listener-generated test normally produces both:

1. A VotifierPlus/NuVotifier message showing that a vote record was received.
2. `[VotingPlugin] Received a vote from service site 'SERVICESITEHERE' by player 'BenCodez'!`

`/av vote <player> <site>` tests VotingPlugin processing but does **not** test the public listener port, token/key, or vote-site connection.

Supported listener options include [VotifierPlus](https://github.com/BenCodez/VotifierPlus/wiki/Setup-guide) and NuVotifier. Public tester availability changes over time; a real test from one configured listing is the strongest end-to-end check.

## Match `ServiceSite`

The incoming service name must exactly match:

```text
VoteSites.yml -> VoteSites.<site>.ServiceSite
```

After a test vote, use `/av servicesites` to view received service names. Do not substitute the display name or vote URL unless the listing actually sends that value.

If no matching site exists and automatic site creation is enabled, VotingPlugin can create a site. Review generated entries before enabling rewards.

## No listener receipt

Check:

- the listener plugin loaded successfully;
- the public host and configured port match the vote listing;
- the port is forwarded and allowed through provider, host, container, and OS firewalls;
- another process is not already using the port;
- the vote listing uses the matching token or public key;
- DNS resolves to the intended public address.

`0.0.0.0` is a wildcard **bind** address, not an address a vote site should connect to. Bind only when the hosting layout requires it, then restrict the listener port to the expected public exposure and keep unrelated management ports private.

## Proxy networks

In the standard VotingPlugin topology:

- VotifierPlus/NuVotifier listens on the proxy.
- VotingPlugin runs on the proxy and backends.
- VotingPlugin forwards through the selected `BungeeMethod`.
- VotifierPlus/NuVotifier backend forwarding targets remain disabled.

A deliberately custom topology can place or forward listeners differently, but each vote must enter VotingPlugin only once. Duplicate listener plugins or forwarding paths commonly cause duplicate rewards.

Test proxy communication separately with:

```text
/votingpluginproxy status
/votingpluginproxy vote <player> <site>
```

Then send a real/listener-generated vote to verify the public listener path.

## Player, UUID, and Bedrock checks

- Keep proxy and backend `OnlineMode` values consistent with the network's identity mode.
- Configure `BedrockPlayerPrefix` to match the actual Floodgate/Geyser prefix.
- Avoid prefixes that can collide with valid Java usernames.
- Do not confuse proxy `AllowUnJoined` with backend `AllowUnjoined`; capitalization is significant. The standard proxy-managed layout uses proxy `false` and backend `true`.

## Vote reaches Votifier but not VotingPlugin

- Confirm VotingPlugin is installed on the process receiving the listener event.
- Check startup errors and plugin compatibility.
- Enable the relevant debug setting, send one bounded test, and review the surrounding log.
- On a proxy, verify the selected `BungeeMethod`, shared database, server names, and transport connection.

Do not publish private keys, tokens, database credentials, broker credentials, or full unredacted configuration files in support reports.
