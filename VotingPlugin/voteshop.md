---
title: VoteShop
description: 
published: true
date: 2026-03-08T01:22:58.352Z
tags: 
editor: markdown
dateCreated: 2026-03-08T01:22:58.352Z
---

# VoteShop

VoteShop allows players to spend **vote points** earned from voting on server listing websites.  
Players can purchase rewards such as items, commands, keys, permissions, or other rewards configured in `Shop.yml`.

---

# Enabling VoteShop

VoteShop is enabled in `Shop.yml`:

```yaml
VoteShop:
  Enabled: true
  Name: VoteShop
```

Players can open the shop using:

```
/voteshop
```

---

# Basic Shop Item

A simple purchasable item:

```yaml
Shop:
  Diamond:
    Identifier_Name: Diamond
    DisplayItem:
      Material: DIAMOND
      Amount: 1
      Name: '&bBuy a Diamond'
      Lore:
        - '&7Cost: &a3 Vote Points'
    Cost: 3
    CloseGUI: true
    Rewards:
      Items:
        Diamond:
          Material: DIAMOND
          Amount: 1
```

---

# DisplayItem

`DisplayItem` defines what appears in the GUI.

Example:

```yaml
DisplayItem:
  Material: DIAMOND
  Amount: 1
  Name: '&bBuy a Diamond'
  Lore:
    - '&7Cost: &a3 Vote Points'
```

If `DisplayItem` is not present, the plugin will automatically fall back to the **legacy display format**:

```yaml
Material: DIAMOND
Amount: 1
Name: '&bBuy a Diamond'
Lore:
  - '&7Cost: &a3 Vote Points'
```

---

# Categories

Categories allow you to organize shop items into separate menus.

Example category button in the main shop:

```yaml
Shop:
  BlocksCategory:
    Category: Blocks
    DisplayItem:
      Material: BRICKS
      Name: '&bBlocks Shop'
```

Category definition:

```yaml
Categories:
  Blocks:
    Name: '&bBlocks Shop'
    Shop:
      EmeraldBlock:
        Cost: 5
        DisplayItem:
          Material: EMERALD_BLOCK
          Name: '&aEmerald Block'
        Rewards:
          Items:
            EmeraldBlock:
              Material: EMERALD_BLOCK
              Amount: 1
```

Clicking the category button opens the category GUI.

---

# Back Button

Categories support returning to the main VoteShop GUI.

```yaml
Categories:
  Blocks:
    BackButton: true
```

Custom back button item:

```yaml
Categories:
  Blocks:
    BackButton: true
    BackButtonItem:
      Material: BARRIER
      Name: '&cBack to VoteShop'
```

Clicking the back button returns the player to the main VoteShop menu.

---

# Confirmation Menu

Items can require confirmation before purchase.

```yaml
RequireConfirmation: true
```

Confirmation GUI is configured in `ShopConfirmPurchase`.

```yaml
ShopConfirmPurchase:
  Title: Confirm Purchase?
  YesItem:
    Material: EMERALD_BLOCK
    Name: '&aYes'
  NoItem:
    Material: BARRIER
    Name: '&cNo'
```

---

# Limits

You can limit how many times a player can purchase an item.

```yaml
Limit: 3
```

Reset limits automatically:

```yaml
Reset:
  Daily: true
  Weekly: false
  Monthly: false
```

---

# Permissions

Require permissions to purchase items.

```yaml
Permission: votingplugin.shop.vip
HideOnNoPermission: true
```

- `HideOnNoPermission: true` hides the item completely.
- `HideOnNoPermission: false` shows the item but prevents purchasing.

---

# Commands as Rewards

Example command reward:

```yaml
Rewards:
  Commands:
    - 'give %player% diamond 1'
```

---

# ExtraItems

ExtraItems are **display-only items** that appear in the GUI but cannot be purchased.

```yaml
ExtraItems:
  Info:
    DisplayItem:
      Material: BOOK
      Name: '&eShop Info'
      Lore:
        - '&7Use vote points to purchase rewards'
```

---

# Slot Positioning

Items can be placed in specific slots using:

```yaml
Slot: 10
```

## Last Slot Shortcut

Setting the slot to **-2** automatically places the item in the **last available slot of the GUI**.

Example:

```yaml
Slot: -2
```

This is useful for:

- Back buttons
- Navigation items
- "Coming Soon" items
- Info buttons

The plugin will automatically place the item at the end of the menu.

---

# Tips

- Use **categories** to keep large shops organized.
- Use **Slot: -2** for navigation buttons like Back.
- Use **DisplayItem** for cleaner configs.
- Use **Limits** for daily or weekly rewards.