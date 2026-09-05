---
title: Dedicated Voting Proxy
description: Route votes through one central proxy when players connect through separate regional proxies
published: true
date: 2026-08-16T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2026-08-16T00:00:00.000Z
---

# Dedicated Voting Proxy

> **Development-build feature:** `DedicatedVotingProxy` is not available in the latest public release, VotingPlugin **7.1.1**. It requires a 7.1.2-SNAPSHOT development build containing merged commit [`6867c488`](https://github.com/BenCodez/VotingPlugin/commit/6867c4880631f0c9e140a27279d26d708876a96b) (PR [#1551](https://github.com/BenCodez/VotingPlugin/pull/1551)) and its backend-presence foundation from [`c916763e`](https://github.com/BenCodez/VotingPlugin/commit/c916763e0e2c059362638f62255558873c350820) (PR [#1550](https://github.com/BenCodez/VotingPlugin/pull/1550)). Release users will not have this setting yet.
{.is-warning}

Use this mode when players connect through multiple regional or player-facing proxies, but one separate proxy should receive votes and coordinate VotingPlugin for the entire network.

The dedicated voting proxy does not need local players. Backend servers report their online-player and current-server state through the configured VotingPlugin communication method so the dedicated proxy can route votes, cached rewards, vote parties, broadcasts, and status requests correctly.

![Dedicated VotingPlugin proxy architecture showing voting websites entering one central voting proxy, regional proxies carrying players separately, one selected communication method, backend presence, and shared SQL storage](https://wiki.bencodez.com/assets/VotingPlugin/dedicated-voting-proxy-architecture.svg)

## When to use it

Use a dedicated voting proxy when all of these are true:

- one central BungeeCord or Velocity proxy runs VotingPlugin and receives votes;
- regional/player-facing proxies route Minecraft players but do **not** run VotingPlugin;
- every participating backend runs the same compatible VotingPlugin development build;
- the dedicated proxy and backends share one SQL database and table configuration;
- the dedicated proxy and backends communicate through `MYSQL`, `REDIS`, `MQTT`, or `SOCKETS`.

This is different from [Multi-Proxy Setup](Multi-Proxy-Setup). `MultiProxySupport` coordinates multiple VotingPlugin proxies. Dedicated mode instead keeps VotingPlugin on one central proxy while the regional proxies remain outside VotingPlugin's vote-delivery path.

## Requirements

1. Install the same compatible development build on the dedicated proxy and every backend.
2. Run VotifierPlus or NuVotifier on the dedicated proxy in the standard layout.
3. Configure the same non-`PLUGINMESSAGING` `BungeeMethod` on the dedicated proxy and every backend.
4. Give each backend a unique `Server` value in `BungeeSettings.yml`; it must match the server name configured on the dedicated proxy.
5. Configure the shared SQL database required by normal VotingPlugin proxy setups.
6. Secure the selected communication transport and allow connections only between participating hosts.

> `PLUGINMESSAGING` cannot be used for dedicated-proxy routing. It depends on the player-facing proxy's native player/server state and does not carry the backend presence snapshots required by a proxy with no local players. If dedicated mode is enabled with `PLUGINMESSAGING`, VotingPlugin logs a severe configuration error and falls back to normal proxy routing.
{.is-danger}

## Dedicated proxy configuration

In the dedicated proxy's `bungeeconfig.yml`:

```yaml
# Development builds containing merged PR #1551 only
DedicatedVotingProxy: true

# Choose one: MYSQL, REDIS, MQTT, or SOCKETS
BungeeMethod: MQTT

# Normal routing behavior is preserved; choose the behavior you want
SendVotesToAllServers: false
```

Configure the matching transport section and the normal `Database` section in the same file. See the method-specific guides:

- [MQTT](proxy-method-MQTT)
- [Redis](proxy-method-REDIS)
- [MySQL](proxy-method-MYSQL)
- [Sockets](proxy-method-SOCKETS)

Enable `DedicatedVotingProxy` on **one** central voting proxy only. Do not enable it on regional proxies.

## Backend configuration

On every backend, configure `BungeeSettings.yml` with the same method and a unique server name. For example:

```yaml
UseBungeecord: true
BungeeMethod: MQTT
Server: lobby

MQTT:
  ClientID: lobby
  BrokerURL: "tcp://mqtt.internal.example:1883"
  Username: 'votingplugin'
  Password: 'replace-with-a-secret'
  Prefix: ''
```

Also configure the shared SQL storage in backend `Config.yml`. Follow the selected method guide for its complete proxy and backend settings. In particular, every MQTT instance needs a unique `ClientID`, and socket endpoints must match the proxy's `SpigotServers` entries.

## Regional proxy configuration

Regional/player-facing proxies continue routing players normally, but they do not participate in VotingPlugin routing:

- do not install or run VotingPlugin on the regional proxies;
- do not forward the same Votifier vote through a regional proxy as well as the dedicated proxy;
- do not configure `DedicatedVotingProxy` on them;
- keep their normal Minecraft backend routing independent from VotingPlugin's selected communication transport.

## Vote routing behavior

Dedicated mode changes where VotingPlugin obtains online-player and current-server state. It does **not** replace the normal `SendVotesToAllServers` setting.

| Setting | Behavior in dedicated mode |
|---|---|
| `SendVotesToAllServers: true` | Preserves normal fan-out behavior and sends the vote to every eligible backend. Existing cache and `WaitForUserOnline` rules still apply. |
| `SendVotesToAllServers: false` | A player confirmed online is routed to their reported current backend. An unknown or offline player follows the existing online-vote cache path until presence confirms them. |

`BlockedServers`, `WhiteListedServers`, `WaitForUserOnline`, backend `ProcessRewards`, proxy broadcasts, and the normal totals settings continue to affect processing. Dedicated mode does not make every backend execute rewards unless the existing settings select that behavior.

## Backend presence and recovery

For `MYSQL`, `REDIS`, `MQTT`, and `SOCKETS`, each backend reports its lifecycle and player presence through the same selected communication path:

- backends announce start, stop, player login, player logout, and periodic heartbeats;
- the dedicated proxy requests a fresh presence resynchronization shortly after startup;
- complete snapshots restore the known online players for each backend;
- a backend that stops reporting is eventually treated as unavailable;
- presence state is memory-only, so players are temporarily unknown after a dedicated-proxy restart until fresh backend snapshots arrive;
- when a completed snapshot confirms players who were already online, VotingPlugin runs its existing login/cache-draining path so voter-keyed cached rewards are released.

The current implementation starts its resynchronization request five seconds after proxy startup, performs presence maintenance every 30 seconds, and treats a silent backend as unavailable after 90 seconds. These timings describe the development implementation and may change before release.

## Security model

Dedicated presence adds no separate presence password, secret file, or persistence file. Each backend's unique configured `Server` name is its identity inside the selected communication system. Therefore, every participant with access to that transport must be trusted not to impersonate another backend.

- Keep Redis, MQTT, MySQL, and socket listeners on private networks, VPNs, or strict firewall allowlists.
- Require dedicated credentials with the minimum necessary permissions.
- Use TLS or a trusted private tunnel when traffic crosses hosts or untrusted networks.
- Do not publish database, broker, socket, or encryption credentials in screenshots or logs.
- For `SOCKETS`, keep the generated/shared encryption key private and follow [Sockets](proxy-method-SOCKETS).

## Migration checklist

1. Back up the proxy and backend VotingPlugin configuration and data.
2. Install a development build containing commits `c916763e` and `6867c488` on the dedicated proxy and every backend.
3. Choose and secure one supported non-plugin-messaging transport.
4. Configure the shared database, transport, backend names, and `SpigotServers` mapping.
5. Set `DedicatedVotingProxy: true` only on the central proxy.
6. Set `SendVotesToAllServers` for the intended normal reward-routing behavior.
7. Remove duplicate VotingPlugin/Votifier vote ingress from regional proxies.
8. Restart the dedicated proxy and every backend; this feature is not intended to be enabled by a partial reload.

## Validation

Test both routing modes before production use:

1. Run `/votingpluginproxy status` on the dedicated proxy and confirm each expected backend responds while it has players online.
2. Run `/votingpluginproxy vote <player> <site>` with a player online and confirm the selected backend behavior.
3. Test an offline or unknown player and confirm the vote is cached, then delivered after presence confirms the player.
4. Test with `SendVotesToAllServers` both enabled and disabled if you may use both modes.
5. Restart the dedicated proxy while players remain online, allow the startup snapshot to complete, and verify cached rewards drain without requiring another player reconnect.
6. Send one real vote through VotifierPlus/NuVotifier to validate the public listener and the complete delivery path.

## Troubleshooting

| Symptom | Check |
|---|---|
| Severe warning says dedicated routing requires another method | Replace `PLUGINMESSAGING` with `MYSQL`, `REDIS`, `MQTT`, or `SOCKETS` on the dedicated proxy and all backends. |
| Players are unknown immediately after proxy startup | Wait for the startup resynchronization and verify backend lifecycle/snapshot messages reach the dedicated proxy. Presence is intentionally not loaded from disk. |
| One backend never becomes available | Verify its unique `Server` name, matching proxy server entry, selected method, credentials, prefix/topic/database, and firewall rules. |
| MQTT clients repeatedly disconnect | Give the dedicated proxy and every backend a unique `ClientID`. |
| Votes or broadcasts are duplicated | Ensure the vote enters VotingPlugin once, regional proxies do not run VotingPlugin, Votifier forwarding is not duplicating delivery, and `SendVotesToAllServers` matches the intended behavior. |
| Offline rewards remain cached after recovery | Confirm the backend appears in status, a complete presence snapshot is accepted, the player is reported on the correct backend, and all instances contain merged PRs #1550 and #1551. |

## Source references

- [Dedicated routing merge (PR #1551)](https://github.com/BenCodez/VotingPlugin/pull/1551)
- [Backend presence foundation (PR #1550)](https://github.com/BenCodez/VotingPlugin/pull/1550)
- [Development `bungeeconfig.yml`](https://github.com/BenCodez/VotingPlugin/blob/master/VotingPlugin/src/main/resources/bungeeconfig.yml)
- [Development `BungeeSettings.yml`](https://github.com/BenCodez/VotingPlugin/blob/master/VotingPlugin/src/main/resources/BungeeSettings.yml)
- [Development proxy implementation](https://github.com/BenCodez/VotingPlugin/blob/master/VotingPlugin/src/main/java/com/bencodez/votingplugin/proxy/VotingPluginProxy.java)

