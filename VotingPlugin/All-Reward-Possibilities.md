---
title: All Reward Possibilities
description: 
published: true
date: 2025-11-07T02:15:45.341Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:17:56.051Z
---

# 🎁 VotingPlugin Reward System — Complete Reference

Most reward types and logic can be configured easily through `/av gui`.  
For manual editing, examples are provided here:  
- [ExampleBasic.yml](https://github.com/BenCodez/AdvancedCore/blob/master/AdvancedCore/src/main/resources/Rewards/ExampleBasic.yml)  
- [ExampleAdvanced.yml](https://github.com/BenCodez/AdvancedCore/blob/master/AdvancedCore/src/main/resources/Rewards/ExampleAdvanced.yml)  
- [Reward Examples (Wiki)](https://wiki.bencodez.com/en/VotingPlugin/Reward-Examples)

---

## ⚙️ Reward Requirements

Define when a reward should run. Multiple can be combined together.

| Requirement | Description |
|--------------|-------------|
| **Permission** | Requires specific permission. (`AdvancedCore.Reward.<RewardName>` by default) |
| **World / BlackListedWorlds** | Restrict or block execution by world name. |
| **Chance** | Chance out of 100 (e.g., `Chance: 40`). |
| **Online / Offline / Both (RewardType)** | Defines if reward runs only for online, offline, or both players.<br>`ONLINE` → Player must be online at the time.<br>`OFFLINE` → Only given if the player is offline.<br>`BOTH` → Default behavior. |
| **JavascriptExpression** | Expression must return `true` to run. |
| **VaultGroup** | Requires player to be in Vault permission group. |
| **RewardExpiration** | Reward expires if not claimed in time (in minutes). |
| **Server / BlockedServers** | Restrict to specific servers or exclude some (Bungee/Velocity setups). |
| **LocationDistance** | Only run if player is within distance of given coordinates. |
| **Timed** | Trigger reward at a specific time of day (hour/minute). |
| **Delayed** | Delay the reward by seconds or ticks. |
| **Date / DayOfMonth** | Trigger reward on specific days, weekdays, or months. |
| **WorldGuardRegion** | (If supported) Limit to specific regions. |
| **AdvancedWorld** | Define rewards per world. |

---

## 🧱 Reward / Effect Types

### 🪙 Money

```yaml
    Money: 1000
    # Or random range:
    # Money:
    #   Min: 100
    #   Max: 3000
    #   Round: false
```

> Requires Vault. Negative values remove money.

---

### 🧠 Experience (EXP / EXPLevels)

```yaml
    EXP: 100
    EXPLevels: 3
    # Random EXP range:
    # EXP:
    #   Min: 100
    #   Max: 1000
    # EXPLevels:
    #   Min: 3
    #   Max: 7
```

---

### 🎒 [Items](https://wiki.bencodez.com/en/VotingPlugin/Item-Configuration)

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
        # ItemFlags, SkullURL, ItemsAdder, CustomModelData, etc. also supported.
```

> Supports chance, random amount ranges, custom models, ItemsAdder/Nexo compatibility, potions, and custom names.

---

### 🧾 Commands

```yaml
    Commands:
      - 'say %player% received a reward!'
    # Random command:
    RandomCommand:
      - 'say random1'
      - 'say random2'
    # NumberCommand:
    NumberCommand:
      Min: 1
      Max: 10
      Command: 'say Random number: %number%'
```

> Commands can run as **console** or **player** and support placeholder parsing.

---

### 🧪 Potions

```yaml
    Potions:
      ABSORPTION:
        Duration: 100
        Amplifier: 1
```

---

### 🏷️ Titles / BossBars / ActionBars

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
      Message: '&aBossbar Message'
      Color: BLUE
      Style: SOLID
      Progress: 0.5
      Delay: 30

    ActionBar:
      Message: '&cThis is an actionbar!'
      Delay: 30
```

---

### 🔊 Sound

```yaml
    Sound:
      Enabled: true
      Sound: 'entity.player.levelup'
      Volume: 1.0
      Pitch: 1.0
```

---

### 💥 Particle Effects

```yaml
    Effect:
      Enabled: true
      Effect: 'EXPLOSION_NORMAL'
      Data: 1
      Particles: 10
      Radius: 5
```

---

### 🎆 Fireworks

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

---

### 💬 Messages

```yaml
    Messages:
      Player: '&aYou received a reward!'
      Broadcast: '&b%player% just voted!'
```

> `Broadcast` supports global proxy broadcast if configured.

---

## 🎲 Advanced Reward Logic

### 🧮 Randomized Rewards

#### RandomItem
Selects one random item from a defined list.

```yaml
    RandomItem:
      Diamond:
        Material: DIAMOND
        Amount: 1
      Iron:
        Material: IRON_INGOT
        Amount: 10
```

#### RandomReward / AdvancedRandomReward
Chooses one random reward block or file.

```yaml
    AdvancedRandomReward:
      reward1:
        Commands:
          - 'say reward1'
      reward2:
        Commands:
          - 'say reward2'
```

#### Random Chance Group

```yaml
    Random:
      Chance: 40
      PickRandom: true
      Rewards:
        - 'RewardA'
      FallBack:
        - 'RewardB'
```

---

### 🎯 AdvancedPriority System

Executes rewards in order — the first one to meet all conditions runs.

```yaml
    AdvancedPriority:
      Reward1:
        Chance: 50
        Messages:
          Player: 'You got first reward'
      Reward2:
        Chance: 20
        Messages:
          Player: 'You got second reward'
      Fallback:
        Messages:
          Player: 'You got unlucky'
```

📘 Docs: [AdvancedPriority Examples](https://github.com/BenCodez/AdvancedCore/wiki/AdvancedPriority-Examples)

---

### ⚖️ SpecialChance (Weighted Chances)

```yaml
    SpecialChance:
      5:
        Commands:
          - 'say 5'
      15:
        Commands:
          - 'say 15'
      30:
        Commands:
          - 'say 30'
      50:
        Commands:
          - 'say 50'
```


> Adds up all numbers (weights). Each reward’s chance = (value / total) × 100%.

---

### 🍀 Lucky Rewards

```yaml
    Lucky:
      '10':
        Messages:
          Player: 'You were lucky and got $100!'
        Money: 100
      '50':
        Messages:
          Player: 'You were lucky and got $1000!'
        Money: 1000
```

> Adds all numbers together and selects 1 out of the total.  
> Example: 1 “10” and 1 “50” = 10 in 60 chance (~16.6%).

---

### 🧠 Javascript Integration

Run logic inside rewards to determine actions or conditions dynamically.

```yaml
    Javascript:
      Enabled: true
      Expression: "BukkitPlayer.hasPermission('vip')"
      TrueRewards:
        Commands:
          - 'say VIP Reward!'
      FalseRewards:
        Commands:
          - 'say Not VIP'
```

📘 Reference: [Javascript API](https://github.com/BenCodez/AdvancedCore/wiki/Javascript-API)

---

### 🎴 Choice Rewards

Allows players to select one of multiple rewards (GUI prompt).

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

> Great for giving players a reward selection (e.g., choose between XP or money).

---

## ✅ Summary

| Category | Examples / Features |
|-----------|--------------------|
| **Requirements** | Chance, Permission, World, Timed, Delayed, LocationDistance |
| **Effects** | Items, Money, EXP, Commands, Potions, Titles, BossBar, ActionBar, Fireworks, Sound, Effects |
| **Advanced Logic** | Priority, AdvancedPriority, SpecialChance, Lucky, Javascript, RandomReward, ChoiceRewards |
| **Meta Options** | Delayed execution, Server restrictions, Date-based triggers, RewardType handling |
