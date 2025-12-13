---
title: Multi Proxy Setup
description: 
published: true
date: 2025-12-13T23:23:09.763Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:15.618Z
---

> This should only be used if each proxy has different backend servers, otherwise votes will duplicate
{.is-warning}

> Setup each proxy as it's own proxy network for VotingPlugin before setting multi-proxy up, each proxy can use a different proxy method
{.is-info}

> Note if using REDIS (Not for multi-proxy method) you will need to set a different redis prefix for each proxy network (This is so that all proxies can use REDIS at the same time without issue)
{.is-warning}

> Check connection status with /votingpluginbungee multiproxystatus - should see a message on each proxy in console
{.is-info}



## 2 Methods available:
- [REDIS](/VotingPlugin/Multi‐Proxy-REDIS) (Recommeneded)
- [Sockets](/VotingPlugin/Multi-Proxy-Sockets)

