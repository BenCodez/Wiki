---
title: File Layout
description: 
published: true
date: 2025-11-06T02:41:24.539Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:09.653Z
---

> 📁 **Default configurations are available here:**  
> [https://github.com/BenCodez/VotingPlugin/tree/master/VotingPlugin/src/main/resources](https://github.com/BenCodez/VotingPlugin/tree/master/VotingPlugin/src/main/resources)
{.is-info}

---

## Spigot Server Files
**Path:** `/plugins/VotingPlugin/`

![](https://i.imgur.com/NRZbbcW.png)

| File / Folder | Description |
|----------------|-------------|
| **Rewards/** | Contains all reward configuration files (see below). |
| **TopVoter/** | Stores previous TopVoter results when totals reset. Must be enabled. Monthly TopVoter tracking is enabled by default. |
| **BungeeSettings.yml** | Important for proxy-related configuration and communication. |
| **Config.yml** | Main settings: player storage method, formats, reminders, and general behavior. |
| **GUI.yml** | Configures GUIs (chest/book). Also allows disabling GUIs entirely. |
| **Shop.yml** | Config for the VoteShop (available since v6.17+). |
| **ServerData.yml** | Internal plugin data for vote party and top voter tracking — do **not** edit manually. |
| **SpecialRewards.yml** | Defines rewards such as AllSites, FirstVote, VoteParty, TopVoter, Milestones, and Cumulative totals. |
| **Users.db** | Player data when using **SQLite**. |
| **VoteSites.yml** | Defines vote sites — includes service name, delay, and rewards. Also contains “EverySiteReward” if configured. |

---

### Rewards Folder
**Path:** `/plugins/VotingPlugin/Rewards/`

![](https://i.imgur.com/etHNpAA.png)

| File / Folder | Description |
|----------------|-------------|
| **DirectlyDefined/** | Auto-generated rewards for SpecialRewards or VoteSites when inline rewards are used. Do **not** edit manually — files are overwritten automatically. |
| **ExampleAdvanced.yml** | Example of advanced reward logic (conditions, randomization, etc.). [View on GitHub →](https://github.com/BenCodez/AdvancedCore/blob/master/AdvancedCore/src/main/resources/Rewards/ExampleAdvanced.yml) |
| **ExampleBasic.yml** | Simple example of per-vote rewards. [View on GitHub →](https://github.com/BenCodez/AdvancedCore/blob/master/AdvancedCore/src/main/resources/Rewards/ExampleBasic.yml) |

> 💡 Any reward configuration shown in the examples can be placed under **Rewards** anywhere in the plugin configuration — they function identically.
{.is-info}

---

## Proxy Server Files
**Path:** `/plugins/VotingPlugin/` *(on BungeeCord or Velocity)*

![](https://i.imgur.com/RYVmnhM.png)

| File | Description |
|------|-------------|
| **bungeeconfig.yml** | Main proxy-side configuration file. Controls how votes are received and forwarded to backend servers. |
| **nonvotedplayerscache.json** | Lists players who logged in recently (up to 5 days) but haven’t voted. Used when `AllowUnJoined: false`. |
| **secretkey.key** | Encryption key for **SOCKET** proxy mode. Must match between proxy and Spigot servers if using that mode. |
| **votecache.json** | Temporary cache for **PLUGINMESSAGING** method to ensure votes are forwarded reliably. |

---

> 🧠 **Tip:**  
> Proxy and Spigot servers can share MySQL databases for full synchronization.  
> Keep configuration paths and server names consistent across all instances for best results.
{.is-info}
