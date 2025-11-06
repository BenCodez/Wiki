---
title: Where to set rewards
description: 
published: true
date: 2025-11-06T02:44:14.351Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:32.400Z
---

# Rewards Overview

> 🧭 **Quick reference guide** to where rewards are defined throughout VotingPlugin.
{.is-info}

---

## 🗳️ VoteSites.yml

| Reward Type | Location / Section | Description |
|--------------|-------------------|--------------|
| **Per-Site Reward** | `Rewards:` | Main reward for voting on a specific site. |
| **Cooldown End Reward** | `CoolDownEndRewards:` | Triggered when a player’s vote cooldown ends for that site. |
| **Global “Every Site” Reward** | `EverySiteReward:` | Given for voting on *any* site (applies to all VoteSites). |

> 💡 Tip: You can use reward files or define rewards inline in the YAML.
{.is-info}

---

## 🎁 SpecialRewards.yml

| Reward Type | Path | Description |
|--------------|------|--------------|
| **All Sites Reward** | `AllSites:` | Given when the player votes on *all* configured sites. |
| **Almost All Sites Reward** | `AlmostAllSites:` | Given when the player votes on all but one site. |
| **First Vote Reward** | `FirstVote:` | Reward for the player’s *first ever* vote. |
| **First Vote of the Day** | `FirstVoteToday:` | Daily first-vote reward. |
| **Cumulative Rewards** | `Cumulative:` | Rewards for reaching specific total vote counts (supports daily/weekly). |
| **Milestones** | `Milestones:` | One-time rewards for specific milestones (e.g., 10th, 25th vote). |
| **Vote Streak Rewards** | `VoteStreak:` | Rewards for maintaining consecutive voting streaks. |
| **Vote Party Rewards** | `VoteParty.Rewards:` | Player-specific rewards when a vote party triggers. |
| **Top Voter Rewards** | `(TOPVOTER)Awards:` | Rewards for top voters (e.g., Monthly, Weekly, Daily). |

> 🧩 Use placeholders and reward files here just like in VoteSites.yml — everything shares the same reward syntax.
{.is-info}

---

## ⚙️ Config.yml

| Reward Type | Path | Description |
|--------------|------|--------------|
| **Vote Reminding** | `VoteReminding:` | Message or reminder system — not an actual reward trigger. |

---

> ✅ **Summary:**  
> All rewards, regardless of where they are defined, share the same reward structure.  
> You can reference [ExampleBasic.yml](https://github.com/BenCodez/AdvancedCore/blob/master/AdvancedCore/src/main/resources/Rewards/ExampleBasic.yml) or [ExampleAdvanced.yml](https://github.com/BenCodez/AdvancedCore/blob/master/AdvancedCore/src/main/resources/Rewards/ExampleAdvanced.yml) for examples.
{.is-success}
