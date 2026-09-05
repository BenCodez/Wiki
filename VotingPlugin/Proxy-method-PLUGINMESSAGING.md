---
title: Proxy method PLUGINMESSAGING
description: Details of the PLUGINMESSAGING setup
published: true
date: 2026-07-26T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2025-08-30T22:18:00.302Z
---

# Method PLUGINMESSAGING

> In the standard layout, VotifierPlus and VotingPlugin run on the proxy, while VotingPlugin runs on each backend server. Custom vote-routing layouts may differ.
{.is-info}

All servers must use the same MySQL database for shared player data.

PLUGINMESSAGING is the recommended method for most networks. It uses the proxy messaging channel and requires at least one online player to transmit a plugin message, but offline votes can still be cached and delivered later.

## Required settings

### Proxy: `bungeeconfig.yml`

```yaml
BungeeMethod: PLUGINMESSAGING
```

Also configure the shared MySQL connection.

### Backend servers: `BungeeSettings.yml`

```yaml
UseBungeecord: true
BungeeMethod: PLUGINMESSAGING
Server: SERVERNAMEHERE
```

Each backend must have a unique `Server` value that matches the name known by the proxy.

### Backend servers: `Config.yml`

Configure the same MySQL database used by the rest of the network.

The proxy and backend settings are separate and use different capitalization:

```yaml
# Backend Config.yml
AllowUnjoined: true
```

- Proxy `bungeeconfig.yml`: `AllowUnJoined`
- Backend `Config.yml`: `AllowUnjoined`

In the standard proxy-managed layout, keep proxy `AllowUnJoined: false` so the
proxy rejects votes for players it cannot validate, and set backend
`AllowUnjoined: true` so forwarded votes are not rejected a second time.

## Reward behavior

Disable `SendVotesToAllServers` when the network should give only one server reward per vote. Leave it enabled when each applicable backend should process the forwarded vote.

## Testing

```text
/votingpluginproxy status
/votingpluginproxy vote <player> <site>
```

The status command needs an online player for PLUGINMESSAGING communication.

## Duplicate or extra rewards

- Ensure every backend has a unique and correct `Server` value.
- Disable NuVotifier forwarding when VotingPlugin is handling forwarding.
- Avoid running a separate vote listener on backend servers unless the custom topology intentionally requires it.

## Optional message security

These settings must match on all connected servers:

```yaml
PluginMessageChannel: 'vp:vp'
PluginMessageEncryption: false
```

When encryption is enabled, copy the same `secretkey.key` to every connected server.
Stop the network while replacing the key, restrict the file to the server
service account, and fully restart every instance afterward. Changing the
channel name alone is not a substitute for encryption or normal proxy/backend
network isolation.
