---
title: Service-sites
description: 
published: true
date: 2025-08-30T22:18:24.404Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:23.897Z
---

Service sites is the identifier that tells VotingPlugin which incoming vote is which votesite.

Majority of voting websites follow the format of using the base of the url, but not all do. 

Best way to find a service site is to look in console on a vote for a message like this:  
```[19:01:21] [Votifier I/O/INFO]: [VotifierPlus] Debug: Received vote record -> Vote (from:SERVICESITEHERE username:BenCodez address:Address timeStamp:TestVote)```  
```[19:01:21] [Server thread/INFO]: [VotingPlugin] Received a vote from service site 'SERVICESITEHERE' by player 'BenCodez'!```

If you don't get the above message check [here](https://github.com/BenCodez/VotingPlugin/wiki/Votifier-Troubleshooting)

Servers lists with known service site can be found [here](https://github.com/BenCodez/VotingPlugin/wiki/Minecraft-Server-Lists)
