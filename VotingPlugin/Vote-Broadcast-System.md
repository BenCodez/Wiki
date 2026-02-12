---
title: Vote Broadcast System
description: 
published: true
date: 2026-02-12T02:01:20.209Z
tags: 
editor: markdown
dateCreated: 2026-02-12T02:01:20.209Z
---

# Vote Broadcast System

The **Vote Broadcast System** controls how vote messages are announced
to players.

It replaces the legacy broadcast behavior with a flexible system
supporting:

-   Per-vote broadcasts
-   Cooldowns
-   Vote batching
-   First-vote-of-day messages
-   Global interval summaries
-   Proxy-wide broadcast routing

Configured in:

-   `Config.yml` (Backend servers)
-   `bungeeconfig.yml` / proxy config (Proxy-side)

------------------------------------------------------------------------

# Backend VoteBroadcast (config.yml)

``` yaml
VoteBroadcast:
  Type: EVERY_VOTE
  Duration: 2m
  MaxSitesListed: 0
  Format:
    BroadcastMsg: '&6[&4Vote&6] &aThanks &e%player% &afor voting on &e%site%&a!'
    Header: '&6[&4Vote&6] &a%player% voted on &e%sites_count% &asites:'
    ListLine: '&7 - &e%site%'
```

## Broadcast Types

### NONE

Disables vote broadcasts entirely.

### EVERY_VOTE

Broadcast every vote (including offline processed votes).

### EVERY_VOTE_ONLINE_ONLY

Broadcast only if the voting player is online.

### COOLDOWN_PER_PLAYER

Broadcast at most once per Duration per player.

### BATCH_WINDOW_PER_PLAYER

Collect votes during Duration and broadcast once.

-   1 vote → BroadcastMsg
-   2+ votes → Header + ListLine

### FIRST_VOTE_OF_DAY

Broadcast only the first vote per calendar day per player.

### INTERVAL_SUMMARY_GLOBAL

Every Duration, broadcast a global vote summary.

------------------------------------------------------------------------

# Duration Format

Supported units:

-   s (seconds)
-   m (minutes)
-   h (hours)
-   d (days)
-   w (weeks)

Example:

    30s
    5m
    1h
    1d

Months are NOT supported.

------------------------------------------------------------------------

# Format Placeholders

Common:

-   %player%
-   %site%
-   %sites_count%
-   %sites%
-   %reason%

Interval-only:

-   %players%
-   %numberofplayers%
-   %numberofsites%

------------------------------------------------------------------------

# Proxy Broadcast System (bungeeconfig.yml)

Proxy broadcasts are controlled separately.

``` yaml
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

## Scope Modes

-   PLAYER_SERVER → Only the server the player is on
-   ALL_SERVERS → All backend servers
-   SERVERS → Only specific listed servers
-   ALL_EXCEPT → All except listed servers

## OfflineMode

Controls what happens if the voting player is offline:

-   NONE → Drop broadcast
-   QUEUE → Send when player logs in
-   FORWARD → Immediately forward to a backend server

### OfflineForward.Servers

Used only when OfflineMode = FORWARD.

Example:

``` yaml
OfflineForward:
  Servers:
  - lobby
```

------------------------------------------------------------------------

# Backend vs Proxy Broadcast Behavior

Backend VoteBroadcast: - Controls message formatting and timing logic -
Runs per-server

ProxyBroadcast: - Controls where broadcasts are routed across the
network - Determines which backend server(s) receive the broadcast

Recommended setup for networks:

-   Use MySQL shared storage
-   Enable ProxyBroadcast
-   Use ALL_SERVERS scope
-   Use BATCH_WINDOW_PER_PLAYER or COOLDOWN_PER_PLAYER on backend

------------------------------------------------------------------------

# Recommended Configurations

## Small Server

``` yaml
Type: EVERY_VOTE
```

## Medium Server

``` yaml
Type: COOLDOWN_PER_PLAYER
Duration: 5m
```

## Large Network

Backend:

``` yaml
Type: BATCH_WINDOW_PER_PLAYER
Duration: 30s
```

Proxy:

``` yaml
ProxyBroadcast:
  Enabled: true
  Scope:
    Mode: ALL_SERVERS
```

# Summary

The new Vote Broadcast system provides:

-   Spam protection
-   Vote batching
-   First vote announcements
-   Global summaries
-   Proxy routing control
-   Offline handling options
-   Network-wide broadcast scope control

It is designed for both standalone servers and large proxy networks.