---
title: Special Rewards
description: Configure milestones, streaks, vote parties, NameMC rewards, and top voter awards
published: true
date: 2025-09-01T02:58:27.182Z
tags:
editor: markdown
dateCreated: 2025-08-30T22:18:26.142Z
---

# Special Rewards

`SpecialRewards.yml` contains rewards that are not tied to one individual vote
site. The current systems are:

| Section | Purpose |
|---|---|
| `VoteMilestones` | Reward exact totals, ranges, or repeating vote/point totals |
| `VoteMilestonesOptions` | Control how matched milestones are selected within groups |
| `VoteParty` | Run global and per-player rewards after a network/server vote target |
| `VoteStreaks` | Reward consecutive daily, weekly, or monthly voting progress |
| `NameMCLikeReward` | Reward players after VotingPlugin confirms a NameMC server like |
| `MonthlyAwards`, `WeeklyAwards`, `DailyAwards` | Reward the matching top voter positions |

See the current
[`SpecialRewards.yml`](https://github.com/BenCodez/VotingPlugin/blob/master/VotingPlugin/src/main/resources/SpecialRewards.yml)
for complete defaults and examples.

## VoteMilestones

`VoteMilestones` is the recommended replacement for the old first-vote,
all-sites, cumulative, and milestone sections.

```yaml
VoteMilestones:
  FirstVote:
    Enabled: true
    Total: AllTime
    At: 1
    Rewards:
      Messages:
        Player: "&aThanks for your first vote!"

  Every25Votes:
    Enabled: true
    Total: ALLTIME_VOTES
    Every: 25
    Rewards:
      Commands:
        - "give %player% diamond 1"
```

Milestones can use exact values, lists, ranges, repeating `Every` values,
limits, and selection groups. See [VoteMilestones](https://github.com/BenCodez/VotingPlugin/wiki/VoteMilestones)
for the complete system.

To reward voting on every configured site in a day, use the
`ALLSITES_TODAY` total and set `At` to the number of vote sites.

## VoteStreaks

`VoteStreaks` is the current streak system. Each definition has a stable ID,
period type, vote requirement, missed-period rules, recurrence behavior, and
rewards.

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
        Player: "&aYou completed a three-day voting streak!"
```

Changing a streak ID disconnects it from progress stored under the previous ID.
On proxy networks, use the same ID for shared progress or different IDs for
independent server progress.

Progress groups can share one progress definition across multiple reward
milestones and can run `LostRewards` when established progress is lost. See
[VoteStreak System](https://github.com/BenCodez/VotingPlugin/wiki/VoteStreak-System)
for the full reference and migration guidance.

## VoteParty

`VoteParty` counts votes toward a shared target. It supports:

- fixed or increasing vote requirements
- all-player or voters-only rewards
- online-only delivery
- daily, weekly, or monthly resets
- reminders as the target approaches
- global commands that run once
- normal per-player rewards

Review reward-forwarding settings before enabling a vote party on a proxy
network so the same party is not executed more than intended.

## NameMCLikeReward

```yaml
NameMCLikeReward:
  Enabled: false
  Url: "play.example.com"
  CheckIntervalMinutes: 10
  Rewards:
    Messages:
      Player: "&aThanks for liking the server on NameMC!"
```

Set `Url` to the server address used on NameMC. VotingPlugin checks eligible
players at the configured interval and runs the standard reward section after
confirmation.

## Top voter awards

Enable the period you use and define rewards by placement:

```yaml
EnableMonthlyAwards: true
MonthlyAwards:
  1:
    Rewards:
      Messages:
        Player: "&aYou came in first place in %TopVoter%!"
```

The corresponding `LoadTopVoter` period in `Config.yml` must also be enabled.

## Legacy sections

These sections are deprecated and retained only for compatibility/reference:

- `FirstVote`
- `FirstVoteToday`
- `AllSites`
- `AlmostAllSites`
- `Cumulative`
- `MileStones`
- `VoteStreak`

Existing `AlmostAllSites` configurations are mapped to an `ALLSITES_TODAY`
milestone at one fewer than the configured number of vote sites. Use
`VoteMilestones` for new count-based rewards and `VoteStreaks` for current
streak behavior. Do not add new configurations using the legacy sections.

To disable a reward section, set it to `{}` or remove it. Example:

```yaml
FirstVote: {}
```
