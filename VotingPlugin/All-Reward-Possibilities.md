---
title: All Reward Possibilities
description: 
published: true
date: 2025-09-01T03:01:32.148Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:17:56.051Z
---

Most of these rewards can be configured in /av gui, examples for rewards are found at [ExampleBasic](https://github.com/BenCodez/AdvancedCore/blob/master/AdvancedCore/Resources/Rewards/ExampleBasic.yml) or [ExampleAdvanced](https://github.com/BenCodez/AdvancedCore/blob/master/AdvancedCore/Resources/Rewards/ExampleAdvanced.yml) or [Wiki page](https://github.com/BenCodez/VotingPlugin/wiki/Reward-Examples)  

Requirements:
- Permission
- World
- Chance
- Online/Offline (Reward type)
- Javascript (true return)
- VaultGroup
- RewardExpiration (Reward has to be claimed within a certain amount of time)
- Server
- LocationDistance (Be within a certain distance of a location)
- Timed (run at a certain time)
- Delayed (delay a reward)

Rewards/Effects:
- Items:
  - RandomItem
  - Chance Items (based on chance to get)
  - Random amounts
- Money
  - random amount support
- EXP/EXPLevels
  - random amount support
- Commands:
  - run as console or player
  - random command from list of commands support
- Potion Effects
- Title
- BossBar
- ActionBar
- Particle Effect
- Messages:
  - message to player
  - broadcast message
- Firework
- Javascript:
  - run rewards based on javascript
  - execute javascript
  - https://github.com/BenCodez/AdvancedCore/wiki/Javascript-API
- Priority system (Priority & AdvancedPriority):
  - Check sub rewards and run first available reward based on requirements only
  - https://github.com/BenCodez/AdvancedCore/wiki/AdvancedPriority-Examples
- Advanced Chance systems (SpecialChance, Lucky)
  - SpecialChance: always picked a reward based on weight of chances
  - Lucky: 1 out of x for chance
