---
title: Multi Proxy Sockets
description: Configure direct socket communication between VotingPlugin proxies
published: true
date: 2026-08-11T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2025-08-30T22:18:16.369Z
---

# Multi-Proxy SOCKETS

Configure each proxy as a working VotingPlugin proxy network before enabling
multi-proxy support. Each proxy network may use a different `BungeeMethod` for
its own backends; `MultiProxyMethod` controls only proxy-to-proxy traffic.

Choose one primary proxy. It normally receives Votifier votes and coordinates
totals and forwarding to the other proxies.

## Address and key requirements

`MultiProxySocketHost` is the local listener on the current proxy.
`MultiProxyServers.<name>` is the address that this proxy connects to on a peer.
Use reachable private IP addresses or internal DNS names.

`0.0.0.0` is a wildcard bind address, not a valid peer destination. Avoid it
when an exact private interface address works. If a host requires a wildcard
bind, apply firewall restrictions first. Permit each listener port only from
the other configured proxy addresses and never expose it to the public
Internet.

All participating proxies must have the same `secretkey.key` in their
VotingPlugin data folders. Stop the proxies, retain the key from one instance,
copy it to the others, restrict it to the service accounts, and then restart.

## Primary proxy example

```yaml
MultiProxySupport: true
PrimaryServer: true
MultiProxyOneGlobalReward: false
MultiProxyMethod: SOCKETS

ProxyServerName: proxy1

MultiProxySocketHost:
  Host: '10.0.0.10'
  Port: 1234

MultiProxyServers:
  proxy2:
    Host: '10.0.0.11'
    Port: 1235
```

On `proxy2`, use a unique `ProxyServerName`, bind
`MultiProxySocketHost` to `10.0.0.11:1235`, and list the primary as
`10.0.0.10:1234` under `MultiProxyServers`.

If a proxy network also uses `BungeeMethod: REDIS` for backend communication,
give each separate network a different regular Redis prefix. That prefix is
separate from the SOCKETS multi-proxy setup.

For one global reward across the entire multi-proxy network, configure both
options on every proxy:

```yaml
MultiProxyOneGlobalReward: true
SendVotesToAllServers: false
```

## Verify

After fully restarting every proxy, run:

```text
/votingpluginproxy multiproxystatus
```

Each proxy should log the status message. Test reconnect behavior and vote
delivery in both directions before using the network in production.

> Release 7.1.1's generated `bungeeconfig.yml` shows the singular value
> `SOCKET`, but the released enum is `SOCKETS`. The unknown-value fallback
> happens to select sockets. Use the explicit `SOCKETS` value shown above so
> the configuration matches the implemented method name.
{.is-warning}
