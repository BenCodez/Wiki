---
title: Vote Broadcast System
description:
published: true
date: 2026-08-14T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2026-02-12T02:01:20.209Z
---

# Vote Broadcast System

The **Vote Broadcast System** controls how vote messages are announced to players.

It supports:

- Per-vote broadcasts
- Cooldowns
- Vote batching
- First-vote-of-day messages
- Global interval summaries
- Proxy-wide broadcast routing

Configured in:

- `Config.yml` on backend servers
- `bungeeconfig.yml` on the proxy

---

## Backend `VoteBroadcast` (`Config.yml`)

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

### Broadcast Types

#### `NONE`

Disables vote broadcasts entirely.

#### `EVERY_VOTE`

Broadcasts every vote, including an offline vote when it is eventually processed.

#### `EVERY_VOTE_ONLINE_ONLY`

Broadcasts only if the voting player is online.

#### `COOLDOWN_PER_PLAYER`

Broadcasts at most once per `Duration` for each player.

#### `BATCH_WINDOW_PER_PLAYER`

Collects votes during `Duration` and broadcasts once.

- 1 vote → `BroadcastMsg`
- 2 or more votes → `Header` + `ListLine`

#### `FIRST_VOTE_OF_DAY`

Broadcasts only the first vote per calendar day for each player.

#### `INTERVAL_SUMMARY_GLOBAL`

Broadcasts a global vote summary every `Duration`.

---

## Duration Format

Supported units:

- `s` (seconds)
- `m` (minutes)
- `h` (hours)
- `d` (days)
- `w` (weeks)

Examples:

```text
30s
5m
1h
1d
```

Months are not supported.

---

## Format Placeholders

Common:

- `%player%`
- `%site%`
- `%sites_count%`
- `%sites%`
- `%reason%`

Interval-only:

- `%players%`
- `%numberofplayers%`
- `%numberofsites%`

---

## Proxy Broadcast System (`bungeeconfig.yml`)

Proxy broadcasts are controlled separately.

> **Availability:** The proxy broadcast settings below are present in the latest public release, **7.1.1**. In 7.1.1, an offline vote that is being queued can delay an `OfflineMode: FORWARD` broadcast until the vote itself is delivered. Immediate forwarding independent of queued vote delivery is available only in development builds containing [VotingPlugin PR #1541](https://github.com/BenCodez/VotingPlugin/pull/1541), merged after 7.1.1.
{.is-warning}

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

### Scope Modes

- `PLAYER_SERVER` → only the server the player is on
- `ALL_SERVERS` → all backend servers
- `SERVERS` → only specifically listed servers
- `ALL_EXCEPT` → all except the listed servers

### `OfflineMode`

Controls what happens if the voting player is offline:

- `NONE` → drop the broadcast
- `QUEUE` → send when the player logs in
- `FORWARD` → select a backend forwarding target. In 7.1.1, queued vote delivery can also delay this broadcast; development builds containing PR #1541 forward it independently.

#### `OfflineForward.Servers`

Used only when `OfflineMode: FORWARD`.

```yaml
OfflineForward:
  Servers:
  - lobby
```

---

## Backend vs. Proxy Broadcast Behavior

**Backend `VoteBroadcast`:**

- Controls message formatting and timing logic.
- Runs on each backend that processes the broadcast.

**Proxy `ProxyBroadcast`:**

- Controls where broadcasts are routed across the network.
- Determines which backend server or servers receive the broadcast.
- Does not replace the backend formatting configuration.

A common network setup uses shared SQL storage, enables `ProxyBroadcast`, selects the required scope, and uses `BATCH_WINDOW_PER_PLAYER` or `COOLDOWN_PER_PLAYER` on backends. Test one online and one offline vote to confirm that only the intended servers announce it.

---

## Example Configurations

### Small Server

```yaml
Type: EVERY_VOTE
```

### Medium Server

```yaml
Type: COOLDOWN_PER_PLAYER
Duration: 5m
```

### Large Network

Backend:

```yaml
Type: BATCH_WINDOW_PER_PLAYER
Duration: 30s
```

Proxy:

```yaml
ProxyBroadcast:
  Enabled: true
  Scope:
    Mode: ALL_SERVERS
```

## Summary

The Vote Broadcast system provides:

- Spam protection
- Vote batching
- First-vote announcements
- Global summaries
- Proxy routing control
- Offline handling options
- Network-wide broadcast scope control

It is designed for both standalone servers and proxy networks.
