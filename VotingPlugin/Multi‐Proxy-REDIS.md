---
title: Multi Proxy REDIS
description: 
published: true
date: 2025-09-01T15:48:09.971Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:17.279Z
---

> Setup each proxy as it's own proxy network for VotingPlugin before setting multi-proxy up, each proxy can use a different proxy method
{.is-info}

> Note if using REDIS (Not for multi-proxy method) you will need to set a different redis prefix for each proxy network (This is so that all proxies can use REDIS at the same time without issue)
{.is-warning}

> Check connection status with /votingpluginbungee multiproxystatus - should see a message on each proxy in console
{.is-info}

## Pick one proxy to be primary, that is the server votifier goes on and will be the one to control everything

Config options for REDIS Only

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
    MultiProxyMethod: REDIS

    ##########################################
    # REDIS Settings
    ##########################################

    # Set multiproxymethod to REDIS to use redis
    MultiProxyRedis:
      # If true the plugin will use the exsiting connection set above
      # Must be on REDIS method to use this setting
      UseExistingConnection: false
      Host: localhost
      Port: 6379
      Username: ''
      Password: ''
      
    # Set each server it's own proxy name here (can be anything)
    ProxyServerName: proxy1

    # Set names of other proxy servers
    # Must match what's set as the proxy server name above from other servers
    # On non primary proxy server just set the primary proxy server name here
    ProxyServers:
    - proxy2
    - proxy3