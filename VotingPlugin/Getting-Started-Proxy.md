---
title: Proxy Network Quick Start
description: First-time Velocity and BungeeCord setup for VotingPlugin 7.1.1
published: true
date: 2026-11-09T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2026-11-09T00:00:00.000Z
---

# Proxy Network Quick Start (Velocity / BungeeCord)

Use this guide if players connect through **Velocity or BungeeCord** to one or more **Paper/Spigot backend servers**. If you run only one Paper/Spigot server, follow the simpler [Standalone Quick Start](/VotingPlugin/Getting-Started-Standalone).

> **Release baseline:** VotingPlugin **7.1.1** / **Java 21**. This guide shows the **standard single-proxy topology** with `PLUGINMESSAGING`. Other transports, multiple proxies, and experimental features belong in the [advanced proxy reference](/VotingPlugin/Proxy-Setups).
{.is-info}

## Overview

```text
Voting website
     |
     | Public TCP Votifier port
     v
Velocity / BungeeCord proxy
  - VotifierPlus (receives vote)
  - VotingPlugin (tracks and forwards vote)
     |
     | PLUGINMESSAGING
     v
Paper/Spigot backend server(s)
  - VotingPlugin (processes rewards)
     |
     +---- Shared MySQL/MariaDB database ---- Proxy and backends
```

**Install VotingPlugin on the proxy and on each participating backend.** In this standard layout, put **one** VotifierPlus/NuVotifier listener on the proxy. **Do not also enable the listener's own backend forwarding**: VotingPlugin handles the forwarding path. Two forwarding routes can duplicate rewards.

## 1. Start with compatible artifacts and a shared database

- Install the correct **proxy** VotingPlugin build on Velocity/BungeeCord and the **backend** VotingPlugin build on every participating Paper/Spigot server. Fully restart after installing.
- Install VotifierPlus (or compatible NuVotifier) on the **proxy**. Set up its public address, separate TCP port, and public key/token as described in the [standalone listener instructions](/VotingPlugin/Getting-Started-Standalone). The address a voting website uses must reach the **proxy's** vote listener, not an internal backend.
- Create one **shared MySQL/MariaDB database** for VotingPlugin, reachable privately from the proxy and all backends. Use compatible credentials and database/table settings across nodes; do not expose the database port publicly.
- Make sure the needed **JDBC driver** is available on **both proxy and backends**. If the platform does not provide it, use the documented [MySQLDriver build](https://bencodez.com/job/MySQLDriver/).

**All VotingPlugin proxy methods require shared SQL storage in this released setup.** Don't begin with SQLite on the backend and expect network-wide totals to synchronize.

## 2. Configure the proxy

Open the proxy's `plugins/VotingPlugin/bungeeconfig.yml`. Start with the following relevant keys (edit the existing file; don't delete unrelated sections):

```yaml
Database:
  Host: 'your-private-database-host'
  Port: 3306
  Database: 'votingplugin'
  Username: 'your_database_user'
  Password: 'REPLACE_WITH_PRIVATE_PASSWORD'
  DbType: MYSQL

BungeeMethod: PLUGINMESSAGING
BungeeManageTotals: true
AllowUnJoined: false
SendVotesToAllServers: false
```

- `BungeeManageTotals: true` is the supported default; the proxy manages vote totals and points.
- `AllowUnJoined: false` rejects votes for players the proxy cannot validate in the standard setup.
- Set `SendVotesToAllServers: false` if you want a vote routed to a player's current/selected server **rather than rewarding each eligible backend**. Use `true` if per-server handling is intended, and review the default blocked/allowlisted servers. The released default is `true`.
- Keep `BungeeMethod: PLUGINMESSAGING` on every participating instance. Plugin messaging normally needs an online player connection to transmit messages; offline votes may be cached depending on settings.

The proxy uses `bungeeconfig.yml` (lowercase name); backends use `BungeeSettings.yml` (different file and fields).

## 3. Configure every backend

In **each** backend's `plugins/VotingPlugin/Config.yml`, switch storage to the **same database**. The following is a partial example, not a replacement for the complete file:

```yaml
DataStorage: MYSQL
Database:
  Host: 'your-private-database-host'
  Port: 3306
  Database: 'votingplugin'
  Username: 'your_database_user'
  Password: 'REPLACE_WITH_PRIVATE_PASSWORD'
  DbType: MYSQL

AllowUnjoined: true
ProcessRewards: true
```

In **each** backend's `plugins/VotingPlugin/BungeeSettings.yml`:

```yaml
UseBungeecord: true
BungeeMethod: PLUGINMESSAGING
Server: survival
```

Replace `survival` with the **actual server name registered on your proxy**. Use a **different unique name for each backend**. Keep online/offline identity mode and any Bedrock prefix consistent where applicable.

The capitalized names are intentionally different:

| Where | Key | Recommended standard value |
|---|---|---|
| Proxy `bungeeconfig.yml` | `AllowUnJoined` | `false` |
| Backend `Config.yml` | `AllowUnjoined` | `true` |

A backend should not reject a vote that the proxy already validated.

## 4. Configure your site and rewards on the backend

On the backend(s) meant to reward players, configure a vote site in `VoteSites.yml` with **`Enabled: true`**, the incoming **`ServiceSite`**, the real **`VoteURL`**, a `DisplayItem`, and a small `Rewards` block.

For an exact copyable example, follow [Standalone: Add your first voting site](/VotingPlugin/Getting-Started-Standalone). That `VoteSites.yml` example applies to a backend too. Keep site definitions consistent across participating backends when appropriate.

The in-game preset wizard (`/av VotePresets`) and `AutoCreateVoteSites` can help, but **the incoming vote must enter the proxy once** and ultimately match the configured site. Configure and test one site before adding many.

## 5. Restart and test in two stages

1. **Fully restart** the proxy and each participating backend after networking/storage changes. Verify successful SQL connections and correct server names.
2. With a player online, check the proxy with `/votingpluginproxy status` to help verify communication.
3. From the proxy, use `/votingpluginproxy vote <player> <site>` to test VotingPlugin's proxy processing/forwarding. This **does not test the external Votifier port**.
4. Send a **real or listener-generated test vote** to the proxy's Votifier listener. Confirm receipt at the proxy and reward delivery on the intended backend(s).
5. Check `/vote`, totals and rewards before advertising the voting page to players.

If rewards repeat, verify `SendVotesToAllServers`, backend eligibility, and that **VotifierPlus forwarding is disabled**. If a vote never reaches a backend, check SQL connection, `Server` names, `BungeeMethod` and online-player/plugin-message requirements.

**Next:** [First-vote verification](/VotingPlugin/Getting-Started-Verification) · [Proxy method PLUGINMESSAGING](/VotingPlugin/Proxy-method-PLUGINMESSAGING) · [Advanced Proxy Setups](/VotingPlugin/Proxy-Setups)
