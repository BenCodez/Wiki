---
title: Multi-Proxy REDIS
description: Configure REDIS communication between multiple VotingPlugin proxies
published: true
date: 2026-07-26T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2025-08-30T22:18:17.279Z
---

# Multi-Proxy REDIS

> Configure each proxy as its own working VotingPlugin proxy network before enabling multi-proxy support. Each proxy network may use a different backend forwarding method.
{.is-info}

When a proxy network already uses `BungeeMethod: REDIS`, give each network a different regular Redis prefix so their backend traffic does not overlap.

Use the following command to check multi-proxy connectivity:

```text
/votingpluginproxy multiproxystatus
```

A status message should appear in the console of each configured proxy.

## Primary proxy

Choose one proxy as the primary proxy. The primary normally receives votes from VotifierPlus and coordinates the multi-proxy system.

## Example configuration

```yaml
MultiProxySupport: true

# Enable only on the primary proxy.
PrimaryServer: true

# Give only one network reward when configured with the matching options.
MultiProxyOneGlobalReward: false

# Current multi-proxy methods include REDIS and SOCKETS.
MultiProxyMethod: REDIS

MultiProxyRedis:
  # Reuse the normal Redis connection only when the proxy itself uses BungeeMethod: REDIS.
  UseExistingConnection: false
  Host: localhost
  Port: 6379
  Username: 'votingplugin'
  Password: 'replace-with-a-secret'

# Unique name for this proxy.
ProxyServerName: proxy1

# Names of the other proxies. A non-primary proxy normally lists the primary.
ProxyServers:
  - proxy2
  - proxy3
```

For one global reward across the entire multi-proxy network, configure both options as follows on every proxy:

```yaml
MultiProxyOneGlobalReward: true
SendVotesToAllServers: false
```

Leaving `SendVotesToAllServers` enabled can forward the same vote to multiple backend servers and allow more than one reward.

Keep Redis on a private network or behind firewall rules that admit only the
configured proxy addresses. Require a non-empty username and password, keep
the credentials identical on participating proxies, and never publish them in
screenshots or configuration examples. `Host: localhost` is valid only when
Redis runs on the same machine as every connecting proxy.

> Multi-proxy support is advanced. Test vote forwarding, duplicate prevention, reconnect behavior, and reward delivery before using it in production.
{.is-warning}
