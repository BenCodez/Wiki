---
title: Reward System
description: 
published: true
date: 2025-11-07T01:57:39.522Z
tags: 
editor: markdown
dateCreated: 2025-09-02T01:43:37.375Z
---

# VotingPlugin Reward System

**VotingPlugin** includes a powerful and flexible reward system for Minecraft servers.  
Rewards can be **defined directly inside configuration files** or **referenced from standalone YAML reward files** for reuse and better organization.

---

## 🧩 1. Directly Defined Rewards (Inline)

Inline rewards are written **directly in your configuration files** — such as `VoteSites.yml` or `SpecialRewards.yml`.  
This is ideal for **quick setups** or **single-use rewards**.

### Example: Inline Vote Reward

```yaml
    VoteSites:
      ExampleSite:
        Enabled: true
        Name: 'Example Voting Site'
        ServiceSite: 'example.com'
        VoteURL: 'https://example.com/vote'
        VoteDelay: 24
        Rewards:
          Items:
            Diamond:
              Material: 'DIAMOND'
              Amount: 1
          Money: 5
          EXP: 100
          Commands:
            - 'say %player% was lucky'
```

💎 This configuration gives:
- 1 **Diamond**
- 5 **currency**
- 100 **experience**
- Executes `/say %player% was lucky`

> ⚠️ **Do not mix** inline reward definitions with reward file references under the same `Rewards:` block.
{.is-warning}

---

## 📁 2. Reward File System

Reward files allow you to organize rewards in separate, reusable `.yml` files.  
Each reward file is stored in:

**`/plugins/VotingPlugin/Rewards/`**

### How It Works
- Each reward file represents one reward set.  
- File names become the **reward name** (no `.yml` extension needed when referenced).  
- Files can define any supported reward types: items, money, EXP, commands, messages, etc.

---

### Referencing Reward Files

```yaml
    VoteSites:
      ExampleSite:
        Rewards: 'MyCustomReward'
```

You can also combine multiple reward files:

```yaml
    Rewards:
    - 'FirstVote'
    - 'VotePartyBonus'
```

> ⚠️ **Important:** Example reward files provided by the plugin are for reference only.  
> Always create your own `.yml` reward files tailored to your setup.
{.is-warning}

---

### Creating a Custom Reward File

1. Navigate to:  
   `/plugins/VotingPlugin/Rewards/`
2. Create a new file — for example:  
   `MyCustomReward.yml`
3. Define your rewards inside it:

```yaml
    Items:
      Diamond:
        Material: 'DIAMOND'
        Amount: 1
    Money: 5
    EXP: 100
    Commands:
      - 'say %player% was lucky'
```

Then reference it in your `VoteSites.yml`:

```yaml
    VoteSites:
      ExampleSite:
        Rewards: 
        - 'MyCustomReward'
```

> ✅ Using reward files keeps your configurations modular and reusable.
{.is-success}

---

### Example Reward File

```yaml
    # plugins/VotingPlugin/Rewards/MyCustomReward.yml
    Items:
      Diamond:
        Material: 'DIAMOND'
        Amount: 1
    Money: 5
    EXP: 100
    Commands:
      - 'say %player% was lucky'
```
---

## ⚙️ 3. When Rewards Are Triggered

Rewards can be executed by a variety of events.  
All reward definitions (inline or file-based) use the **same syntax**.

### Examples

**Using a reward file:**

```yaml
    FirstVote:
      Rewards: 'FirstVoteRewardFile'
```

**Using inline rewards:**

```yaml
    FirstVote:
      Rewards:
        Items:
          Diamond:
            Material: 'DIAMOND'
            Amount: 1
```

### Reward Triggers Include:
- Per-site votes (`VoteSites.yml`)
- Vote parties
- Milestones and cumulative votes
- Vote streaks
- Top voter rewards
- Cooldown end rewards
- Every-site rewards

---

## 💡 4. Best Practices

| Situation | Recommended Approach |
|------------|----------------------|
| Simple one-time reward | Inline definition |
| Reused across multiple events | Separate reward file |
| Large or complex reward logic | Reward file with Priority or SpecialChance |
| Testing or temporary reward | Inline |
| Production setup | Dedicated reward files in `/Rewards/` |

> 🧠 Keep reward file names descriptive (e.g., `DailyVote.yml`, `VotePartyBonus.yml`).
{.is-info}

---

## 🧾 5. Summary

- **Inline Rewards:**  
  - Defined directly in config.  
  - Best for quick setups.  

- **Reward Files:**  
  - Defined in `/Rewards/`.  
  - Reusable, modular, and cleaner for large setups.  

- **Triggers:**  
  - Votes, milestones, streaks, top voter, vote party, cooldowns, and more.  

> 🏁 Always create your own `.yml` files — example files are templates only.
{.is-success}
