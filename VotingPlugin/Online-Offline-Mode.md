---
title: Online/Offline Mode
description: 
published: true
date: 2025-11-06T02:42:46.316Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:18.207Z
---

# Online Mode Handling

## 🆕 Updated in Version 6.18.5+

Online mode behavior can now be configured directly in **Config.yml** using:

    OnlineMode: true

When enabled, VotingPlugin uses **online UUIDs** (Mojang-verified).  
If your setup uses a **mix of premium and cracked players**, you may want to disable it.

> ⚙️ When disabled, VotingPlugin will resolve UUIDs purely by player name.  
> This ensures UUIDs remain consistent across both online and offline players — ideal for hybrid (mixed) setups.
{.is-info}

---

## 🔄 Versions 6.18.4 and Below

For older versions, the same setting exists:

    OnlineMode: true

Only disable this if you **know for certain** your server uses **offline-mode UUIDs exclusively**.

If you’re running a **mixed UUID setup** (premium + cracked):
- Keep `OnlineMode: true`
- Disable `UUIDLookup` on your **proxy**

> 💡 If unsure, keep `OnlineMode` enabled — it’s the safest default for most servers.
{.is-info}
