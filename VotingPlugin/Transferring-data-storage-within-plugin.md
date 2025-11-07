---
title: Transferring data storage within plugin
description: 
published: true
date: 2025-11-07T02:30:01.283Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:28.333Z
---

# 💾 Data Storage Options

VotingPlugin supports multiple data storage systems for player votes, totals, and statistics.  
You can freely switch between them using built-in conversion commands.

---

## 📦 Available Storage Types

| Type | Description |
|-------|--------------|
| **FLAT** | Legacy text-based format (⚠️ *Will be removed soon*) |
| **SQLITE** | Local database stored in `Users.db` (default for small servers) |
| **MYSQL** | External SQL server — best for networks and multi-server setups |

---

## 🔄 Data Conversion

VotingPlugin can **transfer all player data** between these storage systems.  
This includes totals, streaks, and vote history (depending on version).

> ⚠️ **Warning:** Existing data in the target storage will be **overwritten**, not merged.

---

### 🧭 Commands

| Command | Description |
|----------|-------------|
| `/av convertfromdata (storage)` | Import data **into the current storage** from the specified source |
| `/av converttodata (storage)` | Export data **from the current storage** to the specified target |

Example:

/av converttodata MYSQL

> 💡 Run these commands **from the console** for best results — you’ll see live progress updates.

---

## ⚙️ Conversion Details

- Each player’s data is migrated in sequence.  
- Progress updates are logged every **100 users** processed.  
- Large databases may take **hours** to complete depending on hardware and user count.  
- Avoid running this during active voting or other data-modifying actions.  
  This ensures consistency and prevents partial writes.

---

## ✅ Recommendation

- Use **MySQL** for large or multi-server setups.  
- Use **SQLite** for small standalone servers.  
- Do **not** rely on **Flat file** — it is deprecated and will be removed in future releases.

---

> 🧠 Tip: You can confirm your current data storage type in `Config.yml` under `StorageType`.
