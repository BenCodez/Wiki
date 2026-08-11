---
title: Global Data Handling
description: Sync time changes between multiple servers
published: true
date: 2025-11-06T02:31:25.255Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:11.336Z
---

# Global Data Handling (Work in Progress)

> ⚠️ **Work in Progress Feature**
>
> This feature is still being developed, but is stable.  
> Contact **BenCodez** if you encounter any problems or unexpected behavior.
{.is-warning}

---

## Overview

**Global Data Handling** makes the **proxy** (Bungee/Velocity) act as the **primary server** for processing time changes and resetting totals.  
Instead of each backend handling its own time change independently, the proxy coordinates the process — ensuring all servers finish updating before any totals reset.

This feature improves reliability when using **TopVoter** or **VoteParty** resets across multiple servers.

---

## How It Works

When enabled, the proxy manages the timing of vote resets (daily, weekly, monthly).  
During a time change:
- The proxy signals all connected servers to pause vote processing.
- Votes received during this time are **cached** (with timestamps).
- Once all servers report completion, totals reset and cached votes are re-applied.

If a server is offline, the process will automatically skip that server after a set period — preventing the network from stalling indefinitely.

---

## Requirements

- 🗄️ **MySQL required**  
  Global data uses an additional MySQL table for inter-server coordination.  
  It can use the **same MySQL connection** defined in your config or a separate one.

- 🔌 **Proxy Support**  
  Intended for **PLUGINMESSAGING** and **SOCKETS** setups.  
  Support for **MySQL method** may be added later.

- ⚙️ **Proper Server Naming**  
  Each backend must have a **unique server name** set in `BungeeSettings.yml`.

---

## Benefits

✅ Bungee will **cache votes** safely during time changes (stores timestamps)  
✅ **TopVoter rewards** distribute correctly across all servers  
✅ Ensures **consistent TopVoter data** when enabled  
✅ All servers **finish processing time changes together**  
✅ Prevents random resets if a server was offline  
✅ Supports **TimeHourOffSet** configuration for time alignment

---

## Drawbacks

⚠️ **Slight delay** (usually 5–10 seconds) during time changes.  
⚠️ If a server is offline or fails during a time change, it may take **30 min – 2 hours** before that server is skipped.  
 • Votes received during this time are cached (with timestamps) and processed afterward.  
 • Delay only applies if the server went offline *recently* — if it’s been offline for a long period (≈ 12 hours +), it will **not** slow down the process.  
 • This delay behavior may be adjusted in future updates.  
⚠️ Requires an extra MySQL table (but not an extra connection if `UseMainMySQL: true`).  
⚠️ Still experimental — unexpected issues may occur.

---

## Related Command

| Command | Description |
|----------|-------------|
| `/votingpluginproxy forcetimechange <DAY\|WEEK\|MONTH>` | Forces a manual time change event. |

---

## Example Configuration

### bungeeconfig.yml
```yaml
# Global MySQL data handling between server communications
GlobalData:
  Enabled: false
  # Use existing connection from config.yml
  UseMainMySQL: true
  # Custom MySQL settings (if not using main)
  Host: ''
  Port: 3306
  Database: ''
  Username: ''
  Password: ''
  MaxConnections: 1
  # Must be identical on all servers
  Prefix: ''
  #UseSSL: true
  #PublicKeyRetrieval: false
  #UseMariaDB: false

# Time offset for time changes (must match across servers)
TimeHourOffSet: 0
```
---

### BungeeSettings.yml
```yaml
# Global MySQL data handling between server communications
GlobalData:
  Enabled: false
  # Use existing MySQL connection from config.yml
  UseMainMySQL: true
  # Custom MySQL settings (if not using main)
  Host: ''
  Port: 3306
  Database: ''
  Username: ''
  Password: ''
  MaxConnections: 1
  # Must be identical on all servers
  Prefix: ''
  #UseSSL: true
  #PublicKeyRetrieval: false
  #UseMariaDB: false
```
---

## Notes

- Ensure **GlobalData.Enabled** is set to `true` in both **bungeeconfig.yml** and **BungeeSettings.yml**.  
- All servers must share the same `Prefix` and MySQL configuration if using `UseMainMySQL: true`.  
- This system will respect **BlockedServers** settings in `bungeeconfig.yml`.  
- Time synchronization and resets must occur with consistent `TimeHourOffSet` across all servers.

---

🧩 **Intended Use:**  
This feature is ideal for large networks where accurate **TopVoter synchronization** is important, and where time changes need to be coordinated globally instead of per-server.

---

*Still under development — feedback is welcome.*
