---
title: DiscordSRV
description: Configure VotingPlugin rewards and top-voter leaderboards in DiscordSRV
published: true
date: 2026-08-09T01:18:39.000Z
tags:
editor: markdown
dateCreated: 2026-08-09T01:18:39.000Z
---

# DiscordSRV

VotingPlugin can send reward messages and maintain all-time, monthly, weekly,
and daily top-voter leaderboards through DiscordSRV.

Install and configure DiscordSRV first, then enable the integration in
`Config.yml`:

```yaml
DiscordSRV:
  Enabled: true

  TopVoter:
    # Recover automatically if a stored leaderboard message was deleted
    AutoRecoverMessageOnFailure: true

    Monthly:
      Enabled: true
      NewMessageOnUpdate: false
      Channel: 123456789012345678
      Title: 'Top Voters of the Month'
```

Replace `Channel` with the numeric Discord channel ID. The same structure is
available under `AllTime`, `Weekly`, and `Daily`.

## Updating or creating leaderboard messages

`NewMessageOnUpdate` controls whether VotingPlugin edits one leaderboard
message or keeps posting new messages:

| Value | Behavior |
|---|---|
| `false` | Store the message ID and edit that message during later updates. |
| `true` | Post a new message on each update instead of maintaining one stored message. |

When `NewMessageOnUpdate: false`, deleting the stored Discord message used to
leave later edits targeting an invalid ID. With
`AutoRecoverMessageOnFailure: true` (the default), an `Unknown Message` response
causes VotingPlugin to clear the stale ID, post one replacement, and persist
the replacement ID for later updates.

Recovery is serialized per leaderboard so overlapping updates do not create
multiple replacement messages.

## Manual recovery

Use the admin command when automatic recovery is disabled or when you need to
force the next update to create a message:

```text
/av ClearDiscordMessageID Monthly
```

Use `AllTime`, `Monthly`, `Weekly`, or `Daily` for the final argument. The
permission is:

```text
VotingPlugin.Commands.AdminVote.ClearDiscordMessageID
```

## Troubleshooting

- **Channel not found:** verify the numeric channel ID and confirm DiscordSRV's
  bot can see the channel.
- **Missing permissions:** allow the bot to view the channel, send messages,
  and embed links.
- **Deleted leaderboard does not return:** confirm
  `AutoRecoverMessageOnFailure: true` and `NewMessageOnUpdate: false`, then use
  the manual clear command if necessary.
- **Other edit errors:** automatic recovery is intentionally limited to
  Discord's `Unknown Message` response. Correct channel, permission, or
  DiscordSRV connection errors instead of repeatedly clearing the stored ID.
