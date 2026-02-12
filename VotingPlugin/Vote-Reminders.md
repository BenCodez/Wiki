---
title: Vote Reminders
description: 
published: true
date: 2026-02-12T02:23:08.425Z
tags: 
editor: markdown
dateCreated: 2026-02-12T02:23:08.425Z
---

# VoteReminders

VoteReminders let you automatically run **Rewards** (messages, commands, etc.) when certain events happen, such as:
- a player logging in
- a player casting a vote
- a vote cooldown ending (any site / all sites)
- a repeating interval (global check)

This system uses the normal **Rewards** format, so you can reuse existing reward logic.

---

## Enabling VoteReminders

VoteReminders are configured under:

- `VoteReminders` (definitions)
- `VoteReminderOptions` (global behavior / defaults)

If `VoteReminders` is empty, nothing will run.

---

## Reminder types

Each reminder definition has a `Type`:

- `LOGIN` — after a player logs in
- `FIRST_JOIN` — only the first time the player ever joins
- `VOTE_CAST` — after the player successfully casts a vote
- `COOLDOWN_END_ANY_SITE` — when *any* vote site cooldown ends for the player
- `COOLDOWN_END_ALL_SITES` — when the *all-sites* cooldown ends for the player
- `INTERVAL` — runs periodically (server-wide interval task)

---

## Common fields

Each reminder entry supports these fields (most are optional depending on your defaults):

- `Type` — one of the types above
- `Priority` — higher runs first (useful when multiple reminders could match)
- `Delay` — wait before evaluating and firing (example: `3s`, `10s`, `1m`)
- `Cooldown` — per-reminder cooldown per player (example: `3m`, `10m`, `1h`)
- `Conditions` — requirements before firing (see below)
- `Rewards` — what to run (same format as other rewards)

### Conditions

Typical condition keys:

- `CanVoteAny: true|false` — require that the player can vote on at least one site
- `CanVoteAll: true|false` — require that the player can vote on all configured sites

(Other conditions may exist depending on your build, but these are the core ones.)

---

## Example

```yml
VoteReminders:
  OnLogin:
    Type: LOGIN
    Priority: 50
    Delay: 3s
    Cooldown: 3m
    Conditions:
      CanVoteAny: true
    Rewards:
      Messages:
        Player: "&aWelcome back! You can vote now on &e%sitesavailable%&a sites."
```

---

## Placeholders

VoteReminders use the normal Rewards placeholder system. In addition, VoteReminders inject a few extra placeholders you can use inside reminder rewards (messages/commands/etc).

### Always available in VoteReminder rewards

- `%sitesavailable%` — number of vote sites the player can currently vote on (sites not voted on yet)

### Available for specific reminder types

**`VOTE_CAST`**
- `%site%` — the site display name/key that was just voted on (as provided by the vote event)

**`COOLDOWN_END_ANY_SITE`**
- `%votesite%` — the vote site display name whose cooldown ended
- `%votesite_id%` — the vote site key/id whose cooldown ended

> Notes:
> - These are added only when that reminder type fires.
> - If you reference a placeholder that isn’t set for that reminder, it will be blank (or remain unchanged depending on your reward handler).

### Standard VotingPlugin placeholders

All normal VotingPlugin/Rewards placeholders still work here (for example `%player%` and anything your setup provides through VotingPlugin’s placeholder handling / PlaceholderAPI integration).

---

## Cooldowns and storage

VoteReminders support multiple layers of cooldown protection:

- **Global cooldown** (optional): prevents reminders from firing too frequently overall.
- **Per-reminder cooldown**: each reminder definition can have its own `Cooldown`.
- Cooldowns are stored per-player so they persist correctly across sessions (depending on your storage backend).

---

## Tips

- Use **Priority** with `StopAfterMatch` (if enabled in your options) to make “best match wins” behavior.
- Prefer a small **Delay** on `LOGIN` reminders so player data is fully loaded before checking `CanVoteAny/All`.
- Use `INTERVAL` reminders sparingly; they are designed for periodic checks and can be noisy if too frequent.
