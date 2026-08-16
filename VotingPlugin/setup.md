---
title: Setup
description: VotingPlugin installation and initial configuration
published: true
date: 2026-08-14T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2025-08-31T03:20:39.536Z
---

# Setup VotingPlugin

> **Release baseline:** This guide targets VotingPlugin **7.1.1**, released July 23, 2026. The 7.1.1 plugin and proxy artifacts are compiled for **Java 21**.
{.is-info}

## 1. Install a vote listener

Use a compatible listener such as:

- [VotifierPlus](https://github.com/BenCodez/VotifierPlus)
- [NuVotifier](https://github.com/NuVotifier/NuVotifier)

See [Votifier Troubleshooting](Votifier-Troubleshooting) when votes are not reaching the server.

## 2. Configure a proxy network when applicable

VotingPlugin must be installed on the proxy and each backend server when using VotingPlugin's proxy integration. The normal layout places VotifierPlus on the proxy, though custom routing layouts may differ.

Choose one `BungeeMethod` value and use it consistently across the connected servers:

- `PLUGINMESSAGING`
- `REDIS`
- `MQTT`
- `MYSQL`
- `SOCKETS`

These names match the 7.1.1 `BungeeSettings.yml` defaults.

See [Proxy Setups](Proxy-Setups).

## 3. Configure vote sites

VotingPlugin can create vote sites automatically from received votes when `AutoCreateVoteSites: true`, or they can be added through `/av gui`, VotingPluginEditor, or `VoteSites.yml`.

```yaml
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
      - 'give %player% diamond 1'
```

| Field | Description |
|---|---|
| `ServiceSite` | Must exactly match the service name sent by the vote listener |
| `VoteDelay` | Voting interval in hours; use `VoteDelayMin` for minute offsets |
| `VoteURL` | URL shown to players |
| `Rewards` | Reward section processed for the vote |

Use `/av servicesites` or the console output from a received vote to confirm the service name.

## 4. Configure rewards

Rewards can be created with `/av gui`, directly in a vote-site or special-reward section, or in files under `/plugins/VotingPlugin/Rewards/`.

See [Rewards](Rewards) and [Reward Examples](Reward-Examples).

## 5. Permissions

`VotingPlugin.Player` grants the main player commands by default. See [Commands and Permissions](Commands-&-Permissions) for all nodes.

## 6. Restart and test

Restart the server and proxy after changing network settings.

- `/av vote <player> <site>` or `/votingpluginproxy vote <player> <site>` tests VotingPlugin processing and proxy communication.
- A real or listener-generated vote tests the public Votifier port, token/key, service-site value, and complete delivery path.

Run both tests and verify service-site matching, storage, forwarding, and rewards in the logs. An administrative test alone does not prove the public vote listener is reachable.

> **AI disclosure:** This documentation update was written with assistance from ChatGPT.
