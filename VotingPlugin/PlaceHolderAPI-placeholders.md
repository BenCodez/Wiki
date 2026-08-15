---
title: PlaceholderAPI placeholders
description: VotingPlugin PlaceholderAPI values, caching, and output context
published: true
date: 2026-08-14T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2025-08-30T22:18:20.126Z
---

# PlaceholderAPI Support

VotingPlugin exposes PlaceholderAPI values for scoreboards, menus, holograms, and other plugins. Install PlaceholderAPI and the VotingPlugin expansion.

## Output context inside VotingPlugin rewards

PlaceholderAPI expansion is output-path specific in VotingPlugin 7.1.1:

- ordinary reward `Messages.Player` text is passed through PlaceholderAPI;
- reward `ActionBar.Message` and `BossBar.Message` do not have a dedicated PlaceholderAPI pass;
- with the default JavaScript engine disabled, `%votingplugin_*%` commonly remains literal in those action-bar/boss-bar messages;
- reward-local replacements such as `%player%` still work where the reward handler supplies them.

Do not enable the JavaScript engine solely to make an action-bar placeholder expand. Use a normal player message, a reward-local placeholder, or test a different output path instead.

## Placeholder output markers

| Output | Meaning |
|---|---|
| `No player` | No valid player context was supplied. |
| `..` | The value is not cached yet and should populate after an update. |
| `.` or `...` | The specific player's value is not cached. |

## Cache controls

Suffixes can force a live lookup:

| Suffix | Effect |
|---|---|
| `_process` | Processes live instead of returning a cache marker. Avoid on the main thread. |
| `_nocache` | Reads live from SQL instead of the placeholder cache. Avoid on the main thread. |

`Config.yml`:

```yaml
UsePrimaryAccountForPlaceholders: false
PlaceholderCacheLevel: AUTO
CachedPlaceholders: []
# - Total_AllTime
```

Cache levels are `AUTO`, `SPECIFIC`, and `NONE`. For frequently rendered scoreboards or menus, use caching rather than repeated live SQL lookups.

## Inspect values

```text
/av placeholders
/av placeholdersplayer <player>
```

## Dynamic tokens

- `VOTESITE` is a configured vote-site identifier.
- `VOTEMILESTONE` is a VoteMilestone group name.
- `#` is a numeric position or parameter.

## General totals and state

| Placeholder | Description |
|---|---|
| `%votingplugin_total%` | Current month total. |
| `%votingplugin_alltimetotal%` | All-time total. |
| `%votingplugin_lastmonthtotal%` | Last month total. |
| `%votingplugin_disablebroadcast%` | Whether the user disabled broadcasts. |
| `%votingplugin_canlike_namemc%` | `Complete` or `Incomplete` for the NameMC reward. |
| `%votingplugin_total_alltime%` | All-time total. |
| `%votingplugin_total_monthly%` | Monthly total. |
| `%votingplugin_total_weekly%` | Weekly total. |
| `%votingplugin_total_daily%` | Daily total. |
| `%votingplugin_bestdailytotal%` | Highest daily total. |
| `%votingplugin_bestweeklytotal%` | Highest weekly total. |
| `%votingplugin_bestmonthlytotal%` | Highest monthly total. |
| `%votingplugin_points%` | Vote points. |
| `%votingplugin_points_format%` | Formatted vote points. |
| `%votingplugin_canvote%` | Whether the player can vote on all sites. |
| `%votingplugin_canvotesites%` | Number of currently available sites. |
| `%votingplugin_next_anysite%` | Time until any site is available. |
| `%votingplugin_sitesavailable%` | Available site count. |
| `%votingplugin_sitesavailabletotal%` | Total available-site value. |

## Vote streaks

| Placeholder | Description |
|---|---|
| `%votingplugin_dailyvotestreak%` | Current daily streak. |
| `%votingplugin_weeklyvotestreak%` | Current weekly streak. |
| `%votingplugin_monthvotestreak%` | Current monthly streak. |
| `%votingplugin_bestdailyvotestreak%` | Best daily streak. |
| `%votingplugin_bestweeklyvotestreak%` | Best weekly streak. |
| `%votingplugin_bestmonthvotestreak%` | Best monthly streak. |

## Vote-site placeholders

| Placeholder | Description |
|---|---|
| `%votingplugin_next_VOTESITE%` | Time until `VOTESITE` is available. |
| `%votingplugin_last_VOTESITE%` | Time since the last vote on `VOTESITE`. |
| `%votingplugin_canvote_VOTESITE%` | Whether the player can vote on `VOTESITE`. |

## Top-voter placeholders

| Placeholder | Description |
|---|---|
| `%votingplugin_top_all_position%` | User's all-time position. |
| `%votingplugin_top_month_position%` | Current monthly position. |
| `%votingplugin_top_lastmonth_position%` | Previous-month position. |
| `%votingplugin_top_week_position%` | Weekly position. |
| `%votingplugin_top_daily_position%` | Daily position. |
| `%votingplugin_top_allvotes_#%` | Votes at all-time position `#`. |
| `%votingplugin_top_all_#%` | Username at all-time position `#`. |
| `%votingplugin_top_lastmonth_#%` | Username at previous-month position `#`. |
| `%votingplugin_top_lastmonthvotes_#%` | Votes at previous-month position `#`. |
| `%votingplugin_top_month_#%` | Username at monthly position `#`. |
| `%votingplugin_top_monthvotes_#%` | Votes at monthly position `#`. |
| `%votingplugin_top_week_#%` | Username at weekly position `#`. |
| `%votingplugin_top_weekvotes_#%` | Votes at weekly position `#`. |
| `%votingplugin_top_daily_#%` | Username at daily position `#`. |
| `%votingplugin_top_dailyvotes_#%` | Votes at daily position `#`. |

## Parameterized points

| Placeholder | Description |
|---|---|
| `%votingplugin_enoughpoints_#%` | Whether the player has at least `#` points. |

## VoteMilestones

| Placeholder | Description |
|---|---|
| `%votingplugin_votemilestonenext%` | Next value in the default group. |
| `%votingplugin_votemilestonelast%` | Last achieved value in the default group. |
| `%votingplugin_votemilestonevotesuntilnext%` | Votes until the next default-group value. |
| `%votingplugin_votemilestonenext_VOTEMILESTONE%` | Next value in the named group. |
| `%votingplugin_votemilestonelast_VOTEMILESTONE%` | Last value in the named group. |
| `%votingplugin_votemilestonevotesuntilnext_VOTEMILESTONE%` | Votes until the next value in the named group. |

## VoteParty

| Placeholder | Description |
|---|---|
| `%votingplugin_votepartycontributedvotes%` | Player's contributed votes. |
| `%votingplugin_votepartyvotescurrent%` | Current backend vote-party total. |
| `%votingplugin_votepartyvotesneeded%` | Votes still needed. |
| `%votingplugin_votepartyvotesrequired%` | Required total. |
| `%votingplugin_bungeevotepartyvotescurrent%` | Current proxy vote-party total. |
| `%votingplugin_bungeevotepartyvotesneeded%` | Proxy votes still needed. |
| `%votingplugin_bungeevotepartyvotesrequired%` | Proxy required total. |

## Global totals and reset times

| Placeholder | Description |
|---|---|
| `%votingplugin_globalmonthtotal%` | Global monthly total. |
| `%votingplugin_globalalltimetotal%` | Global all-time total. |
| `%votingplugin_globalweeklytotal%` | Global weekly total. |
| `%votingplugin_globaldailytotal%` | Global daily total. |
| `%votingplugin_timeuntildayreset%` | Time until the daily reset. |
| `%votingplugin_timeuntilweekreset%` | Time until the weekly reset. |
| `%votingplugin_timeuntilmonthreset%` | Time until the monthly reset. |
