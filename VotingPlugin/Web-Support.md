---
title: Web Support
description: 
published: true
date: 2025-11-07T02:35:01.516Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:31.670Z
---

## 🌐 Displaying Votes Online (MySQL Required)

If you want to **show vote statistics on your website**, you can use external web integrations that connect directly to your **VotingPlugin MySQL database**.

> ⚠️ These are **third-party resources** — they are not created or maintained by the VotingPlugin author, but are widely used and compatible.

---

### 🧱 Available Web Integrations

**[VoteTop](https://www.spigotmc.org/resources/vt-votetop.36368/)**  
Displays top voters on a standalone web interface connected to your MySQL database.

**[VoteTop - NamelessMC Integration](https://www.spigotmc.org/resources/vt-votetop-for-namelessmc.36872/)**  
Integrates VotingPlugin leaderboards into **NamelessMC**, the popular Minecraft website CMS.

**[Nameless-VotingPlugin (GitHub)](https://github.com/samerton/Nameless-VotingPlugin)**  
Official NamelessMC module for syncing and displaying votes from VotingPlugin.  
Alternate download: [NamelessMC Resource Page](https://namelessmc.com/resources/resource/2-namelessmc-voting-plugin-integration/)

---

> 💡 **Tip:**  
> All of these require your VotingPlugin to use **MySQL** for data storage.  
> Make sure `StorageType: MYSQL` is set in `Config.yml`, and the web app credentials match your plugin’s database connection.
