---
title: Setup
description: 
published: true
date: 2025-11-06T02:04:28.887Z
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

- Choose one of the available proxy setup methods here:  
  👉 [Proxy Setups](https://wiki.bencodez.com/en/VotingPlugin/Proxy-Setups)

Make sure your chosen method (**PLUGINMESSAGING**, **SOCKET**, or **MYSQL**) is consistent across all connected servers.

---

## 3. Create and Configure VoteSites
You can add vote sites in several ways:

- **(Easiest)** Vote once on a site — VotingPlugin will automatically create a matching entry (auto-generation is enabled by default).  
  > ⚠️ Votifier must be set up correctly for this to work.
- **Using GUI:** `/av gui` → Middle-click **VoteSites**, then enter the site name and details.
- **Using the Desktop App:** [VotingPluginEditor](https://github.com/BenCodez/VotingPluginEditor)
- **Manually:** Edit `/plugins/VotingPlugin/VoteSites.yml` (see examples in the file).

> **Important:**  
> The `ServiceSite` name must be correct or rewards will not trigger.  
> You can check valid service sites:
> - In console (displayed whenever a vote is received)
> - Or with `/av servicesites` in-game.

More info: [Adding VoteSites](https://wiki.bencodez.com/en/VotingPlugin/adding-votesites)

---

## 4. Set Up Rewards
Define what players receive when they vote.

- You can use `/av gui` to create or test rewards directly in-game.
- Anything from the example reward files can be placed under `/plugins/VotingPlugin/Rewards/` or in other supported sections.
- Example reward templates:  
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

> Some commands have multiple permission nodes (listed here):  
> [Commands & Permissions](https://wiki.bencodez.com/en/VotingPlugin/Commands-&-Permissions)

---

## 6. Final Steps
You’re all set! Restart your server, vote once to test, and confirm rewards are given.

If anything doesn’t work:
- Check console for errors or missing service sites.
- Use `/adminvote` commands to test manually.
- Ensure the correct database or proxy settings are applied.

> 💬 Still stuck? Contact **BenCodez** via GitHub or Discord.

---

## Additional Setup Guides
External tutorials that may help with hosting panel setups:
- [ServerMiner – Setup Voting](https://serverminer.com/article/how-to-setup-voting-on-your-minecraft-server/)
- [WitherHosting – VotingPlugin Setup](https://support.witherhosting.com/en/article/how-to-install-and-use-votingplugin-java-6epg7/)
