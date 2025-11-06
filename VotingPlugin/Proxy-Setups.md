---
title: Proxy-Setups
description: Details of proxy setups
published: true
date: 2025-11-06T02:14:45.547Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:02.764Z
---

> ⚙️ **Running on Velocity**
>
> Velocity requires a MySQL driver to be installed.  
> You can download a prebuilt plugin here if needed:  
> 🔗 [MySQLDriver (Jenkins)](http://bencodez.com/job/MySQLDriver/)
{.is-info}

> 💾 **Database Requirement**
>
> All proxy methods require **MySQL**, with every server (including the proxy) pointing to the **same database**.
{.is-info}

> 📨 **Votifier Configuration**
>
> **Votifier** (or **VotifierPlus/NuVotifier**) only needs to run on the **proxy**.  
> VotingPlugin automatically handles forwarding votes to backend servers.
{.is-info}

---

# Proxy Methods

VotingPlugin supports several communication methods between your **proxy (BungeeCord/Velocity)** and backend servers.  
All methods achieve the same goal — sharing vote data — but differ in setup complexity and infrastructure requirements.

| Method | Description |
|--------|-------------|
| [PLUGINMESSAGING](/VotingPlugin/Proxy-method-PLUGINMESSAGING) | **Easiest option** — works out of the box. Drop the plugin on proxy and backend servers. |
| [REDIS](/VotingPlugin/proxy-method-REDIS) | Uses a **Redis** server for fast, reliable messaging between servers. |
| [MQTT](/VotingPlugin/proxy-method-MQTT) | Uses an **MQTT broker** to broadcast votes (useful for distributed networks). |
| [SOCKETS](/VotingPlugin/proxy-method-SOCKETS) | Sends votes directly via TCP sockets (requires open ports between servers). |
| [MYSQL](/VotingPlugin/proxy-method-MYSQL) | Stores and synchronizes votes through the **shared MySQL database**. |

---

## How It Works

![Proxy Flow Diagram](/untitled_diagram___mermaid_chart-2025-08-30-234204.png)

When a player votes:

1. The **vote** is received by **Votifier** on the **proxy**.  
2. **VotingPlugin** (running on the proxy) processes the vote.  
3. The vote is then **forwarded** to backend servers using the configured method.  
4. Each backend server’s **VotingPlugin** instance delivers rewards, updates totals, and triggers vote parties.

---

## Abilities

VotingPlugin’s proxy support includes:

- 🌍 **Global or per-server rewards**
- 🎉 **Network-wide vote parties** or individual **server vote parties**
- ⏰ **Global time synchronization** using the `GlobalData` setting
- 🧱 **Blocklist/whitelist** to include or exclude specific servers
- 🔁 **Multi-proxy synchronization** for large networks
- ⚙️ And much more — all configurable in `bungeeconfig.yml`

---

## Multi-Proxy Support

For networks with multiple proxies, VotingPlugin supports **PLUGINMESSAGING** or **REDIS** synchronization across all proxies.

> ⚠️ **Note:** Multi-proxy setups are considered *experimental but functional* in current releases.  
> Follow the guide here:  
> 🔗 [Multi-Proxy Setup](/en/VotingPlugin/Multi-Proxy-Setup)
