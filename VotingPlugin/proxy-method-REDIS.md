---
title: Proxy method REDIS
description: Details of REDIS setup
published: true
date: 2025-08-31T00:16:25.441Z
tags: 
editor: markdown
dateCreated: 2025-08-31T00:16:24.909Z
---

> Votifier+VotingPlugin on proxy server, and only VotingPlugin is required on backend servers
{.is-info}

> All servers use the same mysql table
{.is-info}

> Running on Velocity requires a MySQL driver. Install the [MySQLDriver build](https://bencodez.com/job/MySQLDriver/) if the platform does not already provide one.
{.is-info}



# Method REDIS
- Uses REDIS to communicate between servers
- The most reliable method currently for large networks 


## Required Settings
### Proxy (bungeeconfig.yml):
- `BungeeMethod: REDIS`
- MySQL database information
- Input REDIS info

### Backend Servers:
BungeeSettings.yml:
- `BungeeMethod: REDIS`
- `UseBungeecord: true`
- `Server: SERVERNAMEHERE` (set a unique server name matching the proxy configuration)
- Input REDIS info

Config.yml:
- MySQL database information
- `AllowUnjoined: true` (Proxy handles this)

---

See default config files for every setting, as this is very customizable. 

If you want one reward per vote across the entire network then disable SendVotesToAllServers

## Secure Redis

Keep Redis on a private network or behind firewall rules that allow only the
proxy and backend addresses. Configure a non-empty Redis username and password
on every VotingPlugin instance; all instances in this communication group must
use the same connection details and prefix. Do not expose the default Redis
port to the public Internet or include credentials in screenshots and logs.

`Host: localhost` works only when Redis is on the same machine as that
VotingPlugin instance. Use an internal address when separate hosts share the
broker.


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
- Ensure required settings are working
- Test communication and run test votes (if that works check Votifier)
