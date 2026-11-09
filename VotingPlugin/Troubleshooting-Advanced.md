---
title: Advanced Troubleshooting
description: Diagnose failed, delayed, duplicate, or inconsistent VotingPlugin votes and rewards
published: true
date: 2026-11-09T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2026-11-09T00:00:00.000Z
---

# Advanced Troubleshooting — trace one vote from intake to reward

This is a second-level diagnostic guide for administrators who already followed [first-vote verification](/VotingPlugin/Getting-Started-Verification). It targets **VotingPlugin 7.1.1** unless a section explicitly says otherwise.

The most useful question is: **At what stage does one known test vote stop progressing?** Fix the earliest failed stage before changing unrelated settings.

## 1. Determine the exact failure stage

```text
A. Voting website sends vote
    |
B. VotifierPlus / NuVotifier receives record
    |
C. VotingPlugin receives and matches ServiceSite
    |
D. Player identity and vote data accepted/stored
    |
E. [Proxy only] vote forwarded or cached for eligible backend
    |
F. Reward rules evaluated and delivered (or deferred)
```

| Last confirmed stage | Look at | First place to investigate |
|---|---|---|
| A only | Website dashboard / external test | Listener TCP port, DNS, public IP, firewall, Votifier v1/v2 key or token |
| B | Listener console | Is VotingPlugin installed and loaded **on this process**? Duplicate listener forwarding? |
| C | VotingPlugin console | Enabled `VoteSites` entry, exact `ServiceSite` name, vote delay enforcement |
| D | Database/startup logs | UUID mode, SQL/SQLite errors, player-known/`AllowUnjoined` checks |
| E | Proxy + backend logs | `BungeeMethod`, shared SQL, backend `Server` names, `SendVotesToAllServers` |
| F | Reward logs/console | `Rewards` path, permissions, command syntax, online/offline context, overlapping rewards |

Start with **one** test vote and its timestamp; repeating votes can complicate cooldown and duplicate analysis.

## 2. Internal command tests are not end-to-end tests

A standalone/server admin can run:

```text
/av vote <player> <site>
```

On a proxy:

```text
/votingpluginproxy status
/votingpluginproxy vote <player> <site>
```

These are useful for isolating VotingPlugin and forwarding behavior, but do **not** verify inbound access to the Votifier port or the website's Votifier protocol and key/token.

Send a **real or listener-generated vote** after the internal test. On a healthy path, look for:

```text
[VotifierPlus] Debug: Received vote record -> Vote (from:SERVICESITEHERE username:ExamplePlayer ...)
[VotingPlugin] Received a vote from service site 'SERVICESITEHERE' by player 'ExamplePlayer'!
```

Exact listener logging varies by build and debug configuration.

## 3. No vote reaches VotifierPlus / NuVotifier

- Verify the listener is installed **on the process receiving website traffic**. In a standard proxy topology, it runs on the proxy.
- Read its generated config: `host: 0.0.0.0` means **bind on local interfaces**, not an address for voting sites. Set the site's public hostname/IP separately.
- Confirm the actual **TCP** listener port (e.g., VotifierPlus often defaults to `8192`) is allocated and reachable. This is normally **not** Minecraft's `25565` game port.
- Check firewall rules at the hosting provider, OS, container, router/NAT, and any tunnel. Verify the bind succeeded and no other process owns the port.
- Match the site's Votifier v1 **public key** or enabled v2 **token** protocol. **Never disclose `rsa/private.key`**; do not force v2-only mode while any site still uses v1.
- Restart after changing the listener's bind, port, or protocol settings.

If no listener packet arrives, editing `VoteSites.yml` cannot fix the problem.

## 4. Listener receives the vote, but VotingPlugin does not

- Confirm both plugins loaded without startup exceptions.
- Confirm VotingPlugin and the listener are on the **same proxy/backend process** where the Votifier event is emitted.
- Avoid simultaneously enabling listener-to-backend forwarding **and** VotingPlugin proxy forwarding; each vote should enter VotingPlugin **once**.
- Temporarily enable bounded debug around one vote if needed. Backend `Config.yml` supports `DebugLevel: EXTRA`; the proxy has its own debug options.
- Restore normal logging after gathering a small, redacted excerpt.

## 5. Unmatched service site or generated placeholder

The incoming vote's `ServiceSite` is set by the voting website. The matching `VoteSites.yml` entry might look like:

```yaml
VoteSites:
  MyListing:
    Enabled: true
    ServiceSite: 'SERVICESITEHERE'
    VoteURL: 'https://replace-with-real-vote-url.example'
```

Compare the **actual received value** in logs or `/av servicesites`. Matching is case-insensitive but otherwise requires the received service identifier, not an assumed domain. Review the generated site if `AutoCreateVoteSites: true` is enabled, and **replace its placeholder URL/rewards**.

Once intended sites work, set `AutoCreateVoteSites: false` and reload to avoid unknown service IDs automatically creating more entries. With 7.1.1, creating additional sites through `/av gui` after disabling auto-create may require temporarily re-enabling it; direct YAML edits do not.

## 6. Vote is accepted, but no reward arrives

Check in this order:

1. **Correct section:** A per-site reward belongs in `VoteSites.<site>.Rewards`; a milestone or vote party is configured in `SpecialRewards.yml`. See [Where to Set Rewards](/VotingPlugin/Where-to-set-rewards).
2. **Correct player:** Verify the identity delivered by Votifier and the target stored by VotingPlugin. Do not silently strip the Bedrock prefix.
3. **Command syntax:** For external crate or economy plugins, test the exact give command in the server console using a real username.
4. **Dependencies:** A `Money` reward needs an economy integration; plugin-specific commands need their respective plugin and correct permissions.
5. **Eligibility:** Check permission/world/time restrictions and any `AdvancedPriority` conditions. Only the first matching `AdvancedPriority` branch executes.
6. **Proxy routing:** On eligible backends, check `ProcessRewards`, `SendVotesToAllServers`, and the configured server role.
7. **Offline behavior:** Actions requiring an online player may be deferred or behave differently. Reconnect the player and inspect queued delivery.

A processed vote and successful player total do not prove every reward effect ran.

## 7. Duplicate votes, broadcasts, or rewards

Inspect **all paths** before disabling anything:

- Is VotifierPlus forwarding to backends while VotingPlugin forwards the same incoming vote?
- Are there multiple enabled listener instances seeing the same website notification?
- Is proxy `SendVotesToAllServers: true` intentionally letting multiple backends process a vote? For one-server rewards, review `false` and the targeted backend policy.
- Does `EverySiteReward` overlap with the per-site reward?
- Are both a legacy first-vote reward and its `VoteMilestones` replacement enabled?
- Are multiple enabled milestones or VoteParty reward sections matching the same vote?

Do not try to fix duplicate processing by arbitrarily deleting user totals; isolate and correct the duplicate route first.

## 8. Proxy receives a vote, backend does not

For the standard `PLUGINMESSAGING` topology:

- All involved instances must use the **same selected `BungeeMethod`** and compatible database settings.
- Proxy `bungeeconfig.yml` contains the main shared SQL config; backend `Config.yml` should use `DataStorage: MYSQL` and matching `Database` credentials.
- Backend `BungeeSettings.yml` must have `UseBungeecord: true` and a **unique `Server` name** matching the proxy's registered server.
- Plugin messaging needs an online-player connection to carry messages. Offline votes can be cached for later delivery, depending on settings.
- The proxy key `AllowUnJoined` and backend `AllowUnjoined` differ in capitalization; the standard layout uses **proxy false, backend true**.
- Check `BlockedServers`/`WhiteListedServers` and `SendVotesToAllServers` before blaming the transport.

For HTTP transport or dedicated voting proxies, do **not** follow 7.1.1 instructions: those features are documented as development-build-only in their respective reference pages.

See [Proxy Setups](/VotingPlugin/Proxy-Setups) and [PLUGINMESSAGING](/VotingPlugin/Proxy-method-PLUGINMESSAGING).

## 9. Storage errors or inconsistent totals

| Symptom | Investigation |
|---|---|
| Driver class missing / connection initialization fails | Check selected `DbType` and matching JDBC driver on **both proxy and backends**; Velocity may require MySQLDriver |
| SQL connection refused/authentication failed | Verify private hostname, port, credentials, grants, firewall, and database availability |
| Standalone SQLite data missing | Check whether `DataStorage` changed unexpectedly or the `Users.db` file/path was replaced |
| Different totals across a proxy network | Verify shared SQL, proxy `BungeeManageTotals: true`, server names, and forwarding; do not switch to unsupported per-backend total handling |
| Shared user data is temporarily loading | Inspect the exact API caller and storage/cache logs; don't interpret a transient unavailable value as proof of an actual balance or completed reward |

Before attempting any reset, SQL conversion, or rollback, back up storage and follow [Upgrade and Rollback](/VotingPlugin/Upgrade-and-Rollback) and [Data Storage Migration](/VotingPlugin/Transferring-data-storage-within-plugin).

## 10. Player identity, offline, and Bedrock mismatches

- `OnlineMode` needs to match the network's UUID identity policy on every instance sharing data.
- Floodgate/Geyser players may need the configured `BedrockPlayerPrefix` (often a period) in the vote-site player-name field.
- A prefixed Bedrock name and the matching unprefixed Java name can represent **different people**. Removing the prefix to make a vote site accept the name may credit another identity.
- Do not change identity mode or prefix on a live server without a planned data migration.
- `AllowUnjoined` / `AllowUnJoined` can prevent votes for never-joined identities. That is not the same as processing a valid offline vote for an existing player.

See [Bedrock Player Support](/VotingPlugin/Bedrock-Player-Support) and [Online / Offline Mode](/VotingPlugin/Online-Offline-Mode).

## 11. Time delays, streaks, and reset surprises

- `VoteDelay` influences when `/vote next` considers a site available; it does **not automatically reject** an early real vote.
- `WaitUntilVoteDelay: true` can **reject** early real votes; only use it when the website's actual cooldown matches your configuration.
- Daily/weekly/monthly vote logic, milestones and streaks depend on the configured vote rules and period boundaries; inspect the matching reward section before changing timestamps or user data.
- Shared reset coordination via `GlobalData` is **work in progress** in 7.1.1. Verify a consistent SQL backup and test on staging before enabling it.

See [Service Sites](/VotingPlugin/Service-sites), [Vote Streak System](/VotingPlugin/VoteStreak-System), and [Global Data Handling](/VotingPlugin/Global-Data-Handling).

## 12. What to include in a support report

Record:

- Plugin **exact version/build**, server type/version, Java version, and listener version.
- Standalone or proxy topology, `BungeeMethod`, database type, and backend names (use non-sensitive aliases where needed).
- One bounded **timestamped** test vote and the last stage it reached.
- Relevant redacted listener, proxy, and backend logs with warnings/exceptions.
- The `ServiceSite` value and only the relevant, **redacted** reward/config fragment.
- Whether the affected player was online and whether the issue reproduces after reconnect.

**Do not share** SQL passwords, Votifier private keys, Votifier v2 tokens, proxy/Redis/MQTT credentials, authentication cookies, or full unredacted logs. Disable extra debug after the test.

Back to [First Vote Verification](/VotingPlugin/Getting-Started-Verification) or the [FAQ](/VotingPlugin/faq).
