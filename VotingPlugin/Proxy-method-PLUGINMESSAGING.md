---
title: Proxy method PLUGINMESSAGING
description: Details of PLUGINMESSAGING setup
published: true
date: 2025-08-31T00:11:00.080Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:00.302Z
---

> Votifier+VotingPlugin on proxy server, and only VotingPlugin is required on backend servers
{.is-info}

> All servers use the same mysql table
{.is-info}

> Running on velocity requires a mysql driver to be installed, one available as a plugin here if needed http://bencodez.com/job/MySQLDriver/
{.is-info}



# Method PLUGINMESSAGING
- Uses PLUGINMESSAGING to communicate between servers (Requires online players to send messages, does not effect offline votes)
- Nearly a drop and play method, not recommended for large networks



## Required Settings
### Proxy (bungeeconfig.yml):
- `BungeeMethod: PLUGINMESSAGING`
- MySQL database information

### Backend Servers:
BungeeSettings.yml:
- `BungeeMethod: PLUGINMESSAGING`
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
- Check status & working condition with /votingpluginbungee status (Requires players to be online to test)
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


### Prevent Exploits (A bit overkill):
- These options are extra failsafes to prevent possible exploits
- These 2 settings must match on all servers
- Please ensure plugin messaging is working before enabling
- PluginMessageChannel:
  - Defaults to vp:vp
  - Channel used to send messages
- PluginMessageEncryption:
  - Defaults to false
  - When enabled secretkey.key must match on all servers (Generates when enabled)
  - Encrypts all messaging data and prevents someone trying to force votes

