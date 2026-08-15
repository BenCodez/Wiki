---
title: API
description: Integrate with VotingPlugin 7.1.1 users, vote sites, commands, rewards, and events
published: true
date: 2026-08-14T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2025-08-30T22:17:53.911Z
---

# VotingPlugin Developer API

> **Release baseline:** The signatures and source links on this page target VotingPlugin **7.1.1**. Current Javadocs or `master` may contain unreleased 7.1.2-SNAPSHOT changes.
{.is-info}

VotingPlugin 7.1.1 requires Java 21.

- [Current VotingPlugin Javadocs](https://bencodez.github.io/VotingPlugin/)
- [Current AdvancedCore Javadocs](https://bencodez.github.io/AdvancedCore/)
- [VotingPlugin 7.1.1 source](https://github.com/BenCodez/VotingPlugin/tree/7.1.1)

Declare VotingPlugin as a dependency or soft dependency before accessing it.

## Plugin and hooks

```java
VotingPluginMain plugin = (VotingPluginMain) Bukkit.getPluginManager()
        .getPlugin("VotingPlugin");

if (plugin == null || !plugin.isEnabled()) {
    return;
}

VotingPluginHooks hooks = VotingPluginHooks.getInstance();
UserManager userManager = hooks.getUserManager();
```

Release 7.1.1 `VotingPluginHooks` provides:

| Method | Purpose |
|---|---|
| `getMainClass()` | Current `VotingPluginMain`. |
| `getUserManager()` | VotingPlugin user manager. |
| `backgroundUpdate(Player)` | User vote/offline-reward update. |
| `addCustomReward(RewardInject)` | Registers a custom reward injection. |
| `addCustomRequirement(RequirementInject)` | Registers a custom requirement injection. |

See [`VotingPluginHooks.java` at 7.1.1](https://github.com/BenCodez/VotingPlugin/blob/7.1.1/VotingPlugin/src/main/java/com/bencodez/votingplugin/VotingPluginHooks.java).

## Users

```java
VotingPluginUser byPlayer = plugin.getVotingPluginUserManager()
        .getVotingPluginUser(player);
VotingPluginUser byName = plugin.getVotingPluginUserManager()
        .getVotingPluginUser("BenCodez");
VotingPluginUser byUuid = plugin.getVotingPluginUserManager()
        .getVotingPluginUser(uuid);
```

```java
int points = byPlayer.getPoints();
byPlayer.setPoints(100);
byPlayer.addPoints(10);
byPlayer.removePoints(5);
```

Do not perform blocking storage work on the Bukkit main thread. Account for uncached/offline users and the plugin's scheduler expectations.

## Vote sites

```java
VoteSite site = plugin.getVoteSite("ExampleSite", true);
if (site != null) {
    site.giveRewards(user, user.isOnline(), false);
}
```

The second lookup argument controls enabled-site filtering. Real vote processing also needs the correct service-site, online, storage, and proxy context; do not use this short example as a replacement for VotingPlugin's vote pipeline.

## Add a subcommand

```java
plugin.getVoteCommand().add(new CommandHandler(
        plugin,
        new String[] { "Example", "(player)" },
        "myplugin.command.example",
        "Run the example command"
) {
    @Override
    public void execute(CommandSender sender, String[] args) {
        if (args.length < 2) {
            return;
        }
        sender.sendMessage("Example command for " + args[1]);
    }
});
```

Use `plugin.getAdminVoteCommand()` for an `/adminvote` (`/av`) subcommand. Validate argument counts, sender type, permissions, and player lookup.

See [`CommandLoader.java` at 7.1.1](https://github.com/BenCodez/VotingPlugin/blob/7.1.1/VotingPlugin/src/main/java/com/bencodez/votingplugin/commands/CommandLoader.java).

## Events

```java
@EventHandler
public void onVote(PlayerPostVoteEvent event) {
    getLogger().info(event.getPlayerName() + " voted on " + event.getService());
}
```

Release 7.1.1 includes:

| Event | Purpose |
|---|---|
| `PlayerVoteEvent` | Vote enters VotingPlugin processing and exposes cancellation/override controls. |
| `PlayerPostVoteEvent` | Post-vote stage. |
| `PlayerReceivePointsEvent` | Points are about to be applied. |
| `PlayerSpecialRewardEvent` | A VotingPlugin special reward is processed. |
| `PlayerVoteCoolDownEndEvent` | Overall vote cooldown becomes available. |
| `PlayerVoteSiteCoolDownEndEvent` | One site's cooldown becomes available. |
| `VotePartyEvent` | Vote party triggers. |
| `VoteMilestoneRewardEvent` | A VoteMilestone reward completes. |
| `VoteShopPurchaseEvent` | A VoteShop purchase is attempted. |

Use the [7.1.1 events directory](https://github.com/BenCodez/VotingPlugin/tree/7.1.1/VotingPlugin/src/main/java/com/bencodez/votingplugin/events) as the release-authoritative list.

## Compatibility

- Compile and test against every VotingPlugin version you claim to support.
- Do not infer released API from `master` or snapshot Javadocs.
- Prefer public APIs over reflection.
- Test online, offline/queued, SQL, standalone, and proxy contexts relevant to the integration.
