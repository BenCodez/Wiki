---
title: All Reward Possibilities
description: VotingPlugin reward requirements, effects, and selection systems
published: true
date: 2026-08-14T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2025-08-30T22:17:56.051Z
---

# VotingPlugin Reward System Reference

VotingPlugin 7.1.1 uses its bundled AdvancedCore reward system. Reward syntax can be used in standalone reward files or inline under a VotingPlugin `Rewards` section.

Related guides:

- [Rewards overview](/VotingPlugin/Rewards)
- [Reward files](/VotingPlugin/Reward-File)
- [Where to set rewards](/VotingPlugin/Where-to-set-rewards)
- [AdvancedPriority](/VotingPlugin/AdvancedPriority-Rewards)
- [Item configuration](/VotingPlugin/Item-Configuration)
- [Reward examples](/VotingPlugin/Reward-Examples)

## Reward requirements

| Requirement | Purpose |
|---|---|
| `RequirePermission` / `Permission` | Require the default or configured permission. |
| `Worlds` / `BlackListedWorlds` | Allow or reject named worlds. |
| `Chance` | Independent chance out of 100. |
| `RewardType` | `ONLINE`, `OFFLINE`, or `BOTH`. |
| `JavascriptExpression` | Require a true expression when the JavaScript engine is enabled. |
| `VaultGroup` | Require a Vault permission group. |
| `RewardExpiration` | Expire delayed/queued reward delivery after the configured time. |
| `Server` / `BlockedServers` | Include or exclude proxy backend names. |
| `LocationDistance` | Require an online player within the configured location radius. |
| `Timed` / `Delayed` | Schedule or delay processing. |
| date/day settings | Restrict execution by date, weekday, day, or month. |
| `AdvancedWorld` | Select child rewards by world. |

Multiple requirements can be combined. Any requirement that needs a live player cannot pass without that online context.

## Money and experience

```yaml
Money: 1000
EXP: 100
EXPLevels: 3
```

Random money/experience ranges use the corresponding `Min`, `Max`, and supported rounding options. Money requires Vault and an economy provider.

## Items

```yaml
Items:
  Diamond:
    Material: DIAMOND
    Amount: 1
    Name: '&aSpecial Diamond'
    Lore:
    - 'Line 1'
    Enchants:
      unbreaking: 1
    Glow: false
```

See [Item Configuration](/VotingPlugin/Item-Configuration) for item metadata, skulls, custom models, potions, and supported custom-item integrations.

## Commands

```yaml
Commands:
- 'say %player% received a reward'

RandomCommand:
- 'say first command'
- 'say second command'

NumberCommand:
  Min: 1
  Max: 10
  Command: 'say Random number: %number%'
```

Commands normally run from the configured reward execution context. Validate player-only commands before using them for offline rewards.

## Potions

```yaml
Potions:
  ABSORPTION:
    Duration: 100
    Amplifier: 1
```

## Titles, boss bars, and action bars

```yaml
Title:
  Enabled: true
  Title: '&cTitle!'
  SubTitle: '&aSubTitle!'
  FadeIn: 10
  ShowTime: 50
  FadeOut: 10

BossBar:
  Enabled: true
  Message: '&aBoss bar message'
  Color: BLUE
  Style: SOLID
  Progress: 0.5
  Delay: 30

ActionBar:
  Message: '&cAction bar message'
  Delay: 30
```

> **PlaceholderAPI context in 7.1.1:** ordinary reward player messages pass through PlaceholderAPI. Reward `ActionBar.Message` and `BossBar.Message` do not have a dedicated PlaceholderAPI expansion step. With the release default JavaScript engine disabled, `%votingplugin_*%` expansion placeholders usually remain literal there, although reward-local placeholders such as `%player%` are still replaced. Enabling JavaScript can incidentally change that path, but should not be enabled solely as a PlaceholderAPI workaround.
{.is-info}

These outputs require the player to be online.

## Sound

```yaml
Sound:
  Enabled: true
  Sound: 'entity.player.levelup'
  Volume: 1.0
  Pitch: 1.0
```

## Particles

```yaml
Effect:
  Enabled: true
  Effect: 'EXPLOSION_NORMAL'
  Data: 1
  Particles: 10
  Radius: 5
```

## Fireworks

```yaml
Firework:
  Enabled: true
  Power: 2
  Colors:
  - BLUE
  FadeOutColor:
  - RED
  Trail: true
  Flicker: true
  Types:
  - BALL_LARGE
  Detonate: false
```

## Messages

```yaml
Messages:
  Player: '&aYou received a reward!'
  Broadcast: '&b%player% just voted!'
```

Proxy-wide broadcast routing is controlled separately; see [Vote Broadcast System](/VotingPlugin/Vote-Broadcast-System).

## Random item

```yaml
RandomItem:
  Diamond:
    Material: DIAMOND
    Amount: 1
  Iron:
    Material: IRON_INGOT
    Amount: 10
```

## Random child reward

```yaml
AdvancedRandomReward:
  First:
    Commands:
    - 'say first reward'
  Second:
    Commands:
    - 'say second reward'
```

## Random reward files with fallback

```yaml
Random:
  Chance: 40
  PickRandom: true
  Rewards:
  - RewardA
  FallBack:
  - RewardB
```

## AdvancedPriority

Runs the first child whose requirements pass:

```yaml
AdvancedPriority:
  VIP:
    RequirePermission: true
    Permission: 'server.vip'
    Money: 100
  Default:
    Money: 25
```

Chance entries are ordered independent rolls, not weights. See [AdvancedPriority Rewards](/VotingPlugin/AdvancedPriority-Rewards).

## SpecialChance

Selects by numeric weight:

```yaml
SpecialChance:
  5:
    Commands:
    - 'say weight 5'
  15:
    Commands:
    - 'say weight 15'
  30:
    Commands:
    - 'say weight 30'
  50:
    Commands:
    - 'say weight 50'
```

Each entry's probability is its weight divided by the total weight.

## Lucky

```yaml
Lucky:
  '10':
    Money: 100
  '50':
    Money: 1000
```

Check the generated/default reward examples for the exact Lucky behavior used by the installed build before relying on a complex distribution.

## JavaScript

```yaml
Javascript:
  Enabled: true
  Expression: "BukkitPlayer.hasPermission('vip')"
  TrueRewards:
    Money: 100
  FalseRewards:
    Money: 25
```

JavaScript execution is disabled by default in VotingPlugin 7.1.1. Enabling it expands the attack surface of configuration and should be limited to trusted, reviewed expressions.

## Choice rewards

```yaml
EnableChoices: true
Choices:
  Diamond:
    DisplayItem:
      Name: '&c3 Diamonds'
      Material: DIAMOND
      Amount: 3
    Rewards:
      Items:
        Diamond:
          Material: DIAMOND
          Amount: 3
  Iron:
    DisplayItem:
      Name: '&c15 Iron Ingots'
      Material: IRON_INGOT
      Amount: 15
    Rewards:
      Items:
        Iron:
          Material: IRON_INGOT
          Amount: 15
```

Choice GUIs require the player to be online. Always test fallback/offline behavior before using them for queued proxy votes.
