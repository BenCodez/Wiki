---
title: Online/Offline Mode
description: 
published: true
date: 2025-09-01T02:56:53.048Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:18.207Z
---

# Updated handling 6.18.5+

Online mode can be set within VotingPlugin via this setting:
  
    OnlineMode: true

If your using mixed uuids (online/offline or premium/cracked) then it may work better to disable OnlineMode. VotingPlugin will simply get the uuid based on the player name, essentially ensuring uuids will always be the same. 


# 6.18.4 and below:

Online mode can be set within VotingPlugin via this setting:
  
    OnlineMode: true

Only disable this setting if you know for a fact your using offline uuids exclusively.

In the event of using mixed uuids (Premium and cracked players) leave enabled and disable `UUIDLookup` on proxy


If you are unsure of this setting, leave it enabled.