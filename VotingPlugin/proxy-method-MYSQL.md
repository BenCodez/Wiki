---
title: Proxy method MYSQL
description: Details of MYSQL setup
published: true
date: 2026-01-24T17:37:32.925Z
tags: 
editor: markdown
dateCreated: 2025-08-31T00:27:03.022Z
---

> Votifier+VotingPlugin on proxy server, and only VotingPlugin is required on backend servers
{.is-info}

> All servers use the same mysql table
{.is-info}

> Running on velocity requires a mysql driver to be installed, one available as a plugin here if needed http://bencodez.com/job/MySQLDriver/
{.is-info}



# Method MYSQL
- Uses MYSQL to communicate between servers
- This may not work with all mysql databases
- This will create a table called VotingPlugin_message_queue for sending messages
- Set MaxConnections to atleast 5 for mysql across all servers


## Required Settings
### Proxy (bungeeconfig.yml):
- `BungeeMethod: MYSQL`
- MySQL database information
- Increase MaxConnections by atleast one for best performance

### Backend Servers:
BungeeSettings.yml:
- `BungeeMethod: MYSQL`
- `UseBungeecord: true`
- 'Server: SERVERNAMEHERE` (Set server name on each server, matching names from proxy server)

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
- Ensure required settings are working
- Test communication and run test votes (if that works check votiifer)

