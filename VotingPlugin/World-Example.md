---
title: World Example
description: 
published: true
date: 2025-09-01T03:00:50.117Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:33.123Z
---

You can restrict any rewards to within certain worlds

    Rewards:
      Worlds:
      - world1
      - world2

You can also give rewards based on what world the player is on:

    AdvancedWorld:
      world:
        Commands:
        - say %player% in world
      world_nether:
        Commands:
        - say %player% in nether

