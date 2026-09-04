---
title: Proxy method REDIS
description: Configure the Redis proxy communication method
published: true
date: 2026-08-14T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2025-08-31T00:16:24.909Z
---

# Method REDIS

Redis carries VotingPlugin messages between the proxy and backend servers. It does not replace VotingPlugin's shared SQL storage requirement.

## Standard topology

- VotifierPlus or NuVotifier and VotingPlugin run on the proxy.
- VotingPlugin runs on each participating backend.
- Every instance uses the same SQL database/table naming.
- Every instance connects to the same Redis service and communication prefix.

Disable VotifierPlus/NuVotifier forwarding targets in this standard layout; VotingPlugin performs the backend forwarding.

## Required settings

### Proxy: `bungeeconfig.yml`

```yaml
BungeeMethod: REDIS

Redis:
  Host: redis.internal.example
  Port: 6379
  Username: 'votingplugin'
  Password: 'replace-with-a-secret'
  Prefix: ''
  #Db-Index: 0
```

Configure the proxy `Database` section as well.

### Each backend: `BungeeSettings.yml`

```yaml
UseBungeecord: true
BungeeMethod: REDIS
Server: lobby

Redis:
  Host: redis.internal.example
  Port: 6379
  Username: 'votingplugin'
  Password: 'replace-with-a-secret'
  Prefix: ''
  #Db-Index: 0
```

Give every backend a different `Server` value.

### Each backend: `Config.yml`

Configure the same SQL database and use:

```yaml
AllowUnjoined: true
```

This lowercase-d spelling is the backend key. The proxy key is separately named `AllowUnJoined`; in the standard 7.1.1 proxy-managed layout it remains `false`, so the proxy validates the player before forwarding.

With `BungeeManageTotals: true` (the supported release default), totals are owned by the proxy. Set `SendVotesToAllServers: false` when one backend should execute the per-vote reward for the network.

## Secure Redis

- Keep Redis on a private network or behind firewall rules that allow only participating hosts.
- Require a dedicated Redis ACL user and non-empty password with only the commands/channels VotingPlugin needs.
- Do not expose port 6379 to the public Internet or publish credentials in screenshots and logs.
- `Host: localhost` works only when Redis is on the same machine or network namespace as that VotingPlugin instance.
- VotingPlugin 7.1.1 has no direct Redis SSL/TLS option. Direct Redis TLS is planned for the next release and is currently available only in unreleased 7.1.2-SNAPSHOT builds containing commit `3354cc70` or newer. Until that release, use a trusted private tunnel or a local TLS wrapper that accepts VotingPlugin's local plaintext connection and initiates TLS toward Redis when traffic must cross untrusted networks.

## Testing

1. Restart the proxy and every backend after changing the method.
2. Run `/votingpluginproxy status`.
3. Run `/votingpluginproxy vote <player> <site>`.
4. Confirm exactly the intended backend or backends process the vote.
5. Then send a real/listener-generated vote to test Votifier and public network reachability.

For duplicates, verify unique backend `Server` names, a consistent Redis prefix, `SendVotesToAllServers`, backend `ProcessRewards`, and disabled Votifier forwarding.
