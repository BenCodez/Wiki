---
title: Proxy-Setups
description: Details of proxy setups
published: true
date: 2025-11-06T02:26:59.944Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:02.764Z
---

> ⚙️ **Running on Velocity**
>
> Velocity requires a MySQL driver to be installed.  
> You can download a prebuilt plugin here if needed:  
> 🔗 [MySQLDriver (Jenkins)](http://bencodez.com/job/MySQLDriver/)
{.is-info}

> 💾 **Database Requirement**
>
> All proxy methods require **MySQL**, with every server — including the proxy — pointing to the **same database**.  
> The **proxy** manages vote forwarding, user vote totals, and synchronization between servers.  
> Backend servers handle all **rewards, milestones, and streaks** locally.
{.is-info}

> 📨 **Votifier Configuration**
>
> **Votifier** (or **VotifierPlus/NuVotifier**) only needs to run on the **proxy**.  
> VotingPlugin automatically handles forwarding votes to backend servers.
{.is-info}

---

# Proxy Methods

VotingPlugin supports multiple communication methods between your **proxy (BungeeCord/Velocity)** and backend servers.  
Each method provides the same core functionality — sending votes from the proxy to backend servers — but differs in setup and infrastructure requirements.

| Method | Description |
|--------|-------------|
| [PLUGINMESSAGING](/VotingPlugin/Proxy-method-PLUGINMESSAGING) | **Easiest option** — drop and play. No extra setup needed beyond placing the plugin on all servers. |
| [REDIS](/VotingPlugin/proxy-method-REDIS) | Uses a **Redis** server for fast, reliable network-wide message passing. |
| [MQTT](/VotingPlugin/proxy-method-MQTT) | Relies on an **MQTT broker** for cross-server vote forwarding (ideal for distributed environments). |
| [SOCKETS](/VotingPlugin/proxy-method-SOCKETS) | Uses direct TCP socket connections (requires open ports between servers). |
| [MYSQL](/VotingPlugin/proxy-method-MYSQL) | Shares vote data directly through the **common MySQL database**. |

---

## How It Works

![VotingPlugin proxy architecture showing vote websites, VotifierPlus, proxy communication methods, backend servers, and shared MySQL storage](/assets/VotingPlugin/votingplugin-proxy-architecture.svg)

> This diagram shows the typical single-proxy network layout. Multi-proxy setups and custom Votifier routing may use a different topology.
{.is-info}

When a player votes:

1. The **proxy** receives the vote from **Votifier**.  
2. **VotingPlugin (Proxy)** records the vote in the database and updates totals (if enabled).  
3. The proxy then **forwards** the vote to backend servers using the configured method.  
4. Each backend’s **VotingPlugin** instance handles rewards, milestones, and streaks locally.

> The **proxy** acts as the **central controller** for vote tracking and forwarding.  
> Backend servers focus on **reward delivery and gameplay logic**.

---

## Abilities

VotingPlugin’s proxy integration provides full network-wide support for:

- 🌍 **Global or per-server rewards**
- 🎉 **Proxy-wide or individual server vote parties**
- ⏰ **Global time synchronization** (via the `GlobalData` setting)
- 🧱 **Server blocklist/whitelist** controls
- 🔁 **Multi-proxy synchronization**
- 📊 **Centralized vote totals and logging handled by the proxy**
- ⚙️ **Local reward and streak logic handled by backend servers**

---

## Multi-Proxy Support

For networks with multiple proxies, `MultiProxyMethod` supports **SOCKETS** or
**REDIS** synchronization between proxies. This is separate from the backend
`BungeeMethod` selected for communication between a proxy and its backend
servers.

> ⚠️ **Note:** Multi-proxy setups are *experimental but functional* in current releases.  
> See the full guide here:  
> 🔗 [Multi-Proxy Setup](/en/VotingPlugin/Multi-Proxy-Setup)

---

## More Technical Details (Summary)

The proxy receives and manages votes from Votifier before forwarding them to backend servers.

### Proxy Responsibilities
- 📨 **Receives votes** from Votifier on the proxy.  
- 🕓 **Handles time-change conditions** when `GlobalData` is enabled (queues votes safely).  
- 🧩 **Resolves UUIDs** and supports Bedrock players (prefix detection).  
- 💾 **Manages totals** when `BungeeManageTotals: true` — updates MySQL totals (daily, weekly, monthly, all-time, and points).  
- 🎉 **Updates vote party progress** and broadcasts `VoteUpdate` / `VoteBroadcast`.  
- 🔁 **Forwards or caches votes** for backend servers depending on player presence and configuration.  
- 🌐 **Supports multi-proxy setups**, syncing votes across proxies and preventing duplicate rewards.

### Backend Responsibilities
- Executes rewards, milestones, and streak tracking.  
- Handles all in-game logic and GUI-related features.  

---

### Common Config Keys
| Key | File/location | Description |
|-----|---------------|-------------|
| `BungeeManageTotals` | Proxy `bungeeconfig.yml` | Enables proxy-managed totals. |
| `SendVotesToAllServers` | Proxy `bungeeconfig.yml` | Sends votes to all servers or only the player’s current server. |
| `AllowUnJoined` | Proxy `bungeeconfig.yml` | When false, the proxy validates that the player has joined before accepting the vote. |
| `AllowUnjoined` | Backend `Config.yml` | When true, a backend accepts forwarded votes without repeating the proxy’s joined-player check. |
| `WaitForUserOnline` | Proxy `bungeeconfig.yml` | Queues votes until the player logs in. |
| `GlobalData` | Proxy `bungeeconfig.yml` and backend `BungeeSettings.yml` | Enables global data/time synchronization and vote queueing; enable and align it on the proxy and applicable backends. |
| `MultiProxySupport` | Proxy `bungeeconfig.yml` | Allows votes to synchronize between multiple proxies. |
| `PrimaryServer` | Proxy `bungeeconfig.yml` | Marks the primary proxy for supported multi-proxy responsibilities. |

---

## Simple flow reference

![Simple VotingPlugin proxy flow showing votes entering VotifierPlus and VotingPlugin on the proxy, passing through one selected BungeeMethod, and reaching backend servers](/assets/VotingPlugin/proxy-flow-simple-reference.svg)

This compact version preserves the older proxy-flow overview. The detailed
architecture near the top of this page is the authoritative reference for
communication methods and shared storage.

---

*For a deeper technical breakdown, see the implementation in  
[`VotingPluginProxy.java`](https://github.com/BenCodez/VotingPlugin/blob/master/VotingPlugin/src/main/java/com/bencodez/votingplugin/proxy/VotingPluginProxy.java).*
