---
title: API
description: Integrate with VotingPlugin users, vote sites, commands, and events
published: true
date: 2025-11-23T19:39:23.432Z
tags:
editor: markdown
dateCreated: 2025-08-30T22:17:53.911Z
---

# VotingPlugin Developer API

VotingPlugin exposes user, vote-site, command, reward-extension, and event APIs
for Bukkit plugins.

- [VotingPlugin Javadocs](https://bencodez.github.io/VotingPlugin/)
- [AdvancedCore Javadocs](https://bencodez.github.io/AdvancedCore/)
- [VotingPlugin source](https://github.com/BenCodez/VotingPlugin)

Add VotingPlugin as a dependency or soft dependency in your plugin metadata
before accessing it.

## Getting the plugin and hooks

```java
VotingPluginMain plugin = (VotingPluginMain) Bukkit.getPluginManager()
        .getPlugin("VotingPlugin");

if (plugin == null || !plugin.isEnabled()) {
    return;
}

VotingPluginHooks hooks = VotingPluginHooks.getInstance();
UserManager userManager = hooks.getUserManager();
```

Current `VotingPluginHooks` methods include:

| Method | Purpose |
|---|---|
| `getMainClass()` | Returns the current `VotingPluginMain` instance |
| `getUserManager()` | Returns VotingPlugin's user manager |
| `backgroundUpdate(Player)` | Runs the user's vote/offline-reward update |
| `addCustomReward(RewardInject)` | Registers a custom AdvancedCore reward |
| `addCustomRequirement(RequirementInject)` | Registers a custom reward requirement |

See
[`VotingPluginHooks.java`](https://github.com/BenCodez/VotingPlugin/blob/master/VotingPlugin/src/main/java/com/bencodez/votingplugin/VotingPluginHooks.java)
for the current contract.

## User objects

```java
VotingPluginUser byPlayer = plugin.getVotingPluginUserManager()
        .getVotingPluginUser(player);

VotingPluginUser byName = plugin.getVotingPluginUserManager()
        .getVotingPluginUser("BenCodez");

VotingPluginUser byUuid = plugin.getVotingPluginUserManager()
        .getVotingPluginUser(uuid);
```

Common point operations include:

```java
int points = byPlayer.getPoints();
byPlayer.setPoints(100);
byPlayer.addPoints(10);
byPlayer.removePoints(5);
```

Do not perform blocking database work on the Bukkit main thread. Use the
plugin's existing APIs and scheduler expectations when working with uncached
users.

## Vote sites

`VoteSite` is in `com.bencodez.votingplugin.votesites`.

```java
VoteSite site = plugin.getVoteSite("ExampleSite", true);
if (site != null) {
    site.giveRewards(user, user.isOnline(), false);
}
```

The second `getVoteSite` argument controls whether disabled sites are filtered
out. Reward delivery also needs the correct online and proxy/Bungee context;
do not blindly copy the example when processing a real vote.

## Adding a subcommand

VotingPlugin uses AdvancedCore's `CommandHandler`. Pass the plugin instance to
the current constructor:

```java
plugin.getVoteCommand().add(new CommandHandler(
        plugin,
        new String[] { "Example", "(player)" },
        "myplugin.command.example",
        "Run the example command"
) {
    @Override
    public void execute(CommandSender sender, String[] args) {
        sender.sendMessage("Example command for " + args[1]);
    }
});
```

Use `plugin.getAdminVoteCommand()` to add an `/adminvote` (`/av`) subcommand.
For production code, validate argument counts, console access, permissions, and
player lookup behavior.

Current examples are available in
[`CommandLoader.java`](https://github.com/BenCodez/VotingPlugin/blob/master/VotingPlugin/src/main/java/com/bencodez/votingplugin/commands/CommandLoader.java).

## VotingPlugin events

Register listeners through Bukkit's normal event system:

```java
@EventHandler
public void onVote(PlayerPostVoteEvent event) {
    getLogger().info(event.getPlayerName() + " voted on " + event.getService());
}
```

The current VotingPlugin event classes are:

| Event | When it is used |
|---|---|
| `PlayerVoteEvent` | A vote enters VotingPlugin processing; exposes vote, total, broadcast, and cancellation controls |
| `PlayerPostVoteEvent` | Vote processing has reached the post-vote stage |
| `PlayerReceivePointsEvent` | Vote points are about to be applied; exposes points and cancellation controls |
| `PlayerSpecialRewardEvent` | A VotingPlugin special reward is processed |
| `PlayerVoteCoolDownEndEvent` | A player's overall voting cooldown becomes available |
| `PlayerVoteSiteCoolDownEndEvent` | A specific vote site's cooldown becomes available |
| `VotePartyEvent` | A vote party is triggered |
| `VoteMilestoneRewardEvent` | A VoteMilestone reward completes successfully |
| `VoteShopPurchaseEvent` | A player attempts a VoteShop purchase |

Use the
[`events` source directory](https://github.com/BenCodez/VotingPlugin/tree/master/VotingPlugin/src/main/java/com/bencodez/votingplugin/events)
as the authoritative list. AdvancedCore also publishes reward and lifecycle
events; check its current source or Javadocs before depending on one.

## Compatibility guidance

- Compile against the VotingPlugin and AdvancedCore versions you support.
- Treat source and Javadocs for that version as authoritative.
- Use soft dependency handling if your plugin can operate without VotingPlugin.
- Avoid reflection when a public API is available.
- Test integrations with both cached/offline votes and normal online votes.
