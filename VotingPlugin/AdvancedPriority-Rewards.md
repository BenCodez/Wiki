---
title: AdvancedPriority Rewards
description: Select the first matching reward from an ordered list
published: true
date: 2026-08-14T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2026-02-16T22:48:52.659Z
---

# AdvancedPriority Rewards

`AdvancedPriority` is available in VotingPlugin 7.1.1 through its bundled AdvancedCore reward system. It evaluates child rewards in YAML order and runs the **first** child whose requirements pass.

Use it for mutually exclusive rank tiers, ordered chance attempts, or a final fallback.

## Important syntax difference

A standalone reward file starts directly with `AdvancedPriority`:

```yaml
# plugins/VotingPlugin/Rewards/MyReward.yml
AdvancedPriority:
  VIP:
    RequirePermission: true
    Permission: 'server.vip'
    Commands:
    - 'give %player% diamond 3'
  Default:
    Money: 50
```

Reference it without `.yml`:

```yaml
Rewards:
- MyReward
```

An inline reward is already inside a plugin configuration's `Rewards` section:

```yaml
VoteSites:
  ExampleSite:
    Rewards:
      AdvancedPriority:
        VIP:
          RequirePermission: true
          Permission: 'server.vip'
          Money: 100
        Default:
          Money: 50
```

Do **not** add an extra top-level `Rewards:` wrapper inside a standalone reward file. Conversely, do not omit the surrounding `Rewards:` key when defining the logic inline in `VoteSites.yml`, `SpecialRewards.yml`, or another VotingPlugin section.

## Permission tiers

```yaml
AdvancedPriority:
  Owner:
    RequirePermission: true
    Permission: 'server.owner'
    Money: 500
  VIP:
    RequirePermission: true
    Permission: 'server.vip'
    Money: 200
  Default:
    Money: 50
```

A player with both permissions receives only `Owner` because it appears first. Put the most specific/exclusive requirements first and an unrestricted fallback last.

A negated permission can be written as `Permission: '!server.vip'` when that requirement is appropriate.

## Ordered chance attempts

Each `Chance` is a separate roll made only if earlier entries fail:

```yaml
AdvancedPriority:
  First:
    Chance: 60
    Money: 100
  Second:
    Chance: 30
    Money: 50
  Fallback:
    Money: 10
```

The effective results are:

- `First`: 60%
- `Second`: 40% × 30% = 12%
- `Fallback`: 40% × 70% = 28%

These are **not weighted entries**. Use `SpecialChance` or the appropriate random-reward feature when you need one weighted selection instead of ordered independent checks.

## Item example

```yaml
AdvancedPriority:
  Rare:
    Chance: 5
    Items:
      Diamond:
        Material: DIAMOND
        Amount: 1
  Common:
    Chance: 50
    Items:
      Iron:
        Material: IRON_INGOT
        Amount: 10
  Fallback:
    Items:
      Dirt:
        Material: DIRT
        Amount: 64
```

The iron roll is reached only after the diamond roll fails.

## Sibling rewards are not fallbacks

In an inline configuration, rewards placed beside `AdvancedPriority` are independent and also run:

```yaml
Rewards:
  AdvancedPriority:
    VIP:
      RequirePermission: true
      Permission: 'server.vip'
      Money: 100
    Default:
      Money: 25
  Commands:
  - 'say %player% received a vote reward'
```

The command runs after the `AdvancedPriority` selection. Put a fallback **inside** `AdvancedPriority` when it should run only if every earlier child fails.

## Requirements and execution context

Each child can use normal reward requirements and effects, including permission, world, chance, online/offline, server restrictions, items, money, commands, and messages. Requirements that depend on a live player cannot pass while the reward is processed without the required online context.

Keep child names unique, preserve intentional YAML order, and test one player for every branch before deploying a complex reward.
