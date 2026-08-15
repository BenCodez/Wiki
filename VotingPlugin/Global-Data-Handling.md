---
title: Global Data Handling
description: Coordinate time changes and total resets across a proxy network
published: true
date: 2026-08-14T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2025-08-30T22:18:11.336Z
---

# Global Data Handling

> **Availability:** VotingPlugin 7.1.1 includes `GlobalData`, but its bundled configuration labels the feature **work in progress** and says to use it with caution. Treat it as experimental and test backups and reset behavior before production use.
{.is-warning}

## Purpose

`GlobalData` coordinates daily, weekly, and monthly time changes across a proxy network. The proxy tracks participating backends, waits for their processing, and keeps votes queued while a coordinated time change is active.

It is **not required** for ordinary proxy vote forwarding.

## Release 7.1.1 behavior

During a coordinated time change:

1. The proxy starts the shared process.
2. Participating backends process their reset/time-change work.
3. Votes received during the process are cached with timestamps.
4. The coordinator completes after the required servers finish or a bounded stale-server rule applies.
5. Cached votes are processed afterward.

The released coordinator checks progress every 10 seconds. A backend that never starts can be skipped after 30 minutes; a backend that starts but remains unfinished can be skipped after two hours. A backend not seen online for roughly 12 hours is excluded from the recent-server set instead of delaying the process.

These thresholds describe 7.1.1 implementation behavior, not a recommended outage target.

## Requirements

- Enable `GlobalData.Enabled: true` on the proxy and participating backends.
- Use matching database connection/prefix settings.
- Give every backend a unique `Server` value.
- Keep `TimeHourOffSet` consistent.
- Ensure the proxy and backends can communicate through the selected `BungeeMethod`.
- Keep backups of the SQL data before first enabling coordinated resets.

The 7.1.1 default comments recommend `PLUGINMESSAGING`. They say `SOCKETS` should work but is not fully tested. Do not assume future support for another method until a released default/configuration confirms it.

## Proxy configuration

```yaml
GlobalData:
  Enabled: true
  UseMainMySQL: true
  Host: ''
  Port: 3306
  Database: ''
  Username: ''
  Password: ''
  MaxConnections: 1
  Prefix: ''
  #UseSSL: true
  #PublicKeyRetrieval: false
  #UseMariaDB: false

TimeHourOffSet: 0
```

When `UseMainMySQL: true`, the proxy reuses its main database connection. Otherwise configure a matching dedicated connection.

## Backend configuration

```yaml
GlobalData:
  Enabled: true
  UseMainMySQL: true
  Host: ''
  Port: 3306
  Database: ''
  Username: ''
  Password: ''
  MaxConnections: 1
  Prefix: ''
  #UseSSL: true
  #PublicKeyRetrieval: false
  #UseMariaDB: false
```

Enable the section in each participating backend's `BungeeSettings.yml`. The system also respects proxy blocked-server routing.

## Operational checks

Before relying on it:

- take a current database backup;
- verify every backend has a unique name and matching time offset;
- run a normal vote through every intended route;
- observe one daily/weekly/monthly transition in a test environment;
- confirm queued votes are delivered once;
- confirm a deliberately offline noncritical backend does not cause unexpected rewards or resets.

The related administrative command is:

```text
/votingpluginproxy forcetimechange <DAY|WEEK|MONTH>
```

Use it only with a current backup and during a controlled maintenance/test window.
