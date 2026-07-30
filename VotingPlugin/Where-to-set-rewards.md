---
title: Where to set rewards
description: Find the correct VotingPlugin file and section for each reward
published: true
date: 2025-11-06T02:44:14.351Z
tags:
editor: markdown
dateCreated: 2025-08-30T22:18:32.400Z
---

# Where to Set Rewards

All VotingPlugin reward locations use the same AdvancedCore reward syntax, but
the location determines when the reward runs.

## `VoteSites.yml`

| Reward | Section | Trigger |
|---|---|---|
| Per-site reward | `VoteSites.<site>.Rewards` | A player votes on that site |
| Site cooldown-end reward | `VoteSites.<site>.CoolDownEndRewards` | That site's cooldown becomes available |
| Reward for every site vote | `EverySiteReward` | Any configured vote site is processed |

Rewards can be defined inline or reference reward files.

## `SpecialRewards.yml`

| Reward | Current section | Trigger |
|---|---|---|
| First vote | `VoteMilestones` with `Total: AllTime` and `At: 1` | Player's first recorded vote |
| Vote totals and repeating rewards | `VoteMilestones` with `At` or `Every` | Configured total matches |
| All sites today | `VoteMilestones` with `Total: ALLSITES_TODAY` | Player reaches the configured number of sites |
| Vote streak | `VoteStreaks` | Configured period/progress requirement completes |
| Vote party | `VoteParty.Rewards` | Shared vote-party target is reached |
| NameMC server like | `NameMCLikeReward.Rewards` | NameMC like is confirmed |
| Top voter | `MonthlyAwards`, `WeeklyAwards`, or `DailyAwards` | Matching top voter period completes |

`VoteMilestonesOptions.Groups` controls how multiple matching milestones in one
group are selected.

The old `FirstVote`, `FirstVoteToday`, `AllSites`, `Cumulative`, `MileStones`,
and `VoteStreak` sections are legacy. Use `VoteMilestones` and `VoteStreaks`
for new configurations.

## Reward files

Reusable reward files are stored in the plugin's `Rewards` directory and are
referenced by file name without `.yml`.

Use these current examples as the reward syntax reference:

- [ExampleBasic.yml](https://github.com/BenCodez/AdvancedCore/blob/master/AdvancedCore/src/main/resources/Rewards/ExampleBasic.yml)
- [ExampleAdvanced.yml](https://github.com/BenCodez/AdvancedCore/blob/master/AdvancedCore/src/main/resources/Rewards/ExampleAdvanced.yml)

## Related guides

- [Rewards overview](https://github.com/BenCodez/VotingPlugin/wiki/Rewards)
- [All reward possibilities](https://github.com/BenCodez/VotingPlugin/wiki/All-Reward-Possibilities)
- [VoteMilestones](https://github.com/BenCodez/VotingPlugin/wiki/VoteMilestones)
- [VoteStreak System](https://github.com/BenCodez/VotingPlugin/wiki/VoteStreak-System)
- [Special Rewards](https://github.com/BenCodez/VotingPlugin/wiki/Special-Rewards)
