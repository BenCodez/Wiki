---
title: AdvancedPriority Rewards
description: 
published: true
date: 2026-02-16T22:48:52.659Z
tags: 
editor: markdown
dateCreated: 2026-02-16T22:48:52.659Z
---

# AdvancedPriority within Rewards

## Overview

`AdvancedPriority` is an advanced reward-selection system available in **AdvancedCore** and used by plugins like **VotingPlugin**.  It allows you to create a list of **sub‑rewards** under a single reward entry.  When the reward is processed, the system walks through these sub‑rewards in order and executes the **first** one that meets all of its conditions.  Conditions can include permissions, chance percentages and any other reward requirement supported by AdvancedCore.  This design makes it easy to offer different rewards based on a player’s rank or luck without creating multiple separate reward files.  The documentation emphasises that `AdvancedPriority` checks rewards in order of *rarest* to *most likely* and stops at the first match【436168832069236†L192-L195】.

### How it works

1. You define a primary reward (either in a reward file or inline in a config like `VoteSites.yml`) and include an `AdvancedPriority` section inside its `Rewards` block.
2. Each key under `AdvancedPriority` becomes a *sub‑reward*.  Give each sub‑reward a unique name.
3. Assign any requirements to these sub‑rewards (permissions, chance, JavaScript expressions, etc.).  If the first sub‑reward fails its requirements, the next one is evaluated.  This continues until a sub‑reward succeeds.
4. If none of the sub‑rewards succeed, you can provide a **fallback** reward as the last entry so the player still receives something.

The system lets you structure rewards so that the most exclusive or rare outcome is attempted first, followed by more common ones【436168832069236†L192-L195】.  This avoids duplicating reward files and keeps all logic in one place.

## Permission‑based example

You can use `AdvancedPriority` to give different rewards based on permissions.  In the example below, the plugin will check whether the player has `permhere`; if so, it runs **Reward1** and stops.  If not, it checks for `permhere2`.  If neither permission is present, the normal reward (money) is given【436168832069236†L199-L214】.

```yaml
Rewards:
  AdvancedPriority:
    # first sub‑reward: only runs if the player has permhere
    Reward1:
      RequirePermission: true
      Permission: 'permhere'
      Commands:
        - say Reward1
    # second sub‑reward: requires a different permission
    Reward2:
      RequirePermission: true
      Permission: 'permhere2'
      Commands:
        - say Reward2
    # fallback: give money if no permission matched
    RewardNormal:
      Money: 100
```

Use this pattern to offer rank‑specific or permission‑based perks without needing separate reward files.  If you prefer to prevent a reward unless the player lacks a permission, prefix the permission with an exclamation mark (`Permission: '!permhere'`).

## Chance‑based example

`AdvancedPriority` also supports probabilistic rewards.  You can assign a **chance** (out of 100) to each sub‑reward.  The system will evaluate the sub‑rewards in order: if the first one fails its chance roll, the next one is attempted【436168832069236†L218-L231】.

```yaml
Rewards:
  AdvancedPriority:
    Reward1:
      Chance: 60
      Commands:
        - say Reward1
    Reward2:
      Chance: 30
      Commands:
        - say Reward2
    # fallback runs if neither chance succeeded
    RewardNormal:
      Money: 100
```

In this example, there is a 60 % chance to get the first reward, a 30 % chance to get the second reward, and if both fail the player receives `RewardNormal`.  Order matters: place the highest chance later so rare rewards are evaluated first.

## Item‑based and fallback example

You can also give different items with varying chances.  This example demonstrates three tiers: a rare diamond, a common iron ingot and a fallback dirt reward.  Each sub‑reward includes its own `Items` section and `Chance`【436168832069236†L233-L252】.

```yaml
AdvancedPriority:
  Reward1:
    Items:
      Item1:
        Material: DIAMOND
        Amount: 1
    Chance: 5
  Reward2:
    Items:
      Item1:
        Material: IRON_INGOT
        Amount: 10
    Chance: 50
  Fallback:
    Items:
      Item1:
        Material: DIRT
        Amount: 64
```

The player first has a 5 % chance to receive the diamond, then a 50 % chance for iron.  If both chances fail, the fallback dirt is delivered.  You can extend this pattern with additional sub‑rewards.

## Rarity tiers example

If you want to weight rewards based on rarity without specifying low percentages manually, you can arrange the sub‑rewards from rarest to most common.  The following example shows a **Rarest**, **SecondRarest** and **Fallback** tier【436168832069236†L255-L276】.

```yaml
AdvancedPriority:
  Rarest:
    Chance: 1
    Items:
      item:
        Material: DIAMOND
        Amount: 5
    Messages:
      Player: 'You got rare item'
  SecondRarest:
    Chance: 5
    Items:
      item:
        Material: DIAMOND
        Amount: 1
    Messages:
      Player: 'You got second rare item'
  Fallback:
    Items:
      item:
        Material: DIRT
        Amount: 1
    Messages:
      Player: 'You got normal item'
```

Because the rewards are evaluated in order, players will only reach the `SecondRarest` or `Fallback` tiers if the rarer rewards fail their chance roll.  This structure is ideal for loot‑crate style rewards.

## Using `AdvancedPriority` in reward files vs. inline rewards

`AdvancedPriority` can be placed in **reward files** (YAML files stored in the `Rewards` folder of AdvancedCore) or directly inside the `Rewards` section of a configuration file like `VoteSites.yml`.  Here are two common approaches:

### Reward file example

Create a YAML file (e.g. `MyReward.yml`) inside the `Plugins/AdvancedCore/Rewards` folder and add an `AdvancedPriority` section.  You can then reference this reward by its file name (without the extension) from other plugins.

```yaml
# MyReward.yml
Rewards:
  AdvancedPriority:
    VIPReward:
      RequirePermission: true
      Permission: 'server.vip'
      Items:
        Diamond:
          Material: DIAMOND
          Amount: 3
    NormalReward:
      Money: 50
```

### Inline configuration example

You may also define `AdvancedPriority` directly within a plugin configuration, such as `VoteSites.yml` in VotingPlugin.  The syntax is the same; place `AdvancedPriority` under the `Rewards` section of the site configuration.  The following snippet shows a vote site that gives a diamond if the 50 % chance succeeds, then an emerald with a 20 % chance, otherwise a fallback message【436168832069236†L218-L231】.

```yaml
VoteSites:
  ExampleSite:
    Enabled: true
    ServiceSite: 'ExampleSite.com'
    VoteURL: 'https://example.com/vote'
    Rewards:
      AdvancedPriority:
        Reward1:
          Chance: 50
          Items:
            Diamond:
              Material: DIAMOND
              Amount: 1
        Reward2:
          Chance: 20
          Items:
            Emerald:
              Material: EMERALD
              Amount: 1
        Fallback:
          Messages:
            Player: 'Better luck next time!'
      # You can still define other rewards here; they run after AdvancedPriority
      Items:
        item1:
          Material: COAL
          Amount: 1
```

## Best practices

* **Order matters** – always list the rarest or most exclusive rewards first and put common or fallback rewards last【436168832069236†L192-L195】.
* **Unique names** – ensure each sub‑reward name under `AdvancedPriority` is unique to avoid configuration conflicts.
* **Include a fallback** – adding a fallback reward ensures players always receive something if earlier rewards fail.
* **Combine with requirements** – you can combine chance with other requirements such as permissions, world restrictions or JavaScript expressions.  If any requirement fails, the system moves on to the next reward.
* **Use `&` color codes** – when adding messages in reward files, remember to use Minecraft color codes (e.g. `&a` for green) if you want colored text.

## Conclusion

`AdvancedPriority` provides a flexible way to manage complex reward logic within AdvancedCore and associated plugins.  By listing sub‑rewards in order, you can create tiered loot tables, rank‑based rewards and fallback strategies without duplicating reward files.  Use the examples above as a starting point and adjust the chances, permissions or item lists to fit your server’s needs.