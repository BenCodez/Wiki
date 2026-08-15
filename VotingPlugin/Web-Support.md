---
title: Web Support
description: Display VotingPlugin data through third-party web integrations
published: true
date: 2026-08-14T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2025-08-30T22:18:31.670Z
---

# Web Support

VotingPlugin does not include a first-party web dashboard. Third-party projects can read VotingPlugin's SQL data and display vote statistics, but their compatibility, maintenance status, and security model are separate from VotingPlugin.

## Third-party integrations

- [VoteTop](https://www.spigotmc.org/resources/vt-votetop.36368/) — standalone vote leaderboard.
- [VoteTop for NamelessMC](https://www.spigotmc.org/resources/vt-votetop-for-namelessmc.36872/) — older NamelessMC integration.
- [Nameless-VotingPlugin](https://github.com/samerton/Nameless-VotingPlugin) — community NamelessMC module. An alternate package is available from the [NamelessMC resource page](https://namelessmc.com/resources/resource/2-namelessmc-voting-plugin-integration/).

These links are provided as third-party options, not as guarantees that a project supports VotingPlugin 7.1.1 or the current NamelessMC release. Check the integration's supported schema and versions before deploying it.

## VotingPlugin storage

For VotingPlugin 7.1.1, the backend storage key is:

```yaml
DataStorage: MYSQL
```

Do **not** use `StorageType`; VotingPlugin does not read that key. Configure the matching `MySQL`/`DbType` and JDBC-driver settings from the bundled [7.1.1 `Config.yml`](https://github.com/BenCodez/VotingPlugin/blob/7.1.1/VotingPlugin/src/main/resources/Config.yml).

## Database hardening

- Create a separate, least-privilege database user for the website. Prefer read-only access to only the tables and columns the integration needs.
- Do not reuse VotingPlugin's database password in web application source code, public configuration, screenshots, or support logs.
- Keep the database on a private network or restrict its firewall to the game servers and web host.
- Use encrypted database transport when traffic crosses hosts or untrusted networks, and validate the database certificate where the driver supports it.
- Protect the website with HTTPS and keep the web integration, CMS, and dependencies updated.
- Back up the database before installing an integration that performs migrations or writes to VotingPlugin tables.

Test a copy of the data first when an integration has not been verified against your VotingPlugin release.
