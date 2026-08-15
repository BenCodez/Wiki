---
title: Global Data Handling
description: Sync time changes between multiple servers
published: true
date: 2026-08-14T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2025-08-30T22:18:11.336Z
---

# Global Data Handling (Work in Progress)

> ⚠️ **Release status**
>
> VotingPlugin 7.1.1 includes `GlobalData`, but its bundled configuration labels the feature **work in progress** and says to use it with caution. Test coordinated resets and keep a current database backup before enabling it on a production network.
{.is-warning}

---

## Overview

**Global Data Handling** makes the **proxy** (BungeeCord/Velocity) coordinate time changes and total resets across backend servers. Instead of each backend completing a time change independently, the proxy waits for participating servers before the final reset work completes.

This is intended to improve consistency for **TopVoter** and **VoteParty** resets across multiple servers. It is not required for ordinary proxy vote forwarding.

---

## How It Works

When enabled, the proxy coordinates daily, weekly, and monthly changes.

During a time change:

- The proxy signals participating servers to process the change.
- Votes received during this time are cached with timestamps.
- Once the required servers finish—or a bounded stale-server rule applies—totals are reset and cached votes are processed.

Release 7.1.1 checks coordination progress every 10 seconds. A server that never starts processing can be skipped after 30 minutes; a server that starts but remains unfinished can be skipped after two hours. A server that has not been seen online for roughly 12 hours is excluded from the recent-server set instead of delaying the change.

These thresholds describe the released implementation, not recommended outage targets.

---

## Requirements

- 🗄️ **Shared SQL data**  
  Global data uses an additional SQL table for inter-server coordination. It can reuse the main connection or use a separately configured connection.

- 🔌 **Supported communication path**  
  The 7.1.1 default comments recommend **PLUGINMESSAGING**. They say **SOCKETS** should work but is not fully tested. Do not assume another method is supported for GlobalData until a released configuration or implementation confirms it.

- ⚙️ **Proper server naming**  
  Each participating backend must have a unique `Server` value in `BungeeSettings.yml`.

- 🕓 **Consistent time settings**  
  `TimeHourOffSet` and related time settings must agree across the network.

---

## Benefits

✅ Votes are cached during coordinated time changes  
✅ Backends finish reset processing under one proxy-controlled operation  
✅ TopVoter and VoteParty reset data can remain consistent across servers  
✅ Recently offline or stuck servers are handled by bounded skip rules  
✅ `TimeHourOffSet` can align the network's change time

---

## Drawbacks and cautions

⚠️ Normal coordination introduces a delay while participating servers finish.  
⚠️ A recently offline or failed server can delay completion for 30 minutes to two hours, depending on whether it started processing.  
⚠️ Votes received during that period remain cached and are processed afterward.  
⚠️ The feature requires an additional SQL table, though not necessarily an additional connection when `UseMainMySQL: true`.  
⚠️ The released configuration still labels the feature work in progress.

---

## Related Command

| Command | Description |
|----------|-------------|
| `/votingpluginproxy forcetimechange <DAY\|WEEK\|MONTH>` | Forces a manual coordinated time-change event. |

Use the command only during a controlled test or maintenance window with a current backup.

---

## Example Configuration

### `bungeeconfig.yml`

```yaml
# Global SQL data handling between server communications
GlobalData:
  Enabled: false
  # Use existing main connection
  UseMainMySQL: true
  # Custom SQL settings (if not using main)
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

### `BungeeSettings.yml`

```yaml
# Global SQL data handling between server communications
GlobalData:
  Enabled: false
  # Use existing main connection
  UseMainMySQL: true
  # Custom SQL settings (if not using main)
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

- Set `GlobalData.Enabled: true` in both `bungeeconfig.yml` and every participating backend's `BungeeSettings.yml`.
- Use matching `Prefix` and connection settings.
- The system respects `BlockedServers` in `bungeeconfig.yml`.
- Keep `TimeHourOffSet` consistent.
- Verify every intended server can process a normal forwarded vote before testing a forced time change.
- Confirm cached votes are delivered once after the test completes.

---

🧩 **Intended use:** large networks that require coordinated TopVoter/VoteParty time changes rather than independent backend resets.
