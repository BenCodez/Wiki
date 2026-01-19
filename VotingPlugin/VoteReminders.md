---
title: Vote Reminders
description: 
published: true
date: 2026-01-19T01:56:35.139Z
tags: 
editor: markdown
dateCreated: 2026-01-19T01:56:35.139Z
---

# Vote Reminders (New System)

The **Vote Reminders** system reminds players when they are able to vote again.  
This is a **fully redesigned replacement** for the old `VoteReminding` system, providing **greater flexibility, precision, and control**.

Unlike the legacy system, reminders are:
- **Config-driven** (not hardcoded intervals)
- **Priority-based**
- **Condition-aware**
- **Cooldown-aware (per reminder + global)**
- **Reward-based** (uses the standard reward API)

---

## 📌 Key Concepts

### What is a Vote Reminder?
A **Vote Reminder** is a named rule that:
1. Triggers at a specific **event** (login, first join, interval, etc.)
2. Checks **conditions** (can vote, first join, online time, etc.)
3. Respects **cooldowns**
4. Executes **rewards** (messages, commands, titles, Discord, etc.)

---

## 🧠 Architecture Overview

| Component | Purpose |
|---------|--------|
| `VoteReminderOptions` | Global settings + defaults |
| `VoteReminders` | Individual reminder definitions |
| Reminder `Type` | What triggers the reminder |
| Conditions | When the reminder is allowed to fire |
| Cooldowns | Prevent spam |
| Rewards | What actually happens |

Reminders are **sorted by priority**, then evaluated until:
- One fires (**StopAfterMatch = true**), or
- All are evaluated (**StopAfterMatch = false**)

---

## ⚙️ Global Configuration (`VoteReminderOptions`)

```yml
VoteReminderOptions:
  Enabled: true
  StopAfterMatch: true
  GlobalCooldown: 10m
  DefaultPriority: 0

  Defaults:
    Cooldown: 0
    Delay: 0
    Conditions:
      # CanVoteAny: true
      # CanVoteAll: true
      # MinOnlineTime: 2m
      # FirstJoin: true
    Rewards:
      Messages:
        Player: "&aYou can vote! Sites left: %sitesavailable%"
```

### Options Explained

| Option | Description |
|------|------------|
| `Enabled` | Master toggle for all reminders |
| `StopAfterMatch` | Stop evaluating once a reminder fires |
| `GlobalCooldown` | Shared cooldown across **all** reminders |
| `DefaultPriority` | Used if a reminder has no Priority |
| `Defaults.*` | Applied when a reminder omits values |

---

## 🔔 Defining Reminders (`VoteReminders`)

Each reminder is defined under:

```yml
VoteReminders:
  <ReminderName>:
    ...
```

Example:

```yml
VoteReminders:
  OnLogin:
    Type: LOGIN
    Priority: 50
    Delay: 3s
    Cooldown: 3m
    Conditions:
      CanVoteAny: true
    Rewards:
      Messages:
        Player: "&aWelcome back! You can vote now on &e%sitesavailable%&a sites."
```

---

## 🧩 Reminder Types

| Type | Trigger |
|----|--------|
| `LOGIN` | Player login |
| `FIRST_JOIN` | First-ever join |
| `INTERVAL` | Repeating interval |

### INTERVAL Example

```yml
VoteReminders:
  IntervalReminder:
    Type: INTERVAL
    Interval: 30m
    Cooldown: 2h
    Conditions:
      CanVoteAny: true
```

**Important:**  
For `INTERVAL`, the effective cooldown is:

```
max(Interval, Cooldown)
```

---

## 🧪 Conditions

Conditions control **whether a reminder may fire**.

| Condition | Meaning |
|---------|--------|
| `CanVoteAny` | Player can vote on at least one site |
| `CanVoteAll` | Player can vote on all sites |
| `MinOnlineTime` | Player must be online for this long |
| `FirstJoin` | Only first-ever join |

Example:

```yml
Conditions:
  CanVoteAny: true
  MinOnlineTime: 2m
```

---

## ⏱ Cooldowns & Delay

### Delay
```yml
Delay: 5s
```
- Waits before evaluating conditions
- Useful on login to allow vote data to sync

### Cooldown
```yml
Cooldown: 10m
```
- Per-player
- Per-reminder
- Stored persistently

---

## 🎁 Rewards

Vote Reminders use the **standard VotingPlugin Reward API**.

Anything that works in:
- `votesites.yml`
- `specialrewards.yml`

…also works here.

### Example

```yml
Rewards:
  Messages:
    Player: "&aYou can vote now!"
```

### Available Placeholders

| Placeholder | Description |
|-----------|-------------|
| `%sitesavailable%` | Number of sites player can still vote on |
| All standard reward placeholders | Supported |

---

## 🔐 Permissions

Players must have **one** of:

- `VotingPlugin.Player`
- `VotingPlugin.Login.RemindVotes`

---

## 🔄 Legacy Migration

The old `VoteReminding` system is **automatically migrated once**.

### What gets migrated

| Legacy Option | New System |
|--------------|-----------|
| `Enabled` | `VoteReminderOptions.Enabled` |
| `RemindDelay` | INTERVAL reminder |
| `RemindOnLogin` | LOGIN reminder |
| `Rewards` | Default Rewards |

Migration:
- Runs once
- No backups
- Sets `VoteReminderOptions.MigratedFromLegacy: true`

---

## 🛠 Debugging

Enable debug output:

```yml
DebugLevel: EXTRA
```

Look for log entries starting with:

```
[VoteReminders]
```

---

## ✅ Recommended Setup

Most servers should start with:
- `LOGIN` reminder
- `INTERVAL` reminder
- `StopAfterMatch: true`
- `CanVoteAny: true`

---

## 🚀 Summary

✔ Fully configurable  
✔ Priority-based  
✔ Condition-aware  
✔ Cooldown-safe  
✔ Reward-driven  
✔ Legacy-compatible  

The new Vote Reminders system is **powerful by design**, while remaining simple to configure.