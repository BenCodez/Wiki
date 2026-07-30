---
title: Signs
description: 
published: true
date: 2025-11-23T19:44:30.085Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:25.397Z
---

# Signs

## ⭐ Vote Signs / Leaderboard Signs

This page explains how to create **VotingPlugin leaderboard signs**, place heads, set skulls, and configure the 3×3 update area.

---

## 🪧 Adding a Sign  
![Adding a sign](http://i.imgur.com/w2PRmQv.png)

To create a leaderboard sign:

**Line 1:** `[VotingPlugin]`  
**Line 2:** `Position`  
**Line 3:** `All` / `Monthly` / `Weekly` / `Daily`

The appearance and text for signs are controlled by VotingPlugin’s internal formatting system and configurable sign settings.

---

## 🎥 Setup Video  
[![Watch the video](https://img.youtube.com/vi/kKz31qEvD1k/hqdefault.jpg)](https://youtu.be/kKz31qEvD1k)

---

## 🔄 How Updating Works  
- Signs update in a **3×3 area** around the sign.  
- If you set a **skull** (right-click the sign, then click a skull block), the update location will follow that skull.  
- This allows you to customize exactly where heads appear.

---

## 👤 Heads  
![Heads](http://imgur.com/XF4LqES.png)

VotingPlugin automatically places player heads to match leaderboard positions (1st, 2nd, 3rd, etc.).

---

## 🔳 3×3 Cube of Heads  
(Center of cube is the sign unless a skull is set)

![3x3 Cube of heads](http://imgur.com/RNVPNJv.png)

- The default maximum head layout is a **3×3 cube** centered on the sign.  
- Setting a skull overrides the center point.

---

## ☠️ Setting a Skull  
![SkullSet](https://imgur.com/TBfMTEa.png)

To manually set a skull anchor point:

1. Right-click the **sign**  
2. Then click the **skull block**  

This binds the sign to that skull and forces updates to occur at that exact location.

---

## 📦 Setup Example  
![Vote Signs Setup](https://imgur.com/nvomwro.png)

### 🔢 Important  
Signs should be placed **in order** (1 → 5).  
If not placed sequentially, the heads may **not** update correctly.
