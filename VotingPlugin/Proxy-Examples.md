---
title: Proxy Network Configuration Examples
description: Full example proxy and two-backend configuration for VotingPlugin 7.1.1
published: true
date: 2026-11-09T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2026-11-09T00:00:00.000Z
---

# Proxy Network Configuration Examples — two backends

This guide extends the [Proxy Network Quick Start](/VotingPlugin/Getting-Started-Proxy) with a concrete **single-proxy, two-backend** setup for VotingPlugin **7.1.1 / Java 21**. It uses the recommended `PLUGINMESSAGING` transport. The values here are **illustrative**, not secrets or production addresses.

> This is **not a complete replacement for the generated configuration files**. Edit the indicated keys in each existing file, preserve unrelated settings, and fully restart each node after changing proxy communication or database settings.
{.is-warning}

## Example topology

```text
                  Minecraft voting website
                           |
                     Public TCP 8192*
                           |
                Velocity/Bungee proxy
                VotifierPlus + VotingPlugin
                     (bungeeconfig.yml)
                           |
               PLUGINMESSAGING transport
                       /        \
                survival      skyblock
                Paper         Paper
                VotingPlugin  VotingPlugin
                BungeeSettings.yml each
                       \        /
                   Shared private SQL
```

`*` `8192` is only VotifierPlus's common default; use your actual allocated listening port. It is **not** the Minecraft server's usual game port.

| Example component | Server name | Role |
|---|---|---|
| Proxy | — | Receives public Votifier notifications; manages vote totals and forwards accepted votes |
| Paper backend 1 | `survival` | Can process game rewards |
| Paper backend 2 | `skyblock` | Can process game rewards |
| SQL database | `votingplugin` | Shared player records and configured coordination |

Never expose the SQL database directly to the public internet. Use a matching driver on the proxy and backends ([MySQLDriver](https://bencodez.com/job/MySQLDriver/) only where needed).

## 1. VotifierPlus on the proxy

Install **one** VotifierPlus/NuVotifier listener on the proxy. Its generated listener configuration commonly contains:

```yaml
host: 0.0.0.0
port: 8192
TokenSupport: false
DisableV1: false
Forwarding:
  server1:
    Enabled: false
```

Use the site-provided Votifier v1 public-key flow or a correctly enabled v2 token flow. The server-list site needs the proxy's **public hostname**, the assigned TCP port, and the matching public key/token.

**Keep VotifierPlus backend forwarding disabled** in the standard layout. VotingPlugin, not VotifierPlus, forwards the vote to eligible backends. Do not run duplicate listeners on the backends without a carefully designed custom topology.

## 2. Proxy VotingPlugin: `bungeeconfig.yml`

Edit `plugins/VotingPlugin/bungeeconfig.yml` on the **Velocity/BungeeCord proxy**:

```yaml
Database:
  Host: 'db.internal.example'
  Port: 3306
  Database: 'votingplugin'
  Username: 'vp_user'
  Password: 'REPLACE_WITH_PRIVATE_PASSWORD'
  DbType: MYSQL

BungeeMethod: PLUGINMESSAGING
BungeeManageTotals: true
AllowUnJoined: false
WaitForUserOnline: true
SendVotesToAllServers: false
BlockedServers:
  - hub
WhiteListedServers: []
PluginMessageChannel: 'vp:vp'
PluginMessageEncryption: false
```

- The proxy's real database credentials must be provided privately.
- `BungeeManageTotals: true` is the supported 7.1.1 setting for central totals/points.
- `WaitForUserOnline: true` and plugin messaging allow vote delivery after a player connects; messages typically need an online player connection.
- `SendVotesToAllServers: false` is an **example policy**: it selects one eligible player server rather than each eligible backend. The 7.1.1 default is **true**, so change this only intentionally.
- `BlockedServers` defaults to excluding `hub`. Review or remove that block if your network has different names.
- `WhiteListedServers` takes precedence when configured. Keep empty until you explicitly need a whitelist.

## 3. Backend 1: `survival`

**File A: `plugins/VotingPlugin/Config.yml`**

```yaml
DataStorage: MYSQL
Database:
  Host: 'db.internal.example'
  Port: 3306
  Database: 'votingplugin'
  Username: 'vp_user'
  Password: 'REPLACE_WITH_PRIVATE_PASSWORD'
  DbType: MYSQL

AllowUnjoined: true
ProcessRewards: true
```

**File B: `plugins/VotingPlugin/BungeeSettings.yml`**

```yaml
UseBungeecord: true
BungeeMethod: PLUGINMESSAGING
Server: survival
PluginMessageChannel: 'vp:vp'
PluginMessageEncryption: false
```

Use `survival` **only if that is exactly the name in your proxy's server configuration**.

## 4. Backend 2: `skyblock`

Use the **same shared SQL connection and the same communication channel** as survival, but change its backend identity.

**`Config.yml`**: keep `DataStorage: MYSQL` and the shared `Database` block from backend 1, with `AllowUnjoined: true` and `ProcessRewards: true` when this backend should reward players.

**`BungeeSettings.yml`:**

```yaml
UseBungeecord: true
BungeeMethod: PLUGINMESSAGING
Server: skyblock
PluginMessageChannel: 'vp:vp'
PluginMessageEncryption: false
```

Each backend must have a **different** `Server` name; duplicates can break routing and logs. Keep `VoteSites.yml` entries consistent wherever votes are eligible for rewards.

## 5. Choose how rewards should be routed

| Policy | Typical setting | Consequence |
|---|---|---|
| Reward a voter on one eligible server | `SendVotesToAllServers: false` | Reduces accidental multiple per-server reward processing |
| Each eligible backend processes a received vote | `SendVotesToAllServers: true` | Deliberately permits per-server effects; review overlapping reward definitions |
| Backend should not process forwarded rewards | `ProcessRewards: false` on that backend | Keep this server's reward-processing policy explicit |

Do not use `ProcessRewards: false` as a fix for network or SQL errors. Decide which backend owns each reward, then configure routing and processing accordingly.

## 6. Two similar keys with different capitalization

The values below are **case-sensitive YAML option names**:

| File | Key | Standard value |
|---|---|---|
| Proxy `bungeeconfig.yml` | `AllowUnJoined` | `false` |
| Backend `Config.yml` | `AllowUnjoined` | `true` |

The proxy checks whether a player is known; an enabled backend should not reject the already-validated forwarded vote a second time.

## 7. Restart and verify

1. Back up configurations and database, then restart **proxy + both backends**.
2. Check console logs for JDBC driver failures, SQL connection problems, and duplicate `Server` names.
3. With a player connected, run `/votingpluginproxy status` on the proxy.
4. Run `/votingpluginproxy vote <player> <site>`. This tests VotingPlugin forwarding but **not** the public listener.
5. Send a **real/listener-generated vote** to the proxy's VotifierPlus TCP port. Confirm proxy intake and backend reward delivery. Verify totals and points.
6. Test both routes: a player on survival, then a player on skyblock. Inspect where the rewards land, including reconnection/offline behavior.

## If something goes wrong

| Symptom | First checks |
|---|---|
| Listener receives no vote | Public address, TCP listener port, firewall, protocol/key/token; do not enter `0.0.0.0` on voting websites |
| Votifier receives vote but VotingPlugin does not | Listener and VotingPlugin must be on the same receiving process in the standard topology |
| Proxy receives vote but backend does not | SQL, shared `BungeeMethod`, matching `Server` names, online-player availability |
| Duplicate rewards | Duplicate Votifier forwarding; `SendVotesToAllServers`; shared site rewards; backend `ProcessRewards` |
| Driver class missing on Velocity | Install the correct compatible JDBC driver |
| Player name/UUID mismatches | Align online/offline mode and Bedrock prefix across nodes |

For more detail: [Proxy Setups](/VotingPlugin/Proxy-Setups) · [PLUGINMESSAGING](/VotingPlugin/Proxy-method-PLUGINMESSAGING) · [Votifier Troubleshooting](/VotingPlugin/Votifier-Troubleshooting) · [Getting Started](/VotingPlugin/Getting-Started).
