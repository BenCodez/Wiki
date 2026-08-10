---
title: Reward-File
description: 
published: true
date: 2025-08-30T22:18:22.666Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:22.178Z
---

# Reward Files

![Example VotingPlugin reward-file configuration](https://i.imgur.com/hKOAj4Z.png)

Reward files is how player gets reward. They can be given on voting, or via Rewards.yml (First vote, all sites, Number of votes)

Requirements to give reward possibilities:
- Permission
- World
- Chance

Possible Rewards/Effects that can be defined:
- Items (with random item amounts possible)
- Money (with random money amounts possible)
- Commands
- Potion Effects
- Title
- BossBar
- ActionBar
- Sound
- Particle Effect
- Custom Message (or default message in Format.yml)

Advanced:
- Randomly pick a reward file to give on chance, Also option if chance is unlucky give fallback reward
- Delay when to run reward file (useful for giving players perk on vote, then removing x hours later)
- Run reward file at specific time

See the current AdvancedCore
[basic reward example](https://github.com/BenCodez/AdvancedCore/blob/master/AdvancedCore/src/main/resources/Rewards/ExampleBasic.yml)
and
[advanced reward example](https://github.com/BenCodez/AdvancedCore/blob/master/AdvancedCore/src/main/resources/Rewards/ExampleAdvanced.yml)
for complete configurations.

[Examples](https://gist.github.com/Ben12345rocks/c913ba94878327c1a5bad69dd0c6de85)
