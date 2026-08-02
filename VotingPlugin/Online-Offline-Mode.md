---
title: Online/Offline Mode
description: Configure UUID handling for premium, cracked, and mixed networks
published: true
date: 2025-11-06T02:42:46.316Z
tags:
editor: markdown
dateCreated: 2025-08-30T22:18:18.207Z
---

# Online Mode Handling

`OnlineMode` controls how VotingPlugin resolves player UUIDs.

```yaml
OnlineMode: true
```

## Which value should I use?

| Server or network type | Setting | UUID behavior |
|---|---:|---|
| Premium players only | `OnlineMode: true` | Uses Mojang-authenticated online UUIDs |
| Cracked/offline-mode players | `OnlineMode: false` | Uses offline UUIDs generated from player names |
| Mixed premium and cracked players | `OnlineMode: false` | Keeps VotingPlugin on name-based offline UUIDs for the mixed network |

Use the same value on every VotingPlugin instance that shares player data. On a
proxy network, configure the proxy and backend servers consistently.

## Changing an existing server

Changing `OnlineMode` changes the UUID VotingPlugin expects for a player. If a
server already has vote data, changing this setting without migrating the data
can make existing totals appear under a different UUID.

Before changing it:

1. Back up the VotingPlugin data and database.
2. Stop voting activity while the change and migration are in progress.
3. Change the setting consistently across the network.
4. Migrate or merge the existing UUID data as needed.
5. Test with both a premium and cracked player before reopening voting.

If you are unsure which UUID type your authentication/proxy setup provides,
check a known player's UUID at the proxy and backend before changing this
setting.
