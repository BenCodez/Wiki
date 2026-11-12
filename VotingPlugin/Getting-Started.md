---
title: Getting Started with VotingPlugin
description: Choose a first-time server administrator setup path for VotingPlugin 7.1.1
published: true
date: 2026-11-09T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2026-11-09T00:00:00.000Z
---

# Getting Started — Server Administrators

New to VotingPlugin? Start here. These guides take you from a new installation to a **verified vote and reward**. They are for **server owners and administrators**, not a guide for players using `/vote`.

> **Release baseline:** These guides are checked against the latest published stable release, **VotingPlugin 7.1.1** (July 23, 2026). It requires **Java 21**. Some features in development builds are not available in 7.1.1.
{.is-info}

## Choose your setup

| Your server | Start here | What you will configure |
|---|---|---|
| One Paper or Spigot server, without BungeeCord or Velocity | **[Standalone Server Quick Start](/VotingPlugin/Getting-Started-Standalone)** | VotingPlugin, a Votifier listener, one voting website, and a simple reward |
| Velocity or BungeeCord network with one or more backend servers | **[Proxy Network Quick Start](/VotingPlugin/Getting-Started-Proxy)** | Vote listener on the proxy, VotingPlugin on proxy and backends, shared SQL storage, and vote routing |
| Already installed, but votes or rewards are not working | **[Verify Your First Vote](/VotingPlugin/Getting-Started-Verification)** | Separate internal command tests from real end-to-end vote delivery |

**Follow the standalone path unless you actually run a Velocity/BungeeCord network.** A single Paper server does not need MySQL or proxy settings to get started.

## How the pieces fit together

1. A player votes on a Minecraft server-list website.
2. The website sends a vote notification to a **Votifier-compatible listener** (for example, VotifierPlus). This is a separate plugin.
3. **VotingPlugin** processes the notification, tracks totals, and performs the configured rewards.
4. On a proxy network, VotingPlugin also forwards the vote to the appropriate backend(s).

**VotingPlugin is not the public Votifier listener.** Installing VotingPlugin alone does not open a Votifier port.

## Before you begin

- A supported Paper/Spigot server and **Java 21** for VotingPlugin 7.1.1.
- Access to server files, console logs, and full restarts.
- A public **TCP port separate from your Minecraft game port** that a voting website can reach. Your host may need to allocate an extra port.
- One Minecraft server-list website that lets you set a Votifier address, port, and public key or token.
- An operator/admin account and a test player name that has joined the server.

Download VotingPlugin from [SpigotMC](https://www.spigotmc.org/resources/votingplugin.15358/) or the [published release](https://github.com/BenCodez/VotingPlugin/releases/tag/7.1.1). Download VotifierPlus from its [project page](https://github.com/BenCodez/VotifierPlus); NuVotifier is another compatible listener. Use compatible server and proxy artifacts for your topology.

## A beginner-friendly setup order

1. **Install and start both plugins.** Check the console for startup errors.
2. **Expose the Votifier listener port.** Configure your listing website with the listener's public address, actual port, and correct key/token.
3. **Create or configure one voting site.** Use `/av VotePresets` (in-game), automatic site detection, or `VoteSites.yml`.
4. **Add one simple reward.** Use an inline `Rewards` block. Leave advanced features for later.
5. **Test twice.** First use the VotingPlugin admin command, then send a real or listener-generated vote through the public port. Both checks matter.
6. **Finish setup.** Check `/vote`, check logs, and disable `AutoCreateVoteSites` after all expected sites are configured.

For the exact steps and copyable examples, choose **[Standalone](/VotingPlugin/Getting-Started-Standalone)** or **[Proxy](/VotingPlugin/Getting-Started-Proxy)** above.

## Once the first vote works

Next, customize [Rewards](/VotingPlugin/Rewards), [VoteShop](/VotingPlugin/voteshop), [Vote Reminders](/VotingPlugin/VoteReminders), and [Vote Streaks](/VotingPlugin/VoteStreak-System). For the full option-by-option reference, use [Setup](/VotingPlugin/setup), [File Layout](/VotingPlugin/File-Layout), and [Commands & Permissions](/VotingPlugin/Commands-&-Permissions).

**Have a problem?** Start with the [first-vote troubleshooting table](/VotingPlugin/Getting-Started-Verification), then [Votifier Troubleshooting](/VotingPlugin/Votifier-Troubleshooting). Never post private keys, tokens, or database passwords.
