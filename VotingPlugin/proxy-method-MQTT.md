---
title: Proxy method MQTT
description: Configure the MQTT proxy communication method
published: true
date: 2026-08-14T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2025-08-31T00:18:41.324Z
---

# Method MQTT

MQTT uses a broker to carry VotingPlugin messages between the proxy and backend servers. It does not replace VotingPlugin's shared SQL storage requirement.

## Standard topology

- VotifierPlus or NuVotifier and VotingPlugin run on the proxy.
- VotingPlugin runs on each participating backend.
- Every instance uses the same SQL database/table naming.
- Every instance connects to the same MQTT broker and prefix.
- Each proxy and backend has a **unique** MQTT `ClientID`.

Disable VotifierPlus/NuVotifier forwarding targets in this standard layout; VotingPlugin performs the backend forwarding.

## Required settings

### Proxy: `bungeeconfig.yml`

```yaml
BungeeMethod: MQTT

MQTT:
  ClientID: proxy
  BrokerURL: "tcp://mqtt.internal.example:1883"
  Username: 'votingplugin'
  Password: 'replace-with-a-secret'
  Prefix: ''
```

Configure the proxy `Database` section as well.

### Each backend: `BungeeSettings.yml`

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

Give every backend a different `Server` and `ClientID`.

### Each backend: `Config.yml`

Configure the same SQL database and use:

```yaml
AllowUnjoined: true
```

This lowercase-d spelling is the backend key. The proxy key is separately named `AllowUnJoined`; in the standard 7.1.1 proxy-managed layout it remains `false`, so the proxy validates the player before forwarding.

With `BungeeManageTotals: true` (the supported release default), totals are owned by the proxy. Set `SendVotesToAllServers: false` when one backend should execute the per-vote reward for the network.

## Secure MQTT

- Keep the broker on a private network or VPN and restrict its listener to participating hosts.
- Require authentication and use a dedicated broker account with only the required topics.
- Use TLS or a trusted private tunnel when MQTT crosses hosts or networks. The default `tcp://` example is not encrypted.
- Never publish credentials, broker certificates, or complete connection strings in screenshots or logs.
- Keep client IDs unique; duplicate IDs cause clients to disconnect each other.

## Testing

1. Restart the proxy and every backend after changing the method or client IDs.
2. Run `/votingpluginproxy status`.
3. Run `/votingpluginproxy vote <player> <site>`.
4. Confirm exactly the intended backend or backends process the vote.
5. Then send a real/listener-generated vote to test Votifier and public network reachability.

For duplicates, verify unique backend `Server` names, unique MQTT client IDs, `SendVotesToAllServers`, backend `ProcessRewards`, and disabled Votifier forwarding.
