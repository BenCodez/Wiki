---
title: Proxy-Setups
description: Configure VotingPlugin on BungeeCord and Velocity networks
published: true
date: 2026-08-14T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2025-08-30T22:18:02.764Z
---

> ⚙️ **Running on Velocity**
>
> Velocity requires a matching JDBC driver. Install the [MySQLDriver build](https://bencodez.com/job/MySQLDriver/) only when the platform does not already provide the driver selected by `DbType`.
{.is-info}

> 💾 **Shared database requirement**
>
> VotingPlugin 7.1.1 proxy methods use one shared SQL database. The release configuration calls this MySQL and also exposes matching MariaDB/PostgreSQL JDBC options. Every proxy and backend must use compatible connection settings and table naming.
{.is-info}

> 📨 **Votifier topology**
>
> In the standard layout, VotifierPlus or NuVotifier runs on the proxy and VotingPlugin forwards votes through one selected `BungeeMethod`. Custom Votifier forwarding topologies are possible, but must be designed deliberately to avoid duplicate delivery.
{.is-info}

# Proxy Methods

VotingPlugin supports several communication methods between a BungeeCord/Velocity proxy and backend servers. Select **one** `BungeeMethod` and configure it consistently on the proxy and every participating backend.

| Method | Description |
|---|---|
| [PLUGINMESSAGING](/VotingPlugin/Proxy-method-PLUGINMESSAGING) | Uses the proxy's plugin-message channel; the release default and usual starting point. |
| [REDIS](/VotingPlugin/proxy-method-REDIS) | Uses a private Redis service for cross-server messages. |
| [MQTT](/VotingPlugin/proxy-method-MQTT) | Uses an MQTT broker with a unique client ID for each instance. |
| [SOCKETS](/VotingPlugin/proxy-method-SOCKETS) | Uses direct TCP sockets and requires explicit peer addresses, secrets, and firewall rules. |
| [MYSQL](/VotingPlugin/proxy-method-MYSQL) | Uses the shared database as the communication path; release defaults do not recommend it. |

## How It Works

![VotingPlugin proxy architecture showing vote websites, VotifierPlus, one selected proxy communication method, backend servers, and shared SQL storage](/assets/VotingPlugin/votingplugin-proxy-architecture.svg)

> This diagram shows the typical single-proxy network. Multi-proxy and custom Votifier-routing designs can differ, but the configured backend communication methods converge through one selected path.
{.is-info}

When a player votes:

1. The proxy-side vote listener receives the vote.
2. VotingPlugin validates and records the vote.
3. The proxy forwards or caches it through the configured `BungeeMethod`.
4. The selected backend server or servers process in-game rewards and related gameplay logic.

With the release default `BungeeManageTotals: true`, the proxy manages totals and points. When it is `false`, each backend adds its own totals; the 7.1.1 bundled configuration describes that layout as unsupported. Do not document or design a network as though the proxy always owns totals regardless of this setting.

## Reward ownership

`SendVotesToAllServers` controls where the forwarded vote is processed:

- `true` sends the vote to all eligible backends, so each backend can run its own reward.
- `false` sends it to the player's selected/current backend, which is the usual setting for one reward across the network.

Backend `ProcessRewards`, per-server reward settings, blocked/allowlisted servers, vote-party settings, and reward-level `Server`/`BlockedServers` restrictions can further change what executes.

## Common configuration keys

| Key | File/location | Purpose |
|---|---|---|
| `BungeeMethod` | Proxy `bungeeconfig.yml`; backend `BungeeSettings.yml` | Selects the proxy-to-backend transport. |
| `BungeeManageTotals` | Proxy `bungeeconfig.yml` | Uses proxy-managed totals when true; true is the supported release default. |
| `SendVotesToAllServers` | Proxy `bungeeconfig.yml` | Selects all eligible backends or the player's selected/current backend. |
| `AllowUnJoined` | Proxy `bungeeconfig.yml` | Controls the proxy's joined-player validation. Capitalization is significant. |
| `AllowUnjoined` | Backend `Config.yml` | Lets a backend accept forwarded data without repeating the proxy's validation. |
| `WaitForUserOnline` | Proxy `bungeeconfig.yml` | Delays forwarding until the player is online when enabled. |
| `Server` | Backend `BungeeSettings.yml` | Unique backend identifier used for routing and per-server behavior. |
| `GlobalData` | Proxy and backend configuration | Optional, experimental coordination of time changes and resets. |

## Multi-proxy support

Multi-proxy synchronization is separate from `BungeeMethod`. In 7.1.1, `MultiProxyMethod` supports `SOCKETS` or `REDIS`, and the bundled configuration labels the overall multi-proxy feature as work in progress. Follow [Multi-Proxy Setup](/VotingPlugin/Multi-Proxy-Setup) and do not expose its brokers or socket listeners publicly.

## Simple flow reference

![Simple VotingPlugin proxy flow showing votes entering VotifierPlus and VotingPlugin on the proxy, passing through one selected BungeeMethod, and reaching backend servers](/assets/VotingPlugin/proxy-flow-simple-reference.svg)

This compact image preserves the older flow reference. The detailed architecture near the top is the authoritative overview.

For release-specific implementation details, see [`VotingPluginProxy.java` from tag 7.1.1](https://github.com/BenCodez/VotingPlugin/blob/7.1.1/VotingPlugin/src/main/java/com/bencodez/votingplugin/proxy/VotingPluginProxy.java).
