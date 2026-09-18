---
title: Reward File
description: Create reusable VotingPlugin reward YAML files
published: true
date: 2026-08-14T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2025-08-30T22:18:22.178Z
---

# Reward Files

![Example VotingPlugin reward-file configuration](https://i.imgur.com/hKOAj4Z.png)

Reusable reward files are stored in:

```text
plugins/VotingPlugin/Rewards
```

Reference a file by its name without `.yml`.

## Basic example

`plugins/VotingPlugin/Rewards/Thanks.yml`:

```yaml
Money: 100
Commands:
- 'say %player% voted'
Messages:
  Player: '&aThanks for voting!'
```

Reference it from a VotingPlugin reward location:

```yaml
Rewards:
- Thanks
```

A reward file starts directly with reward keys. Do not wrap the entire file in another `Rewards:` section.

## Common requirements

```yaml
RequirePermission: true
Permission: 'server.vip'
Worlds:
- world
Chance: 25
RewardType: ONLINE
```

Requirements can be combined. Online-only requirements and effects need a live player context.

## Common effects

Reward files can provide:

- items and random item amounts;
- economy money through Vault;
- experience and levels;
- console or player commands;
- potion effects;
- titles, boss bars, and action bars;
- sounds, particles, and fireworks;
- player messages and broadcasts;
- delayed or scheduled child rewards;
- ordered, random, weighted, or choice-based child rewards.

Use [All Reward Possibilities](/VotingPlugin/All-Reward-Possibilities) for syntax and [AdvancedPriority Rewards](/VotingPlugin/AdvancedPriority-Rewards) for first-match selection.

## Offline delivery

VotingPlugin may queue a reward until the player is available. Avoid assuming that online-only effects, permissions, worlds, inventories, GUI choices, action bars, or player commands can run identically while offline. Test the actual proxy/standalone delivery path.

Do not edit generated files under `Rewards/DirectlyDefined`; change the inline source configuration instead.
