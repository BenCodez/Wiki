---
title: Transferring data storage within plugin
description: 
published: true
date: 2025-11-07T02:30:01.283Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:28.333Z
---

# Data storage and migration

VotingPlugin stores player votes, totals, and statistics in SQLite or an
external SQL database. Back up the source and destination before converting.

---

## Select storage

| Type | Description |
|-------|--------------|
| **SQLITE** | Local `Users.db` database; the release default for standalone servers |
| **MYSQL** | External MySQL, MariaDB, or PostgreSQL database; required for proxy networks |

The setting is `DataStorage`, not `StorageType`:

```yaml
DataStorage: SQLITE
```

`FLAT` remains a deprecated legacy conversion source in the code, but it is
not listed as a current storage choice in the 7.1.1 default configuration. Do
not select it for a new installation.

### MySQL, MariaDB, and PostgreSQL

Keep `DataStorage: MYSQL` for all three external database engines, then select
the driver family with `Database.DbType`:

```yaml
DataStorage: MYSQL
Database:
  Host: 'database.internal.example'
  Port: 5432
  Database: 'votingplugin'
  Username: 'votingplugin'
  Password: 'replace-with-a-secret'
  DbType: POSTGRESQL
```

Valid `DbType` values in release 7.1.1 are `MYSQL`, `MARIADB`, and
`POSTGRESQL`. A matching JDBC driver must be present:

| `DbType` | Driver class |
|---|---|
| `MYSQL` | `com.mysql.cj.jdbc.Driver` |
| `MARIADB` | `org.mariadb.jdbc.Driver` |
| `POSTGRESQL` | `org.postgresql.Driver` |

If the platform does not provide the driver, install the
[MySQLDriver build](https://bencodez.com/job/MySQLDriver/), which the released
default configuration identifies as bundling all three. Keep database
credentials out of screenshots and support logs, grant the database account
only the permissions VotingPlugin needs, and restrict database network access
to the server and proxy hosts.

---

## Convert existing data

The conversion commands copy user records between supported storage systems.
They do not change `DataStorage` for you or clear destination-only records.
Matching destination records can be updated, so always use backups rather
than treating conversion as a reversible merge.

---

### 🧭 Commands

| Command | Description |
|----------|-------------|
| `/av convertfromdata <storage>` | Copy from the specified source into the currently configured storage |
| `/av converttodata <storage>` | Copy from the currently configured storage into the specified target |

For example, while `DataStorage: SQLITE` is active:

```text
/av converttodata MYSQL
```

This copies SQLite user data into the configured external database. After it
finishes, stop the server, set `DataStorage: MYSQL`, and restart. Do not switch
storage or let new votes arrive while a conversion is running.

Run these commands from the console so progress and failures remain visible.

---

## ⚙️ Conversion Details

- Configure and test the destination connection before converting.
- Stop vote intake and other data-modifying activity during the copy.
- Review the complete console output; a final command message is not a
  substitute for checking earlier database exceptions.
- Verify representative totals, points, last-vote times, and streaks before
  reopening voting.

---

## Recommendation

- Use `MYSQL` for large or multi-server setups.
- Use `SQLITE` for small standalone servers.
- Do not use `FLAT` for a new installation.

---

Confirm the active storage in `Config.yml` under `DataStorage` and in the
startup log.
