---
title: Performance Settings
description: Tune VotingPlugin database, background task, top voter, and skull settings
published: true
date: 2025-11-07T02:04:13.072Z
tags:
editor: markdown
dateCreated: 2025-08-30T22:18:19.128Z
---

# VotingPlugin Performance Settings

VotingPlugin's defaults are suitable for most servers. Change one group of
settings at a time, restart when a setting requires it, and compare timings
before and after the change.

## Database connections

```yaml
Database:
  MaxConnections: 1
```

One connection is the default. A second connection may help a busy network,
but increasing the pool without evidence can add database load without
improving throughput.

## Top voter data

Only load the totals that your commands, placeholders, signs, or awards use:

```yaml
LoadTopVoter:
  AllTime: true
  Monthly: true
  Weekly: false
  Daily: false

# -1 removes the limit
MaxiumNumberOfTopVotersToLoad: 1000
```

`LoadTopVoter` categories must be enabled for their matching top voter views
and awards. Reducing `MaxiumNumberOfTopVotersToLoad` can limit work on servers
with a very large user table.

## Optional processing

```yaml
# Requires a restart when changed
PerSiteCoolDownEvents: false

# Controls only the legacy VoteStreak system
UseVoteStreaks: true

# Stores highest/best vote totals
UseHighestTotals: true

# Parses JavaScript in PlaceholderAPI placeholders
UseJavascriptPlaceholders: false
```

- Enable `PerSiteCoolDownEvents` only if you use per-site cooldown events or
  rewards.
- `UseVoteStreaks` does **not** disable the current `VoteStreaks` system in
  `SpecialRewards.yml`; it controls only the legacy `VoteStreak` system.
- Disable `UseHighestTotals` only if you do not use best/highest totals.
- Leave `UseJavascriptPlaceholders` disabled unless a placeholder requires
  JavaScript processing.

## Cooldown and interaction listeners

```yaml
DisableCoolDownCheck: false
DisableInteractEvent: false
```

Setting `DisableCoolDownCheck: true` disables cooldown checking. Do not use it
if you rely on cooldown-end behavior.

Setting `DisableInteractEvent: true` disables VotingPlugin's player-interaction
listener. It can reduce unnecessary listener work when you do not use features
that depend on interaction, such as VotingPlugin signs or heads.

## Background updates

```yaml
AlwaysUpdate: false
UpdateWithPlayersOnlineOnly: false
DelayBetweenUpdates: 3m
ExtraBackgroundUpdate: false
```

| Setting | Guidance |
|---|---|
| `AlwaysUpdate` | Leave `false` so background work runs only when needed |
| `UpdateWithPlayersOnlineOnly` | Set `true` if delayed updates while the server is empty are acceptable |
| `DelayBetweenUpdates` | Uses a duration such as `3m` or `10m`; longer values reduce frequency but delay visible updates |
| `ExtraBackgroundUpdate` | Leave `false` unless additional cross-server player checks are required |

Do not omit the unit from `DelayBetweenUpdates`.

## Tab completion

```yaml
DisableAdvancedTab: false
```

Setting this to `true` disables permission checks during advanced tab
completion. The possible improvement is small, so change it only when tab
completion is a measured problem.

## Player skull caching

```yaml
PreloadSkulls: true
SkullLoadDelay: 4s
```

`PreloadSkulls: true` caches VoteTop skulls ahead of use. Setting it to `false`
loads and caches skulls as they are requested instead. Choose based on whether
you prefer startup preloading or on-demand loading.

`SkullLoadDelay` is a duration. Increasing it slows requests and may help when
the configured skull profile service rate-limits the server.

There is no `LoadSkulls` setting in the current configuration.

## Placeholder settings

See the
[PlaceholderAPI placeholders guide](https://github.com/BenCodez/VotingPlugin/wiki/PlaceHolderAPI-placeholders)
for cache, `_process`, and `_nocache` behavior.

## Suggested starting point

```yaml
Database:
  MaxConnections: 1

LoadTopVoter:
  AllTime: true
  Monthly: true
  Weekly: false
  Daily: false

UseJavascriptPlaceholders: false
AlwaysUpdate: false
DelayBetweenUpdates: 3m
ExtraBackgroundUpdate: false
DisableAdvancedTab: false
PreloadSkulls: true
SkullLoadDelay: 4s
```

This is a starting point, not a universal optimum. Features that a server
actively uses should not be disabled solely for theoretical performance gains.
Use `/av status`, `/av debug`, server timings, and database metrics to confirm
whether a change actually helps.
