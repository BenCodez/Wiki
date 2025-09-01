---
title: Item Configuration
description: 
published: true
date: 2025-08-31T03:31:39.538Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:13.003Z
---

The following item format works throughout the plugin anywhere an item is specified. 

        Items:
          # Item
          # This is not item display name
          # No duplicate names
          Diamond:
            # Item Material
            # https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Material.html
            Material: 'DIAMOND'
            # Item data value (Eg 1:4, data is 4)
            # No longer used in newer minecraft versions
            Data: 0
            # Will only give Amount if min and max amounts are 0
            Amount: 1
            # Set item durability
            # Set to 0 or remove line for no durability
            #Durability: 100
            
            # Random amount of items between Min and Max will be given
            # if min and max are not both 0
            
            # Min amount of items
            #MinAmount: 1
            
            # Max amount of items
            #MaxAmount: 4
            
            # Chance for this specific item
            #Chance: 30
            
            # Item name
            # Remove this value to have no name
            Name: '&aSpecial Diamond'
            
            # Lore
            # Remove this value to have no lore
            Lore: 
            - 'Line 1'
            
            # Enchants
            # use vanilla names
            Enchants:
              unbreaking: 1

            # Set glowing effect on item (enchanted item effect)
            Glow: false
            
            # Hide item tool tip
            #HideToolTip: false
              
            # Skull options
            # Use material PLAYER_HEAD and %player% for player skulls
            #Skull: 'PLAYERNAME'
            # One place to find skull textures is here: https://minecraft-heads.com/
            #SkullTexture: 'SKULLTEXTURE'
            #SkullURL: 'URL'
            #Get texture from a player uuid
            #SkullUUID: 'PLAYER UUID'
             
            # Hide enchants     
            #ItemFlags:
            #- HIDE_ENCHANTS
            
            # CustomModelData nbt tag
            #CustomModelData: 100

            # Item models, 1.21.5+ only
            #ItemModel: "custom:modelname"
              
            # Set power of firework
            #Power: 1
            
            # Whether or not to break lore into more than 1 line
            # Disable for certain custom items if needed
            #CheckLoreLength: true
            #LoreLength: -1
            
            # Color of potion bottle
            # 0-255
            #PotionColor:
              #Red: 0
              #Green: 0
              #Blue: 0
              
            #Potions:
              #SPEED:
                #Duration: 20
                #Amplifier: 1

            #GUI options
            #Methods to set slots, applies to GUI's only
            #Slot: 0
            #FillSlots:
            #- 0

            #Fills all empty slots
            #FillEmptySlots: false

            #Close gui on click
            #CloseGUI: true

            #ItemsAdder: CUSTOMITEMNAME


Conditional Items (Not available in older versions):

    Items:
      Item1:
        # Javacript for conditional
        # Uses return value to get item info (can be anything, like numbers)
        ConditionalJavascript: 'User.canVoteAll()'
        Conditional:
          false:
            Material: 'REDSTONE_BLOCK'
            Amount: 1
          true:
            Material: 'EMERALD_BLOCK'
            Amount: 1
