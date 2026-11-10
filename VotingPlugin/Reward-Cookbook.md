---
title: Rewards Cookbook
description: Tested-style, copyable VotingPlugin reward recipes for server administrators
published: true
date: 2026-11-09T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2026-11-09T00:00:00.000Z
---

# Rewards Cookbook — copyable recipes for server administrators

These examples target **stable VotingPlugin 7.1.1** and its bundled AdvancedCore reward system. Pick the correct file and merge the example into the existing section; do not paste duplicate top-level YAML keys.

> **Before editing:** Back up your files, use spaces instead of tabs, reload only when the relevant setting supports it, and test with a known player. A successful `/av vote <player> <site>` checks internal reward handling, **not** the public Votifier port. Follow [first-vote verification](/VotingPlugin/Getting-Started-Verification) for an end-to-end test.
{.is-info}

## Choose where a reward belongs

| Goal | File and section |
|---|---|
| Reward a vote from one configured website | `VoteSites.yml` → `VoteSites.<site>.Rewards` |
| Reward every site vote | `VoteSites.yml` → `EverySiteReward` |
| First vote / every 25 votes / daily targets | `SpecialRewards.yml` → `VoteMilestones` |
| Group reward after the VoteParty threshold | `SpecialRewards.yml` → `VoteParty.Rewards` |
| Daily/weekly/monthly streak | `SpecialRewards.yml` → `VoteStreaks` |
| Purchase an item with vote points | `Shop.yml` → `Shop` or `Categories` |
| Share a common reward definition | `Rewards/MyReward.yml`, referenced by name |

See [Where to Set Rewards](/VotingPlugin/Where-to-set-rewards) for all reward locations.

## 1. Give a diamond and a thank-you message for a site vote

**File:** `plugins/VotingPlugin/VoteSites.yml`

```yaml
VoteSites:
  MyFirstSite:
    Enabled: true
    Name: 'My First Site'
    ServiceSite: 'REPLACE_WITH_RECEIVED_SERVICE'
    VoteURL: 'https://example.invalid/replace-with-real-vote-url'
    VoteDelay: 24h
    DisplayItem:
      Material: DIAMOND
      Amount: 1
    Rewards:
      Messages:
        Player: '&aThank you for voting!'
      Items:
        Diamond:
          Material: DIAMOND
          Amount: 1
```

Use this as **one entry beneath your existing `VoteSites:`**. Replace the `ServiceSite` with the actual identifier sent by the vote listener; it is not necessarily the domain or display name. The example URL must also be replaced before use. The bundled `ExampleVoteSite` starts disabled: edit it or leave it disabled.

## 2. Give money for each configured website vote

**File:** `VoteSites.yml`, at the file's top-level `EverySiteReward` section.

```yaml
EverySiteReward:
  Money: 100
  Messages:
    Player: '&aYou earned 100 for voting!'
```

This requires a working economy integration. An `EverySiteReward` is shared across sites, so avoid duplicating the same reward under every site's `Rewards` unless you intentionally want to pay twice.

## 3. Give a crate key using another plugin's command

**Location:** An individual `Rewards` block in `VoteSites.yml` or a reusable reward file.

```yaml
Rewards:
  Commands:
    - 'REPLACE_WITH_CRATE_PLUGIN_CONSOLE_COMMAND %player%'
```

**This is a placeholder, not an executable key-give command.** Check the installed crate plugin's actual give-key command and permissions, test it manually from the **server console**, and then copy that command here. `%player%` is substituted with the voting player's name where supported. Do not assume different crate plugins use compatible syntax.

## 4. Reuse the same reward across several sites

**New file:** `plugins/VotingPlugin/Rewards/VoteThanks.yml`

```yaml
Money: 50
Messages:
  Player: '&aThanks for voting!'
```

**Under an existing site in `VoteSites.yml`:**

```yaml
Rewards:
  - VoteThanks
```

A **standalone reward file does not have a top-level `Rewards:` wrapper**. Reference by filename without `.yml`. Do not edit the generated `Rewards/DirectlyDefined` folder; edit the original inline configuration or your own reward file.

## 5. Reward the first lifetime vote only

**File:** `SpecialRewards.yml`, **inside the existing `VoteMilestones` section**.

```yaml
VoteMilestones:
  FirstVoteAllTime:
    Enabled: true
    Total: ALLTIME_VOTES
    At: 1
    Rewards:
      Messages:
        Player: '&aThanks for your very first vote!'
```

The 7.1.1 defaults already contain a first-vote milestone. **Edit the existing entry** rather than adding another enabled first-vote milestone. The first vote brings the lifetime total to 1.

## 6. Reward every 25 lifetime votes

**File:** `SpecialRewards.yml`, under `VoteMilestones`.

```yaml
VoteMilestones:
  Every25Votes:
    Enabled: true
    Total: ALLTIME_VOTES
    Every: 25
    Rewards:
      Commands:
        - 'give %player% diamond 2'
      Messages:
        Player: '&6You reached another 25 lifetime votes!'
```

Matches at 25, 50, 75, and later multiples. Use `At` for specific totals instead. The release sample contains a disabled `Every25Votes`: edit that existing entry if present. See [Vote Milestones](/VotingPlugin/VoteMilestones).

## 7. Set up a simple VoteParty

**File:** `SpecialRewards.yml`. Edit the **existing** `VoteParty` section, keeping unrelated per-server/proxy settings.

```yaml
VoteParty:
  Enabled: true
  VotesRequired: 20
  GiveAllPlayers: false
  GiveOnlinePlayersOnly: true
  Broadcast: '&6VoteParty reached!'
  GlobalCommands: []
  Rewards:
    Messages:
      Player: '&aThe server reached a VoteParty!'
    Items:
      Diamond:
        Material: DIAMOND
        Amount: 1
```

This is a **partial configuration example**, not a replacement for the entire original section. Review `GiveAllPlayers` (eligibility) and `GiveOnlinePlayersOnly` (who can receive rewards) for your server. `GlobalCommands` runs once for the party, not once per voter, so **do not use `%player%` there**. See [Special Rewards](/VotingPlugin/Special-Rewards).

## 8. Create a seven-day voting streak

**File:** `SpecialRewards.yml` under the existing `VoteStreaks` section:

```yaml
VoteStreaks:
  SevenDays:
    Type: DAILY
    Enabled: true
    Recurring: false
    Requirements:
      Amount: 7
      VotesRequired: 1
    AllowMissedAmount: 0
    AllowMissedPeriod: 7
    Rewards:
      Messages:
        Player: '&bSeven-day voting streak complete!'
```

This requires at least one qualifying vote in each successful daily period for seven periods, with no missed-period forgiveness in this example. Check calendar reset/time-zone behavior on your server. See [Vote Streak System](/VotingPlugin/VoteStreak-System).

## 9. Sell a diamond for vote points

**File:** `Shop.yml`. Ensure the existing `VoteShop.Enabled` setting is true and add/edit an item under its existing `Shop:` section:

```yaml
Shop:
  Diamond:
    Identifier_Name: Diamond
    DisplayItem:
      Material: DIAMOND
      Amount: 1
      Name: '&bBuy a diamond'
      Lore:
        - '&7Cost: &a3 vote points'
    Cost: 3
    CloseGUI: true
    Rewards:
      Items:
        Diamond:
          Material: DIAMOND
          Amount: 1
```

This is the ordinary `Shop:` item structure in 7.1.1. Only merge one item, not a duplicate `Shop:` root. Players can use `/vote shop` to open the shop. Vote points are configured separately in `Config.yml`. See [VoteShop](/VotingPlugin/voteshop).

## 10. Give a better reward to VIPs

**Within a reward section** (or at the root of a reusable reward file):

```yaml
AdvancedPriority:
  VIP:
    RequirePermission: true
    Permission: 'yourserver.vip'
    Money: 200
  Default:
    Money: 50
```

`AdvancedPriority` selects the **first matching** child. The `Default` entry acts as the fallback. Replace the sample permission and confirm your permission plugin grants it. See [AdvancedPriority Rewards](/VotingPlugin/AdvancedPriority-Rewards).

## Troubleshooting rewards

- **No reward:** Confirm that VotingPlugin received a vote, the matching site is enabled, the reward is placed under the correct key, and an admin test runs the desired effect.
- **Money is missing:** Confirm a compatible economy plugin and integration are available.
- **Command fails:** Try the exact command from console with a real player name. Check which plugin owns the command.
- **Duplicate rewards:** Check per-site reward plus `EverySiteReward`, overlapping milestones, and proxy forwarding/`SendVotesToAllServers`.
- **Offline rewards differ:** Online-player actions (GUIs, player-context commands, titles, permissions, world checks) may be queued or have different behavior. Test while offline and after rejoining; do not assume every effect works offline.

More: [Rewards Overview](/VotingPlugin/Rewards) · [Reward File](/VotingPlugin/Reward-File) · [All Reward Possibilities](/VotingPlugin/All-Reward-Possibilities) · [First Vote Verification](/VotingPlugin/Getting-Started-Verification)
