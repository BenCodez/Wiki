---
title: VoteStreak System
description: 
published: true
date: 2026-06-07T22:22:58.028Z
tags: 
editor: markdown
dateCreated: 2026-02-12T02:13:10.098Z
---

# Vote Streak System (7.0+)

The **VoteStreak system** rewards players for maintaining consistent voting streaks across days, weeks, or months.

It supports:

- Daily, weekly, and monthly streaks
- Forgiveness for missed periods
- Flexible vote requirements per period
- Multiple independent streak definitions
- Progress groups with multiple milestones sharing one streak
- One-time and recurring milestone rewards
- Lost-streak rewards for progress groups
- Proxy and global data support
- Full Rewards system integration

---

## Location

```text
/plugins/VotingPlugin/SpecialRewards.yml
```

The configuration is stored under:

```yaml
VoteStreaks:
```

---

# Standard VoteStreaks

A standard VoteStreak has one required streak amount and one Rewards section.

## Basic Structure

```yaml
VoteStreaks:
  DailyStreak:
    Type: DAILY
    Enabled: true
    Recurring: false
    Requirements:
      Amount: 3
      VotesRequired: 3
    AllowMissedAmount: 1
    AllowMissedPeriod: 7
    Rewards:
      Commands:
        - "say %player% completed a voting streak!"
```

In this example, the player must cast at least three votes during a day for that day to count as a successful streak period.

## Standard VoteStreak Options

| Option | Description |
|---|---|
| `Type` | Streak period type. Supported values are `DAILY`, `WEEKLY`, and `MONTHLY`. |
| `Enabled` | Enables or disables the VoteStreak. |
| `Recurring` | Controls whether the reward repeats at multiples of the required amount. |
| `Requirements.Amount` | Number of successful periods required to complete the streak. |
| `Requirements.VotesRequired` | Number of votes required during each period for that period to count. |
| `AllowMissedAmount` | Number of missed periods that may be forgiven. |
| `AllowMissedPeriod` | Number of recent periods used when checking missed-period forgiveness. |
| `Rewards` | Rewards executed when the streak requirement is completed. |

## Recurring Rewards

With:

```yaml
Recurring: false
```

The reward runs when the streak reaches the exact configured amount.

For example, with `Amount: 5`, the reward runs at a streak of 5.

With:

```yaml
Recurring: true
```

The reward repeats at each multiple of the configured amount.

For example, with `Amount: 5`, the reward runs at streaks 5, 10, 15, 20, and so on.

---

# Progress Groups

Progress groups allow multiple milestones to share the same streak progress.

Instead of creating several separate VoteStreaks with their own counters, a progress group defines the streak rules once and places multiple reward milestones under that shared streak.

Progress groups are stored under:

```yaml
VoteStreaks:
  ProgressGroups:
```

## Progress Group Structure

```yaml
VoteStreaks:
  ProgressGroups:
    DailyVoting:
      Type: DAILY
      Enabled: true
      VotesRequired: 1
      AllowMissedAmount: 1
      AllowMissedPeriod: 7
      RequireMilestoneForLostRewards: true

      LostRewards:
        Messages:
          Player:
            - "&cYou lost your daily voting streak."

      Milestones:
        ThreeDays:
          Enabled: true
          Amount: 3
          Recurring: false
          Rewards:
            Messages:
              Player:
                - "&aYou reached a 3-day voting streak!"

        SevenDays:
          Enabled: true
          Amount: 7
          Recurring: false
          Rewards:
            Commands:
              - "give %player% diamond 1"
            Messages:
              Player:
                - "&aYou reached a 7-day voting streak!"

        EveryThirtyDays:
          Enabled: true
          Amount: 30
          Recurring: true
          Rewards:
            Messages:
              Player:
                - "&6You completed another 30 days of voting!"
```

## How Progress Groups Work

All enabled milestones inside a progress group use:

- The same streak type
- The same vote requirement
- The same missed-period rules
- The same stored streak progress
- The same last-update period

In the example above:

- `ThreeDays` rewards the player at a streak of 3.
- `SevenDays` rewards the player at a streak of 7.
- `EveryThirtyDays` rewards the player at 30, 60, 90, and every later multiple of 30.

A player does not maintain a separate streak for each milestone. The milestones are checkpoints within one shared streak.

## Progress Group Options

| Option | Description |
|---|---|
| `Type` | Shared streak period type for the group. |
| `Enabled` | Enables or disables the entire progress group. |
| `VotesRequired` | Votes required during each period for the period to count. |
| `AllowMissedAmount` | Number of missed periods that may be forgiven. |
| `AllowMissedPeriod` | Number of recent periods used when checking missed-period forgiveness. |
| `RequireMilestoneForLostRewards` | When enabled, LostRewards only run after the player has reached at least one enabled milestone in the group. |
| `LostRewards` | Rewards executed when an established streak in the group is lost. |
| `Milestones` | Reward checkpoints belonging to the shared streak. |

## Milestone Options

| Option | Description |
|---|---|
| `Enabled` | Enables or disables the milestone. |
| `Amount` | Streak amount required for the milestone. |
| `Recurring` | Controls whether the milestone runs once at its exact amount or repeats at multiples of its amount. |
| `Rewards` | Rewards executed when the milestone is reached. |

---

# Lost-Streak Rewards

Lost-streak rewards are supported on progress groups.

They are configured under:

```yaml
VoteStreaks:
  ProgressGroups:
    <GroupId>:
      LostRewards:
```

Example:

```yaml
VoteStreaks:
  ProgressGroups:
    DailyVoting:
      Type: DAILY
      Enabled: true
      VotesRequired: 1
      AllowMissedAmount: 0
      AllowMissedPeriod: 7
      RequireMilestoneForLostRewards: true

      LostRewards:
        Messages:
          Player:
            - "&cYour voting streak was lost."

      Milestones:
        ThreeDays:
          Enabled: true
          Amount: 3
          Recurring: false
          Rewards:
            Messages:
              Player:
                - "&aYou established a 3-day streak!"
```

## Requiring a Milestone Before LostRewards

Use:

```yaml
RequireMilestoneForLostRewards: true
```

With this enabled, `LostRewards` only run after the player has reached at least one enabled milestone in that progress group.

This prevents a lost-streak message or consolation reward from running for a player who only completed one successful period and never reached a configured milestone.

Use:

```yaml
RequireMilestoneForLostRewards: false
```

to allow `LostRewards` after any established streak progress is lost.

`LostRewards` are only available for progress groups. They are not configured on individual standard VoteStreak definitions.

---

# Advanced Streak Logic

Understanding how streak validation works is important when configuring missed-period forgiveness.

## No Misses Allowed

```yaml
AllowMissedAmount: 0
AllowMissedPeriod: 3
```

Example timeline:

```text
Day 1: Successful
Day 2: Successful
Day 3: Successful -> Reward
Day 4: Missed -> Streak resets
```

## One Miss Allowed

```yaml
AllowMissedAmount: 1
AllowMissedPeriod: 7
```

Example timeline:

```text
Day 1: Successful
Day 2: Successful
Day 3: Missed, but forgiven
Day 4: Successful
Day 5: Successful -> Reward
```

## Window Tracking

`AllowMissedPeriod` controls how far back the system checks when applying missed-period forgiveness.

Example:

```yaml
Requirements:
  Amount: 5
AllowMissedAmount: 1
AllowMissedPeriod: 7
```

The system checks the configured period window and validates that the missed-period rules are still satisfied. When the allowed number of missed periods is exceeded, the streak is lost and its progress resets.

For a progress group, the same logic is configured directly on the group:

```yaml
VotesRequired: 1
AllowMissedAmount: 1
AllowMissedPeriod: 7
```

---

# Period Types

## Daily

```yaml
Type: DAILY
```

The player must meet `VotesRequired` during each calendar day.

## Weekly

```yaml
Type: WEEKLY
```

The player must meet `VotesRequired` during each calendar week.

## Monthly

```yaml
Type: MONTHLY
```

The player must meet `VotesRequired` during each calendar month.

Period boundaries are calendar-based rather than a rolling number of hours from the player's last vote.

---

# Independent and Shared Progress

## Independent Standard VoteStreaks

Each standard VoteStreak ID stores its own progress:

```yaml
VoteStreaks:
  SurvivalDaily:
    Type: DAILY
    # ...

  SkyblockDaily:
    Type: DAILY
    # ...
```

`SurvivalDaily` and `SkyblockDaily` are separate streaks.

## Shared Progress Within a Group

All milestones under one progress group use the same progress:

```yaml
VoteStreaks:
  ProgressGroups:
    NetworkDaily:
      Type: DAILY
      # ...
      Milestones:
        ThreeDays:
          Amount: 3
        SevenDays:
          Amount: 7
        ThirtyDays:
          Amount: 30
```

The player has one `NetworkDaily` streak with reward checkpoints at 3, 7, and 30.

## Proxy or Network Usage

To share streak data across a proxy network, use the same VoteStreak or progress-group ID on every server that participates in the shared configuration.

Changing an ID creates a different stored streak and does not continue progress from the old ID.

---

# Rewards

Standard VoteStreak rewards are configured at:

```yaml
VoteStreaks.<Id>.Rewards
```

Progress-group milestone rewards are configured at:

```yaml
VoteStreaks.ProgressGroups.<GroupId>.Milestones.<MilestoneId>.Rewards
```

Progress-group lost rewards are configured at:

```yaml
VoteStreaks.ProgressGroups.<GroupId>.LostRewards
```

VoteStreaks use VotingPlugin's full Rewards system, including reward types such as:

- Commands
- Messages
- Items
- Broadcasts
- RandomCommands

Example:

```yaml
Rewards:
  Commands:
    - "eco give %player% 100"
  Messages:
    Player:
      - "&aYou received $100 for maintaining your voting streak!"
```

---


# Administrative Commands

VoteStreak progress can be inspected and modified with `/av` or `/adminvote`.

All modern VoteStreak commands use this structure:

```text
/av user <player> VoteStreaks <action> <streak-or-group> [value]
```

`<streak-or-group>` may be either:

- A standard VoteStreak ID, such as `DailyStreak`
- A progress-group ID, such as `DailyVoting`

Use the group ID when modifying a progress group. Do not enter an individual milestone ID because every milestone inside the group shares the group's stored progress.

## Command Reference

| Action | Command | Description |
|---|---|---|
| View status | `/av user <player> VoteStreaks Status <streak-or-group>` | Displays the player's stored amount, current-period votes, satisfied state, last-update period, and other available state information. |
| Advance by one | `/av user <player> VoteStreaks Advance <streak-or-group>` | Advances the streak by one successful period and executes any rewards crossed by the advancement. |
| Advance by an amount | `/av user <player> VoteStreaks Advance <streak-or-group> <amount>` | Advances the streak by the specified positive amount and executes any standard rewards or group milestones crossed. |
| Set amount | `/av user <player> VoteStreaks SetAmount <streak-or-group> <amount>` | Sets the current streak amount without executing rewards. Values below zero are stored as zero. |
| Add to amount | `/av user <player> VoteStreaks AddAmount <streak-or-group> <amount>` | Adds or subtracts from the current streak amount without executing rewards. The resulting amount cannot be below zero. |
| Set current votes | `/av user <player> VoteStreaks SetVotes <streak-or-group> <amount>` | Sets the votes recorded in the current period. Values below zero are stored as zero. |
| Set satisfied state | `/av user <player> VoteStreaks SetSatisfied <streak-or-group> <true-or-false>` | Sets whether the current period has already satisfied its vote requirement. |
| Set last-update date | `/av user <player> VoteStreaks SetLastUpdate <streak-or-group> <yyyy-MM-dd>` | Changes the last-update date and converts it to the correct stored daily, weekly, or monthly period. |
| Reset one streak | `/av user <player> VoteStreaks Reset <streak-or-group>` | Resets the stored state for one standard VoteStreak or progress group. |
| Reset by type | `/av user <player> VoteStreaks Reset DAILY` | Resets all daily VoteStreak and progress-group states for the player. `WEEKLY` and `MONTHLY` are also supported. |
| Reset everything | `/av user <player> VoteStreaks Reset ALL` | Resets all VoteStreak and progress-group states for the player. |

## Command Examples

View a player's progress-group state:

```text
/av user Notch VoteStreaks Status DailyVoting
```

Advance the group by one period and execute any newly crossed milestones:

```text
/av user Notch VoteStreaks Advance DailyVoting
```

Advance the group by five periods:

```text
/av user Notch VoteStreaks Advance DailyVoting 5
```

Set the shared group streak to 20 without executing milestone rewards:

```text
/av user Notch VoteStreaks SetAmount DailyVoting 20
```

Subtract two from the current amount without executing rewards:

```text
/av user Notch VoteStreaks AddAmount DailyVoting -2
```

Set the votes recorded during the current period:

```text
/av user Notch VoteStreaks SetVotes DailyVoting 3
```

Mark the current period as satisfied:

```text
/av user Notch VoteStreaks SetSatisfied DailyVoting true
```

Set the last update to June 1, 2026:

```text
/av user Notch VoteStreaks SetLastUpdate DailyVoting 2026-06-01
```

Reset only the `DailyVoting` progress group:

```text
/av user Notch VoteStreaks Reset DailyVoting
```

Reset every daily streak and progress group:

```text
/av user Notch VoteStreaks Reset DAILY
```

## Advance Versus SetAmount

Use `Advance` when the player should receive rewards for milestones crossed by the adjustment.

For example, suppose a progress group contains milestones at 3, 7, and 10 and the player currently has a streak of 2:

```text
/av user Notch VoteStreaks Advance DailyVoting 6
```

The new amount becomes 8. The milestones at 3 and 7 are crossed and may execute.

By comparison:

```text
/av user Notch VoteStreaks SetAmount DailyVoting 8
```

changes the stored amount directly and does not execute the milestones at 3 or 7.

`AddAmount` also changes stored progress without giving rewards.

## SetVotes and SetSatisfied

`SetVotes` changes the raw vote count recorded for the active period.

```text
/av user Notch VoteStreaks SetVotes DailyVoting 2
```

`SetSatisfied` directly changes whether that active period is considered completed:

```text
/av user Notch VoteStreaks SetSatisfied DailyVoting true
```

These values are related but are adjusted separately. Setting the vote count does not automatically perform the same reward-triggering behavior as `Advance`.

## Setting the Last-Update Date

The accepted date format is:

```text
yyyy-MM-dd
```

Examples:

```text
2026-06-01
2026-01-15
2025-12-31
```

VotingPlugin converts the date into the correct internal period key based on the configured streak type:

- A `DAILY` streak stores the corresponding day.
- A `WEEKLY` streak stores the corresponding calendar week.
- A `MONTHLY` streak stores the corresponding calendar month.

An invalid date or an unknown streak/group ID is rejected.

## Reset Behavior and LostRewards

Administrative reset commands clear stored VoteStreak progress.

```text
/av user <player> VoteStreaks Reset <streak-or-group>
```

A manual reset does **not** represent a naturally failed streak and should not be used to test `LostRewards`. Lost-streak rewards are intended for streaks lost through normal streak validation.

## Legacy VoteStreak Commands

The old daily, weekly, and monthly streak fields can still be changed with:

```text
/av user <player> VoteStreaks SetLegacy DAY <amount>
/av user <player> VoteStreaks SetLegacy WEEK <amount>
/av user <player> VoteStreaks SetLegacy MONTH <amount>
```

These commands modify the legacy streak fields only. They do not modify a configured `VoteStreaks.<Id>` definition or a progress group.

For new configurations, use the modern commands with a VoteStreak or progress-group ID.

## Permissions

Each command uses its own permission beneath the VoteStreaks admin-command path:

```text
VotingPlugin.Commands.AdminVote.VoteStreaks.Advance
VotingPlugin.Commands.AdminVote.VoteStreaks.SetAmount
VotingPlugin.Commands.AdminVote.VoteStreaks.AddAmount
VotingPlugin.Commands.AdminVote.VoteStreaks.SetLastUpdate
VotingPlugin.Commands.AdminVote.VoteStreaks.SetVotes
VotingPlugin.Commands.AdminVote.VoteStreaks.SetSatisfied
VotingPlugin.Commands.AdminVote.VoteStreaks.Status
VotingPlugin.Commands.AdminVote.VoteStreaks.Reset
VotingPlugin.Commands.AdminVote.VoteStreaks.SetLegacy
```

Users with the main VotingPlugin admin permission also have access when the server's permission setup grants that parent permission.

---

# Placeholder Reference

| Placeholder | Description |
|---|---|
| `%player%` | Player name |
| `%streak%` | Current streak amount |
| `%type%` | Streak type, such as `DAILY`, `WEEKLY`, or `MONTHLY` |
| `%amount%` | Required streak or milestone amount |
| `%votesrequired%` | Votes required during each period |
| `%currentvotes%` | Votes currently counted during the active period |

---

# Internal Logic Overview

When a vote is received, VotingPlugin:

1. Identifies the standard VoteStreak or progress group.
2. Determines the current daily, weekly, or monthly period.
3. Updates the vote count for that period.
4. Checks whether `VotesRequired` has been met.
5. Updates the shared or independent streak progress.
6. Applies the missed-period rules.
7. Checks eligible rewards or milestones.
8. Executes rewards that have just been reached.

For progress groups, all milestones are checked against the group's shared streak amount.

Important behavior:

- Streaks are evaluated when voting activity is processed.
- Period boundaries are calendar-based.
- Missed periods are handled during streak validation.
- Non-recurring rewards trigger only at their exact configured amount.
- Recurring rewards trigger at multiples of their configured amount.
- LostRewards execute when qualifying progress is lost.
- Stored data is associated with the VoteStreak or progress-group ID.

---

# Migration from the Legacy VoteStreak System

The new VoteStreak system replaces the legacy `VoteStreak` configuration.

Legacy daily, weekly, and monthly streak rewards can be migrated into progress groups so that milestones of the same period type share one streak counter.

Typical migrated group IDs include:

```yaml
VoteStreaks:
  ProgressGroups:
    LegacyDaily:
    LegacyWeekly:
    LegacyMonthly:
```

Only enabled legacy entries should be migrated. Existing reward configuration and recurring behavior are preserved where possible.

After confirming that migration completed correctly, use the new `VoteStreaks` configuration rather than maintaining both systems.

---

# Best Practices

- Keep VoteStreak and progress-group IDs descriptive and stable.
- Use a progress group when several rewards should share one streak.
- Use separate standard VoteStreaks when progress must remain independent.
- Avoid duplicate milestones with the same amount unless intentional.
- Use `RequireMilestoneForLostRewards: true` to prevent premature lost-streak rewards.
- Test recurring milestones to ensure they reward at the intended multiples.
- Test missed-period behavior before enabling valuable production rewards.
- Back up player data before renaming existing streak or group IDs.