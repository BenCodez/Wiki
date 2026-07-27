---
title: Legacy Vote Reminding
description: Archived documentation for the pre-VoteReminders system
published: true
date: 2026-07-26T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2025-08-30T22:18:29.070Z
---

# Legacy Vote Reminding

> This page documents the old `VoteReminding` configuration. New installations should use the current [Vote Reminders system](/VotingPlugin/VoteReminders).
{.is-warning}

The current system uses `VoteReminderOptions` and named entries under `VoteReminders`. It supports priorities, conditions, per-reminder cooldowns, delays, and standard reward sections.

VotingPlugin automatically migrates supported legacy settings once and records the migration with:

```yaml
VoteReminderOptions:
  MigratedFromLegacy: true
```

## Legacy configuration reference

The old system used a single `VoteReminding` section in `Config.yml`:

```yaml
VoteReminding:
  Enabled: true
  RemindOnLogin: true
  RemindOnlyOnce: true
  RemindDelay: 30
  Rewards:
    Messages:
      Player: '&aYou have %sitesavailable% sites to vote on!'
```

Legacy per-site cooldown completion rewards were configured in `VoteSites.yml`:

```yaml
CoolDownEndRewards:
  Messages:
    Player: '&aYou can vote again on %SiteName%!'
```

Do not use this page as the starting point for a new configuration. See [Vote Reminders](/VotingPlugin/VoteReminders) for the active format and migration details.

> **AI disclosure:** This documentation update was written with assistance from ChatGPT.
