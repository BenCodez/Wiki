---
title: Reward-File
description: 
published: true
date: 2025-08-30T22:18:22.666Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:22.178Z
---

![](http://i.imgur.com/hKOAj4Z.png)

Reward files is how player gets reward. They can be given on voting, or via Rewards.yml (First vote, all sites, Number of votes)

Requirements to give reward possiblities:
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

See [ExampleReward](https://github.com/Ben12345rocks/AdvancedCore/blob/master/AdvancedCore/Rewards/ExampleReward.yml) for examples on the above! 

[Examples](https://gist.github.com/Ben12345rocks/c913ba94878327c1a5bad69dd0c6de85)