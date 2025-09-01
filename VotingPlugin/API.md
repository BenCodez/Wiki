---
title: API
description: 
published: true
date: 2025-08-30T22:17:54.801Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:17:53.911Z
---

Want to hook into my plugin? Here's a basic overview on the API. This is useful if you want to make a addon or an extend the features of my plugin. More API to come! Feel free to request API if needed.

JavaDoc available [here](http://bencodez.github.io/VotingPlugin/)

### [VotingPluginHooks](https://bencodez.github.io/VotingPlugin/com/bencodez/votingplugin/VotingPluginHooks.html) - Class to make getting into the api a bit easier
- VotingPluginHooks.getInstance()
- Method to get main class
- Method to get user manager
- Method to inject into reward api

#### User object:
- [User object](https://bencodez.github.io/VotingPlugin/com/bencodez/votingplugin/user/VotingPluginUser.html)
- Creating object (plugin is main class):  
  - `plugin.getVotingPluginUserManager().getVotingPluginUser(playerName);`
  - `plugin.getVotingPluginUserManager().getVotingPluginUser(player);`
  - `plugin.getVotingPluginUserManager().getVotingPluginUser(uuid);`
  - [VotingPluginUserManager](https://bencodez.github.io/VotingPlugin/com/bencodez/votingplugin/user/UserManager.html)
- Using Examples:  
  - Get user points: `user.getPoints();`  
  - Set user points: `user.setPoints(int);`  

#### VoteSite object:
- [Object to handle vote sites](https://bencodez.github.io/VotingPlugin/com/bencodez/votingplugin/objects/VoteSite.html)
- The class ConfigVoteSites that handles the file reading/editing
- Create object:   
    `plugin.getVoteSite(name);`
- Using object:
  - Give vote site rewards: `voteSite.giveRewards(user); // user is user object`

#### Adding commands into /vote or /adminvvote
- With my command system, you can add your own custom commands in /vote or /adminvote, with tab complete support
- Define what arguments to add ("(player)","(sitename)","(string)","(number)","(reward)","(list)","(boolean)" are ones the plugin will add tab support and for example, check if argument is a number)
- Also use & to define multiple possible args (E.g. "Help&?")
- Examples (plugin is my Main plugin class, either add a CommandHandler to voteCommand or adminVoteCommand):  

        plugin.voteCommand.add(new CommandHandler(new String[] { "Next",
				"(player)" }, "Permission", "Help message for /vote help or /av help") {
			@Override
			public void execute(CommandSender sender, String[] args) {
                            // code to run when command is executed, if player has perms and
                            // args like number is met, plugin will check if it should be a number and check if args match
                            // no need to add it here
			}
		});
- See my [CommandLoader](https://github.com/BenCodez/VotingPlugin/blob/master/VotingPlugin/src/com/bencodez/votingplugin/commands/CommandLoader.java) class for more examples

#### [PlayerVoteEvent](https://bencodez.github.io/VotingPlugin/com/bencodez/votingplugin/events/PlayerVoteEvent.html):
- When a player votes, it will trigger a PlayerVoteEvent
- You can use this to cancel a vote, or whatever you want to do with it

#### [PlayerPostVotEvent](https://bencodez.github.io/VotingPlugin/com/bencodez/votingplugin/events/PlayerPostVoteEvent.html):
- Triggered after a vote has processed

#### [PlayerReceivePointsEvent](https://bencodez.github.io/VotingPlugin/com/bencodez/votingplugin/events/PlayerReceivePointsEvent.html):
- Trigger everytime player received vote points

#### [PlayerSpecialRewardEvent](https://bencodez.github.io/VotingPlugin/com/bencodez/votingplugin/events/PlayerSpecialRewardEvent.html):
- Trigger via any special reward
- [SpecialRewardType](https://bencodez.github.io/VotingPlugin/com/bencodez/votingplugin/events/SpecialRewardType.html)

#### [PlayerVoteCoolDownEndEvent](https://bencodez.github.io/VotingPlugin/com/bencodez/votingplugin/events/PlayerVoteCoolDownEndEvent.html):
- Trigger when player vote cool down ends on allsites

#### [PlayerVoteSiteCoolDownEndEvent](https://bencodez.github.io/VotingPlugin/com/bencodez/votingplugin/events/PlayerVoteSiteCoolDownEndEvent.html):
- Trigger when player vote cool down ends on a votesite

#### [VotePartyEvent](https://bencodez.github.io/VotingPlugin/com/bencodez/votingplugin/events/VotePartyEvent.html): 
- Triggered when a voteparty happens

#### [PlayerRewardEvent](https://bencodez.github.io/AdvancedCore/com/bencodez/advancedcore/listeners/PlayerRewardEvent.html):
- When a player is given a reward, it will trigger a PlayerRewardEvent
- You can use this to cancel a reward, or whatever you want to do with it

#### [PluginUpdateVersionEvent](https://bencodez.github.io/AdvancedCore/com/bencodez/advancedcore/listeners/PluginUpdateVersionEvent.html):
- Triggerd when plugin version changes

#### [AdvancedCoreLoginEvent](https://bencodez.github.io/AdvancedCore/com/bencodez/advancedcore/listeners/AdvancedCoreLoginEvent.html): 
- Triggerd on login, this includes any delay from login plugins like AuthMe
- Also accounts for vanished logins (if enabled)



