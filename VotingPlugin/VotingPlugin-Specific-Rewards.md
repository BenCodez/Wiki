---
title: VotingPlugin Specific Rewards
description: 
published: true
date: 2025-09-01T02:59:08.144Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:30.743Z
---

## Specific rewards for VotingPlugin (Not in AdvancedCore by default)

    #Vote total requirements
    VoteTotal:
      # If enabled you only need atleast the amount of votes required, otherwise it has to match
      AtleastMode: false
      # Value of -1 is disabled (default value)
      Daily: -1
      Weekly: -1
      Monthly: -1
      AllTime: -1
      Points: -1
      MilestoneCount: -1

    # Voting points to be given
    Points: 10

    # Bossbar with progress based on voting sites voted on
    VoteBossBar:
      Enabled: true
      Message: '&aBossbar'
      # Bar Colors:
      # https://hub.spigotmc.org/javadocs/spigot/org/bukkit/boss/BarColor.html
      Color: 'BLUE'
      # Bar Styles:
      # https://hub.spigotmc.org/javadocs/spigot/org/bukkit/boss/BarStyle.html
      Style: 'SOLID'
      # Delay until bar goes away (in ticks)
      Delay: 30

    DiscordSRV:
      Enabled: true
      Message: MESSAGE HERE
      ChannelID: CHANNELID
