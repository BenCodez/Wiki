---
title: Reward System
description: 
published: true
date: 2025-09-02T01:43:37.375Z
tags: 
editor: markdown
dateCreated: 2025-09-02T01:43:37.375Z
---

# VotingPlugin Reward System

**VotingPlugin** uses a flexible reward system for Minecraft servers. Rewards can be **defined directly in the config** (called inline or directly defined) or **referenced from separate YAML reward files**. This page explains how to configure both methods for server administrators.

---

## 1. Directly Defined Rewards (Inline)

Inline rewards are defined **directly in the main config** (e.g., `VoteSites.yml` or `Config.yml`).  
This method is best for quick setups or one-off rewards.

**Example: Inline Vote Reward**

```yaml
VoteSites:
  ExampleSite:
    Enabled: true
    Name: 'Example Voting Site'
    ServiceSite: 'example.com'
    VoteURL: 'http://example.com/vote'
    VoteDelay: 24
    Rewards:
      Items:
        Diamond:
          Material: 'DIAMOND'
          Amount: 1
      Money: 5
      EXP: 100
      Commands:
        Console:
          - 'say %player% was lucky'
          
```
          
- Gives: 1 Diamond, 5 currency, 100 EXP, and executes a console command.
- Syntax: Same as reward files.
- No .yml file required.

⚠️ You cannot mix example reward files with inline definitions in the same Rewards: block.


## 2. Reward File System

Reward files allow you to organize reusable rewards in separate .yml files.

How It Works

Each reward file lives in plugins/VotingPlugin/Rewards/.

Named <RewardName>.yml.

Contains items, commands, money, messages, or other supported rewards.

Referencing Reward Files

In the main config, reference the reward file by its base name (without .yml):

```yaml
VoteSites:
  ExampleSite:
    Rewards: 'MyCustomReward'
  ```


Multiple reward files can be used together:

```yaml
Rewards:
  - 'FirstVote'
  - 'VotePartyBonus'
```

⚠️ Important: Example reward files provided by the plugin or wiki cannot be used directly. You must create your own .yml files.

  
Example Reward File
  
```yaml
# plugins/VotingPlugin/Rewards/MyCustomReward.yml
Items:
  Diamond:
    Material: 'DIAMOND'
    Amount: 1
Money: 5
EXP: 100
Commands:
  Console:
    - 'say %player% was lucky'
```

## 3. When Rewards Are Triggered

Rewards can be triggered by several events, but use the same internal reward handling


Reference reward files or inline definitions depending on the event:

```yaml
FirstVote:
  Rewards: 'FirstVoteRewardFile'  # Using a reward file
```
  
```yaml
FirstVote:
  Rewards:                        # Inline rewards
    Items:
      Diamond:
        Material: 'DIAMOND'
        Amount: 1
```

## 4. Best Practices

Use inline rewards for simple, one-time setups.

Use reward files for complex or reusable reward sets.

Never use example reward files directly; always create your own .yml files.

Keep reward file names unique and descriptive.

Organize your rewards consistently to simplify maintenance.

## 5. Summary

Inline rewards are quick and embedded directly in the main config.

Reward files are reusable, separate .yml files that can be referenced by name.

Rewards are triggered by votes, vote parties, milestones, streaks, cooldowns, and top-voter events.

Always create your own reward files; example files are for reference only.

Use consistent naming and organization for clarity and maintainability.