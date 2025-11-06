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

![Proxy Flow Diagram](/untitled_diagram___mermaid_chart-2025-08-30-234204.png)

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

For networks with multiple proxies, VotingPlugin supports **PLUGINMESSAGING** or **REDIS** synchronization across proxies.

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
| Key | Description |
|-----|--------------|
| `BungeeManageTotals` | Enables proxy-managed totals. |
| `SendVotesToAllServers` | Sends votes to all servers or only player’s current server. |
| `AllowUnJoined` | Ignores votes from players who never joined if false. |
| `WaitForUserOnline` | Queues votes until player logs in. |
| `GlobalData` | Enables global data/time sync and vote queueing. |
| `MultiProxySupport` | Allows votes to sync between multiple proxies. |
| `PrimaryServer` | Marks the main proxy handling totals. |

---

*For a deeper technical breakdown, see the implementation in  
[`VotingPluginProxy.java`](https://github.com/BenCodez/VotingPlugin/blob/master/VotingPlugin/src/main/java/com/bencodez/votingplugin/proxy/VotingPluginProxy.java).*
