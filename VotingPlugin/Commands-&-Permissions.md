---
title: Commands & Permissions
description: 
published: true
date: 2026-02-14T20:48:15.801Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:03.502Z
---

## Commands and Permissions (From /av perms, use /av perms (player) to see what the specific player has):

| splits permissions up, meaning it can be either one before/after the |

    Command
      Permissions (seperated by |
      Help messasge
      
    /vote Help/?
      VotingPlugin.Commands.Vote.Help|VotingPlugin.Player
      View help page
    /vote Help/? (number)
      VotingPlugin.Commands.Vote.Help|VotingPlugin.Player
      View help page
    /vote ToggleReminders
      VotingPlugin.Commands.Vote.ToggleReminders
      Enable/disable vote reminders
    /vote Shop
      VotingPlugin.Commands.Vote.Shop|VotingPlugin.Player
      Open VoteShop GUI
    /vote Shop (Text)
      VotingPlugin.Commands.Vote.Shop|VotingPlugin.Player
      Open VoteShop GUI
    /vote URL (SiteName)
      VotingPlugin.Commands.Vote.URL.VoteSite
      Open VoteURL GUI for VoteSite
    /vote URL
      VotingPlugin.Commands.Vote.URL|VotingPlugin.Player
      Open VoteURL GUI
    /vote Last (player)
      VotingPlugin.Commands.Vote.Last.Other|VotingPlugin.Mod
      See other players last votes
    /vote Last
      VotingPlugin.Commands.Vote.Last|VotingPlugin.Player
      See your last votes
    /vote ToggleBroadcast
      VotingPlugin.Commands.Vote.ToggleBroadcast|VotingPlugin.Player
      Toggle whether or not you will recieve vote broadcasts
    /vote Next (player)
      VotingPlugin.Commands.Vote.Next.Other|VotingPlugin.Mod
      See other players next votes
    /vote Points (player)
      VotingPlugin.Commands.Vote.Points.Other|VotingPlugin.Mod
      View pints of other player
    /vote Points
      VotingPlugin.Commands.Vote.Points|VotingPlugin.Player
      View your points
    /vote Next
      VotingPlugin.Commands.Vote.Next|VotingPlugin.Player
      See your next votes
    /vote GUI (player)
      VotingPlugin.Commands.Vote.GUI.Other|VotingPlugin.Mod
      Open VoteGUI
    /vote GUI
      VotingPlugin.Commands.Vote.GUI|VotingPlugin.Player
      Open VoteGUI
    /vote LastMonthTop
      VotingPlugin.Commands.Vote.LastMonthTop|VotingPlugin.Player
      Open list of Top Voters from last month
    /vote Top
      VotingPlugin.Commands.Vote.Top|VotingPlugin.Player
      Open list of Top Voters
    /vote Top All
      VotingPlugin.Commands.Vote.Top.All|VotingPlugin.Player
      Open page of Top Voters
    /vote Top All (number)
      VotingPlugin.Commands.Vote.Top.All|VotingPlugin.Player
      Open page of Top Voters
    /vote Top Monthly
      VotingPlugin.Commands.Vote.Top.Monthly|VotingPlugin.Player
      Open page of Top Voters
    /vote Top Monthly (number)
      VotingPlugin.Commands.Vote.Top.Monthly|VotingPlugin.Player
      Open page of Top Voters
    /vote Top Weekly
      VotingPlugin.Commands.Vote.Top.Weekly|VotingPlugin.Player
      Open page of Top Voters
    /vote Top Weekly (number)
      VotingPlugin.Commands.Vote.Top.Weekly|VotingPlugin.Player
      Open page of Top Voters
    /vote Top Daily
      VotingPlugin.Commands.Vote.Top.Daily|VotingPlugin.Player
      Open page of Top Voters
    /vote Top Daily (number)
      VotingPlugin.Commands.Vote.Top.Daily|VotingPlugin.Player
      Open page of Top Voters
    /vote Top (number)
      VotingPlugin.Commands.Vote.Top|VotingPlugin.Player
      Open page of Top Voters
    /vote Party
      VotingPlugin.Commands.Vote.Party|VotingPlugin.Player
      View current amount of votes and how many more needed
    /vote Today (number)
      VotingPlugin.Commands.Vote.Today|VotingPlugin.Player
      Open page of who Voted Today
    /vote Today
      VotingPlugin.Commands.Vote.Today|VotingPlugin.Player
      View who list of who voted today
    /vote Total All
      VotingPlugin.Commands.Vote.Total.All|VotingPlugin.Player
      View server total votes
    /vote Total (player)
      VotingPlugin.Commands.Vote.Total.Other|VotingPlugin.Mod
      View other players total votes
    /vote Total
      VotingPlugin.Commands.Vote.Total|VotingPlugin.Player
      View your total votes
    /vote Best
      VotingPlugin.Commands.Vote.Best|VotingPlugin.Player
      View your best voting
    /vote Best (player)
      VotingPlugin.Commands.Vote.Best.Other|VotingPlugin.Mod
      View someone's best voting
    /vote Streak
      VotingPlugin.Commands.Vote.Streak|VotingPlugin.Player
      View your voting streak
    /vote Streak (player)
      VotingPlugin.Commands.Vote.Streak.Other|VotingPlugin.Mod
      View someone's voting streak
    /vote
      VotingPlugin.Commands.Vote|VotingPlugin.Player
      See voting URLs
    /vote List/All
      VotingPlugin.Commands.Vote.List|VotingPlugin.Player
      See voting URLs
    /vote Choices
      VotingPlugin.Choices|VotingPlugin.Player
      Let user select his choice reward
    /vote Choices SetPreference (ChoiceReward)
      VotingPlugin.ChoicesPreference|VotingPlugin.Player
      Let user pick his choice preferences
    /vote Choices SetPreference (ChoiceReward) (String)
      VotingPlugin.ChoicesPreference|VotingPlugin.Player
      Let user pick his choice preferences
    /av CurrentPluginTime
      VotingPlugin.Commands.AdminVote.CurrentPluginTime|VotingPlugin.Admin
      Current plugin time
    /av User (player) SetPoints (number)
      VotingPlugin.Commands.AdminVote.SetPoints|VotingPlugin.Admin
      Set players voting points
    /av ResyncMilestones
      VotingPlugin.Commands.AdminVote.ResyncMilestones|VotingPlugin.Admin
      Resync Milestones to all time total
    /av PauseRewards
      VotingPlugin.Commands.AdminVote.PauseRewards|VotingPlugin.Admin
      Pause rewards globally
    /av ResumeRewards
      VotingPlugin.Commands.AdminVote.ResumeRewards|VotingPlugin.Admin
      Resume rewards globally
    /av ResetMilestoneCount
      VotingPlugin.Commands.AdminVote.ResetMilestoneCount|VotingPlugin.Admin
      Resets milestone count to 0
    /av ResyncMilestonesAlreadyGiven
      VotingPlugin.Commands.AdminVote.ResyncMilestonesGiven|VotingPlugin.Admin
      Resync Milestones already given
    /av ResetPoints
      VotingPlugin.Commands.AdminVote.ResetPoints|VotingPlugin.Admin
      Clears all points of all players
    /av ResyncMilestones (player)
      VotingPlugin.Commands.AdminVote.SetResyncMilestones|VotingPlugin.Admin
      Resync Milestones to alltimetotal for player
    /av User (player) AddPoints (number)
      VotingPlugin.Commands.AdminVote.AddPoints|VotingPlugin.Admin
      Add to players voting points
    /av User (player) RemovePoints (number)
      VotingPlugin.Commands.AdminVote.RemovePoints|VotingPlugin.Admin
      Remove voting points
    /av Help/?
      VotingPlugin.Commands.AdminVote.Help|VotingPlugin.Admin
      See this page
    /av ServiceSites/Status
      VotingPlugin.Commands.AdminVote.ServiceSites|VotingPlugin.Admin
      See a list of all service sites the server got
    /av CorrectServiceSites
      VotingPlugin.Commands.AdminVote.CorrectServiceSites|VotingPlugin.Admin
      Attempt to correct invalid services sites
    /av Help/? (number)
      VotingPlugin.Commands.AdminVote.Help|VotingPlugin.Admin
      See this page
    /av Edit BungeeSettings
      VotingPlugin.Commands.AdminVote.Edit.BungeeSettings
      Edit BungeeSettings.yml
    /av Edit VoteShop
      VotingPlugin.Commands.AdminVote.Edit.VoteShop
      Edit VoteShop
    /av Edit MileStones
      VotingPlugin.Commands.AdminVote.Edit.MileStones
      Edit milestones rewards
    /av Edit Cumulative
      VotingPlugin.Commands.AdminVote.Edit.Cumulative
      Edit cumulative rewards
    /av Edit VoteParty
      VotingPlugin.Commands.AdminVote.Edit.VoteParty
      Edit voteparty
    /av Perms
      VotingPlugin.Commands.AdminVote.Perms|VotingPlugin.Admin
      List permissions
    /av Perms (Number)
      VotingPlugin.Commands.AdminVote.Perms|VotingPlugin.Admin
      List permissions
    /av PermsPlayer (Player)
      VotingPlugin.Commands.AdminVote.Perms.Other|VotingPlugin.Admin
      List permissions from the plugin the player has
    /av PermsPlayer (Player) (Number)
      VotingPlugin.Commands.AdminVote.Perms.Other|VotingPlugin.Admin
      List permissions from the plugin the player has
    /av Perms (Number) (Player)
      VotingPlugin.Commands.AdminVote.Perms.Other|VotingPlugin.Admin
      List permissions from the plugin the specificed player has
    /av PermsDebug
      VotingPlugin.Commands.AdminVote.PermsDebug
      Dev permission list, generate this list, requires dev debug
    /av Reload
      VotingPlugin.Commands.AdminVote.Reload|VotingPlugin.Admin
      Reload plugin, will not reload user storage
    /av ReloadAll
      VotingPlugin.Commands.AdminVote.Reload|VotingPlugin.Admin
      Reload plugin, including user storage
    /av Version
      VotingPlugin.Commands.AdminVote.Version|VotingPlugin.Admin
      List version info
    /av Sites
      VotingPlugin.Commands.AdminVote.Sites|VotingPlugin.Admin
      List VoteSites
    /av GUI
      VotingPlugin.Commands.AdminVote.GUI|VotingPlugin.Admin
      Admin GUI
    /av Sites (sitename)
      VotingPlugin.Commands.AdminVote.Sites.Site|VotingPlugin.Admin
      View Site Info
    /av TopPoints
      VotingPlugin.Commands.AdminVote.TopPoints|VotingPlugin.Admin
      Open the top points GUI
    /av UUID (player)
      VotingPlugin.Commands.AdminVote.UUID|VotingPlugin.Admin
      View UUID of player
    /av PlayerName (uuid)
      VotingPlugin.Commands.AdminVote.PlayerName|VotingPlugin.Admin
      View PlayerName of player
    /av ClearTotal
      VotingPlugin.Commands.AdminVote.ClearTotal.All|VotingPlugin.Admin
      Reset totals for all players
    /av ResetTotal (TopVoter)
      VotingPlugin.Commands.AdminVote.ResetTotal.All|VotingPlugin.Admin
      Reset specific totals for all players (DAY/WEEK/MONTH)
    /av ClearOfflineVoteRewards
      VotingPlugin.Commands.AdminVote.ClearOfflineVoteRewards|VotingPlugin.Admin
      Reset offline votes/rewards
    /av User (player) SetVoteStreak DAY (number)
      VotingPlugin.Commands.AdminVote.SetVoteStreak.Day|VotingPlugin.Admin
      Set votestreak for player
    /av User (player) SetVoteStreak WEEK (number)
      VotingPlugin.Commands.AdminVote.SetVoteStreak.Week|VotingPlugin.Admin
      Set votestreak for player
    /av User (player) SetVoteStreak MONTH (number)
      VotingPlugin.Commands.AdminVote.SetVoteStreak.Month|VotingPlugin.Admin
      Set votestreak for player
    /av User (player) SetTotal AllTime (number)
      VotingPlugin.Commands.AdminVote.SetTotal.AllTime|VotingPlugin.Admin
      Set AllTime totals for player
    /av User (player) AddTotal AllTime (number)
      VotingPlugin.Commands.AdminVote.AddTotal.AllTime|VotingPlugin.Admin
      Add AllTime totals for player
    /av User (player) SetTotal Monthly (number)
      VotingPlugin.Commands.AdminVote.SetTotal.Monthly|VotingPlugin.Admin
      Set Monthly totals for player
    /av User (player) AddTotal Monthly (number)
      VotingPlugin.Commands.AdminVote.AddTotal.Monthly|VotingPlugin.Admin
      Add Monthly totals for player
    /av User (player) SetTotal Weekly (number)
      VotingPlugin.Commands.AdminVote.SetTotal.Weekly|VotingPlugin.Admin
      Set Weekly totals for player
    /av User (player) AddTotal Weekly (number)
      VotingPlugin.Commands.AdminVote.AddTotal.Weekly|VotingPlugin.Admin
      Add Weekly totals for player
    /av User (player) SetTotal Daily (number)
      VotingPlugin.Commands.AdminVote.SetTotal.Daily|VotingPlugin.Admin
      Set Daily totals for player
    /av User (player) AddTotal Daily (number)
      VotingPlugin.Commands.AdminVote.AddTotal.Daily|VotingPlugin.Admin
      Add Daily totals for player
    /av User (player) ClearTotal
      VotingPlugin.Commands.AdminVote.ClearTotal|VotingPlugin.Admin
      Clear Totals for player
    /av User (player) ResetAllVotedSites
      VotingPlugin.Commands.AdminVote.ResetAllVotedSites|VotingPlugin.Admin
      Resets all voted
    /av User (player) ResetVotedSite (Sitename)
      VotingPlugin.Commands.AdminVote.ResetVotedSite|VotingPlugin.Admin
      Resets last voted for specific site
    /av User (player) AddMilestoneCount (number)
      VotingPlugin.Commands.AdminVote.AddMilestoneCount|VotingPlugin.Admin
      Add milestonecount
    /av User (player) SetMilestoneCount (number)
      VotingPlugin.Commands.AdminVote.SetMilestoneCount|VotingPlugin.Admin
      Set milestonecount
    /av User (player) ClearGottenMilestones
      VotingPlugin.Commands.AdminVote.ClearGottenMilestones|VotingPlugin.Admin
      Clears received milestones
    /av Vote (player) All
      VotingPlugin.Commands.AdminVote.Vote|VotingPlugin.Admin
      Trigger manual vote
    /av Vote (player) (Sitename)
      VotingPlugin.Commands.AdminVote.Vote|VotingPlugin.Admin
      Trigger manual vote
    /av VoteExact (PlayerExact) (Sitename)
      VotingPlugin.Commands.AdminVote.VoteExact|VotingPlugin.Admin
      Trigger manual vote with exact player name
    /av Vote (player)
      VotingPlugin.Commands.AdminVote.Vote|VotingPlugin.Admin
      Trigger manual vote via GUI
    /av Vote
      VotingPlugin.Commands.AdminVote.Vote|VotingPlugin.Admin
      Manual vote syntax
    /av User (Player) ForceVote All
      VotingPlugin.Commands.AdminVote.Vote|VotingPlugin.Admin
      Trigger manual vote
    /av User (Player) ForceVote (Sitename)
      VotingPlugin.Commands.AdminVote.Vote|VotingPlugin.Admin
      Trigger manual vote
    /av User (Player) ForceCoolDownEndRewards (Sitename)
      VotingPlugin.Commands.AdminVote.ForceCoolDownEndRewards|VotingPlugin.Admin
      Trigger CoolDownEndRewards manually
    /av VoteSite (sitename) Create
      VotingPlugin.Commands.AdminVote.VoteSite.Edit|VotingPlugin.Admin
      Create VoteSite
    /av Config TempDebug
      VotingPlugin.Commands.AdminVote.Config.Edit|VotingPlugin.Admin
      Enable debug, effective until reload/restart
    /av Config TempExtraDebug
      VotingPlugin.Commands.AdminVote.Config.Edit|VotingPlugin.Admin
      Enable extra debug, effective until reload/restart
    /av VoteSite (sitename) SetServiceSite (string)
      VotingPlugin.Commands.AdminVote.VoteSite.Edit|VotingPlugin.Admin
      Set VoteSite SerivceSite
    /av CheckVoteCoolDownRewards
      VotingPlugin.Commands.AdminVote.VoteSite.CheckVoteCoolDownRewards|VotingPlugin.Admin
      Force check all vote cooldown rewards
    /av VoteSite (sitename) SetVoteURL (string)
      VotingPlugin.Commands.AdminVote.VoteSite.Edit|VotingPlugin.Admin
      Set VoteSite VoteURL
    /av VoteSite (sitename) SetPriority (number)
      VotingPlugin.Commands.AdminVote.VoteSite.Edit|VotingPlugin.Admin
      Set VoteSite Priority
    /av VoteSite (sitename) SetVoteDelay (number)
      VotingPlugin.Commands.AdminVote.VoteSite.Edit|VotingPlugin.Admin
      Set VoteSite VoteDelay
    /av UpdateCheck
      VotingPlugin.Commands.AdminVote.UpdateCheck|VotingPlugin.Admin
      Check for update
    /av VoteSite (sitename) SetEnabled (boolean)
      VotingPlugin.Commands.AdminVote.VoteSite.Edit|VotingPlugin.Admin
      Set VoteSite Enabled
    /av VoteSite (sitename) Check
      VotingPlugin.Commands.AdminVote.VoteSite.Check|VotingPlugin.Admin
      Check to see if VoteSite is valid
    /av BackgroundUpdate
      VotingPlugin.Commands.AdminVote.BackgroundUpdate|VotingPlugin.Admin
      Force a background update
    /av ClearOfflineVotes
      VotingPlugin.Commands.AdminVote.ClearOfflineVotes|VotingPlugin.Admin
      Clear all offline votes
    /av Test (Player) (sitename) (number)
      VotingPlugin.Commands.AdminVote.Test|VotingPlugin.Admin
      Test voting speed, for debug
    /av TestSpam (Player) (sitename) (number)
      VotingPlugin.Commands.AdminVote.TestSpam|VotingPlugin.Admin
      Test voting spam speed, for debug
    /av TestReward (Player) (reward) (number)
      VotingPlugin.Commands.AdminVote.TestReward|VotingPlugin.Admin
      Test reward speed, for debug
    /av Placeholders
      VotingPlugin.Commands.AdminVote.Placeholders|VotingPlugin.Admin
      See possible placeholderapi placeholders
    /av VoteParty Force
      VotingPlugin.Commands.AdminVote.VoteParty.Force|VotingPlugin.Admin
      Force a voteparty reward, resets vote count
    /av VoteParty SetVoteCount (Number)
      VotingPlugin.Commands.AdminVote.VoteParty.SetVoteCount|VotingPlugin.Admin
      Set voteparty count
    /av VoteParty AddVoteCount (Number)
      VotingPlugin.Commands.AdminVote.VoteParty.SetVoteCount|VotingPlugin.Admin
      Add voteparty count
    /av VoteParty SetExtraRequired (Number)
      VotingPlugin.Commands.AdminVote.VoteParty.SetExtraRequired|VotingPlugin.Admin
      Set VotePartyExtraRequired value
    /av User (player) ForceVoteShop (VoteShop)
      VotingPlugin.Commands.AdminVote.ForceVoteShop|VotingPlugin.Admin
      Force a voteshop reward
    /av User (player) ForceMilestone (Number)
      VotingPlugin.Commands.AdminVote.ForceMilestone|VotingPlugin.Admin
      Force a milestone
    /av User (player) ForceTopVoter Daily (Number)
      VotingPlugin.Commands.AdminVote.ForceTopVoter.Daily|VotingPlugin.Admin
      Force a top voter reward
    /av User (player) ForceVoteStreak Day (Number)
      VotingPlugin.Commands.AdminVote.ForceVoteStreak|VotingPlugin.Admin
      Force a votestreak reward for Day
    /av User (player) ForceTopVoter Weekly (Number)
      VotingPlugin.Commands.AdminVote.ForceTopVoter.Weekly|VotingPlugin.Admin
      Force a top voter reward
    /av User (player) ForceVoteStreak Week (Number)
      VotingPlugin.Commands.AdminVote.ForceVoteStreak|VotingPlugin.Admin
      Force a votestreak reward for Week
    /av User (player) ForceTopVoter Monthly (Number)
      VotingPlugin.Commands.AdminVote.ForceTopVoter.Monthly|VotingPlugin.Admin
      Force a top voter reward
    /av User (player) ForceVoteStreak Month (Number)
      VotingPlugin.Commands.AdminVote.ForceVoteStreak|VotingPlugin.Admin
      Force a votestreak reward for Month
    /av User (player) ForceCumulative (Number)
      VotingPlugin.Commands.AdminVote.ForceCumulative|VotingPlugin.Admin
      Force a cumulative reward
    /av User (player) ForceAllSites
      VotingPlugin.Commands.AdminVote.ForceAllSites|VotingPlugin.Admin
      Force a allsites reward
    /av User (player) ForceAlmostAllSites
      VotingPlugin.Commands.AdminVote.ForceAllSites|VotingPlugin.Admin
      Force a almostallsites reward
    /av User (player) ForceFirstVote
      VotingPlugin.Commands.AdminVote.ForceFirstVote|VotingPlugin.Admin
      Force a firstvote reward
    /av User (player) ForceFirstVoteToday
      VotingPlugin.Commands.AdminVote.ForceFirstVoteToday|VotingPlugin.Admin
      Force a firstvotetoday reward
    /av PurgeNoData
      VotingPlugin.PurgeNoData
      Purge players from database with no data and haven't been online for a number of days (Set in Config.yml)
    /av RemoveOfflineUUIDs
      VotingPlugin.Commands.AdminVote.RemoveOfflineUUIDs|VotingPlugin.Admin
      Purges database of offline UUIDs, keeps online UUIDs
    /av Placeholders (player)
      VotingPlugin.Commands.AdminVote.Placeholders.Players|VotingPlugin.Admin
      See possible placeholderapi placeholders with player values
    /av MergeDataFrom (UserStorage)
      VotingPlugin.Commands.AdminVote.MergeDataFrom|VotingPlugin.Admin
      Merge player totals from other storage type
    /av
      VotingPlugin.Commands.AdminVote|VotingPlugin.Admin
      Base command
    /av RunCMD All (List)
      VotingPlugin.RunCMD.All|VotingPlugin.Admin
      Run command for every user, use %player% for player
    /av RunSQLQuery (List)
      VotingPlugin.RunSQLQuery|VotingPlugin.Admin
      Execute sql query
    /av UpdateMySQLColumnSizes
      VotingPlugin.UpdateMySQLColumn|VotingPlugin.Admin
      Update current mysql column sizes
    /av TotalNumberOfUsers
      VotingPlugin.TotalNumberOfUsers|VotingPlugin.Admin
      Gets current number of users in VotingPlugin database
    /av GiveAll (reward)
      VotingPlugin.GiveAll|VotingPlugin.Admin
      Give all users a reward
    /av GiveAllOnline (reward)
      VotingPlugin.GiveAllOnline|VotingPlugin.Admin
      Give all users a reward
    /av GiveReward (Player) (Reward)
      VotingPlugin.GiveReward|VotingPlugin.Admin
      Give a player a reward file
    /av User (Player) ForceReward (Reward)
      VotingPlugin.GiveReward|VotingPlugin.Admin
      Give a player a reward file
    /av GiveReward (Player) (Reward) (Text) (Text)
      VotingPlugin.GiveReward|VotingPlugin.Admin
      Give a player a reward file and set a placeholder
    /av Report
      VotingPlugin.Report|VotingPlugin.Admin
      Create Report File
    /av ClearOfflineRewards
      VotingPlugin.ClearOfflineRewards|VotingPlugin.Admin
      Clear offline rewards
    /av ForceRunOfflineRewards
      VotingPlugin.ForceRunOfflineRewards|VotingPlugin.Admin
      Force run all offline rewards as if they were online for all players
    /av ForceRunOfflineRewards (player)
      VotingPlugin.ForceRunOfflineRewards|VotingPlugin.Admin
      Force run all offline rewards as if they were online for a specific player
    /av GUI
      VotingPlugin.AdminGUI|VotingPlugin.Admin
      Open AdminGUI
    /av Rewards
      VotingPlugin.RewardEdit|VotingPlugin.Admin
      Open RewardGUI
    /av User
      VotingPlugin.UserEdit|VotingPlugin.Admin
      Open UserGUI
    /av User (Player)
      VotingPlugin.UserEdit|VotingPlugin.Admin
      Open UserGUI
    /av User (Player) RemoveTempPermissions
      VotingPlugin.RemoveTempPermission|VotingPlugin.Admin
      Remove temp permissions
    /av User (Player) AddTempPermissions (Text) (Number)
      VotingPlugin.AddTempPermission|VotingPlugin.Admin
      Add temp permission for number of seconds
    /av User (Player) AddTempPermissions (Text)
      VotingPlugin.AddTempPermission|VotingPlugin.Admin
      Add temp permission
    /av Report
      VotingPlugin.Report|VotingPlugin.Admin
      Create a zip file to send for debuging
    /av UserRemove (player)
      VotingPlugin.UserRemove|VotingPlugin.Admin
      Remove User
    /av UserUUIDRemove (uuid)
      VotingPlugin.UserRemove|VotingPlugin.Admin
      Remove User
    /av ClearCache
      VotingPlugin.ClearCache|VotingPlugin.Admin
      Clear MySQL Cache
    /av Purge
      VotingPlugin.Purge|VotingPlugin.Admin
      Purge Data
    /av DownloadJenkins
      VotingPlugin.Download|VotingPlugin.Admin
      Download from jenkins. Please use at your own risk
    /av ForceTimeChange (TimeType)
      VotingPlugin.ForceTimeChange|VotingPlugin.Admin
      Force time change, use at your own risk!
    /av Javascript (List)
      VotingPlugin.Javascript|VotingPlugin.Admin
      Execute javascript
    /av SetRequestMethod (RequestMethod)
      VotingPlugin.SetRequestMethod|VotingPlugin.Admin
      SetRequestMethod
    /av SetRequestMethod
      VotingPlugin.SetRequestMethod|VotingPlugin.Admin
      SetRequestMethod
    /av User All SetData (text) (text)
      VotingPlugin.SetAllData|VotingPlugin.Admin
      Set all users data
    /av User (player) SetData (text) (text)
      VotingPlugin.SetData|VotingPlugin.Admin
      Set user data
    /av User (Player) ViewData
      VotingPlugin.ViewData|VotingPlugin.Admin
      View playerdata
    /av User (Player) ViewCache
      VotingPlugin.ViewCache|VotingPlugin.Admin
      View playerdata
    /av User (Player) ForceCache
      VotingPlugin.ForceCache|VotingPlugin.Admin
      View playerdata
    /av User (Player) HasPermission (Text)
      VotingPlugin.HasPermission|VotingPlugin.Admin
      View playerdata
    /av Choices SetPreference (ChoiceReward) (String) (Player)
      VotingPlugin.ChoicesSetPreferenceOther|VotingPlugin.Admin
      Let user pick his choice preferences
    /av ConvertToData (UserStorage)
      VotingPlugin.Commands.AdminVote.ConvertToData|VotingPlugin.Admin
      Convert user storage from current storage type the one specificed
    /av ConvertFromData (UserStorage)
      VotingPlugin.Commands.AdminVote.ConvertFromData|VotingPlugin.Admin
      Convert user storage from current storage type from the one specificed
    VotingPlugin.Player : Allows basic access player commands
    VotingPlugin.Mod : Allows mod commands
    VotingPlugin.Admin : Allows admincommands
    VotingPlugin.Admin.Debug : Permission to view debug info ingame
    VotingPlugin.TopVoter.Ignore : Allows you to be exempt from top voter
    VotingPlugin.NoRemind : Ignore vote reminding
    VotingPlugin.BypassWaitUntilVoteDelay : Bypass WaitUntilVoteDelay
    VotingPlugin.Sign.Create : Permission to create sign
    VotingPlugin.Admin.GenerateServiceSite : Permission for generating votesite message
    VotingPlugin.Login.RemindVotes : Permission to allow timed reminders
    VotingPlugin.Login.RemindVotes.All : Remind if player can vote on all votesites, rather than any

## BungeeCord/Velocity:

    /votingpluginproxy vote (player) (site)
    /votingpluginproxy status
    /votingpluginproxy help
    /votingpluginproxy forcetimechange (DAY/WEEK/MONTH)
    /votingpluginproxy reload
    /votingpluginproxy reloadall
    /votingpluginproxy voteparty force - Force a vote party
    /votingpluginproxy voteparty setvotecount (number) - Set current vote party votes
    /votingpluginproxy multiproxystatus