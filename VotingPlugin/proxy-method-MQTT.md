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

> Running on velocity requires a mysql driver to be installed, one available as a plugin here if needed http://bencodez.com/job/MySQLDriver/
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
- 'Server: SERVERNAMEHERE` (Set server name on each server, matching names from proxy server)
- Input MQTT info

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
- Test communication and run test votes (if that works check votiifer)

