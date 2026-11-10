---
title: VotingPlugin Commands & Permissions (Development)
description: Automatically generated command and permission reference for server administrators
published: true
date: 2026-11-09T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2026-11-09T00:00:00.000Z
---

# Commands & Permissions — Development

These command tables are automatically maintained from VotingPlugin's development
command definitions. They are intended for **server administrators**, not for
players learning how to vote. The latest stable release may have different commands.
For the released-version reference, see
[Commands & Permissions](/VotingPlugin/Commands-&-Permissions).

> **Availability:** Some commands depend on server settings, permissions, or
> optional features. Use `/av help`, `/av perms` and `/vote help` on your server
> to confirm what your installed version actually supports.
{.is-info}

## Administrator commands (`/av`)

| Command | Permission | Description |
|---|---|
| `/av ` | `VotingPlugin.Commands.AdminVote\|VotingPlugin.Admin` | Base command |
| `/av BackgroundUpdate` | `VotingPlugin.Commands.AdminVote.BackgroundUpdate\|VotingPlugin.Admin` | Force a background update |
| `/av CheckVoteCoolDownRewards` | `VotingPlugin.Commands.AdminVote.VoteSite.CheckVoteCoolDownRewards\|VotingPlugin.Admin` | Force check all vote cooldown rewards |
| `/av ClearDiscordMessageID (topvoter)` | `VotingPlugin.Commands.AdminVote.ClearDiscordMessageID` | Clear discord message ID for top voter |
| `/av ClearTotal` | `VotingPlugin.Commands.AdminVote.ClearTotal.All\|VotingPlugin.Admin` | Reset totals for all players |
| `/av Config TempDebug` | `VotingPlugin.Commands.AdminVote.Config.Edit\|VotingPlugin.Admin` | Enable debug, effective until reload/restart |
| `/av Config TempExtraDebug` | `VotingPlugin.Commands.AdminVote.Config.Edit\|VotingPlugin.Admin` | Enable extra debug, effective until reload/restart |
| `/av CorrectServiceSites` | `VotingPlugin.Commands.AdminVote.CorrectServiceSites\|VotingPlugin.Admin` | Attempt to correct invalid services sites |
| `/av CurrentPluginTime` | `VotingPlugin.Commands.AdminVote.CurrentPluginTime\|VotingPlugin.Admin` | Current plugin time |
| `/av Edit BungeeSettings` | `VotingPlugin.Commands.AdminVote.Edit.BungeeSettings\|VotingPlugin.Admin` | Edit BungeeSettings.yml |
| `/av Edit VoteMilestones` | `VotingPlugin.Commands.AdminVote.Edit.VoteMilestones` | Edit VoteMilestones rewards |
| `/av Edit VoteParty` | `VotingPlugin.Commands.AdminVote.Edit.VoteParty` | Edit voteparty |
| `/av Edit VoteShop` | `VotingPlugin.Commands.AdminVote.Edit.VoteShop` | Edit VoteShop |
| `/av GUI` | `VotingPlugin.Commands.AdminVote.GUI\|VotingPlugin.Admin` | Admin GUI |
| `/av Help/?` | `VotingPlugin.Commands.AdminVote.Help\|VotingPlugin.Admin` | See this page |
| `/av Help/? (number)` | `VotingPlugin.Commands.AdminVote.Help\|VotingPlugin.Admin` | See this page |
| `/av MergeDataFrom (UserStorage)` | `VotingPlugin.Commands.AdminVote.MergeDataFrom\|VotingPlugin.Admin` | Merge player totals from other storage type |
| `/av MergeOfflineUUIDs (Boolean)` | `VotingPlugin.Commands.AdminVote.MergeOfflineUUIDs\|VotingPlugin.Admin` | Offline-mode data repair: fixes incorrect UUIDs for names, merges duplicates, and normalizes PlayerName casing. Use /av MergeOfflineUUIDs true to apply. |
| `/av MigrateVoteStreaks` | `VotingPlugin.Commands.AdminVote.MigrateVoteStreaks\|VotingPlugin.Admin` | Migrate legacy VoteStreak config to VoteStreaks |
| `/av NameMCLikeRecovery (uuid) (list)` | `VotingPlugin.Commands.AdminVote.NameMCLikeRecovery\|VotingPlugin.Admin` | Console only: /av NameMCLikeRecovery <uuid> status, then delivered\|retry <token> |
| `/av OfflineVoteRecovery (uuid) (list)` | `VotingPlugin.Commands.AdminVote.OfflineVoteRecovery\|VotingPlugin.Admin` | Console only: /av OfflineVoteRecovery <uuid> status, then delivered\|retry\|already-cleared <token> |
| `/av PauseRewards` | `VotingPlugin.Commands.AdminVote.PauseRewards\|VotingPlugin.Admin` | Pause rewards globally |
| `/av Perms` | `VotingPlugin.Commands.AdminVote.Perms\|VotingPlugin.Admin` | List permissions |
| `/av Perms (Number)` | `VotingPlugin.Commands.AdminVote.Perms\|VotingPlugin.Admin` | List permissions |
| `/av Perms (Number) (Player)` | `VotingPlugin.Commands.AdminVote.Perms.Other\|VotingPlugin.Admin` | List permissions from the plugin the specified player has |
| `/av PermsDebug` | `VotingPlugin.Commands.AdminVote.PermsDebug` | Dev permission list, generate this list, requires dev debug |
| `/av PermsPlayer (Player)` | `VotingPlugin.Commands.AdminVote.Perms.Other\|VotingPlugin.Admin` | List permissions from the plugin the player has |
| `/av PermsPlayer (Player) (Number)` | `VotingPlugin.Commands.AdminVote.Perms.Other\|VotingPlugin.Admin` | List permissions from the plugin the player has |
| `/av Placeholders` | `VotingPlugin.Commands.AdminVote.Placeholders\|VotingPlugin.Admin` | See possible placeholderapi placeholders |
| `/av Placeholders (player)` | `VotingPlugin.Commands.AdminVote.Placeholders.Players\|VotingPlugin.Admin` | See possible placeholderapi placeholders with player values |
| `/av PlayerName (uuid)` | `VotingPlugin.Commands.AdminVote.PlayerName\|VotingPlugin.Admin` | View PlayerName of player |
| `/av PurgeNoData` | `VotingPlugin.PurgeNoData` | Purge players from database with no data and haven't been online for a number of days (Set in Config.yml) |
| `/av Reload` | `VotingPlugin.Commands.AdminVote.Reload\|VotingPlugin.Admin` | Reload plugin, will not reload user storage |
| `/av ReloadAll` | `VotingPlugin.Commands.AdminVote.Reload\|VotingPlugin.Admin` | Reload plugin, including user storage |
| `/av RemoveOfflineUUIDs` | `VotingPlugin.Commands.AdminVote.RemoveOfflineUUIDs\|VotingPlugin.Admin` | Purges database of offline UUIDs, keeps online UUIDs |
| `/av RemoveOnlineUUIDs` | `VotingPlugin.Commands.AdminVote.RemoveOnlineUUIDs\|VotingPlugin.Admin` | Purges database of online UUIDs, keeps proper offline UUIDs |
| `/av ResetPoints` | `VotingPlugin.Commands.AdminVote.ResetPoints\|VotingPlugin.Admin` | Clears all points of all players |
| `/av ResetTotal (TopVoter)` | `VotingPlugin.Commands.AdminVote.ResetTotal.All\|VotingPlugin.Admin` | Reset specific totals for all players (DAY/WEEK/MONTH) |
| `/av ResumeRewards` | `VotingPlugin.Commands.AdminVote.ResumeRewards\|VotingPlugin.Admin` | Resume rewards globally |
| `/av ResyncMilestones` | `VotingPlugin.Commands.AdminVote.ResyncMilestones\|VotingPlugin.Admin` | Resync Milestones to all time total |
| `/av ServiceSites/Status` | `VotingPlugin.Commands.AdminVote.ServiceSites\|VotingPlugin.Admin` | See a list of all service sites the server got |
| `/av Sites` | `VotingPlugin.Commands.AdminVote.Sites\|VotingPlugin.Admin` | List VoteSites |
| `/av Sites (sitename)` | `VotingPlugin.Commands.AdminVote.Sites.Site\|VotingPlugin.Admin` | View Site Info |
| `/av Test (Player) (sitename) (number)` | `VotingPlugin.Commands.AdminVote.Test\|VotingPlugin.Admin` | Test voting speed, for debug |
| `/av TestReward (Player) (reward) (number)` | `VotingPlugin.Commands.AdminVote.TestReward\|VotingPlugin.Admin` | Test reward speed, for debug |
| `/av TestSpam (Player) (sitename) (number)` | `VotingPlugin.Commands.AdminVote.TestSpam\|VotingPlugin.Admin` | Test voting spam speed, for debug |
| `/av TopPoints` | `VotingPlugin.Commands.AdminVote.TopPoints\|VotingPlugin.Admin` | Open the top points GUI |
| `/av UpdateCheck` | `VotingPlugin.Commands.AdminVote.UpdateCheck\|VotingPlugin.Admin` | Check for update |
| `/av User (player) AddPoints (number)` | `VotingPlugin.Commands.AdminVote.AddPoints\|VotingPlugin.Admin` | Add to players voting points |
| `/av User (player) ClearTotal` | `VotingPlugin.Commands.AdminVote.ClearTotal\|VotingPlugin.Admin` | Clear Totals for player |
| `/av User (Player) ForceCoolDownEndRewards (Sitename)` | `VotingPlugin.Commands.AdminVote.ForceCoolDownEndRewards\|VotingPlugin.Admin` | Trigger CoolDownEndRewards manually |
| `/av User (Player) ForceVote (Sitename)` | `VotingPlugin.Commands.AdminVote.Vote\|VotingPlugin.Admin` | Trigger manual vote |
| `/av User (Player) ForceVote All` | `VotingPlugin.Commands.AdminVote.Vote\|VotingPlugin.Admin` | Trigger manual vote |
| `/av User (player) ForceVoteMilestone (milestone)` | `VotingPlugin.Commands.AdminVote.User.ForceVoteMilestone\|VotingPlugin.Admin` | Force execute a specific VoteMilestone (skips totals, respects limits) |
| `/av User (player) ForceVoteMilestoneNoLimits (milestone)` | `VotingPlugin.Commands.AdminVote.User.ForceVoteMilestoneNoLimits\|VotingPlugin.Admin` | Force execute a specific VoteMilestone (skips totals, bypasses limits) |
| `/av User (player) ForceVoteShop (VoteShop)` | `VotingPlugin.Commands.AdminVote.ForceVoteShop\|VotingPlugin.Admin` | Force a voteshop reward |
| `/av User (player) RemovePoints (number)` | `VotingPlugin.Commands.AdminVote.RemovePoints\|VotingPlugin.Admin` | Remove voting points |
| `/av User (player) ResetAllVotedSites` | `VotingPlugin.Commands.AdminVote.ResetAllVotedSites\|VotingPlugin.Admin` | Resets all voted |
| `/av User (player) ResetVotedSite (Sitename)` | `VotingPlugin.Commands.AdminVote.ResetVotedSite\|VotingPlugin.Admin` | Resets last voted for specific site |
| `/av User (player) ResetVoteMilestoneLimits` | `VotingPlugin.Commands.AdminVote.User.ResetVoteMilestoneLimits\|VotingPlugin.Admin` | Reset ALL VoteMilestone limits for a player |
| `/av User (player) ResetVoteMilestoneLimits (milestonegroup)` | `VotingPlugin.Commands.AdminVote.User.ResetVoteMilestoneLimits\|VotingPlugin.Admin` | Reset VoteMilestone limits for a player (group) |
| `/av User (player) SetPoints (number)` | `VotingPlugin.Commands.AdminVote.SetPoints\|VotingPlugin.Admin` | Set players voting points |
| `/av User (player) VoteStreaks AddAmount (votestreakstate) (number)` | `VotingPlugin.Commands.AdminVote.VoteStreaks.AddAmount\|VotingPlugin.Admin` | Add to a configured VoteStreak amount without giving rewards |
| `/av User (player) VoteStreaks Advance (votestreakstate)` | `VotingPlugin.Commands.AdminVote.VoteStreaks.Advance\|VotingPlugin.Admin` | Advance a configured VoteStreak by one and give crossed rewards |
| `/av User (player) VoteStreaks Advance (votestreakstate) (number)` | `VotingPlugin.Commands.AdminVote.VoteStreaks.Advance\|VotingPlugin.Admin` | Advance a configured VoteStreak and give crossed rewards |
| `/av User (player) VoteStreaks Force (votestreak)` | `VotingPlugin.Commands.AdminVote.ForceVoteStreak\|VotingPlugin.Admin` | Force a configured VoteStreaks reward by id |
| `/av User (player) VoteStreaks Force (votestreak) (number)` | `VotingPlugin.Commands.AdminVote.ForceVoteStreak\|VotingPlugin.Admin` | Force a configured VoteStreaks reward by id with a streak amount |
| `/av User (player) VoteStreaks Reset (votestreakreset)` | `VotingPlugin.Commands.AdminVote.VoteStreaks.Reset\|VotingPlugin.Admin` | Reset VoteStreak state by id, progress group, type, or ALL |
| `/av User (player) VoteStreaks SetAmount (votestreakstate) (number)` | `VotingPlugin.Commands.AdminVote.VoteStreaks.SetAmount\|VotingPlugin.Admin` | Set a configured VoteStreak amount without giving rewards |
| `/av User (player) VoteStreaks SetLastUpdate (votestreakstate) (text)` | `VotingPlugin.Commands.AdminVote.VoteStreaks.SetLastUpdate\|VotingPlugin.Admin` | Set the last update date for a configured VoteStreak using yyyy-MM-dd |
| `/av User (player) VoteStreaks SetLegacy DAY (number)` | `VotingPlugin.Commands.AdminVote.VoteStreaks.SetLegacy\|VotingPlugin.Admin` | Set the legacy daily vote streak amount |
| `/av User (player) VoteStreaks SetLegacy MONTH (number)` | `VotingPlugin.Commands.AdminVote.VoteStreaks.SetLegacy\|VotingPlugin.Admin` | Set the legacy monthly vote streak amount |
| `/av User (player) VoteStreaks SetLegacy WEEK (number)` | `VotingPlugin.Commands.AdminVote.VoteStreaks.SetLegacy\|VotingPlugin.Admin` | Set the legacy weekly vote streak amount |
| `/av User (player) VoteStreaks SetSatisfied (votestreakstate) (boolean)` | `VotingPlugin.Commands.AdminVote.VoteStreaks.SetSatisfied\|VotingPlugin.Admin` | Set whether the current VoteStreak period is satisfied |
| `/av User (player) VoteStreaks SetVotes (votestreakstate) (number)` | `VotingPlugin.Commands.AdminVote.VoteStreaks.SetVotes\|VotingPlugin.Admin` | Set votes recorded in the current VoteStreak period |
| `/av User (player) VoteStreaks Status (votestreakstate)` | `VotingPlugin.Commands.AdminVote.VoteStreaks.Status\|VotingPlugin.Admin` | Show the stored state for a configured VoteStreak |
| `/av UUID (player)` | `VotingPlugin.Commands.AdminVote.UUID\|VotingPlugin.Admin` | View UUID of player |
| `/av Version` | `VotingPlugin.Commands.AdminVote.Version\|VotingPlugin.Admin` | List version info |
| `/av Vote` | `VotingPlugin.Commands.AdminVote.Vote\|VotingPlugin.Admin` | Manual vote syntax |
| `/av Vote (player)` | `VotingPlugin.Commands.AdminVote.Vote\|VotingPlugin.Admin` | Trigger manual vote via GUI |
| `/av Vote (player) (Sitename)` | `VotingPlugin.Commands.AdminVote.Vote\|VotingPlugin.Admin` | Trigger manual vote |
| `/av Vote (player) All` | `VotingPlugin.Commands.AdminVote.Vote\|VotingPlugin.Admin` | Trigger manual vote |
| `/av VoteExact (PlayerExact) (Sitename)` | `VotingPlugin.Commands.AdminVote.VoteExact\|VotingPlugin.Admin` | Trigger manual vote with exact player name |
| `/av VoteLog` | `VotingPlugin.Commands.AdminVote.VoteLog\|VotingPlugin.Admin` | See vote logs |
| `/av VoteLog (Number)` | `VotingPlugin.Commands.AdminVote.VoteLog\|VotingPlugin.Admin` | See vote logs |
| `/av VoteMilestone/VM Force (player) (milestone)` | `VotingPlugin.Commands.AdminVote.VoteMilestone.Force\|VotingPlugin.Admin` | Force execute a specific VoteMilestone (skips totals, respects limits) |
| `/av VoteMilestone/VM ForceGroup (player) (milestonegroup)` | `VotingPlugin.Commands.AdminVote.VoteMilestone.ForceGroup\|VotingPlugin.Admin` | Force execute VoteMilestones for a group (skips totals, respects limits) |
| `/av VoteMilestone/VM ForceGroupNoLimits (player) (milestonegroup)` | `VotingPlugin.Commands.AdminVote.VoteMilestone.ForceGroupNoLimits\|VotingPlugin.Admin` | Force execute VoteMilestones for a group (skips totals, bypasses limits) |
| `/av VoteMilestone/VM ForceNoLimits (player) (milestone)` | `VotingPlugin.Commands.AdminVote.VoteMilestone.ForceNoLimits\|VotingPlugin.Admin` | Force execute a specific VoteMilestone (skips totals, bypasses limits) |
| `/av VoteMilestone/VM List (milestonegroup)` | `VotingPlugin.Commands.AdminVote.VoteMilestone.List\|VotingPlugin.Admin` | List VoteMilestones in a group |
| `/av VoteMilestone/VM Preview (player) (milestonegroup)` | `VotingPlugin.Commands.AdminVote.VoteMilestone.Preview\|VotingPlugin.Admin` | Preview VoteMilestones for a group (shows totals/matches; does not execute) |
| `/av VoteMilestone/VM PreviewMilestone (player) (milestone)` | `VotingPlugin.Commands.AdminVote.VoteMilestone.PreviewMilestone\|VotingPlugin.Admin` | Preview a specific VoteMilestone (shows total/match/limit; does not execute) |
| `/av VoteMilestone/VM Status (player) (milestonegroup)` | `VotingPlugin.Commands.AdminVote.VoteMilestone.Status\|VotingPlugin.Admin` | Show VoteMilestone status for a group (current total; does not execute) |
| `/av VoteMilestone/VM StatusMilestone (player) (milestone)` | `VotingPlugin.Commands.AdminVote.VoteMilestone.StatusMilestone\|VotingPlugin.Admin` | Show status for a specific VoteMilestone (given/missing/due/pending; does not execute) |
| `/av VoteParty AddVoteCount (Number)` | `VotingPlugin.Commands.AdminVote.VoteParty.SetVoteCount\|VotingPlugin.Admin` | Add voteparty count |
| `/av VoteParty Force` | `VotingPlugin.Commands.AdminVote.VoteParty.Force\|VotingPlugin.Admin` | Force a voteparty reward, resets vote count |
| `/av VoteParty SetExtraRequired (Number)` | `VotingPlugin.Commands.AdminVote.VoteParty.SetExtraRequired\|VotingPlugin.Admin` | Set VotePartyExtraRequired value |
| `/av VoteParty SetVoteCount (Number)` | `VotingPlugin.Commands.AdminVote.VoteParty.SetVoteCount\|VotingPlugin.Admin` | Set voteparty count |
| `/av VotePresets` | `VotingPlugin.Commands.AdminVote.VotePresets\|VotingPlugin.Admin` | Open vote presets menu |
| `/av VotePresets (Text)` | `VotingPlugin.Commands.AdminVote.VotePresets\|VotingPlugin.Admin` | Find vote preset from url |
| `/av VoteSite (sitename) Check` | `VotingPlugin.Commands.AdminVote.VoteSite.Check\|VotingPlugin.Admin` | Check to see if VoteSite is valid |
| `/av VoteSite (sitename) Create` | `VotingPlugin.Commands.AdminVote.VoteSite.Edit\|VotingPlugin.Admin` | Create VoteSite |
| `/av VoteSite (sitename) SetEnabled (boolean)` | `VotingPlugin.Commands.AdminVote.VoteSite.Edit\|VotingPlugin.Admin` | Set VoteSite Enabled |
| `/av VoteSite (sitename) SetPriority (number)` | `VotingPlugin.Commands.AdminVote.VoteSite.Edit\|VotingPlugin.Admin` | Set VoteSite Priority |
| `/av VoteSite (sitename) SetServiceSite (string)` | `VotingPlugin.Commands.AdminVote.VoteSite.Edit\|VotingPlugin.Admin` | Set VoteSite ServiceSite |
| `/av VoteSite (sitename) SetVoteDelay (TEXT)` | `VotingPlugin.Commands.AdminVote.VoteSite.Edit\|VotingPlugin.Admin` | Set VoteSite VoteDelay |
| `/av VoteSite (sitename) SetVoteURL (string)` | `VotingPlugin.Commands.AdminVote.VoteSite.Edit\|VotingPlugin.Admin` | Set VoteSite VoteURL |

## Voting commands (`/vote`)

| Command | Permission | Description |
|---|---|
| `/vote ` | `VotingPlugin.Commands.Vote\|VotingPlugin.Player` | See voting URLs |
| `/vote Best` | `VotingPlugin.Commands.Vote.Best\|VotingPlugin.Player` | View your best voting |
| `/vote Best (player)` | `VotingPlugin.Commands.Vote.Best.Other\|VotingPlugin.Mod` | View someone's best voting |
| `/vote DateEvents` | `VotingPlugin.Commands.Vote.DateEvents\|VotingPlugin.Player` | View date-window vote milestone progress |
| `/vote GivePoints (player) (number)` | `VotingPlugin.Commands.Vote.GivePoints` | Give someone points from your points |
| `/vote GUI` | `VotingPlugin.Commands.Vote.GUI\|VotingPlugin.Player` | Open VoteGUI |
| `/vote GUI (player)` | `VotingPlugin.Commands.Vote.GUI.Other\|VotingPlugin.Mod` | Open VoteGUI |
| `/vote Help/?` | `VotingPlugin.Commands.Vote.Help\|VotingPlugin.Player` | View help page |
| `/vote Help/? (number)` | `VotingPlugin.Commands.Vote.Help\|VotingPlugin.Player` | View help page |
| `/vote Last` | `VotingPlugin.Commands.Vote.Last\|VotingPlugin.Player` | See your last votes |
| `/vote Last (player)` | `VotingPlugin.Commands.Vote.Last.Other\|VotingPlugin.Mod` | See other players last votes |
| `/vote LastMonthTop` | `VotingPlugin.Commands.Vote.LastMonthTop\|VotingPlugin.Player` | Open list of Top Voters from last month |
| `/vote List/All` | `VotingPlugin.Commands.Vote.List\|VotingPlugin.Player` | See voting URLs |
| `/vote Next` | `VotingPlugin.Commands.Vote.Next\|VotingPlugin.Player` | See your next votes |
| `/vote Next (player)` | `VotingPlugin.Commands.Vote.Next.Other\|VotingPlugin.Mod` | See other players next votes |
| `/vote Party` | `VotingPlugin.Commands.Vote.Party\|VotingPlugin.Player` | View current amount of votes and how many more needed |
| `/vote Points` | `VotingPlugin.Commands.Vote.Points\|VotingPlugin.Player` | View your points |
| `/vote Points (player)` | `VotingPlugin.Commands.Vote.Points.Other\|VotingPlugin.Mod` | View pints of other player |
| `/vote PreviousMonthsTotals` | `VotingPlugin.Commands.Vote.PreviousMonthsTotals` | Open list of Top Voters from all known previous months |
| `/vote Shop` | `VotingPlugin.Commands.Vote.Shop\|VotingPlugin.Player` | Open VoteShop GUI |
| `/vote Shop (Text)` | `VotingPlugin.Commands.Vote.Shop\|VotingPlugin.Player` | Open VoteShop GUI |
| `/vote Streak` | `VotingPlugin.Commands.Vote.Streak\|VotingPlugin.Player` | View your voting streak |
| `/vote Streak (player)` | `VotingPlugin.Commands.Vote.Streak.Other\|VotingPlugin.Mod` | View someone's voting streak |
| `/vote Today` | `VotingPlugin.Commands.Vote.Today\|VotingPlugin.Player` | View who list of who voted today |
| `/vote Today (number)` | `VotingPlugin.Commands.Vote.Today\|VotingPlugin.Player` | Open page of who Voted Today |
| `/vote ToggleBroadcast` | `VotingPlugin.Commands.Vote.ToggleBroadcast\|VotingPlugin.Player` | Toggle whether or not you will receive vote broadcasts |
| `/vote ToggleReminders` | `VotingPlugin.Commands.Vote.ToggleReminders\|VotingPlugin.Player` | Enable/disable vote reminders |
| `/vote Top` | `VotingPlugin.Commands.Vote.Top\|VotingPlugin.Player` | Open list of Top Voters |
| `/vote Top (number)` | `VotingPlugin.Commands.Vote.Top\|VotingPlugin.Player` | Open page of Top Voters |
| `/vote Total` | `VotingPlugin.Commands.Vote.Total\|VotingPlugin.Player` | View your total votes |
| `/vote Total (player)` | `VotingPlugin.Commands.Vote.Total.Other\|VotingPlugin.Mod` | View other players total votes |
| `/vote Total All` | `VotingPlugin.Commands.Vote.Total.All\|VotingPlugin.Player` | View server total votes |
| `/vote URL` | `VotingPlugin.Commands.Vote.URL\|VotingPlugin.Player` | Open VoteURL GUI |
| `/vote URL (SiteName)` | `VotingPlugin.Commands.Vote.URL.VoteSite` | Open VoteURL GUI for VoteSite |

## Optional and dynamically configured commands

The tables show command names that can be determined directly. This generated
snapshot omits 9 dynamically constructed command templates
rather than displaying Java expressions as usable commands.
Commands registered through configuration, optional integrations, and
other command dispatchers can also differ from these tables.

For proxy administration (`/votingpluginproxy`), see
[Proxy Setups](/VotingPlugin/Proxy-Setups).
For command access on a running server, use `/av perms` or
`/av permsplayer <player>`.
