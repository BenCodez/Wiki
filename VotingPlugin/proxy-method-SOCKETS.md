---
title: Proxy method SOCKETS
description: Details of SOCKETS setup
published: true
date: 2025-08-31T00:22:50.356Z
tags: 
editor: markdown
dateCreated: 2025-08-31T00:22:49.805Z
---

> Votifier+VotingPlugin on proxy server, and only VotingPlugin is required on backend servers
{.is-info}

> All servers use the same mysql table
{.is-info}

> Running on velocity requires a mysql driver to be installed, one available as a plugin here if needed http://bencodez.com/job/MySQLDriver/
{.is-info}

> Requires ability for servers to communicate via sockets, which isn't always possible (Requires a open port for each server)
{.is-warning}




# Method SOCKETS
- Uses sockets to communicate between servers
- Requires a port for each server (similar to votifier)


## Required Settings
### Proxy (bungeeconfig.yml):
- `BungeeMethod: SOCKETS`
- MySQL database information
- Set host/port (Use 0.0.0.0 for the ip if unsure)
- specify all servers socket info

### Backend Servers:
BungeeSettings.yml:
- `BungeeMethod: SOCKETS`
- `UseBungeecord: true`
- 'Server: SERVERNAMEHERE` (Set server name on each server, matching names from proxy server)
- Set host/port - each server needs a different port (Use 0.0.0.0 for the ip if unsure)
- Specify proxy socket info

Config.yml:
- MySQL database information
- `AllowUnjoined: true` (Proxy handles this)

---

See default config files for every setting, as this is very customizable. 

If you want one reward per vote across the entire network then disable SendVotesToAllServers


## Troubleshooting:
Testing communication:
- Check status & working condition with /votingpluginbungee status
- See console for results

Test voting:
- Run bungee test vote with /votingpluginbungee vote (player) (site)

Double/Extra Rewards:
- Ensure server names in BungeeSettings.yml differ and match names in proxy server
- NuVotifier forwarding method set to none (And no votifier plugins on spigot servers)

Not working:
- Restart all servers
- Ensure required settings are set
- Ensure ports are open and servers can reach eachother
- Test communication and run test votes (if that works check votiifer)

