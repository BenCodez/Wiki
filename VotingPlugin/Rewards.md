---
title: Rewards
description: Choose inline rewards or reusable reward files
published: true
date: 2026-08-14T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2025-08-30T22:18:22.882Z
---

# Rewards

VotingPlugin uses the bundled AdvancedCore reward system. The same reward effects and requirements can be used inline in VotingPlugin configuration or in reusable files under `plugins/VotingPlugin/Rewards`.

Start with:

- [Where to Set Rewards](/VotingPlugin/Where-to-set-rewards)
- [All Reward Possibilities](/VotingPlugin/All-Reward-Possibilities)
- [Reward File Format](/VotingPlugin/Reward-File)
- [AdvancedPriority Rewards](/VotingPlugin/AdvancedPriority-Rewards)

## Inline rewards

Most VotingPlugin sections already provide a `Rewards` location:

```yaml
Rewards:
  Money: 100
  Commands:
  - 'say %player% voted'
  Messages:
    Player: '&aThanks for voting!'
```

VotingPlugin can create internal files in `Rewards/DirectlyDefined` so inline rewards can be queued for later delivery. Do not edit that generated directory; edit the original configuration section.

Set a reward section to `{}` or `[]` when the surrounding option supports an empty reward and you want it disabled.

## Reusable reward files

Create `plugins/VotingPlugin/Rewards/MyReward.yml`:

```yaml
Money: 100
Commands:
- 'say %player% voted'
```

Reference the file without `.yml`:

```yaml
Rewards:
- MyReward
```

A standalone reward file starts with reward keys such as `Money`, `Commands`, `Items`, or `AdvancedPriority`. It does **not** need an extra top-level `Rewards:` wrapper.

Multiple files can be listed:

```yaml
Rewards:
- EconomyReward
- CosmeticReward
```

## Nested and selection rewards

Some advanced reward keys contain child rewards. For example:

```yaml
AdvancedPriority:
  VIP:
    RequirePermission: true
    Permission: 'server.vip'
    Money: 200
  Default:
    Money: 50
```

`AdvancedPriority` runs only its first matching child. Other selection and random systems have different semantics; do not treat chance values as weights unless that feature explicitly documents weighted selection.

## Placeholders and player context

Reward-local placeholders such as `%player%`, `%money%`, `%exp%`, and date placeholders are replaced where supported. PlaceholderAPI expansion depends on the output path: ordinary player messages expand PlaceholderAPI values, while reward action bars and boss bars do not have a dedicated PlaceholderAPI pass under the default 7.1.1 JavaScript setting. See [PlaceholderAPI Support](/VotingPlugin/PlaceHolderAPI-placeholders).

Requirements and effects that need an online Bukkit player cannot run with the same behavior while the player is offline. Test both online votes and queued/offline delivery when using permissions, worlds, GUI choices, action bars, boss bars, or player-executed commands.
