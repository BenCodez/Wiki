---
title: FAQ
description: 
published: true
date: 2025-11-07T02:39:25.597Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:10.405Z
---

# ❓ VotingPlugin — Quick FAQ

### 1) `/vote` says “vote here: www.votelinkhere.com”
This is **VentureChat** intercepting the `/vote` command.  
Remove or change VentureChat’s `/vote` alias so VotingPlugin handles it instead.

- Check VentureChat’s config for command aliases and **remove `/vote`** there.
- Restart/reload VentureChat and test `/vote` again.

---

### 2) How do I add rewards for **crate keys**?
Put the crate plugin’s give-key command under a reward’s **Commands** list. Example:

Rewards:
  Commands:
  - "command here %player%"

Examples (replace with your crate plugin’s command):
- CrazyCrates:  `"cc give physical <CrateName> 1 %player%"`
- CMI:          `"cmi give %player% key:<KeyName> 1"`
- CratesPlus:   `"crate givekey %player% <CrateName> 1"`

> Use your crate plugin’s exact syntax. `%player%` is replaced with the voter’s name.

---

### 3) How do I **test a vote**?
Use:
- `/av vote <player> <site>`

---

### 4) **YML error**
Your file is formatted incorrectly. Validate it here:
- https://yaml-online-parser.appspot.com/

Tips:
- Use **spaces**, not tabs.
- Keep indentation consistent.
- Quote strings with special characters (`'&aText'`).

---

### 5) “No voting site with the service site: ‘SERVICE SITE HERE’”
Either **Votifier isn’t working** or the **ServiceSite** value doesn’t match.
- Run a test vote and check console.
- Fix using this guide: https://wiki.bencodez.com/en/VotingPlugin/Votifier-Troubleshooting

---

### 6) “No plugin.yml / failed to load”
Redownload the jar. The file is likely **corrupted**.

---

### 7) **Extreme troubleshooting / debugging**
- In `Config.yml`: set `DebugLevel: EXTRA`
- For proxy issues: enable `BungeeDebug` in `BungeeSettings.yml` **and** enable debug on the proxy.

---

### 8) **Hex color support?**
Yes. Use the format:
- `&#FF0000#`  (surround the hex with `&#` and `#`)

---

### 9) **Reload command**
- `/av reload`
- `/av reloadall`  *(also reloads user storage)*

---

### 10) **Out of memory / resource limit reached (Pterodactyl)**
If memory is fine, you may be hitting the **PID limit**. On the node:
- Increase `"container_pid_limit"` to **1024** in `/etc/pterodactyl/config.yml` (default is 512), then restart the node services.


