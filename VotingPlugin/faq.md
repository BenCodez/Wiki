---
title: FAQ
description: 
published: true
date: 2025-08-31T03:35:54.873Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:10.405Z
---

### 1. /vote says "vote here: www.votelinkhere.com"  
This is venturechat overtaking the command

### 2. How do I add rewards for crate keys?:

    Rewards:
      Commands:
      - 'command here %player%'

### 3. How to test a vote?  
/av vote (player) (site)

### 4. YML Error  
This means the file is formatted incorrectly, use a website such as https://yaml-online-parser.appspot.com/ to clearly see the error, contact BenCodez if you can't fix it

### 5. No voting site with the service site: 'SERVICE SITE HERE'
This means either votifier isn't working or service site is incorrect  
Check here: https://github.com/BenCodez/VotingPlugin/wiki/Votifier-Troubleshooting  

### 6. No plugin.yml / failed to load
Redownload the jar. Most likely a corrupt download/jar file

### 7. Extreme Troubleshooting/debugging:
Set DebugLevel to EXTRA in Config.yml  
For bungee related issues enable BungeeDebug in BungeeSettings.yml & debug on bungee.  

### 8. Hex support?
Yes, format is as follows:  
Hex format: &#FF0000#  

### 9. No reload command?  
There is, /av reload and /av reloadall (Also reloads user storage)

### 10. Out of memory/resource limit reached
If your not out of memory you probably hit the resource limit. You can try this following solution for pterodactyl:
Upgrade the "container_pid_limit":  to 1024 into /etc/pterodactyl/config.yml default is 512