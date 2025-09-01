---
title: Time Changes
description: 
published: true
date: 2025-09-01T02:59:48.487Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:26.884Z
---

VotingPlugin has events to detect time changes which are based on server time. 

This can be offset with `TimeHourOffSet: 0` in Config.yml, just change the number.

With 6.13+ you can now set timezone with `TimeZone: 'UTC"`

You can view current plugin time with `/av CurrentPluginTime`.

To force time changes use `/av forcetimechange (TimeType)`. Must also be done from console.

TimeTypes:
- DAY
- WEEK
- MONTH

If you want the plugin to bypass time changes on startup you can set `IgnoreTime: true` in ServerData.yml. You might need to add this. You could also edit the day/week/month in ServerData.yml as well.

