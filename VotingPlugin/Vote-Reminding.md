---
title: Vote Reminding
description: 
published: true
date: 2025-11-07T02:27:40.177Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:29.070Z
---

# 🗳️ Vote Reminding

VotingPlugin includes a **vote reminding** system to notify players when they can vote again on one or more sites.  
This helps increase player participation without needing manual announcements or automation tools.

---

## ⚙️ How It Works

Vote reminding checks a player’s **vote cooldowns** and notifies them when a site becomes available.

- Requires vote delays to be correctly set up in `VoteSites.yml`
- Works automatically on player login or at set intervals
- Messages, titles, and action bars can be customized
- Fully configurable via `/av gui`

---

## 🧾 Permissions

| Permission | Description |
|-------------|--------------|
| `VotingPlugin.Player` | Default permission (required for vote reminding) |
| `VotingPlugin.Login.RemindVotes` | Enables standard vote reminders |
| `VotingPlugin.NoRemind` | Disables vote reminders for a player |
| `VotingPlugin.Login.RemindVotes.All` | Only reminds if **all** vote sites are available (instead of any) |

> 🧠 **Note:**  
> Since **v6.5+**, vote reminders now trigger if **any site** is available (previously required all sites).  
> Use the `RemindVotes.All` permission if you want to keep the old behavior.
{.is-info}

---

## ⏰ Cooldown End Reminders

You can also notify players **when a site cooldown ends** — per site.  
Add this inside each vote site section in `VoteSites.yml`:

CoolDownEndRewards:
  Messages:
    Player: "&aYou can vote again on %SiteName%!"

This works alongside the global VoteReminding system.

---

## 🧩 Example Configuration (`Config.yml`)

```yaml
# ------------------------------------------------
# VoteReminding
# ------------------------------------------------
VoteReminding:
  # Enable vote reminding system
  Enabled: true

  # Remind players on login if they can vote
  RemindOnLogin: true

  # Remind only once per available vote period (doesn't affect login)
  RemindOnlyOnce: true

  # Delay between reminders (in minutes)
  # Set to -1 to disable
  RemindDelay: 30

  # Reward section runs when a reminder is triggered
  Rewards:
    Messages:
      Player: '&aYou have %sitesavailable% sites to vote on!'
    Title:
      Enabled: false
      Title: '&cRemember to vote!'
      SubTitle: '&aType /vote'
      FadeIn: 10
      ShowTime: 50
      FadeOut: 10
    ActionBar:
      Message: '&cRemember to vote'
      Delay: 30
```

---

## ✅ Summary

| Feature | Description |
|----------|--------------|
| **RemindOnLogin** | Sends reminder when player joins |
| **RemindOnlyOnce** | Prevents repeating reminders |
| **RemindDelay** | Sets time interval for checking reminders |
| **Rewards** | Defines reminder messages, titles, and visuals |
| **CoolDownEndRewards** | Sends reminder when specific site cooldown expires |
| **Permissions** | Control who receives reminders and when |

> 💡 Tip: You can edit all VoteReminding messages and rewards using `/av gui` for easier setup.
