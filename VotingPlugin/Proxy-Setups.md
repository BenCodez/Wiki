---
title: Proxy-Setups
description: Details of proxy setups
published: true
date: 2025-11-06T02:24:05.144Z
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
2. **VotingPlugin (Proxy)** records the vote in the database and updates totals.  
3. The proxy then **forwards** the vote to backend servers using the configured method.  
4. Each backend’s **VotingPlugin** instance gives rewards and handles player-specific logic such as milestones and streaks.

> The **proxy** acts as the **central controller** for vote tracking and forwarding.  
> Backend servers are responsible for **executing rewards**, **tracking streaks**, and managing local features.

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

## More Technical Details

The proxy handles incoming votes and forwards them to backend servers. Below is a deeper look at what happens internally.

### Responsibilities (Proxy)
- **Receive vote** from Votifier on the proxy.
- **Time-change handling** (`GlobalData`):
  - If a time change is detected and `timeQueue` is true, the vote is cached in the **time-change queue** and processed later.
- **Player & UUID resolution:**
  - Detects Bedrock players and adjusts name if missing prefix.
  - Skips votes for unjoined players when `AllowUnJoined: false`.
  - Performs UUID lookups if `UUIDLookup` and `OnlineMode` allow.
- **Totals management** (`BungeeManageTotals: true`):
  - Requires MySQL connection; if missing, vote processing stops.
  - Inserts player record if new and enforces per-site vote delay (If set).
  - Retrieves current totals (AllTime, Month, Week, Day, Points, MilestoneCount, and optional Date-based totals).
  - Applies limits (`MaxAmountOfVotesPerDay`, `LimitVotePoints`) if configured.
  - Updates player totals and generates a `BungeeMessageData` packet for forwarding.
- **Vote party counters:**  
  - Updates proxy vote party total and includes vote party progress in `VoteUpdate` messages.
- **Forwarding & caching:**  
  - If `SendVotesToAllServers: true`, sends or caches votes for each server based on player presence and config.
  - Otherwise, sends `VoteOnline` to the player’s current server or caches if offline.
- **Broadcasts:**  
  - Sends `VoteBroadcast` and `VoteUpdate` across servers when `Broadcast: true`.
- **Multi-proxy support:**
  - Shares votes with other proxies through `MultiProxySupport`.
  - Respects `MultiProxyOneGlobalReward` and `PrimaryServer` to prevent duplicate rewards.

### Handled by Backend Servers
- Executing rewards (commands, items, messages)
- Handling milestones
- Managing streaks and local reward tracking

---

### Key Config Options Referenced
| Key | Purpose |
|-----|----------|
| `BungeeManageTotals` | Enables proxy-managed totals. |
| `SendVotesToAllServers` | Sends votes to all servers or just target player’s server. |
| `WaitForUserOnline` | Forces votes to cache until player is online. |
| `AllowUnJoined` | Whether players must have joined before. |
| `UUIDLookup` | Allows online UUID fetching. |
| `OnlineMode` | Controls whether to use online UUID lookup. |
| `GlobalData` | Enables global time-change handling and synchronization. |
| `StoreMonthTotalsWithDate` | Stores monthly totals using date-based column names. |
| `UseMonthDateTotalsAsPrimaryTotal` | Uses date-based totals as main totals. |
| `LimitVotePoints` | Caps total points a player can earn. |
| `MaxAmountOfVotesPerDay` | Caps daily votes per player. |
| `Broadcast` | Enables global broadcast messages. |
| `BlockedServers` | Prevents forwarding to specific servers. |
| `MultiProxySupport` | Enables cross-proxy vote forwarding. |
| `MultiProxyOneGlobalReward` | Prevents duplicate rewards when multiple proxies handle votes. |
| `PrimaryServer` | Marks one proxy as the primary vote processor. |

---

*Based on core logic in [`VotingPluginProxy.java`](https://github.com/BenCodez/VotingPlugin/blob/master/VotingPlugin/src/main/java/com/bencodez/votingplugin/proxy/VotingPluginProxy.java)*
