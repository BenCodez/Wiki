---
title: Multi Proxy Sockets
description: 
published: true
date: 2025-09-01T15:47:18.586Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:16.369Z
---

> Each proxy needs a open port for communication
{.is-warning}


> Setup each proxy as it's own proxy network for VotingPlugin before setting multi-proxy up, each proxy can use a different proxy method
{.is-info}

> Note if using REDIS (Not for multi-proxy method) you will need to set a different redis prefix for each proxy network (This is so that all proxies can use REDIS at the same time without issue)
{.is-warning}

> Check connection status with /votingpluginbungee multiproxystatus - should see a message on each proxy in console
{.is-info}

Additional things required:
- Primary server/main proxy needs to be set as primary server (by enabling option). This server will handle adding totals and such and forward the vote to the other proxies.
- Each sub proxy needs a host/port and needs to be set in the primary proxy under MutliProxyServers.
- You also need to have the same secretkey.key file across all proxies (copy/paste from one server after it generates)

Check connection status with /votingpluginbungee multiproxystatus

    ##########################################
    # Multi-proxy setup
    # This is still a WIP, use with caution
    # Primary server  needs votifier and config option enabled
    # Set socket host on each proxy and primary server set sub proxies
    # All servers should be on pluginmessaging or sockets setup
    ##########################################

    # Support for multiple proxies
    MultiProxySupport: false

    # Enable on primary proxy server with votifier
    PrimaryServer: false

    # If enabled, player will only get 1 reward on a server on the network
    # Must be enabled on all proxies for this to work
    # Must also disable sendtoallservers
    MultiProxyOneGlobalReward: false

    # Multi-proxy available methods:
    #  SOCKET
    #  REDIS
    MultiProxyMethod: SOCKET

    ##########################################
    # SOCKET settings for mutli-proxy
    ##########################################

    # Set this for each proxy
    MultiProxySocketHost:
      Host: 0.0.0.0
      Port: 1234

    # Set other sub proxies here
    # On non primary proxy only set primary proxy
    MultiProxyServers:
      secondproxy:
        Host: 0.0.0.0
        Port: 1235