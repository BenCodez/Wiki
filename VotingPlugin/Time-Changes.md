---
title: Time Changes
description: 
published: true
date: 2025-11-10T01:11:56.600Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:26.884Z
---

# ⏰ Time Change Handling

VotingPlugin uses **Java’s LocalDateTime** with **ZoneId.of()** to handle time-based features — like daily, weekly, and monthly resets.

---

## ⚙️ Configuration Options

### 🕐 Time Offset

You can shift the plugin’s internal time relative to your system clock:

    TimeHourOffSet: 0

Examples:
- `TimeHourOffSet: -6` → Runs 6 hours **behind** system time  
- `TimeHourOffSet: 2` → Runs 2 hours **ahead** of system time  

---
    
📅 Weekly Offset (6.19.1+)

You can shift the weekly reset by a number of days using:


    TimeWeekOffSet: 0

Examples:
- `TimeWeekOffSet: 1` → Moves the weekly reset 1 day later
- `TimeWeekOffSet: -2` → Moves the weekly reset 2 days earlier

---

### 🌍 Time Zone (6.13+)

You can define a specific time zone in `Config.yml` using standard Java zone IDs.  
VotingPlugin validates these using `ZoneId.of("YourZoneHere")`.

    TimeZone: 'UTC'
    


This is useful when you want weekly resets to start on a different weekday than the default (Monday).
The offset is applied after timezone and hour offset adjustments.

For example, if your server’s week normally resets Monday at midnight and TimeWeekOffSet: 2,
the weekly reset will now occur Wednesday at midnight instead.

#### ✅ Common Working Examples

| Example | Description |
|:--|:--|
| `'UTC'` | Universal Coordinated Time |
| `'America/Regina'` | Central Canada (no daylight savings) |
| `'America/New_York'` | Eastern Time (auto daylight savings) |
| `'America/Los_Angeles'` | Pacific Time |
| `'Europe/London'` | United Kingdom |
| `'Australia/Sydney'` | Eastern Australia |
| `'Asia/Tokyo'` | Japan |

> Use one of the above examples or check the [IANA timezone list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) for your region.  
> If invalid, Java will throw an error when loading.

---

### 🧭 Checking Plugin Time

You can view the time VotingPlugin is currently using:

    /av CurrentPluginTime

---

### 🧨 Forcing Time Changes

To manually trigger a time change (for testing):

    /av forcetimechange (TimeType)

Valid types:
- `DAY`
- `WEEK`
- `MONTH`

Example:
> `/av forcetimechange MONTH`

Must be run from **console**.

---

### 🚫 Skipping Time Changes on Startup

If you need to skip automatic time changes when the server starts,  
set this in `ServerData.yml`:

    IgnoreTime: true

---

## ✅ Summary

| Setting | Description |
|----------|-------------|
| `TimeHourOffSet` | Adjusts time by a set number of hours. |
| `TimeZone` | Uses a valid Java Zone ID to define your region. |
| `IgnoreTime` | Skips time-change events on startup. |
| `/av CurrentPluginTime` | Displays plugin time. |
| `/av forcetimechange` | Forces daily/weekly/monthly reset. |
