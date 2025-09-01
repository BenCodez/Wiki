---
title: Transferring data storage within plugin
description: 
published: true
date: 2025-09-01T02:58:46.994Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:28.333Z
---

All available data storage options:
- FLAT (Will be removed soon)
- SQLITE
- MYSQL

The plugin has the capabilities to transfer player data between data storage options.

### Warning: existing values will be replaced. This does not combine totals.  

Commands:  
/av convertfromdata (data storage) - Convert to current data storage from one specified - imports data  
/av converttodata (data storage) - Convert from current data storage to one specified - exports data  

Simply run the command, use console to run commands and view current status.

This can take hours depending on how many users. There will be a console message for every 100 users converted stating how many are left to convert.

It is recommended to not be setting data (voting or anything else) while converting.