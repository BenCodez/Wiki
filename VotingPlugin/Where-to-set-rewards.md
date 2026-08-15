---
title: Where to set rewards
description: Find the correct VotingPlugin file and section for each reward
published: true
date: 2026-08-14T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2025-08-30T22:18:32.400Z
---

# Where to Set Rewards

All locations use the same reward syntax, but the location determines when the reward runs.

## `VoteSites.yml`

| Reward | Section | Trigger |
|---|---|---|
| Per-site reward | `VoteSites.<site>.Rewards` | A vote on that site is processed. |
| Cooldown-end reward | `VoteSites.<site>.CoolDownEndRewards` | That site's cooldown becomes available. |
| Every-site reward | `EverySiteReward` | Any configured site is processed. |

## `SpecialRewards.yml`

| Reward | Section | Trigger |
|---|---|---|
| First recorded vote | `VoteMilestones` with `Total: AllTime` and `At: 1` | First recorded all-time vote. |
| Exact/repeating totals | `VoteMilestones` with `At` or `Every` | A configured total matches. |
| All sites today | `VoteMilestones` with `Total: ALLSITES_TODAY` | The configured enabled-site count is reached. |
| Vote streak | `VoteStreaks` | A period/progress requirement completes. |
| Vote party | `VoteParty.Rewards` | Shared target is reached. |
| NameMC like | `NameMCLikeReward.Rewards` | Like verification succeeds. |
| Top voter | `MonthlyAwards`, `WeeklyAwards`, or `DailyAwards` | The period completes. |

`VoteMilestonesOptions.Groups` controls selection when multiple milestones in one group match.

The legacy `AlmostAllSites` section is compiled in memory as an `ALLSITES_TODAY` milestone at one fewer than the number of **enabled** vote sites, with a minimum of 1 and a once-per-day limit. VotingPlugin does not rewrite `SpecialRewards.yml`. Manually migrate and test before removing the legacy section; do not leave both active if they award the same behavior.

## Reward files

Reusable files belong in `plugins/VotingPlugin/Rewards` and are referenced without `.yml`.

A reward file starts directly with reward keys:

```yaml
Money: 100
Commands:
- 'say %player% voted'
```

Inline configurations wrap the same keys in their location's `Rewards` section.

## Related guides

- [Rewards](/VotingPlugin/Rewards)
- [Reward File](/VotingPlugin/Reward-File)
- [All Reward Possibilities](/VotingPlugin/All-Reward-Possibilities)
- [AdvancedPriority Rewards](/VotingPlugin/AdvancedPriority-Rewards)
- [VoteMilestones](/VotingPlugin/VoteMilestones)
- [VoteStreak System](/VotingPlugin/VoteStreak-System)
- [Special Rewards](/VotingPlugin/Special-Rewards)
