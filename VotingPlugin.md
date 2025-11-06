---
title: VotingPlugin
description: 
published: true
date: 2025-11-06T01:54:48.406Z
tags: 
editor: markdown
dateCreated: 2025-08-31T02:55:49.572Z
---

# VotingPlugin — Overview

VotingPlugin is a highly configurable Minecraft voting and rewards system designed for **Spigot/Paper** servers, with optional **BungeeCord/Velocity** proxy support.  
It focuses on **reliability, flexibility, and performance**, handling high vote volumes with ease.

---

## Highlights
- **Stable & Reliable** – Handles offline players, delayed callbacks, and high vote loads.
- **Flexible Rewards** – Reward per site, per milestone, top voters, and more.
- **Network Support** – Works on single servers or proxy networks (Bungee/Velocity).
- **Integrated Placeholders** – Extensive PlaceholderAPI support for live stats.
- **Simple Admin Tools** – Clear configuration files and easy-to-test rewards.
- **SQL Storage** – Supports MySQL and SQLite (flatfile may be removed in future).

---

## Supported Platforms
- **Spigot/Paper:** 1.19+  
- **Proxies:** BungeeCord, Waterfall, Velocity  
- **Vote Listeners:** Works with **NuVotifier**, **VotifierPlus** (by BenCodez), and compatible alternatives.

---

## Default File Layout

**Default configuration files:**  
[https://github.com/BenCodez/VotingPlugin/tree/master/VotingPlugin/src/main/resources](https://github.com/BenCodez/VotingPlugin/tree/master/VotingPlugin/src/main/resources)

### Spigot Server Files
Path: `/plugins/VotingPlugin/`

| File / Folder | Description |
|----------------|-------------|
| **Rewards/** | Contains reward files (see examples below). |
| **TopVoter/** | Stores previous TopVoter info (must be enabled). Monthly TopVoter is enabled by default. |
| **BungeeSettings.yml** | Important Bungee-related settings. |
| **Config.yml** | Main plugin settings: user storage, formatting, vote reminding, permissions, etc. |
| **GUI.yml** | Configures GUI options (chest/book menus). Can disable GUIs if desired. |
| **Shop.yml** | VoteShop configuration (available in version 6.17+). |
| **ServerData.yml** | Internal plugin data for vote parties and top voter stats (do not edit). |
| **SpecialRewards.yml** | Defines rewards for AllSites, FirstVote, TopVoter, VoteParty, Milestones, Cumulative totals, etc. |
| **Users.db** | Player data when using SQLite. |
| **VoteSites.yml** | Defines all vote sites, including URL/service name, delay, and rewards. |

---

### Rewards Folder
Path: `/plugins/VotingPlugin/Rewards/`

| File / Folder | Description |
|----------------|-------------|
| **DirectlyDefined/** | Auto-generated rewards linked to SpecialRewards or VoteSites (do not edit). |
| **ExampleAdvanced.yml** | Example of advanced reward logic (conditions, random ranges, etc.) – [View on GitHub](https://github.com/BenCodez/AdvancedCore/blob/master/AdvancedCore/src/main/resources/ExampleAdvanced.yml) |
| **ExampleBasic.yml** | Example of simple per-vote rewards – [View on GitHub](https://github.com/BenCodez/AdvancedCore/blob/master/AdvancedCore/src/main/resources/ExampleBasic.yml) |

---

### Proxy Server Files
| File | Description |
|------|-------------|
| **bungeeconfig.yml** | Contains proxy-side configuration (Bungee/Velocity). |
| **nonvotedplayerscache.json** | Caches users who logged in within 5 days but haven’t voted (requires `AllowUnJoined: false`). |
| **secretkey.key** | Encryption key for SOCKET communication. Must match Spigot servers if using SOCKET mode. |
| **votecache.json** | Cache used for PLUGINMESSAGING mode. |

---

## Quick Start
1. **Install a vote listener plugin** – either **VotifierPlus** or **NuVotifier**.  
2. **Place VotingPlugin** in your `/plugins/` directory.  
3. **Configure** `/plugins/VotingPlugin/VoteSites.yml` with your vote sites and rewards.  
4. **Edit** `Config.yml` to your preferences.  
5. **Restart the server** and test a vote.

> For proxies, also configure `bungeeconfig.yml` and set up the same MySQL database across servers.

---

## Commands and Permissions

| Command | Description |
|----------|-------------|
| `/vote` | Shows vote sites and player totals. |
| `/v` | Alias for `/vote`. |
| `/adminvote` | Admin command root. |
| `/av` | Alias for `/adminvote`. |

### Permissions
- **`VotingPlugin.Player`** – Main permission for normal player commands.  
  Granted by default (can be disabled in `Config.yml`).

> See the [Commands and Permissions](./Admin/Commands-and-Permissions) page for all available nodes and usage.

---

## Storage
VotingPlugin stores player and vote data in the backend defined in:
- `Config.yml` (Spigot)
- `bungeeconfig.yml` (Proxy)

### Supported Backends
- **SQLite** – Default local database (`Users.db`).
- **MySQL** – Recommended for networks and multi-server setups.

> Flatfile support may be removed in future versions.

---

## Reward System
VotingPlugin rewards players automatically after a vote.  
If the player is offline, rewards are given on next login (no claim GUI).

Reward types include:
- Commands  
- Messages  
- Experience  
- Points (internal or economy)  
- Random ranges using `NumberCommand`

Examples:  
- [ExampleBasic.yml](https://github.com/BenCodez/AdvancedCore/blob/master/AdvancedCore/src/main/resources/Rewards/ExampleBasic.yml)  
- [ExampleAdvanced.yml](https://github.com/BenCodez/AdvancedCore/blob/master/AdvancedCore/src/main/resources/Rewards/ExampleAdvanced.yml)

---

## Configuration Highlights

| Option | Description |
|---------|-------------|
| **OnlineMode** | Controls whether votes are processed by online player name or all votes are accepted. ([See OnlineMode page](./OnlineMode)) |
| **VoteReminding** | Periodically reminds players to vote. |
| **TopVoter Settings** | Monthly/weekly tracking and resets. |
| **BungeeSettings.yml** | Used for proxy setups. |
| **SpecialRewards.yml** | AllSites, VoteParty, and milestone rewards. |

---

## Network / Proxy Setup
VotingPlugin supports all major proxy methods:

- **PLUGINMESSAGING** – Easiest for most setups.  
- **SOCKET** – Encrypted communication between proxy and servers (requires `secretkey.key`).  
- **MYSQL** – Shared database synchronization across servers.  

Detailed instructions and examples:  
[https://wiki.bencodez.com/en/VotingPlugin/Proxy-Setups](https://wiki.bencodez.com/en/VotingPlugin/Proxy-Setups)

---

## Troubleshooting
- Confirm your vote listener plugin (**VotifierPlus** or **NuVotifier**) is running and configured correctly.
- Verify ports, tokens, and callback URLs on your vote sites.
- Use `/adminvote` subcommands for testing (not `/av debug`).
- Check your server logs for incoming votes and reward messages.

> Common problems: incorrect service names, blocked ports, or outdated Votifier configurations.

---

## Developer Tools
- **VotingPluginEditor** – Desktop application for configuring VotingPlugin visually.  
  [View on GitHub](https://github.com/BenCodez/VotingPluginEditor)

---

## Related Pages
- [Installation](./Installation)  
- [Configuration](./Configuration)  
- [Vote Sites](./Vote-Sites)  
- [Rewards](./Rewards)  
- [Top Voter](./TopVoter)  
- [Proxy Setups](https://wiki.bencodez.com/en/VotingPlugin/Proxy-Setups)  
- [OnlineMode](./OnlineMode)

---

### Support
For issues, report them on the [GitHub repository](https://github.com/BenCodez/VotingPlugin/issues) or on Discord.

> Keep both **VotifierPlus** and **VotingPlugin** updated for best reliability and feature compatibility.