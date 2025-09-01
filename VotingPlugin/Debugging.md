---
title: Debugging
description: 
published: true
date: 2025-08-30T22:18:06.824Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:06.105Z
---

Proxy debug:

    Debug: false

Spigot/Backend Servers:


       Config.yml
       # Debug levels:
       # NONE
       # INFO - basic debug
       # EXTRA - General debug with extra info, usually use this
       # DEV - EXTREME DEBUG, only use in super rare cases
       DebugLevel: NONE

       BungeeSettings.yml:
       # Enables more debug messages for communication between servers
       BungeeDebug: false