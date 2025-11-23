---
title: API
description: 
published: true
date: 2025-11-23T19:39:23.432Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:17:53.911Z
---

# 🧩 VotingPlugin Developer API

Want to hook into VotingPlugin for your own plugin or addon?  
This guide provides an overview of the public API, available events, and examples for extending or integrating with VotingPlugin.

**JavaDocs**  
- VotingPlugin: https://bencodez.github.io/VotingPlugin/  
- AdvancedCore: https://bencodez.github.io/AdvancedCore/

---

## ⚙️ Getting Started with the API

### 🔗 VotingPluginHooks  
Helper class to access core API functions.

Class: VotingPluginHooks  
https://bencodez.github.io/VotingPlugin/com/bencodez/votingplugin/VotingPluginHooks.html

Example usage (pseudo-code):

- `VotingPluginHooks hooks = VotingPluginHooks.getInstance()`  
- `hooks.getPlugin()`  
- `hooks.getUserManager()`  
- `hooks.injectRewardAPI()`
- '`VotingPluginMain plugin =
        (VotingPluginMain) Bukkit.getPluginManager().getPlugin("VotingPlugin");`

---

## 👤 User Object

Class: VotingPluginUser  
https://bencodez.github.io/VotingPlugin/com/bencodez/votingplugin/user/VotingPluginUser.html

Manager: VotingPluginUserManager  
https://bencodez.github.io/VotingPlugin/com/bencodez/votingplugin/user/UserManager.html

### Creating a user
- `plugin.getVotingPluginUserManager().getVotingPluginUser(player)`  
- `plugin.getVotingPluginUserManager().getVotingPluginUser("BenCodez")`  
- `plugin.getVotingPluginUserManager().getVotingPluginUser(uuid)`

### Using a user
- `user.getPoints()`  
- `user.setPoints(100)`  
- `user.addPoints(10)`  
- `user.removePoints(5)`

---

## 🌐 VoteSite Object

Class: VoteSite  
https://bencodez.github.io/VotingPlugin/com/bencodez/votingplugin/objects/VoteSite.html

### Example usage
- `VoteSite site = plugin.getVoteSite("ExampleSite")`  
- `site.giveRewards(user)`

---

## 🧰 Adding Custom Commands

VotingPlugin supports registering custom sub-commands under:

- `/vote`
- `/adminvote` (alias: `/av`)

Supported argument types include:

`(player)`, `(sitename)`, `(string)`, `(number)`, `(reward)`, `(list)`, `(boolean)`

Use `Help&?` to add multiple aliases.

Example (pseudo-code):
```
plugin.getVoteCommand().add(new CommandHandler(
        new String[] { "Next", "(player)" },
        "Permission",
        "Help message"
) {
    @Override
    public void execute(CommandSender sender, String[] args) {
        // your code
    }
});

```

More examples:  
https://github.com/BenCodez/VotingPlugin/blob/master/VotingPlugin/src/main/java/com/bencodez/votingplugin/commands/CommandLoader.java

---

# 🧱 VotingPlugin Events

All events use Bukkit’s normal event system (`@EventHandler`).  
Below is the **complete list of VotingPlugin + AdvancedCore events**.

---

## 🗳️ PlayerVoteEvent  
https://bencodez.github.io/VotingPlugin/com/bencodez/votingplugin/events/PlayerVoteEvent.html

Triggered when a vote is received (before processing).  
Can be cancelled.

---

## 🎉 PlayerPostVoteEvent  
https://bencodez.github.io/VotingPlugin/src/main/java/com/bencodez/votingplugin/events/PlayerPostVoteEvent.html

Triggered after the vote is fully processed and rewards are applied.

---

## 💰 PlayerReceivePointsEvent  
https://bencodez.github.io/VotingPlugin/com/bencodez/votingplugin/events/PlayerReceivePointsEvent.html

Triggered whenever a player receives vote points.

---

## ⭐ PlayerSpecialRewardEvent  
https://bencodez.github.io/VotingPlugin/com/bencodez/votingplugin/events/PlayerSpecialRewardEvent.html

Triggers on:

- Milestones  
- Streak rewards  
- VoteParty rewards  
- Top voter rewards  
- AllSites / AlmostAllSites rewards  

SpecialRewardType:  
https://bencodez.github.io/VotingPlugin/com/bencodez/votingplugin/events/SpecialRewardType.html

---

## ⏰ PlayerVoteCoolDownEndEvent  
https://bencodez.github.io/VotingPlugin/com/bencodez/votingplugin/events/PlayerVoteCoolDownEndEvent.html

Triggered when cooldown ends for **all sites**.

---

## 🕓 PlayerVoteSiteCoolDownEndEvent  
https://bencodez.github.io/VotingPlugin/com/bencodez/votingplugin/events/PlayerVoteSiteCoolDownEndEvent.html

Triggered when cooldown ends for **one specific votesite**.

---

## 🎊 VotePartyEvent  
https://bencodez.github.io/VotingPlugin/com/bencodez/votingplugin/events/VotePartyEvent.html

Triggered when:

- The vote party threshold is reached  
- A vote party reward is fired  

Supports cross-server vote party logic.

---

## 🎁 PlayerRewardEvent (AdvancedCore)  
https://bencodez.github.io/AdvancedCore/com/bencodez/advancedcore/listeners/PlayerRewardEvent.html

Triggered whenever **any reward file** executes, not just voting rewards.

You can:

- Cancel the reward  
- Log rewards  
- Modify reward execution  

---

## 🔄 PluginUpdateVersionEvent (AdvancedCore)  
https://bencodez.github.io/AdvancedCore/com/bencodez/advancedcore/listeners/PluginUpdateVersionEvent.html

Triggered when plugin version changes.

---

## 👥 AdvancedCoreLoginEvent (AdvancedCore)  
https://bencodez.github.io/AdvancedCore/com/bencodez/advancedcore/listeners/AdvancedCoreLoginEvent.html

Triggered when a player logs in *after AuthMe / Vanish / LoginSecurity delays*.

Useful for:

- vote reminding  
- delivering queued rewards  
- placeholder recalculation  

---

## 🧮 PlayerPointsUpdateEvent  
https://bencodez.github.io/VotingPlugin/com/bencodez/votingplugin/events/PlayerPointsUpdateEvent.html

Triggered whenever:

- Points are added  
- Points are removed  
- Points are set to a new value  

---

## 🗓️ TimeChangeEvent  
https://bencodez.github.io/VotingPlugin/com/bencodez/votingplugin/events/TimeChangeEvent.html

Triggered when the plugin detects a **DAY**, **WEEK**, or **MONTH** rollover.
