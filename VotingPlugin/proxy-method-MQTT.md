---
title: Proxy method MQTT
description: Details of MQTT setup
published: true
date: 2025-08-31T00:18:41.870Z
tags: 
editor: markdown
dateCreated: 2025-08-31T00:18:41.324Z
---

> Votifier+VotingPlugin on proxy server, and only VotingPlugin is required on backend servers
{.is-info}

> All servers use the same mysql table
{.is-info}

> Running on Velocity requires a MySQL driver. Install the [MySQLDriver build](https://bencodez.com/job/MySQLDriver/) if the platform does not already provide one.
{.is-info}



# Method MQTT
- Uses MQTT broker to communicate between servers
- Works quite similar to REDIS


## Required Settings
### Proxy (bungeeconfig.yml):
- `BungeeMethod: MQTT`
- MySQL database information
- Input MQTT info

### Backend Servers:
BungeeSettings.yml:
- `BungeeMethod: MQTT`
- `UseBungeecord: true`
- `Server: SERVERNAMEHERE` (set a unique server name matching the proxy configuration)
- Input MQTT info

Config.yml:
- MySQL database information
- `AllowUnjoined: true` (Proxy handles this)

---

See default config files for every setting, as this is very customizable. 

If you want one reward per vote across the entire network then disable SendVotesToAllServers

## Secure MQTT

Give every proxy and backend a unique MQTT `ClientID`. Require broker
credentials, keep the broker on a private network or VPN, and restrict its
listener to the participating server addresses. The default `tcp://` transport
must not cross an untrusted or public network without transport protection
provided by the broker or network. Do not include MQTT credentials in
screenshots, logs, or a public repository.


## Troubleshooting:
Testing communication:
- Check status and connectivity with `/votingpluginproxy status`.
- See console for results

Test voting:
- Run a proxy test vote with `/votingpluginproxy vote <player> <site>`.

Double/Extra Rewards:
- Ensure server names in BungeeSettings.yml differ and match names in proxy server
- NuVotifier forwarding method set to none (And no votifier plugins on spigot servers)

Not working:
- Restart all servers
- Ensure required settings are set
- Test communication and run test votes (if that works check Votifier)
