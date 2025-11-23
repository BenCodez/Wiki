---
title: Setup
description: 
published: true
date: 2025-11-23T20:03:03.560Z
tags: 
editor: markdown
dateCreated: 2025-08-31T03:20:39.536Z
---

# Setup VotingPlugin

Follow these steps to set up VotingPlugin on your server.

---

## 1. Verify Votifier Installation
Make sure your vote listener plugin is correctly installed and working:

- **Recommended:** [VotifierPlus](https://github.com/BenCodez/VotifierPlus) (by BenCodez)
- **Alternative:** [NuVotifier](https://github.com/NuVotifier/NuVotifier)

If you’re not receiving votes, check this guide:  
➡️ [Votifier Troubleshooting](https://wiki.bencodez.com/en/VotingPlugin/Votifier-Troubleshooting)

---

## 2. Proxy Setup (If Using Bungee/Velocity)
If you run a network, you’ll still need to configure VotingPlugin on **each** backend server.

Choose one of the available proxy setup methods here:  
👉 [Proxy Setups](https://wiki.bencodez.com/en/VotingPlugin/Proxy-Setups)

Make sure your chosen method (**PLUGINMESSAGING**, **SOCKET**, or **MYSQL**) is consistent across all connected servers.

---

## 3. Create and Configure VoteSites

VotingPlugin allows you to define one or more voting sites that reward players when they vote.  
You can configure them in several different ways.

---

### Option 1 – Auto-Generate from a Vote
If a player votes and the site isn’t listed, VotingPlugin can automatically create a new entry in `VoteSites.yml`.

- Enabled by default (`AutoCreateVoteSites: true` in `Config.yml`)
- The plugin detects the site name from the vote listener (VotifierPlus/NuVotifier) and creates a template entry.

⚠️ **Your vote listener must be working properly** for this to function.  
Each received vote prints the service site name in console, for example:  
**Received vote from MinecraftServers.org for player BenCodez**

---

### Option 2 – In-Game GUI
You can create or edit vote sites through the GUI:

1. Run `/av gui`  
2. Middle-click **VoteSites**  
3. Enter the new site name  
4. Fill in details (service site, vote URL, rewards, etc.)

---

### Option 3 – Desktop Editor
Use the standalone configuration tool for a graphical editor:  
➡️ [VotingPluginEditor](https://github.com/BenCodez/VotingPluginEditor)

This lets you visually edit vote sites and validate fields before saving.

---

### Option 4 – Manual Configuration
Edit the file:

`/plugins/VotingPlugin/VoteSites.yml`

Example:
```
VoteSites:
  MinecraftServers:
    Enabled: true
    ServiceSite: MinecraftServers.org
    VoteURL: https://minecraftservers.org/vote/example
    VoteDelay: 24
    Rewards:
      Messages:
        Player: '&aThanks for voting on %ServiceSite%!'
      Commands:
      - give %player% diamond 1
```

**Key fields**

| Field | Description |
|--------|-------------|
| **ServiceSite** | Must match the site name sent by Votifier. Use `/av servicesites` or check console to confirm. |
| **VoteDelay** | How often a player can vote on that site (`24`, `12`, `1`, etc.), Use VoteDelayMin for minute offsets. |
| **VoteURL** | The URL players use to vote. |
| **Rewards** | Commands, messages, and items executed when a vote is received. |

⚠️ **Important:** The `ServiceSite` must match exactly or no rewards will trigger.  
Use `/av servicesites` in-game to list all known sites.

---

## 4. Set Up Rewards
Define what players receive when they vote.

- Use `/av gui` to create or test rewards directly in-game.
- Anything from the example reward files can be placed under `/plugins/VotingPlugin/Rewards/`.

Example reward templates:  
- [ExampleBasic.yml](https://github.com/BenCodez/AdvancedCore/blob/master/AdvancedCore/src/main/resources/Rewards/ExampleBasic.yml)  
- [ExampleAdvanced.yml](https://github.com/BenCodez/AdvancedCore/blob/master/AdvancedCore/src/main/resources/Rewards/ExampleAdvanced.yml)

Learn more: [Reward System](https://wiki.bencodez.com/en/VotingPlugin/reward-system)

---

## 5. Permissions
By default, players receive the permission:

`VotingPlugin.Player` → gives access to all main player commands.

If your permissions plugin does **not** auto-grant it, add it manually.

You can:
- View all permissions: `/av perms`  
- Check a specific player: `/av permsplayer <player>`

Some commands have multiple permission nodes (listed here):  
👉 [Commands & Permissions](https://wiki.bencodez.com/en/VotingPlugin/Commands-&-Permissions)

---

## 6. Final Steps
You’re all set! Restart your server, vote once to test, and confirm rewards are given.

If anything doesn’t work:
- Check console for errors or missing service sites.  
- Use `/adminvote` commands to test manually.  
- Ensure the correct database or proxy settings are applied.

💬 Still stuck? Contact **BenCodez** via GitHub or Discord.

---

## Additional Setup Guides
External tutorials that may help with hosting panel setups:

- [ServerMiner – Setup Voting](https://serverminer.com/article/how-to-setup-voting-on-your-minecraft-server/)  
- [WitherHosting – VotingPlugin Setup](https://support.witherhosting.com/en/article/how-to-install-and-use-votingplugin-java-6epg7/)
