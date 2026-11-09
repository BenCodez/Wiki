---
title: Verify Your First Vote
description: Test VotingPlugin processing and the real Votifier-to-reward path
published: true
date: 2026-11-09T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2026-11-09T00:00:00.000Z
---

# Verify Your First Vote

Use this guide after the [Standalone](/VotingPlugin/Getting-Started-Standalone) or [Proxy](/VotingPlugin/Getting-Started-Proxy) quick start. **A successful admin test is not proof that your voting website can reach your server.**

## Test A — check VotingPlugin internally

On a standalone/backend server, run as an administrator:

```text
/av vote <player> <site>
```

Here, `<site>` is the configured VotingPlugin vote-site key (for example, `MyFirstSite`). Use a player account that has joined the server. Check that the expected test reward runs and the vote is recorded.

On a proxy setup, run **on the proxy**:

```text
/votingpluginproxy status
/votingpluginproxy vote <player> <site>
```

The proxy status check is most useful with an online player when using `PLUGINMESSAGING`.

**What this proves:** VotingPlugin can process the test; the proxy command also exercises its forwarding path. **What it does not prove:** the website's public connection, firewall, Votifier key/token, or website-supplied service name.

## Test B — send a real/listener-generated Votifier vote

1. Confirm the listener is running and its separate TCP port is publicly reachable.
2. In your Minecraft server-list dashboard, enter the public vote-listener address, real listener port, and matching **public key** (v1) or **token** (v2).
3. Use the website's official **test-vote** action if available, or cast a real vote. Use the exact player name expected by your server/network.
4. Watch the **listener and VotingPlugin logs**. On the standard setup you should see evidence that the listener received the vote and a VotingPlugin message similar to:

```text
[VotingPlugin] Received a vote from service site 'SERVICESITEHERE' by player 'ExamplePlayer'!
```

5. Run `/av servicesites` if you need to see received identifiers. Confirm that `VoteSites.yml` contains an **enabled** entry whose `ServiceSite` matches the received value (case-insensitive matching; do not guess other differences).
6. Confirm the expected **reward** arrives and the player's total updates. On a proxy network, inspect both proxy and backend logs.

Example text varies by listener build and debug settings. The important evidence is that the listener **received a record** and VotingPlugin **processed the same vote**.

## Troubleshooting: find the first failed stage

| What you see | Likely stage | What to check next |
|---|---|---|
| Can't connect to the listener / timeout / no Votifier message | **Network / listener** | Verify public hostname/IP, allocated **TCP** port, listener startup, OS/host firewall, router forwarding; do not put `0.0.0.0` in the website settings |
| Listener receives nothing or rejects the request | **Protocol / credentials** | Website protocol must match enabled v1 public-key or v2 token support; check key/token and restart after listener config changes |
| Listener reports a vote but VotingPlugin does not | **Plugin integration** | VotingPlugin must be installed and loaded **on the process receiving the vote**; inspect startup errors and enable bounded debug if needed |
| VotingPlugin receives vote but site is missing/wrong | **Site matching** | Compare incoming `ServiceSite` to `VoteSites.yml`; use `/av servicesites`; make sure `Enabled: true` and remove placeholder URLs |
| VotingPlugin records vote but no reward arrives | **Reward processing** | Check `Rewards` block, reward command syntax, player online/offline behavior, `ProcessRewards` on backends, and console errors |
| Vote reaches proxy but not backend | **Proxy routing** | Confirm shared SQL, `BungeeMethod`, backend `Server` name, `UseBungeecord`, plugin-message online-player requirement, and allowed target servers |
| Reward happens more than once | **Duplicate forwarding** | Use a single Votifier intake; disable VotifierPlus backend forwarding when VotingPlugin does it; review `SendVotesToAllServers` |
| Bedrock player is missing rewards | **Player identity** | Follow [Bedrock Player Support](/VotingPlugin/Bedrock-Player-Support); ensure the complete configured player prefix reaches the voting service |

## Important settings to revisit after success

- **`AutoCreateVoteSites: true`** is helpful during discovery. After every intended site is set up, switch it to `false` and reload so unknown services cannot create more entries.
- **`VoteDelay` is not inherently vote rejection.** Only enable `WaitUntilVoteDelay` if the website's interval actually matches the configured delay.
- Keep listener keys/tokens, SQL passwords, and private network addresses out of public issues. **Never publish the RSA private key.**
- For offline rewards, test a separate vote while the player is offline and confirm delivery after joining, especially with rewards requiring an online player.

## More detailed help

- [Votifier Troubleshooting](/VotingPlugin/Votifier-Troubleshooting)
- [Service Sites](/VotingPlugin/Service-sites)
- [Rewards](/VotingPlugin/Rewards)
- [Proxy Setups](/VotingPlugin/Proxy-Setups)
- [FAQ](/VotingPlugin/faq)

If you open a support ticket, include your VotingPlugin version, server/proxy type, redacted listener and VotingPlugin log excerpts around a **single test vote**, and the relevant non-secret `ServiceSite` and reward configuration.
