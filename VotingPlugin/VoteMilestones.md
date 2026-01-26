---
title: VoteMilestones
description: 
published: true
date: 2026-01-26T02:35:50.692Z
tags: 
editor: markdown
dateCreated: 2026-01-26T02:35:50.692Z
---

# VoteMilestones

VoteMilestones allow you to run rewards when a player’s **vote totals, points, or site counts** reach specific conditions.

This system replaces legacy milestone systems such as `FirstVote`, `Cumulative`, and `MileStones`, while remaining fully backward-compatible through automatic migration.

This page explains **how VoteMilestones really work**, followed by **lots of real examples**.

---

## Where VoteMilestones are configured

All VoteMilestones are configured in:

```
plugins/VotingPlugin/SpecialRewards.yml
```

They live under two root sections:

```yml
VoteMilestonesOptions:
VoteMilestones:
```

---

## How VoteMilestones work

On **every vote**, VotingPlugin:

1. Updates the relevant total (votes, points, sites, etc.)
2. Evaluates **all VoteMilestones**
3. Determines which milestones match
4. Applies **group selection rules**
5. Applies **limits** (cooldowns / windows)
6. Executes rewards

VoteMilestones are **not automatically one-time** unless you use a `Limit`.

---

## VoteMilestonesOptions (group selection)

Groups control **how many milestones can trigger per vote**.

```yml
VoteMilestonesOptions:
  Groups:
    Default: ALL
    RankRewards: HIGHEST
```

### Group modes

| Mode      | Meaning                                        |
| --------- | ---------------------------------------------- |
| `ALL`     | All matching milestones in the group run       |
| `FIRST`   | Only the first matching milestone (file order) |
| `HIGHEST` | Only the “best” milestone runs                 |

**HIGHEST rules**

1. `At` milestones beat `Every`
2. Higher matched value wins
3. Earlier file order breaks ties

If a milestone has **no Group**, it automatically uses `Default`.

---

## VoteMilestone fields

Basic structure:

```yml
VoteMilestones:
  ExampleId:
    Enabled: true
    Total: ALLTIME_VOTES
    At: 100
    Group: Default
    Limit:
      Type: NONE
    Rewards:
      Commands:
        - "say %player% hit %amount%"
```

### Core keys

| Key       | Purpose                                |
| --------- | -------------------------------------- |
| `Enabled` | Enable/disable milestone               |
| `Total`   | What value is checked                  |
| `At`      | Exact totals (supports ranges & lists) |
| `Every`   | Repeating trigger                      |
| `Group`   | Group selection bucket                 |
| `Limit`   | Prevents re-triggering                 |
| `Rewards` | What runs when matched                 |

---

## Supported totals (`Total:`)

| Value            | Meaning                  |
| ---------------- | ------------------------ |
| `ALLTIME_VOTES`  | Lifetime votes           |
| `DAILY_VOTES`    | Votes today              |
| `WEEKLY_VOTES`   | Votes this week          |
| `MONTHLY_VOTES`  | Votes this month         |
| `POINTS`         | Vote points              |
| `ALLSITES_TODAY` | Unique sites voted today |

Friendly aliases like `AllTime`, `Daily`, `Weekly`, `Monthly`, and `Points` also work.

---

## Triggers: `At` vs `Every`

### `Every` (multiples)

```yml
Every: 25
```

Triggers when the total is divisible by 25 (25, 50, 75, …)

---

### `At` (exact totals)

#### Single value

```yml
At: 50
```

#### List

```yml
At:
  - 25
  - 50
  - 100
```

#### Ranges (with optional steps)

```yml
At:
  - "10..100 step 10"
  - "250..500 step 50"
```

Ranges are expanded safely and automatically.

---

## Limits

Limits control **how often** a milestone can trigger.

```yml
Limit:
  Type: COOLDOWN
  Duration: 12h
```

### Limit types

| Type           | Behavior          |
| -------------- | ----------------- |
| `NONE`         | No limit          |
| `WINDOW_DAY`   | Once per day      |
| `WINDOW_WEEK`  | Once per week     |
| `WINDOW_MONTH` | Once per month    |
| `COOLDOWN`     | Once per duration |

Duration supports:

```
30m, 12h, 1d, 2w, 1mo
```

---

# Examples

---

## Example: First-ever vote

```yml
VoteMilestones:
  FirstVote:
    Enabled: true
    Total: ALLTIME_VOTES
    At: 1
    Rewards:
      Messages:
        Player: "&aThanks for your first vote!"
      Commands:
        - "eco give %player% 100"
```

---

## Example: First vote of the day

```yml
VoteMilestones:
  FirstVoteToday:
    Enabled: true
    Total: DAILY_VOTES
    At: 1
    Rewards:
      Messages:
        Player: "&eThanks for voting today!"
```

---

## Example: Every 10 total votes

```yml
VoteMilestones:
  Every10Votes:
    Enabled: true
    Total: ALLTIME_VOTES
    Every: 10
    Rewards:
      Commands:
        - "crate give %player% vote 1"
```

---

## Example: Multiple exact milestones

```yml
VoteMilestones:
  BigMilestones:
    Enabled: true
    Total: ALLTIME_VOTES
    At:
      - 25
      - 50
      - 100
    Rewards:
      Broadcast:
        Message: "&6%player% reached %amount% total votes!"
```

---

## Example: Range + step milestones

```yml
VoteMilestones:
  SteppedMilestones:
    Enabled: true
    Total: ALLTIME_VOTES
    At:
      - "10..100 step 10"
      - "250..500 step 50"
    Rewards:
      Commands:
        - "eco give %player% %amount%"
```

---

## Example: Monthly milestone

```yml
VoteMilestones:
  Monthly50:
    Enabled: true
    Total: MONTHLY_VOTES
    At: 50
    Rewards:
      Commands:
        - "points give %player% 25"
```

---

## Example: Vote points rewards

```yml
VoteMilestones:
  PointRewards:
    Enabled: true
    Total: POINTS
    At:
      - 100
      - 500
      - 1000
    Rewards:
      Commands:
        - "lp user %player% parent add vip"
```

---

## Example: All vote sites today

```yml
VoteMilestones:
  AllSitesToday:
    Enabled: true
    Total: ALLSITES_TODAY
    At: 5
    Limit:
      Type: WINDOW_DAY
    Rewards:
      Messages:
        Player: "&aYou voted on all sites today!"
```

---

## Example: Cooldown-based milestone

```yml
VoteMilestones:
  VoteBonusCooldown:
    Enabled: true
    Total: ALLTIME_VOTES
    Every: 50
    Limit:
      Type: COOLDOWN
      Duration: 12h
    Rewards:
      Commands:
        - "eco give %player% 250"
```

---

## Example: Rank rewards (HIGHEST group)

```yml
VoteMilestonesOptions:
  Groups:
    RankRewards: HIGHEST

VoteMilestones:
  Rank50:
    Group: RankRewards
    Total: ALLTIME_VOTES
    At: 50
    Rewards:
      Commands:
        - "lp user %player% parent add bronze"

  Rank100:
    Group: RankRewards
    Total: ALLTIME_VOTES
    At: 100
    Rewards:
      Commands:
        - "lp user %player% parent add silver"
```

---

## Legacy migration

The following legacy sections are automatically migrated at startup:

```
FirstVote
FirstVoteToday
Cumulative
MileStones
AllSites
AlmostAllSites
```

New configurations should always use **VoteMilestones**.

---

## Placeholders

| Placeholder       | Meaning                 |
| ----------------- | ----------------------- |
| `%player%`        | Player name             |
| `%amount%`        | Matched milestone value |
| `%total%`         | Same as amount          |
| `%votemilestone%` | Milestone ID            |
| `%total_type%`    | Total type enum         |
