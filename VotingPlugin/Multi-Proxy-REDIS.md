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
/votingpluginbungee multiproxystatus
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

# Current multi-proxy methods include REDIS and SOCKET.
MultiProxyMethod: REDIS

MultiProxyRedis:
  # Reuse the normal Redis connection only when the proxy itself uses BungeeMethod: REDIS.
  UseExistingConnection: false
  Host: localhost
  Port: 6379
  Username: ''
  Password: ''

# Unique name for this proxy.
ProxyServerName: proxy1

# Names of the other proxies. A non-primary proxy normally lists the primary.
ProxyServers:
  - proxy2
  - proxy3
```

When `MultiProxyOneGlobalReward` is enabled, enable it consistently on all proxies and review `SendVotesToAllServers` so the configured reward behavior matches the intended topology.

> Multi-proxy support is advanced. Test vote forwarding, duplicate prevention, reconnect behavior, and reward delivery before using it in production.
{.is-warning}

> **AI disclosure:** This documentation update was written with assistance from ChatGPT.
