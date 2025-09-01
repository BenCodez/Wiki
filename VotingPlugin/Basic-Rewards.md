---
title: Basic-Rewards
description: 
published: true
date: 2025-08-30T22:17:57.613Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:17:56.854Z
---

This page is how the basic reward section works on votesites and bonus rewards. This is recommended if you not an advanced user.

#### Money:
* Can give money directly if vault is installed (or use commands)
* Set ingame with /av VoteSite (SiteName) SetMoney (Money) or /av BonusReward SetMoney (Money)

##### Money Example

    # Example gives $500 to player, set to 0 for none (Requires vault)
    # You could also use a command
    Money: 500

#### Items:
* Can have a name, lore, enchants
* Can set via ingame with /av VoteSite (SiteName) AddItem (Item) - HOLD ITEM IN HAND (or /av BonusReward AddItem (item))

##### Item Example

    Items:
      # item (can be anything, just don't have 2 the same)
      Diamond:
        # item id
        ID: 264
        # item data
        Data: 0
        # item amount
        Amount: 1
        # name - set to '' (that's 2 ') for no name, e.g Name: ''
        Name: '&4Example'
        # lore - set to '' (that's 2 ') for no lore, e.g Lore: ''
        Lore:
        - '&4Line 1'
        # Enchants - do not enter this below if you don't want enchants
        # Example gives Protection and Unbreaking 1
        # Enchants can be found here: https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/enchantments/Enchantment.html
        Enchants:
          PROTECTION_ENVIRONMENTAL: 1
          DURABILITY: 1

#### Commands:
* Issue commands from console or as player
* Add ingame with /av VoteSite (SiteName) AddCommandPlayer/AddCommandConsole (CMD) - Command with the / (or /av BonusReward AddCommandPlayer/AddCommandConsole (CMD))

##### Command Example

    # Commands to run on vote (when player is online)
    # use %player% for the player's name
    Commands:
      # Console commands
      Console:
      - 'say Example command: %player%'
      # Player commands
      Player:
      - 'vote total'