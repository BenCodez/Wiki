---
title: Setup
description: Install VotingPlugin on standalone and proxy networks
published: true
date: 2026-08-14T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2025-08-30T22:18:27.000Z
---

# Setup

> **Release baseline:** This guide targets VotingPlugin **7.1.1**, released July 23, 2026. VotingPlugin 7.1.1 is compiled for **Java 21**, so the server or proxy runtime that loads it must use Java 21 or newer.
{.is-info}

## Requirements

- A supported Bukkit-family backend such as Spigot or Paper.
- A vote listener such as [VotifierPlus](https://github.com/BenCodez/VotifierPlus) or NuVotifier.
- Java 21 or newer for VotingPlugin 7.1.1.
- On a proxy network, a shared SQL database and a matching JDBC driver on every process that connects to it.

Do not place private database, Redis, MQTT, or socket credentials in screenshots, public repositories, or support logs.

## Standalone server

1. Install VotingPlugin in the backend server's `plugins` directory.
2. Install and configure VotifierPlus or NuVotifier on the same server.
3. Start the server once so VotingPlugin generates its files.
4. Configure each entry in `VoteSites.yml`, especially `ServiceSite`, `VoteURL`, vote delays, and rewards.
5. Restart after changing settings that are documented as restart-only.

The bundled 7.1.1 defaults are available in the [7.1.1 resource directory](https://github.com/BenCodez/VotingPlugin/tree/7.1.1/VotingPlugin/src/main/resources).

## Proxy network

The standard VotingPlugin layout is:

- VotifierPlus or NuVotifier on the BungeeCord/Velocity proxy.
- VotingPlugin on the proxy and every participating backend.
- One selected `BungeeMethod` configured consistently on the proxy and backends.
- One shared SQL database with compatible settings and drivers.
- A unique `Server` value in each backend's `BungeeSettings.yml`.

Start with [Proxy Setups](/VotingPlugin/Proxy-Setups), then follow the page for the selected communication method. Disable VotifierPlus/NuVotifier forwarding targets unless a custom topology deliberately requires them; VotingPlugin normally performs the backend forwarding.

## Configure vote sites

The incoming service name must exactly match `VoteSites.yml -> VoteSites.<site>.ServiceSite`. After sending a real or listener-generated test vote, use `/av servicesites` to see the value VotingPlugin received.

For current vote-site fields and examples, use the release-bundled [VoteSites.yml](https://github.com/BenCodez/VotingPlugin/blob/7.1.1/VotingPlugin/src/main/resources/VoteSites.yml) and [Service Sites](/VotingPlugin/Service-sites).

## Test the complete path

There are two different tests:

1. **Listener/network test:** Send a vote from a real listing or a Votifier tester. This verifies the public listener port, token/key, proxy routing, and the exact `ServiceSite` value.
2. **VotingPlugin processing test:** Run `/av vote <player> <site>` on a backend, or `/votingpluginproxy vote <player> <site>` on the proxy. This verifies VotingPlugin processing but does **not** prove that the public Votifier listener is reachable.

A healthy listener test normally produces a Votifier receipt followed by VotingPlugin's `Received a vote from service site ...` message. Follow [Votifier Troubleshooting](/VotingPlugin/Votifier-Troubleshooting) when either line is missing.

## Updating

Back up the entire `plugins/VotingPlugin` directory and database before changing versions. Compare generated/default configuration for the version being installed instead of copying unreleased `master` defaults into a 7.1.1 installation.
