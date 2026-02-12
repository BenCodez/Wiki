---
title: VoteStreak System
description: 
published: true
date: 2026-02-12T02:13:10.098Z
tags: 
editor: markdown
dateCreated: 2026-02-12T02:13:10.098Z
---

# Vote Streak System (7.0+)

The **VoteStreak system** allows you to reward players for maintaining
consistent voting streaks across days, weeks, or months.

It supports: - Forgiveness for missed periods - Flexible vote
requirements per period - Proxy/global support - Full Rewards system
integration - Multiple streak definitions at once

------------------------------------------------------------------------

## Location

    /plugins/VotingPlugin/SpecialRewards.yml

Section:

``` yaml
VoteStreaks:
```

------------------------------------------------------------------------

# Basic Structure

``` yaml
VoteStreaks:
  <IdName>:
    Type: DAILY
    Enabled: true
    Requirements:
      Amount: 3
      VotesRequired: 3
    AllowMissedAmount: 1
    AllowMissedPeriod: 7
    Rewards:
      Commands:
        - "say %player% completed a streak!"
```

------------------------------------------------------------------------

# Advanced Streak Logic Explained

Understanding how streak validation works is critical.

## 1️⃣ No Misses Allowed (Strict Mode)

Config:

``` yaml
AllowMissedAmount: 0
AllowMissedPeriod: 3
```

Example timeline:

Day 1 ✔\
Day 2 ✔\
Day 3 ✔ → Reward\
Day 4 ✘ → Streak resets

------------------------------------------------------------------------

## 2️⃣ With Forgiveness (AllowMissedAmount: 1)

Config:

``` yaml
AllowMissedAmount: 1
AllowMissedPeriod: 7
```

Example timeline:

Day 1 ✔\
Day 2 ✔\
Day 3 ✘ (allowed miss)\
Day 4 ✔\
Day 5 ✔ → Reward

------------------------------------------------------------------------

## 3️⃣ Window Tracking Behavior

AllowMissedPeriod controls how far back the system checks.

Example:

AllowMissedPeriod: 7\
Amount: 5\
AllowMissedAmount: 1

The system checks the last 7 periods and validates: - At least 5
successful periods - No more than 1 missed period

If that condition fails → streak resets.

------------------------------------------------------------------------

# Proxy / Global Streak Examples

## Per-Server Streaks (Independent)

Use different IDs per server:

``` yaml
VoteStreaks:
  SurvivalDaily:
  SkyblockDaily:
```

Each server tracks its own streak progress.

------------------------------------------------------------------------

## Global Streak (Shared Across Network)

Use the same ID on all servers:

``` yaml
VoteStreaks:
  GlobalDaily:
```

This causes the streak to be shared network-wide.

Changing the ID will reset stored streak data.

------------------------------------------------------------------------

# Internal Logic Explanation (For Developers)

When a vote is received:

1.  Identify streak ID\
2.  Determine current period (daily/weekly/monthly)\
3.  Increment vote count for that period\
4.  Validate if VotesRequired is met\
5.  Update streak success/failure tracking\
6.  Apply AllowMissedAmount logic\
7.  If streak count \>= Amount → Execute Rewards

Important behavior:

-   Streaks are evaluated per vote event.
-   Period boundaries are calendar-based.
-   Missed periods are evaluated during streak validation.
-   Rewards trigger only once when threshold is reached.
-   Data is stored under the streak ID.

------------------------------------------------------------------------

# Rewards Section

VoteStreaks use the full Rewards system.

Supported reward types:

-   Commands
-   Messages
-   Items
-   Broadcast
-   RandomCommands

------------------------------------------------------------------------

# Placeholder Reference Table

  Placeholder       Description
  ----------------- ------------------------------------
  %player%          Player name
  %streak%          Current streak count
  %type%            Streak type (DAILY/WEEKLY/MONTHLY)
  %amount%          Required streak amount
  %votesrequired%   Votes required per period
  %currentvotes%    Current votes in this period

------------------------------------------------------------------------

# Best Practices

✔ Keep streak IDs descriptive\
✔ Avoid excessive overlapping streak rewards\
✔ Carefully configure forgiveness rules\
✔ Test reset behavior before production\
✔ Combine with VoteMilestones for layered rewards

------------------------------------------------------------------------

This system replaces the legacy VoteStreak section and provides
significantly more flexibility and control.