---
title: Global Data Handling
description: Sync time changes between multiple servers
published: true
date: 2025-08-31T03:39:51.007Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:11.336Z
---

## This is a work in progress feature. Contact BenCodez if you run into problems

Global data handling will make proxy server be primary server to handle time changes instead of every server for itself. This allows all servers to finishing processing time changes and store top voters before resetting totals.

In order for this feature to work MySQL needs to be used to create another table to handle server communication. This can use the existing mysql settings (and without opening another connection) or use different settings altogether.

Intended for PLUGINMESSAGING and SOCKETS. May eventually work for MYSQL setup in the future.

Benefits:
- Bungee will cache votes during time changes
  - Stores time of vote
- TopVoter rewards should all be given out on each server
- TopVoter information will all be stored correctly if enabled
- All servers finish there time handling before totals are reset
- No one server randomly resetting all totals if it was offline during time change
- Supports TimeHourOffSet

Cons:
- Slightly longer delay on time change, by only 5-10 seconds though (If a player is online on each server then there is almost no delay)
- If a server is offline or error occurs during time change then it will take 30 minutes to 2 hours before the time change is skipped on that server
  - Votes are cached with times during this, so they should all process afterword
  - This time delay may change in the future
  - There won't be a major delay if server has been offline for atleast 12 hours
- Requires another mysql table to use (but can avoid using another connection)
- Still a work in progress, issues could appear
- Server name must be set properly in BungeeSettings.yml

Related commands:
- /votingpluginbungee forcetimechange (TimeType)

bungeeconfig.yml settings:

    # Global mysql data handle for between server commmunications
    # This is NOT required for bungee voting to work
    # This is still a WIP, use with caution
    # This will create a different table then from users storing server info to process
    #
    # If you use this you need to enable this on BungeeSettings.yml on each server with votingplugin
    # Make sure server name is set correctly in BungeeSettings.yml or this will not work correctly
    # 
    # Please use PLUGINMESSAGING for this, SOCKETS should work as well, but not fully tested
    #
    # This will make votes cache until time change has finished processing
    # In the event a server is offline or time change fails, the time change process
    # will continue after a set amount of time (in essense skipping a specific server)
    # This will also respect blocked servers
    GlobalData:
      Enabled: false
      # Use existing connection above
      UseMainMySQL: true
      # Mysql settings only used if above is false
      Host: ''
      # Default port is 3306
      Port: 3306 
      Database: ''
      Username: ''
      Password: ''
      # Max number of connections
      MaxConnections: 1
      # Must be the same on all servers
      Prefix: ''
      #UseSSL: true
      #PublicKeyRetrieval: false
      #Attempt to use mariadb driver
      #UseMariaDB: false
      
    # Time offset for time changes
    # Must match on all servers
    TimeHourOffSet: 0


BungeeSettings.yml settings:

    # Global mysql data handle for between server commmunications
    # This is NOT required for bungee voting to work
    # This is still a WIP, use with caution
    # This will create a different table then from users storing server info to process
    #
    # If you use this you need to enable this on BungeeSettings.yml on each server with votingplugin
    # Make sure server name is set correctly in BungeeSettings.yml or this will not work correctly
    # 
    # Please use PLUGINMESSAGING for this, SOCKETS should work as well, but not fully tested
    #
    # This will make votes cache until time change has finished processing
    # In the event a server is offline or time change fails, the time change process
    # will continue after a set amount of time (in essense skipping a specific server)
    # This will also respect blocked servers in bungeeconfig.yml
    GlobalData:
      Enabled: false
      # Use existing mysql connection from config.yml
      UseMainMySQL: true
      # Mysql settings only used if above is false
      Host: ''
      # Default port is 3306
      Port: 3306 
      Database: ''
      Username: ''
      Password: ''
      # Max number of connections
      MaxConnections: 1
      # Must be the same on all servers
      Prefix: ''
      #UseSSL: true
      #PublicKeyRetrieval: false
      #Attempt to use mariadb driver
      #UseMariaDB: false
