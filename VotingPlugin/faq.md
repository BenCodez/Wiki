---
title: FAQ
description: Quick answers to common VotingPlugin questions
published: true
date: 2026-07-26T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2025-08-30T22:18:10.405Z
---

# ❓ VotingPlugin — Quick FAQ

## 1) `/vote` says “vote here: www.votelinkhere.com”

This is usually **VentureChat** intercepting `/vote`. Remove or change VentureChat's `/vote` alias, restart or reload VentureChat, and test again.

---

## 2) How do I add rewards for crate keys?

Put the crate plugin's give-key command in the reward's `Commands` list:

```yaml
Rewards:
  Commands:
    - "command here %player%"
```

Examples, which must be adjusted to match the crate plugin's current command syntax:

```yaml
Rewards:
  Commands:
    - "cc give physical <CrateName> 1 %player%"
    - "cmi give %player% key:<KeyName> 1"
    - "crate givekey %player% <CrateName> 1"
```

`%player%` is replaced with the voter's name.

---

## 3) How do I test a vote?

```text
/av vote <player> <site>
```

---

## 4) YAML error

Validate the file with a YAML parser and check that:

- spaces are used instead of tabs;
- indentation is consistent;
- strings containing special characters are quoted;
- lists use the correct indentation.

Example:

```yaml
Messages:
  Player: '&aThanks for voting!'
```

---

## 5) “No voting site with the service site: ‘SERVICE SITE HERE’”

Either the vote listener is not receiving the vote or `ServiceSite` does not exactly match the value sent by the vote service.

Run a test vote, check the console, and follow [Votifier Troubleshooting](Votifier-Troubleshooting).

---

## 6) “No plugin.yml” or “failed to load”

Redownload the jar. It is probably corrupted or is not the correct server plugin artifact.

---

## 7) Extreme troubleshooting and debugging

```yaml
DebugLevel: EXTRA
```

For proxy issues, also enable `BungeeDebug` in `BungeeSettings.yml` and debug output on the proxy.

---

## 8) Hex color support

Use:

```text
&#FF0000#
```

The hexadecimal color is surrounded by `&#` and `#`.

---

## 9) Reload commands

```text
/av reload
/av reloadall
```

`/av reloadall` also reloads user storage.

---

## 10) Out of memory or resource limit reached in Pterodactyl

First determine whether the failure is Java heap exhaustion or a container PID limit. A PID-limit problem is normally visible in Wings, Docker, or host logs and is different from insufficient Java memory.

Only a Pterodactyl node administrator should change the host-wide setting. When logs confirm PID exhaustion, the node administrator can review `container_pid_limit` in `/etc/pterodactyl/config.yml` and restart the required node services after making an appropriate change.

> Do not increase a node-wide process limit as a substitute for diagnosing Java heap usage, runaway processes, or plugin errors.
{.is-warning}
