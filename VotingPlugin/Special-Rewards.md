---
title: Special Rewards
description: Configure milestones, streaks, vote parties, NameMC, and top-voter awards
published: true
date: 2026-08-14T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2025-08-30T22:18:26.142Z
---

# Special Rewards

This page targets VotingPlugin 7.1.1. Use the [7.1.1 `SpecialRewards.yml`](https://github.com/BenCodez/VotingPlugin/blob/7.1.1/VotingPlugin/src/main/resources/SpecialRewards.yml) for release defaults; `master` can contain unreleased changes.

| Section | Purpose |
|---|---|
| `VoteMilestones` | Exact, ranged, or repeating vote/point totals. |
| `VoteMilestonesOptions` | Selection behavior for matching groups. |
| `VoteParty` | Global and per-player rewards at a shared target. |
| `VoteStreaks` | Daily, weekly, or monthly progress and lost-progress behavior. |
| `NameMCLikeReward` | Reward a verified NameMC server like. |
| `MonthlyAwards`, `WeeklyAwards`, `DailyAwards` | Top-voter placement rewards. |

## VoteMilestones

```yaml
VoteMilestones:
  FirstVote:
    Enabled: true
    Total: AllTime
    At: 1
    Rewards:
      Messages:
        Player: '&aThanks for your first vote!'

  Every25Votes:
    Enabled: true
    Total: ALLTIME_VOTES
    Every: 25
    Rewards:
      Commands:
      - 'give %player% diamond 1'
```

Milestones support exact values, lists, ranges, `Every`, limits, and selection groups. See [VoteMilestones](/VotingPlugin/VoteMilestones).

## VoteStreaks

```yaml
VoteStreaks:
  DailyVote:
    Type: DAILY
    Enabled: true
    Requirements:
      Amount: 3
      VotesRequired: 1
    AllowMissedAmount: 0
    AllowMissedPeriod: 3
    Recurring: true
    Rewards:
      Messages:
        Player: '&aYou completed a three-day voting streak!'
```

Changing a streak ID disconnects it from progress stored under the old ID. Progress groups can share progress and run `LostRewards`; see [VoteStreak System](/VotingPlugin/VoteStreak-System).

## VoteParty

`VoteParty` supports fixed/increasing requirements, online-only delivery, reset periods, reminders, global commands, and normal per-player rewards. On proxy networks, review `SendVotesToAllServers`, per-server rewards, and vote-party ownership so the same party is not executed on every backend unintentionally.

## NameMC

```yaml
NameMCLikeReward:
  Enabled: false
  Url: 'play.example.com'
  CheckIntervalMinutes: 10
  Rewards:
    Messages:
      Player: '&aThanks for liking the server on NameMC!'
```

## Top-voter awards

```yaml
EnableMonthlyAwards: true
MonthlyAwards:
  1:
    Rewards:
      Messages:
        Player: '&aYou came in first place in %TopVoter%!'
```

Enable the corresponding `LoadTopVoter` period in `Config.yml`.

## Legacy sections

Deprecated compatibility sections include:

- `FirstVote`
- `FirstVoteToday`
- `AllSites`
- `AlmostAllSites`
- `Cumulative`
- `MileStones`
- `VoteStreak`

`AlmostAllSites` is compiled at load time as an `ALLSITES_TODAY` milestone at one fewer than the number of **enabled** sites, minimum 1, limited once per day. This does not rewrite YAML. Migrate and test manually, then remove or empty the legacy section to avoid duplicate rewards.

```yaml
FirstVote: {}
```
