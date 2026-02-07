---
title: WebHooks
description: 
published: true
date: 2026-02-07T01:20:23.906Z
tags: 
editor: markdown
dateCreated: 2026-02-07T01:20:23.906Z
---

# Webhook Rewards

Webhook Rewards let you send HTTP requests when a reward runs (for example: Discord messages, website notifications, automation triggers, external logging, etc.).

This system is **generic** and not Discord-only. Discord is just the most common use case.

---

## How it works

Webhook rewards are split into **two parts**:

1. **Webhook Definitions** (in `Config.yml`)
   - Defines *where* and *how* requests are sent
2. **Webhook Reward Entries** (in reward configs)
   - Defines *what* is sent and *when*

Rewards reference webhook definitions by **ID**.

---

## Full Config.yml example (recommended)

```yml
Webhooks:
  Enabled: true
  Definitions:
    discord-staff:
      Enabled: true
      Url: "https://discord.com/api/webhooks/XXXX/XXXX"
      Method: POST
      ContentType: "application/json"
      TimeoutMs: 8000
      Headers:
        X-Server: "{SERVER}"
      HandleDiscordRateLimits: true
      Retry:
        Enabled: true
        MaxAttempts: 5
        BackoffMs: 1500
        MaxBackoffMs: 15000
      Signature:
        Enabled: false
        Algo: "HMAC_SHA256"
        Header: "X-Signature"
        Secret: "change-me"
```

---

## Config option breakdown

### `Webhooks.Enabled`
Master enable switch.  
If `false`, **no webhook requests are sent**, even if rewards reference them.

---

### `Definitions`
Holds named webhook endpoints.  
Rewards reference these using:

```yml
webhook: "discord-staff"
```

---

### `Definitions.<id>.Enabled`
Enables or disables a **single webhook definition**.

Useful for temporarily disabling one endpoint without editing rewards.

---

### `Url`
Target endpoint URL.

Examples:
- Discord webhook URL
- Custom REST API
- Automation tools (Zapier, Make, n8n, etc.)

Discord webhook tokens are **automatically redacted in logs**.

---

### `Method`
HTTP method used for the request.

Supported values:
- `POST` (default)
- `PUT`
- `PATCH`

---

### `ContentType`
Sent as the `Content-Type` header.

Almost always:
```
application/json
```

---

### `TimeoutMs`
Connect + read timeout in **milliseconds**.

Prevents webhook requests from hanging threads.

Default: `8000`

---

### `Headers`
Optional additional HTTP headers.

- Values support placeholders
- Useful for API keys, authorization, server identification

Example:
```yml
Headers:
  Authorization: "Bearer YOUR_TOKEN"
  X-Server: "{SERVER}"
```

---

### `HandleDiscordRateLimits`
Discord-specific safety option.

If enabled and Discord responds with **HTTP 429** containing `retry_after`:
- VotingPlugin waits for the requested duration
- Then retries automatically

Recommended: `true` for Discord webhooks.

---

### `Retry`
Controls retry behavior for **all webhook types**.

| Option | Description |
|------|-------------|
| `Enabled` | Enables retries |
| `MaxAttempts` | Total attempts (including first) |
| `BackoffMs` | Initial delay before retry |
| `MaxBackoffMs` | Maximum backoff cap |

This protects external services and avoids message loss.

---

### `Signature`
Optional request signing using **HMAC**.

When enabled:
- VotingPlugin signs the raw request body
- Signature is sent in the configured header

| Field | Description |
|------|-------------|
| `Enabled` | Turns signing on/off |
| `Algo` | `HMAC_SHA256` |
| `Header` | Header name to send signature |
| `Secret` | Shared secret (supports placeholders) |

Use this if you control the receiving API and want to verify authenticity.

---

## Using webhooks in rewards

Webhook rewards are executed through an injected reward section.

### Recommended format

```yml
WebhookReward:
  Webhooks:
    - webhook: "discord-staff"
      content:
        enabled: true
        message: "✅ {PLAYER} voted on {SERVICE_SITE}"
```

Why this format?
- Works cleanly with AdvancedCore injected rewards
- Keeps webhook data grouped and predictable

---

## Discord embed example

```yml
WebhookReward:
  Webhooks:
    - webhook: "discord-staff"
      content:
        enabled: false
      embed:
        enabled: true
        title: "New Vote!"
        description: "{PLAYER} voted on {SERVICE_SITE}"
        color: "#2ecc71"
        footer:
          enabled: true
          message: "{TIMESTAMP}"
```

---

## Raw JSON example (generic APIs)

```yml
WebhookReward:
  Webhooks:
    - webhook: "my-api"
      json: |
        {
          "event": "vote",
          "player": "{PLAYER}",
          "uuid": "{UUID}",
          "site": "{SERVICE_SITE}",
          "server": "{SERVER}"
        }
```

Use raw JSON when sending to:
- Your own web services
- Logging endpoints
- Automation tools

---

## Troubleshooting

### Nothing sends
Check:
- `Webhooks.Enabled` is `true`
- The webhook definition exists and is enabled
- The reward is actually running
- The reward references a valid webhook ID

---

### Discord messages missing
Common causes:
- Deleted Discord channel
- Invalid webhook URL
- Rate limits with retries disabled
- Invalid JSON (raw mode)

---

## Summary

- Webhooks are **definition-based**
- Rewards reference webhooks by ID
- Supports Discord, APIs, and automation services
- Retry-safe, rate-limit-aware, and extensible

This system is designed to grow without breaking existing configurations.