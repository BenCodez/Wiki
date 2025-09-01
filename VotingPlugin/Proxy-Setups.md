---
title: Proxy-Setups
description: Details of proxy setups
published: true
date: 2025-09-01T15:40:28.614Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:02.764Z
---

> Running on velocity requires a mysql driver to be installed, one available as a plugin here if needed http://bencodez.com/job/MySQLDriver/
{.is-info}

> All methods require MYSQL with all servers pointing to the same database
{.is-info}

> Votifier is only required on proxy as VotingPlugin does the forwarding
{.is-info}




# Proxy methods:
- [PLUGINMESSAGING](/VotingPlugin/Proxy-method-PLUGINMESSAGING) (Easiest, drop and play)
- [REDIS](/VotingPlugin/proxy-method-REDIS) (Requires a REDIS server)
- [MQTT](/VotingPlugin/proxy-method-MQTT) (Requires a MQTT broker)
- [SOCKETS](/VotingPlugin/proxy-method-SOCKETS) (Requires port access between servers)
- [MYSQL](/VotingPlugin/proxy-method-MYSQL) (Uses MYSQL database)


## How it works
![untitled_diagram___mermaid_chart-2025-08-30-234204.png](/untitled_diagram___mermaid_chart-2025-08-30-234204.png)

Vote reaches votifier on proxy when then gets processed by VotingPlugin. VotingPlugin will then forward accordingly.

#### Abilities:
- Global or per server rewards
- Proxy vote party or per server vote party
- Global time change sync (Uses GlobalData setting)
- Block/whitelist certain servers
- Sync with other proxies
- And more

### [Multi-Proxy](/en/VotingPlugin/Multi-Proxy-Setup)
- Use PLUGINMESSAGING or REDIS with multiple proxies
- Experimental but working



