---
title: Proxy method MYSQL
description: Details of the MYSQL proxy setup
published: true
date: 2026-07-26T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2025-08-31T00:27:03.022Z
---

# Method MYSQL

> In the standard layout, VotifierPlus and VotingPlugin run on the proxy, while VotingPlugin runs on each backend server. Custom vote-routing layouts may differ.
{.is-info}

The `MYSQL` method uses a shared MySQL-backed message queue. It creates the `VotingPlugin_message_queue` table and may not be compatible with every MySQL-compatible service.

## Required settings

### Proxy: `bungeeconfig.yml`

```yaml
BungeeMethod: MYSQL
```

Configure the shared MySQL connection and provide enough connections for the proxy and backend workload. The current documentation recommendation is at least five total connections across a small network, with additional headroom for larger installations.

### Backend servers: `BungeeSettings.yml`

```yaml
UseBungeecord: true
BungeeMethod: MYSQL
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
/votingpluginbungee status
/votingpluginbungee vote <player> <site>
```

Check the proxy and backend consoles for status results and queue-processing errors.

## Duplicate or extra rewards

- Ensure every backend has a unique and correct `Server` value.
- Disable NuVotifier forwarding when VotingPlugin is handling forwarding.
- Avoid running a separate vote listener on backend servers unless the custom topology intentionally requires it.

## Troubleshooting

- Restart the proxy and all backend servers after configuration changes.
- Verify the shared database credentials and permissions.
- Confirm that `VotingPlugin_message_queue` can be created and updated.
- Check `/votingpluginbungee status` before testing vote rewards.

> **AI disclosure:** This documentation update was written with assistance from ChatGPT.
