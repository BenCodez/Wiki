---
title: PlaceHolderAPI placeholders
description: 
published: true
date: 2026-02-22T01:44:23.986Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:20.126Z
---

# 🧩 PlaceholderAPI Support

VotingPlugin provides full **PlaceholderAPI** integration for use in other plugins (scoreboards, menus, holograms, etc.).  
Install **PlaceholderAPI** and then install the VotingPlugin expansion.

---

## ℹ️ Placeholder Behavior

| Output | Meaning |
|---|---|
| **No player** | Placeholder was used without a valid player context |
| **..** | Value not cached yet — should return once cache updates |
| **.** or **...** | Placeholder not cached for the specific player (rare) |

---

## ⚙️ Placeholder Controls

You can modify placeholder behavior using suffixes:

| Suffix | Effect |
|---|---|
| `_process` | Forces the placeholder to process live and return a value instead of `.` or `..`. *(Avoid on main thread.)* |
| `_nocache` | Skips cache and retrieves a live value directly from MySQL. *(Avoid on main thread.)* |

---

## 🧩 Configuration Example (`Config.yml`)

```yaml
# ---------------------------------------
# PlaceholderAPI Placeholder Settings
# ---------------------------------------

# When enabled, the command /vote setprimaryaccount (playername)
# will appear after restart.
# The primary account is used instead of the player’s account
# to fetch placeholders and vote reminders (useful for alts).
UsePrimaryAccountForPlaceholders: false

# Cache levels:
# AUTO - Auto cache after use (recommended)
# SPECIFIC - Cache only listed placeholders
# NONE - Disable caching entirely
PlaceholderCacheLevel: AUTO

# Placeholders to always cache
# Use for placeholders that appear frequently (like on scoreboards)
# Remove "votingplugin_" prefix from listed placeholders
CachedPlaceholders: []
# - Total_AllTime
```

---

## 🔍 View Placeholders In-Game

- `/av placeholders` — shows all available placeholders  
- `/av placeholdersplayer (player)` — shows live values for a player

---

## 🧩 Tokens used below

Some placeholders take a dynamic segment:

- `VOTESITE` → the configured vote site name (example: `pmc`, `worldsite`, `guiadd`)
- `VOTEMILESTONE` → the VoteMilestone **group** name (example: `default`, `legacy_cumulative`)

---

## 📜 Full Placeholder List

| Placeholder | Description |
|---|---|
| `%votingplugin_total%` | Month total |
| `%votingplugin_alltimetotal%` | All-time total |
| `%votingplugin_lastmonthtotal%` | Last month total |
| `%votingplugin_disablebroadcast%` | Returns true/false if user has broadcast disabled |
| `%votingplugin_total_alltime%` | User total for AllTime |
| `%votingplugin_total_monthly%` | User total for Monthly |
| `%votingplugin_total_weekly%` | User total for Weekly |
| `%votingplugin_total_daily%` | User total for Daily |
| `%votingplugin_bestdailytotal%` | Best daily total |
| `%votingplugin_bestweeklytotal%` | Best weekly total |
| `%votingplugin_bestmonthlytotal%` | Best monthly total |
| `%votingplugin_dailyvotestreak%` | Current daily votestreak |
| `%votingplugin_weeklyvotestreak%` | Current weekly votestreak |
| `%votingplugin_monthvotestreak%` | Current month votestreak |
| `%votingplugin_bestdailyvotestreak%` | Best daily votestreak |
| `%votingplugin_bestweeklyvotestreak%` | Best weekly votestreak |
| `%votingplugin_bestmonthvotestreak%` | Best month votestreak |
| `%votingplugin_points%` | User points |
| `%votingplugin_points_format%` | User points (formatted) |
| `%votingplugin_canvote%` | Return true/false if player can vote on all sites |
| `%votingplugin_canvotesites%` | Return number of votesites available |
| `%votingplugin_next_anysite%` | How long until user can vote on anysite |
| `%votingplugin_sitesavailable%` | Get number of sites available to be voted on |
| `%votingplugin_sitesavailabletotal%` | Get total number of sites available to be voted on |

### VoteSite placeholders (per-site)

| Placeholder | Description |
|---|---|
| `%votingplugin_next_VOTESITE%` | How long until user can vote on `VOTESITE` |
| `%votingplugin_last_VOTESITE%` | How long ago user voted on `VOTESITE` |
| `%votingplugin_canvote_VOTESITE%` | Whether or not player can vote on `VOTESITE` |

### Top voter placeholders

| Placeholder | Description |
|---|---|
| `%votingplugin_top_all_position%` | Get user top voter position |
| `%votingplugin_top_month_position%` | Get user's current top voter position |
| `%votingplugin_top_lastmonth_position%` | Get user top voter position for lastmonth |
| `%votingplugin_top_week_position%` | Get user top voter position |
| `%votingplugin_top_daily_position%` | Get user top voter position |
| `%votingplugin_top_allvotes_#%` | Get user votes at position `#` in top voter |
| `%votingplugin_top_all_#%` | Get username at position `#` in top voter |
| `%votingplugin_top_lastmonth_#%` | Get user at position `#` in last month top voter |
| `%votingplugin_top_lastmonthvotes_#%` | Get user votes at position `#` in last month top voter |
| `%votingplugin_top_month_#%` | Get username at position `#` in top voter |
| `%votingplugin_top_monthvotes_#%` | Get user votes at position `#` in top voter |
| `%votingplugin_top_week_#%` | Get username at position `#` in top voter |
| `%votingplugin_top_weekvotes_#%` | Get user votes at position `#` in top voter |
| `%votingplugin_top_daily_#%` | Get username at position `#` in top voter |
| `%votingplugin_top_dailyvotes_#%` | Get user votes at position `#` in top voter |

### Points placeholder with parameter

| Placeholder | Description |
|---|---|
| `%votingplugin_enoughpoints_#%` | Return true/false if player has said points |

### VoteMilestone placeholders

| Placeholder | Description |
|---|---|
| `%votingplugin_votemilestonenext%` | Next VoteMilestone value for default group |
| `%votingplugin_votemilestonelast%` | Last achieved VoteMilestone value for default group |
| `%votingplugin_votemilestonevotesuntilnext%` | Votes until next VoteMilestone for default group |
| `%votingplugin_votemilestonenext_VOTEMILESTONE%` | Next VoteMilestone value for group `VOTEMILESTONE` |
| `%votingplugin_votemilestonelast_VOTEMILESTONE%` | Last achieved VoteMilestone value for group `VOTEMILESTONE` |
| `%votingplugin_votemilestonevotesuntilnext_VOTEMILESTONE%` | Votes until next VoteMilestone for group `VOTEMILESTONE` |

### VoteParty placeholders

| Placeholder | Description |
|---|---|
| `%votingplugin_votepartycontributedvotes%` | See vote party placeholders contributed |
| `%votingplugin_votepartyvotescurrent%` | Current amount of voteparty votes |
| `%votingplugin_votepartyvotesneeded%` | Voteparty votes needed |
| `%votingplugin_votepartyvotesrequired%` | Amount of votes needed for voteparty |
| `%votingplugin_bungeevotepartyvotescurrent%` | Current amount of bungee voteparty votes |
| `%votingplugin_bungeevotepartyvotesneeded%` | Voteparty bungee votes needed |
| `%votingplugin_bungeevotepartyvotesrequired%` | Amount of votes needed for bungee voteparty |

### Global totals and resets

| Placeholder | Description |
|---|---|
| `%votingplugin_globalmonthtotal%` | Global month total |
| `%votingplugin_globalalltimetotal%` | Global alltime total |
| `%votingplugin_globalweeklytotal%` | Global weekly total |
| `%votingplugin_globaldailytotal%` | Global daily total |
| `%votingplugin_timeuntildayreset%` | Time until plugin time day changes |
| `%votingplugin_timeuntilweekreset%` | Time until plugin time week changes |
| `%votingplugin_timeuntilmonthreset%` | Time until plugin time month changes |

---

> 🧠 **Performance tip:**  
> Use caching (`AUTO` or `SPECIFIC`) for placeholders displayed frequently (like scoreboards).  
> The `_process` or `_nocache` suffixes should only be used on async operations.