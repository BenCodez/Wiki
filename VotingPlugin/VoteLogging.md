---
title: Vote Logging
description: 
published: true
date: 2026-02-14T19:12:57.372Z
tags: 
editor: markdown
dateCreated: 2026-02-14T19:12:02.555Z
---

# VoteLogging

VoteLogging is the unified logging system in **VotingPlugin** that records vote-related activity to storage (**MySQL only**).  
It is intended for auditing, analytics, debugging, and tracking reward/vote activity across your network.

---

# Overview

VoteLogging works by listening to internal vote/reward events and writing structured entries to a storage backend.

Common logging listeners include:

- `PlayerPostVoteLoggerListener`
- `PlayerSpecialRewardLoggerListener`
- `VoteMilestoneVoteLogListener`
- `VoteShopPurchaseLoggerListener`

When MySQL logging is enabled, entries are written through the MySQL table handler (for example: `VoteLogMysqlTable`).

---

# What Gets Logged

VoteLogging currently logs the following (MySQL only):

- Votes
- Vote shop purchases
- **Top Voter** rewards
- **VoteMilestone** rewards
- **VoteStreaks** (new system; not the legacy/old version)

---

# Configuration

VoteLogging can be configured on both backend servers and proxies.

## Backend configuration (Config.yml)

```yaml
###########################################
# Vote Logging
# Optional logging of votes and rewards (MySQL only)
###########################################

# Currently logs:
# - Votes
# - Vote shop purchases
# - Top voter rewards
# - VoteMilestones rewards
# - VoteStreaks (not the old version)

VoteLogging:
  # If enabled, will log votes in MySQL
  # Enable on backend servers to access commands
  Enabled: false
  # Purge votes older than X days
  # Set to -1 to disable automatic purging
  PurgeDays: 30
  UseMainMySQL: true
  # MySQL settings only used if above is false
```

### Field reference

- **Enabled**: Master toggle for VoteLogging on this server.
- **PurgeDays**: Automatically deletes vote log records older than this many days.
  - Set to `-1` to disable automatic purging.
- **UseMainMySQL**: If `true`, VoteLogging uses the main plugin MySQL settings.
  - If `false`, VoteLogging uses the MySQL settings defined under VoteLogging (if present).

---

## Proxy configuration

```yaml
VoteLogging:
  # If enabled, will log votes in mysql
  # Enable on backend servers to access commands
  Enabled: false
  # Purge votes older than X days
  # Set to -1 to disable automatic purging
  PurgeDays: 30
  UseMainMySQL: true
  # Mysql settings only used if above is false
```

> Tip: If you want logs available for commands that query VoteLogging, enable VoteLogging on the backend server(s) that run those commands.

---

# Operational Notes

## Purging behavior
If **PurgeDays** is enabled (not `-1`), the system will periodically remove older log entries from MySQL to keep the database size manageable.

## Recommended setup
- Enable VoteLogging on your backend server(s) where you want command access.
- Use `UseMainMySQL: true` unless you have a specific reason to isolate VoteLogging into a separate database.

---

# Disabling VoteLogging

To disable completely:

```yaml
VoteLogging:
  Enabled: false
```

This stops VoteLogging from writing any new entries.
