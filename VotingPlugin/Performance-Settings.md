---
title: Performance Settings
description: 
published: true
date: 2025-09-01T03:00:19.842Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:19.128Z
---

This pages provides a brief overview of all VotingPlugin config options to can optimize plugin performance.  
This page is still a work in progress

### Mysql
Adjust concurrent plugin connections to mysql database  
Having more than can improve performance slightly, but more than 2 is won't make much of a difference

    MaxConnections: 1

### TopVoter settings
Disabling loading unneeded top voter data can improve background performance.  
Especially when multiple servers with large amounts of users are present

    # These are required to be enabled in order for top voter awards to work
    LoadTopVoter:
      AllTime: true
      Monthly: true
      Weekly: false
      Daily: false

Lowering this number improves background loading performance with large amounts of users
      
    # Maxium number of players to show on top voter
    # Set to -1 for no limit
    MaxiumNumberOfTopVotersToLoad: 1000

### Background task settings
Enabling this allows persite cooldown rewards/reminders, but uses more resources

    # Enable per site cooldown events, requires more resources to use
    # Requires restart
    PerSiteCoolDownEvents: false

Enabling this disables cool down checks for all voting sites combined. Has no effect on vote reminders

    # If true, cooldown check is disabled
    DisableCoolDownCheck: false

Enabling this may improve performance slightly

    # If true, disable PlayerInteractEvent (for clicking signs and skulls)
    DisableInteractEvent: false

Disabling processing and storing votestreaks  
Also lowers amount of sql queries needed

    # If false, votestreaks will be disabled
    UseVoteStreaks: true

Disabling processing and storing highest totals
Also lowers amount of sql queries needed

    # If false, storing best totals will be disabled
    UseHighestTotals: true

Enabling this can have a significant performance impact depending on what javascript is ran  
Also has a performance impact even if no javascript is used in placeholders  

    # When enabled, javascript will be parsed on placeholders (from placeholderapi)
    # allows more fancy placeholders with math for example
    UseJavascriptPlaceholders: false

Not recommended enabling unless you have a really good reason  
This causes background updates to always happen based on the update interval set below

    # Only update in the background when needed when set to false
    AlwaysUpdate: false

Only perform background updates with players online

    # Update in the background only if players are online
    UpdateWithPlayersOnlineOnly: false

Delay between checking if a background update should be done  
Between 3-10 minutes is recommended for most people

    # Delay between background updates like signs and more
    # Default: 3 Minutes
    # Longer times result in longer wait in stuff updating after a vote, like topvoter
    DelayBetweenUpdates: 3

This options performances extra background checks  
Should only be needed in some multi-server setups that don't trigger updates on other servers

    # Enable to true for extra player checks
    # Recommend leaving this to false
    ExtraBackgroundUpdate: false

This could improve performance of tab completes

    # Disable checking permissions on tab complete
    DisableAdvancedTab: false

### Placeholder settings
Default settings are the best  
Details available here: https://github.com/BenCodez/VotingPlugin/wiki/PlaceHolderAPI-Expansion

### Skulls
This options preloads skulls for top voter GUI  
This can have a huge performance impact in some cases

    # Preload skulls to improve performance for vote top
    # when using skulls as the item to display players
    # If false, skulls will be cached as they are used
    # assuming loadskulls is enabled
    PreloadSkulls: false

Similar to preload skulls option, but only loads as skulls are used  
This is more recommended then PreloadSkulls

    # Setting to false disables saving skulls in a cache to improve speeds
    # Will reduce ram usage (very little) if disabled, but slow GUI speeds when using skulls
    LoadSkulls: true

