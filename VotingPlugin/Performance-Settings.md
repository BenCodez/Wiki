---
title: Performance Settings
description: 
published: true
date: 2025-11-07T02:04:13.072Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:19.128Z
---

# ⚙️ VotingPlugin Performance & Optimization Guide

This page provides a **brief overview of configuration options** in VotingPlugin that can help **improve performance**, reduce background processing, and fine-tune MySQL load handling.  
*(This page is still a work in progress — more sections will be added soon.)*

---

## 🗄️ MySQL Settings

These settings control how VotingPlugin interacts with your MySQL database.  
Increasing connections can improve responsiveness slightly, but using **more than 2 connections rarely provides any benefit**.

    MaxConnections: 1

✅ **Recommended:** `1` or `2`  
⚠️ Avoid setting this too high — it only increases resource usage.

---

## 🏆 TopVoter Settings

The **TopVoter system** tracks player totals across daily, weekly, monthly, and all-time categories.  
Disabling categories you don’t use reduces memory and SQL usage — especially helpful on **large networks**.

```yaml
    # Enable only what you need
    LoadTopVoter:
      AllTime: true
      Monthly: true
      Weekly: false
      Daily: false
```

To further reduce background load, lower the number of players processed:

    # Maximum number of players to show on top voter
    # Set to -1 for no limit
    MaxiumNumberOfTopVotersToLoad: 1000

✅ **Recommendation:** Limit to a few hundred for large player bases.

---

## 🔄 Background Task Settings

VotingPlugin performs various **background updates** (for cooldowns, reminders, placeholders, signs, etc.).  
The options below let you balance performance vs. feature richness.

### Per-Site Cooldowns

    PerSiteCoolDownEvents: false

> When enabled, allows per-site cooldown rewards and reminders — but increases CPU usage.  
> Disable if not needed.

---

### Global Cooldown Checks

    DisableCoolDownCheck: false

> When `true`, disables all cooldown checking.  
> Has no effect on reminders, but removes cooldown logic completely.

---

### Interact Events

    DisableInteractEvent: false

> When `true`, disables processing of **PlayerInteractEvent** (used for signs/skulls).  
> Slightly improves performance if you don’t use vote signs or heads.

---

### Vote Streaks & Totals

    UseVoteStreaks: true
    UseHighestTotals: true

> Disable these if you don’t use **vote streaks** or **best totals**.  
> This lowers SQL queries and speeds up player data saving.

---

### JavaScript Placeholders

    UseJavascriptPlaceholders: false

> ⚠️ Has **significant performance impact**, even if no JavaScript is actively used.  
> Only enable for advanced math or logic placeholders.

---

### AlwaysUpdate

    AlwaysUpdate: false

> Forces background updates to run on every interval, even if no changes occurred.  
> 🔧 **Not recommended** — increases unnecessary database activity.

---

### Update With Players Online Only

    UpdateWithPlayersOnlineOnly: false

> When enabled, only runs background updates if **at least one player** is online.  
> Recommended for smaller servers to reduce idle activity.

---

### Delay Between Background Updates

    DelayBetweenUpdates: 3

> Interval (in minutes) between background checks like **sign updates** or **top voter sync**.  
> 3–10 minutes is ideal for most setups.  
> Longer = lower background activity, slower updates after votes.

---

### Extra Background Update

    ExtraBackgroundUpdate: false

> Performs **additional player data checks** across servers.  
> Only needed in multi-server setups where updates don’t trigger correctly.

---

### Tab Completion Optimization

    DisableAdvancedTab: false

> Disables checking permissions for tab completion.  
> May improve command responsiveness slightly for large permission setups.

---

## 🧩 Placeholder Settings

Default PlaceholderAPI options are already optimized.  
You can learn more on the dedicated wiki page:

🔗 [PlaceholderAPI Expansion Documentation](https://github.com/BenCodez/VotingPlugin/wiki/PlaceHolderAPI-Expansion)

---

## 💀 Skull Settings (GUI Optimization)

Skulls are used to display player heads in **VoteTop GUIs**.  
They can be heavy on performance — especially on large servers.

### Preload Skulls

    PreloadSkulls: false

> Preloads **all skull textures** on startup.  
> ⚠️ Can cause significant memory usage and startup delay.

---

### Load Skulls (Recommended)

    LoadSkulls: true

> Caches skulls as players appear in VoteTop GUIs.  
> Recommended over PreloadSkulls — faster in use, lighter on memory.

---

## 🧠 General Tips

- Disable **unused systems** like streaks or daily top voters.  
- Avoid **preloading skulls** unless absolutely necessary.  
- Use **fewer MySQL connections** unless you experience database queueing.  
- Keep **DelayBetweenUpdates** between **3–10 minutes**.  
- Run `/av status` to monitor background update intervals and timings.

---

✅ **Summary of Recommended Performance Settings**

| Option | Recommended | Reason |
|--------|--------------|--------|
| `MaxConnections` | 1–2 | Efficient MySQL usage |
| `LoadTopVoter.Weekly/Daily` | false | Skip unused categories |
| `UseVoteStreaks` | false (if unused) | Reduces SQL load |
| `UseHighestTotals` | false (if unused) | Fewer queries |
| `UseJavascriptPlaceholders` | false | Avoids heavy parsing |
| `PreloadSkulls` | false | Reduces memory |
| `LoadSkulls` | true | Balanced performance |
| `AlwaysUpdate` | false | Only update when needed |
| `DelayBetweenUpdates` | 3–10 | Best balance |
| `UpdateWithPlayersOnlineOnly` | true | Skip idle processing |

---

> ⚡ Tip: Test configuration changes gradually and monitor timings with `/av debug` or `/av status`.  
> If your server uses multiple instances, make sure all share the same MySQL configuration for consistency.
{.is-info}
