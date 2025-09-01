---
title: File Layout
description: 
published: true
date: 2025-09-01T14:15:55.543Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:09.653Z
---

> Default configurations available here https://github.com/BenCodez/VotingPlugin/tree/master/VotingPlugin/src/main/resources
{.is-info}


### Spigot Server Files:  
/plugins/VotingPlugin/

![](https://i.imgur.com/NRZbbcW.png)

Rewards folder - Contains reward files (see screenshot below)  
TopVoter - Contains TopVoter info when it resets (Stores all previous information) Must be enabled for it to work. Monthly top voter is enabled by default  
BungeeSettings.yml - Contains most important bungee settings  
Config.yml - User storage info, formats, vote reminding  
GUI.yml - Options to disable GUI's, configs for CHEST GUI's and BOOK GUI's  
Shop.yml - Options for VoteShop (6.17+)  
ServerData.yml - Plugin related information such as vote party and month/week/day info for top voter (Shouldn't need to edit this file)  
SpecialRewards.yml - Rewards for AllSites, FirstVote, Top voter rewards, voteparty, milestones, cumulative  
Users.db - Users info when using SQLITE  
VoteSites.yml - Contains all votesites information such as service site, vote delay, rewards for votesites, also as EverySiteReward  

/plugins/VotingPlugin/Rewards/  
![](https://i.imgur.com/etHNpAA.png)  

DirectlyDefined - This contains rewards that are set in SpecialRewards or VoteSites that aren't using reward files, this should almost never generate with newer versions (DO NOT EDIT FILES IN THIS FOLDER, THEY WILL BE OVERRIDDEN)  
ExampleAdvanced.yml - Contains examples of advanced rewards, works anywhere under rewards  
ExampleBasic.yml - Contains examples of basic rewards, works anywhere under rewards  

### Proxy Server Files:

![](https://i.imgur.com/RYVmnhM.png)

bungeeconfig.yml - Contains all bungee related configs  
nonvotedplayerscache.json - Contains users that login for up to 5 days who have not voted. Requires AllowUnJoined set to false in bungeeconfig.yml  
secretkey.key - Encryption key for SOCKET bungee method  (Must be copied to spigot servers if using the SOCKET method)  
votecache.json - Contains a vote cache for PLUGINMESSAGNG bungee method  