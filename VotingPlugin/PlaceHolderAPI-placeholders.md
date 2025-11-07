---
title: PlaceHolderAPI placeholders
description: 
published: true
date: 2025-11-07T02:34:23.168Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:20.126Z
---

# 🧩 PlaceholderAPI Support

VotingPlugin provides full **PlaceholderAPI** integration for use in other plugins (scoreboards, menus, holograms, etc.).  
You can download the official expansion from the [PlaceholderAPI Expansion Cloud](https://www.spigotmc.org/resources/placeholderapi.6245/).  
*(Required only for versions before 6.14 — included automatically in newer builds.)*

---

## ℹ️ Placeholder Behavior

| Symbol | Meaning |
|---------|----------|
| **"No player"** | Placeholder was used without a valid player context |
| **".."** | Value not cached yet — should return once cache updates |
| **"." or "..."** | Placeholder not cached for specific player (rare) |

---

## ⚙️ Placeholder Controls

You can modify placeholder behavior using suffixes:

| Suffix | Effect |
|---------|---------|
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
# Remove "VotingPlugin_" prefix from listed placeholders
CachedPlaceholders: []
#- Total_AllTime

# Custom placeholder returns
# Example: %votingplugin_custom_enoughpoints_5%
# DO NOT USE ON MAIN THREAD
#CustomPlaceholderReturns:
#  'enoughpoints_5':
#    'true': 'User has enough points'
#    'false': 'User does not have enough points'
```

---

## 🔍 View Placeholders In-Game

- `/av placeholders` — shows all available placeholders  
- `/av placeholdersplayer (player)` — shows live values for a player

---

## 📜 Full Placeholder List

| Placeholder | Description |
|--------------|--------------|
| `%votingplugin_total%` | Month total |
| `%votingplugin_alltimetotal%` | All-time total |
| `%votingplugin_lastmonthtotal%` | Last month total |
| `%votingplugin_disablebroadcast%` | Returns true/false if broadcast disabled |
| `%votingplugin_disablereminders%` | Returns true/false if reminders disabled |
| `%votingplugin_milestonecount%` | Milestone count |
| `%votingplugin_milestone_numberofvotesuntil_20%` | Votes until milestone 20 |
| `%votingplugin_milestone_numberofvotesuntil_1%` | Votes until milestone 1 |
| `%votingplugin_nextmilestone_votes_required%` | Votes required for next milestone |
| `%votingplugin_nextmilestone_votes_until%` | Votes until next milestone |
| `%votingplugin_lastmilestone_votes_since%` | Votes since last milestone |
| `%votingplugin_total_alltime%` | Total all-time votes |
| `%votingplugin_total_monthly%` | Total monthly votes |
| `%votingplugin_total_weekly%` | Total weekly votes |
| `%votingplugin_total_daily%` | Total daily votes |
| `%votingplugin_bestdailytotal%` | Highest daily total |
| `%votingplugin_bestweeklytotal%` | Highest weekly total |
| `%votingplugin_bestmonthlytotal%` | Highest monthly total |
| `%votingplugin_dailyvotestreak%` | Current daily vote streak |
| `%votingplugin_weeklyvotestreak%` | Current weekly vote streak |
| `%votingplugin_monthvotestreak%` | Current monthly vote streak |
| `%votingplugin_bestdailyvotestreak%` | Best daily streak |
| `%votingplugin_bestweeklyvotestreak%` | Best weekly streak |
| `%votingplugin_bestmonthvotestreak%` | Best monthly streak |
| `%votingplugin_points%` | Player points |
| `%votingplugin_points_format%` | Formatted points value |
| `%votingplugin_canvote%` | True/false if can vote on all sites |
| `%votingplugin_canvotesites%` | Number of available vote sites |
| `%votingplugin_next_anysite%` | Time until next available vote site |
| `%votingplugin_sitesavailable%` | Number of sites player can vote on |
| `%votingplugin_sitesavailabletotal%` | Total sites that can be voted on |
| `%VotingPlugin_Next_VOTESITE%` | Time until player can vote again on site |
| `%VotingPlugin_Last_VOTESITE%` | How long ago the player voted on the site |
| `%VotingPlugin_CanVote_VOTESITE%` | True/false if can vote on the specific site |
| `%votingplugin_top_all_position%` | Player’s all-time top voter position |
| `%votingplugin_top_month_position%` | Player’s monthly top voter position |
| `%votingplugin_top_lastmonth_position%` | Player’s last-month top voter position |
| `%votingplugin_top_week_position%` | Player’s weekly top voter position |
| `%votingplugin_top_daily_position%` | Player’s daily top voter position |
| `%votingplugin_enoughpoints_#%` | True/false if player has enough points |
| `%votingplugin_votepartycontributedvotes%` | Votes contributed to VoteParty |
| `%votingplugin_top_allvotes_#%` | Votes of player at top position (all-time) |
| `%votingplugin_top_all_#%` | Username at position in all-time top voter list |
| `%votingplugin_top_lastmonth_#%` | Username at position in last-month top voter list |
| `%votingplugin_top_lastmonthvotes_#%` | Votes at position in last-month top voter list |
| `%votingplugin_top_month_#%` | Username at position in current-month top voter list |
| `%votingplugin_top_monthvotes_#%` | Votes at position in current-month top voter list |
| `%votingplugin_top_week_#%` | Username at position in weekly top voter list |
| `%votingplugin_top_weekvotes_#%` | Votes at position in weekly top voter list |
| `%votingplugin_top_daily_#%` | Username at position in daily top voter list |
| `%votingplugin_top_dailyvotes_#%` | Votes at position in daily top voter list |
| `%votingplugin_votepartyvotescurrent%` | Current VoteParty vote count |
| `%votingplugin_votepartyvotesneeded%` | Votes remaining until VoteParty triggers |
| `%votingplugin_votepartyvotesrequired%` | Total votes required for VoteParty |
| `%votingplugin_bungeevotepartyvotescurrent%` | Current proxy-wide VoteParty votes |
| `%votingplugin_bungeevotepartyvotesneeded%` | Votes needed for proxy VoteParty |
| `%votingplugin_bungeevotepartyvotesrequired%` | Total votes required for proxy VoteParty |
| `%votingplugin_globalmonthtotal%` | Global monthly total votes |
| `%votingplugin_globalalltimetotal%` | Global all-time total votes |
| `%votingplugin_globalweeklytotal%` | Global weekly total votes |
| `%votingplugin_globaldailytotal%` | Global daily total votes |
| `%votingplugin_timeuntildayreset%` | Time remaining until daily reset |
| `%votingplugin_timeuntilweekreset%` | Time remaining until weekly reset |
| `%votingplugin_timeuntilmonthreset%` | Time remaining until monthly reset |

---

> 🧠 **Performance Tip:**  
> Use caching (`AUTO` or `SPECIFIC`) for placeholders displayed frequently (like on scoreboards).  
> The `_process` or `_nocache` suffixes should only be used on async operations.
