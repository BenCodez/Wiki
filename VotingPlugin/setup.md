---
title: Setup
description: 
published: true
date: 2025-08-31T03:20:40.070Z
tags: 
editor: markdown
dateCreated: 2025-08-31T03:20:39.536Z
---


# Setup VotingPlugin

1. [Verify votifier install](https://github.com/BenCodez/VotingPlugin/wiki/Votifier-Troubleshooting)  
2. If running a proxy server, use one of [these proxy setups](/VotingPlugin/Proxy-Setups), you'll still need to configure each server  
3. [Create/Setup VoteSites](/VotingPlugin/adding-votesites) (Multiple methods):  
    * (Easiest) Vote on website, will cause a site to be auto-generated (enabled by default) with the correct service site  
       * votifier must be setup properly for this to work
    * Use [VotingPluginEditor](https://github.com/BenCodez/VotingPluginEditor)
    * Create ingame, /av gui (Middle click votesites and enter name, then enter values)
    * Add manually to VoteSites.yml, just  (See the examples in the file)

   Note: The service site must be correct, otherwise there will be no rewards given. Service site will be said in console on every vote, /av servicesites will list all known service sites received from votifier   
4. Setup [Rewards](https://github.com/BenCodez/AdvancedCore/wiki/Rewards)    
Anything in the example rewards files can be put under Rewards anywhere in the plugin where applicable, works the same everywhere. Some Specific examples on the side bar. This can also now be fully done ingame with /av gui  
5. Setup Permissions (By default, players will get the permission VotingPlugin.Player (You may need to give it manually on some permissions plugins), which gives them the main player commands)  
Note: Some permissions on commands may have 2 permissions (Shown on wiki for commands/permissions on the side), use /av perms ingame, use /av permsplayer (player) for checking what a player can access  
6. You should be all good to go! Contact me (BenCodez) if you run into issues  

Other articles covering setup:  
https://serverminer.com/article/how-to-setup-voting-on-your-minecraft-server/
https://support.witherhosting.com/en/article/how-to-install-and-use-votingplugin-java-6epg7/


