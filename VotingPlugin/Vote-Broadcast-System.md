---
title: Vote Broadcast System
description: Configure backend formatting and proxy-wide vote broadcast routing
published: true
date: 2026-08-14T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2026-02-12T02:01:20.209Z
---

# Vote Broadcast System

VotingPlugin separates backend broadcast formatting/timing from proxy routing.

## Backend `VoteBroadcast`

Configured in backend `Config.yml`:

```yaml
VoteBroadcast:
  Type: EVERY_VOTE
  Duration: 2m
  MaxSitesListed: 0
  Format:
    BroadcastMsg: '&6[&4Vote&6] &aThanks &e%player% &afor voting on &e%site%&a!'
    Header: '&6[&4Vote&6] &a%player% voted on &e%sites_count% &asites:'
    ListLine: '&7 - &e%site%'
```

### Types

| Type | Behavior |
|---|---|
| `NONE` | Disables backend vote broadcasts. |
| `EVERY_VOTE` | Broadcasts every processed vote. |
| `EVERY_VOTE_ONLINE_ONLY` | Broadcasts only while the voting player is online. |
| `COOLDOWN_PER_PLAYER` | Broadcasts at most once per `Duration` for each player. |
| `BATCH_WINDOW_PER_PLAYER` | Collects a player's votes during `Duration`, then emits one message/list. |
| `FIRST_VOTE_OF_DAY` | Broadcasts only the player's first vote of the calendar day. |
| `INTERVAL_SUMMARY_GLOBAL` | Periodically broadcasts a global summary. |

`Duration` accepts `s`, `m`, `h`, `d`, or `w`; months are not supported.

Common format placeholders include `%player%`, `%site%`, `%sites_count%`, `%sites%`, and `%reason%`. Interval summaries also expose `%players%`, `%numberofplayers%`, and `%numberofsites%`.

## Proxy `ProxyBroadcast`

> **Release boundary:** These settings exist in public release 7.1.1. In 7.1.1, an offline vote being queued can delay an `OfflineMode: FORWARD` broadcast until vote delivery. Immediate forwarding independent of the queued vote is development-only in builds containing [PR #1541](https://github.com/BenCodez/VotingPlugin/pull/1541), merged after 7.1.1.
{.is-warning}

Configured in proxy `bungeeconfig.yml`:

```yaml
ProxyBroadcast:
  Enabled: true
  Scope:
    Mode: ALL_SERVERS
    Servers: []
  OfflineMode: FORWARD
  OfflineForward:
    Servers:
    - lobby
```

### Scope modes

| Mode | Routing |
|---|---|
| `PLAYER_SERVER` | The player's backend. |
| `ALL_SERVERS` | All eligible backends. |
| `SERVERS` | Only the listed backends. |
| `ALL_EXCEPT` | All eligible backends except the listed entries. |

### Offline modes

| Mode | Behavior |
|---|---|
| `NONE` | Drops the proxy broadcast while the player is offline. |
| `QUEUE` | Sends it when the player logs in. |
| `FORWARD` | Selects an eligible backend forwarding target. In 7.1.1, queued vote delivery can still delay it; PR #1541 changes that only in development builds. |

`OfflineForward.Servers` is used only with `FORWARD` and is ignored where the selected scope already determines all targets.

## Backend versus proxy responsibilities

**Backend `VoteBroadcast`**

- Chooses message text and aggregation timing.
- Runs on each backend that processes the broadcast.
- Controls cooldown, batching, first-vote, and interval-summary formats.

**Proxy `ProxyBroadcast`**

- Chooses which backend or backends receive a proxy-wide broadcast.
- Controls offline routing.
- Does not replace the backend format configuration.

Before enabling both layers, test one vote online and one vote offline. Confirm that only the intended backends announce it and that Votifier forwarding is not creating a second vote path.

## Examples

Small standalone server:

```yaml
Type: EVERY_VOTE
```

Moderate-volume backend:

```yaml
Type: COOLDOWN_PER_PLAYER
Duration: 5m
```

High-volume network backend:

```yaml
Type: BATCH_WINDOW_PER_PLAYER
Duration: 30s
```

Proxy-wide routing:

```yaml
ProxyBroadcast:
  Enabled: true
  Scope:
    Mode: ALL_SERVERS
```
