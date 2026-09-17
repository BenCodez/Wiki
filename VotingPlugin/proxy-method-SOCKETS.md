---
title: Proxy method SOCKETS
description: Configure VotingPlugin direct sockets between a proxy and backend servers
published: true
date: 2026-08-11T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2025-08-31T00:22:49.805Z
---

# Method SOCKETS

`SOCKETS` is VotingPlugin's advanced direct-TCP communication method. Use
`PLUGINMESSAGING` for most networks. Choose `SOCKETS` only when every proxy and
backend can reach explicitly controlled private listener ports.

VotifierPlus and VotingPlugin normally run on the proxy; VotingPlugin runs on
each backend. All instances must use the same external database.

## Address roles

Each instance has a listening address and one or more peer addresses:

| Setting | Role |
|---|---|
| Proxy `BungeeServer` | Address and port the proxy listens on |
| Proxy `SpigotServers.<name>` | Address and port the proxy connects to for that backend |
| Backend `BungeeServer` | Address and port the backend connects to on the proxy |
| Backend `SpigotServer` | Address and port that backend listens on |

Use a private IP address or internal DNS name that is reachable from the peer.
`0.0.0.0` is a wildcard **bind** address, not a connectable destination. Avoid
it when an exact private interface address works. If the host requires a
wildcard bind, restrict the port with a firewall before starting VotingPlugin.
Never place these listener ports directly on the public Internet.

## Proxy configuration

In the proxy `bungeeconfig.yml`:

```yaml
BungeeMethod: SOCKETS

BungeeServer:
  Host: '10.0.0.10'
  Port: 1297

SpigotServers:
  lobby:
    Host: '10.0.0.21'
    Port: 1298
  survival:
    Host: '10.0.0.22'
    Port: 1298
```

The keys under `SpigotServers` must match the unique `Server` value on each
backend. Backends on different IP addresses may reuse a port; two processes on
the same address need different listener ports.

Also configure the shared external database and the normal proxy settings
described in [Proxy Setups](/VotingPlugin/Proxy-Setups).

## Backend configuration

On the `lobby` backend, in `BungeeSettings.yml`:

```yaml
UseBungeecord: true
BungeeMethod: SOCKETS
Server: lobby

BungeeServer:
  Host: '10.0.0.10'
  Port: 1297

SpigotServer:
  Host: '10.0.0.21'
  Port: 1298
```

Use that backend's own address and unique `Server` value on every other
backend. In backend `Config.yml`, configure the same external database and set
`AllowUnjoined: true` when the proxy performs the joined-player validation.

## Shared key and firewall

The SOCKETS implementation uses `secretkey.key` from the VotingPlugin data
folder. Stop the network, keep the key generated for one instance, and copy
the same file to the proxy and every participating backend. Do not paste the
key into configuration, screenshots, logs, or support messages. Limit file
access to the service account that runs the server.

Apply network rules in both directions:

- allow inbound proxy `BungeeServer.Port` only from backend server addresses;
- allow each backend `SpigotServer.Port` only from the proxy address; and
- deny all other sources, especially public interfaces.

The shared key does not replace firewall restrictions.

## Restart and verify

Fully restart the proxy and all backends after changing the method, addresses,
ports, or shared key. Then, from the proxy console:

```text
/votingpluginproxy status
/votingpluginproxy vote <player> <site>
```

The proxy command requires `votingpluginproxy.admin` when run by a player.
Keep `BungeeDebug: true` only while troubleshooting; review the proxy and every
backend log, then disable it when finished.

If status fails, verify the listener address, peer address, matching ports,
firewall source rules, shared key, unique backend `Server` names, and that no
other process already owns a listener port.

To avoid duplicate rewards, keep Votifier forwarding disabled and do not run a
second vote listener on the backends unless a custom topology explicitly
requires it.
