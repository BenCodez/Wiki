---
title: Reward-Examples
description: 
published: true
date: 2025-08-30T22:18:21.944Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:21.108Z
---

The following is from ExampleBasic and ExampleAdvanced reward files.

    # This is a reward file
    # Define rewards in here (Items, commands, etc)
    # File name is the reward name, without file extention
    # This reward is named "ExampleBasic"
    # That is what you put as a reward for other plugins, like VotingPlugin
    # DO NOT HAVE DUPLICATE NAMES!!
    
    # Wiki Page: 
    # https://github.com/BenCodez/AdvancedCore/wiki/Reward-files
    
    # This is basic reward file
    # You can have multiple reward files that contain all kinds of rewards
    # Below are some basic things you can have, see the advanced example for more
    
    # You can just remove values you don't want (just delete it)
    # If you just want money just have a reward file containg only "Money: 100", for example
    # You can simply copy and paste from here what you want
    # in other reward files, that is the way they are designed
    
    # If true:
    # Only allow one item with chance to go through (from items below)
    # If no chance specificied it will only give the first item
    OnlyOneItemChance: false
    
    # Items to give to user
    Items:
      # Item
      # This is not item display name
      # No duplicate names
      Diamond:
        # Item Material
        # https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Material.html
        Material: 'DIAMOND'
        # Item data value (Eg 1:4, data is 4)
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
        
        # Chance for this specific item to be given
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
          
        # Skull options
        #Skull: 'PLAYERNAME'
        #SkullTexture: 'SKULLTEXTURE'
         
        # Hide enchants     
        #ItemFlags:
        #- HIDE_ENCHANTS
        
        # CustomModelData nbt tag
        #CustomModelData: 100
          
        # Set power of firework
        #Power: 1
        
        # Whether or not to break lore into more than 1 line
        # Disable for certain custom items if needed
        #CheckLoreLenth: true
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
          
    # Amount of money to give, requires vault
    # Use 0 to give none
    # Money is not per world
    # Use negative to take money
    # May need to use a command if it doesn't work
    Money: 1000
    
    # Pick random number between min and max money amount
    #Money:
    #  Min: 100
    #  Max: 3000
    
    #######
    # Experience rewards
    #######
    # Give player experience (not levels)
    #EXP: 100
    
    # Pick a random number between min and max EXP amount to give
    #EXP:
    #  Min: 100
    #  Max: 1000
    
    EXPLevels: 3
    
    # Random amount of EXP levels between 3 to 7
    # EXPLevels:
      # Min: 3
      # Max: 7
    
    # Commands to run
    # Use %player% for player name
    # Remove for no commands
    Commands:
    - say hi
    #Commands:
      # Commands here will be run by console
    #  Console:
    #  - 'say %player% was lucky'
      # Commands here are run by player
    #  Player:
    #  - 'vote total'
    
    # The messages are sent when rewards above are given to user
    # set to '' to give no message (or just remove the option)
    Messages:
      Player: '&aMessage on reward'
      Broadcast: '&aThis is a broadcast'
      
    # Can also do this to message player
    #Message: '&aMessage to player

    # This is a reward file
    # Define rewards in here (Items, commands, etc)
    # File name is the reward name, without file extention
    # This reward is named "ExampleAdvanced"
    # That is what you put as a reward for other plugins, like VotingPlugin
    # DO NOT HAVE DUPLICATE NAMES!!
    
    # Wiki Page: 
    # https://github.com/BenCodez/AdvancedCore/wiki/Reward-files
    
    # You can just remove values you don't want (just delete it)
    # If you just want money just have a reward file containg only "Money: 100", for example
    # Don't use this file as a reward, example only
    
    # This is the advanced example, if you only want an item or command then look
    # at the basic example, you can simply copy and paste from here what you want
    # in other reward files, that is the way they are designed
    
    # This will delay the reward file from running
    Delayed:
      Enabled: false
      Hours: 1
      Minutes: 0
      Seconds: 0
      
    # Specific time of day to give this reward file
    # in 24 hour time, relative to local time zone
    Timed:
      Enabled: false
      Hour: 12
      Minute: 0
    
    # Chance out of 100
    # Set to 0 or 100 for always, or delete this line to disable chance
    # Will not give any rewards unless chance is lucky or disabled
    Chance: 40
    
    # Item conditional example
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
    
    # Player must be with a certain distance of said location
    #LocationDistance:
    #  World: world
    #  X: 0
    #  Y: 0
    #  Z: 0
    #  Distance: 10
      
    # Will give one command from the list
    RandomCommand: []
    
    # Will give one reward from the list of rewards
    RandomReward: []
    
    # Works similar to RandomReward above, just avoids reward files
    # Similar style to AdvancedPriority
    AdvancedRandomReward:
      reward1:
        Commands:
        - say reward1
      reward2:
        Commands:
        - say reward2
      reward3:
        Commands:
        - say reward3
    
    # Give one of the following items
    RandomItem:
      Diamond:
        Material: DIAMOND
        Amount: 1
      Iron:
        Material: IRON_INGOT
        Amount: 10
    
    # Require permission to give this reward file
    # Permission is AdvancedCore.Reward.(REWARDNAME) by default
    # E.g: AdvancedCore.Reward.ExampleAdvanced
    RequirePermission: false
    
    # Permission that must be required if RequirePermission is true
    # Add ! in front to make it only run when permission isn't there instead
    Permission: 'AdvancedCore.Reward.ExampleAdvanced'
    
    #TempPermission:
    #  Permission: 'PERMISSIONHERE'
    #  # Time in seconds
    #  Expiration: 60
    
    # Amount of time to still allow the reward to be executed
    # if reward is saved offline
    # Time in minutes
    #RewardExpiration: 1440
    
    # Javascript
    # Only use this if you know what you are doing
    # 
    # Bukkit API placeholders:
    # Using "BukkitServer" in your javascript will return Bukkit.getServer()
    # You can use any methods inside of the Server class
    # Example: BukkitServer.getBannedPlayers().size().toFixed()
    #
    # "BukkitPlayer" in your javascript will return the Player object of the player getting the reward
    # You can use any methods inside of the Player class
    # Example: BukkitPlayer.hasPermission("some.permission")
    Javascript:
      Enabled: false
      Expression: ''
      # Reward files to run if expression is true
      TrueRewards: {}
      # Reward files to run if expression is false
      FalseRewards: {}
      
    # Do things like set health or other things
    # not possible with commands
    Javascripts: []
    
    # Javascript expression which must be true in order to give this reward
    JavascriptExpression: ''
    
    # List of reward files to try and execute
    # Will only execute first possible reward that can be given
    # Recommend using AdvancedPriority (same thing but can avoid having multiple files)
    Priority: []
      
    # Advanced example
    # 50% chance for reward1, if reward1 not given then 20% chance to get reward2, if reward2 not given then fallback
    AdvancedPriority:
      # Similar to priority, but no need to have to use reward files
      # Add requirements under each reward
      # Will go in order from list here and try to run each of the following rewards...
      # This name can be anything, but they need to be different
      Reward1:
        Chance: 50
        # Any other requirement here
        # If any requirement fails, the next will be attempted
        Messages:
          Player: 'You got first reward'
      Reward2:
        Chance: 20
        Messages:
          Player: 'You got second reward'
      # Fallback, 100% chance
      Fallback:
        Messages:
          Player: 'You got unlucky'
          
    # Give rewards based on what world the player is on
    AdvancedWorld:
      world:
        Commands:
        - say %player% in world
      world_nether:
        Commands:
        - say %player% in nether
          
    # Special chance
    # percentage is caculated with all numbers added up
    # E.g. below:
    # Total is 100, so 5 is 5 out of 100, and so on
    # The number represents a weight value essentially
    # Decimals are allowed as well, just use _ as the decimal
    # no duplicates numbers allowed
    SpecialChance:
      5:
        # rewards here
        Commands:
        - say 5
      15:
        Commands:
        - say 15
      30:
        Commands:
        - say 30
      50:
        Commands:
        - say 50
        
    # Let the user pick a reward file to get
    # User can only pick one
    EnableChoices: false
    Choices:
      Diamond:
        DisplayItem:
          Name: '&c3 Diamonds'
          Material: DIAMOND
          Amount: 3
        Rewards:
          Items:
            Diamond:
              Material: 'DIAMOND'
              Amount: 3
          Messages:
            Player: '&aYou picked %choice%'
      Iron:
        DisplayItem:
          Name: '&c15 Iron Ingots'
          Material: IRON_INGOT
          Amount: 15
        Rewards:
          Items:
            Iron:
              Material: 'IRON_INGOT'
              Amount: 15
          Messages:
            Player: '&aYou picked %choice%'
    
    # Will execute rewards in one of the given worlds when player is in world
    Worlds:
    - 'world1'
    - 'world2'
    
    # Reward will never execute in the worlds below
    # Similar to Worlds, but in reverse
    BlackListedWorlds:
    - 'world3'
    - 'world4'

    # Reward type
    # Possible Values: ONLINE,OFFLINE,BOTH
    # Default: BOTH
    # Make this reward file only give rewards depending 
    # if player was online/offline when the reward attempted to give
    RewardType: 'BOTH'
    
    # If true, reward file will execute even if player is offline
    # Does not support all rewards
    # ONLY USE THIS IF YOU KNOW WHAT YOU ARE DOING
    ForceOffline: false
    
    # Vault group required to get reward 
    #VaultGroup: 'NORMAL'
      
    # Potions to give on reward
    Potions:
      # Potion effect name
      # Potions can be found here:
      # https://hub.spigotmc.org/javadocs/spigot/org/bukkit/potion/PotionEffectType.html
      ABSORPTION:
        # Duration in seconds
        Duration: 100
        # Amplifier
        Amplifier: 1
        
    # Title to send to player
    Title:
      Enabled: false
      Title: '&cTitle!'
      SubTitle: '&aSubTitle!'
      FadeIn: 10
      ShowTime: 50
      FadeOut: 10
      
    # Send bossbar to player
    # This requires 1.9+
    BossBar:
      Enabled: false
      # Message to send
      Message: '&aBossbar'
      # Bar Colors:
      # https://hub.spigotmc.org/javadocs/spigot/org/bukkit/boss/BarColor.html
      Color: 'BLUE'
      # Bar Styles:
      # https://hub.spigotmc.org/javadocs/spigot/org/bukkit/boss/BarStyle.html
      Style: 'SOLID'
      # Precentage for bar
      Progress: 0.50
      # Delay until bar goes away (in ticks)
      Delay: 30
      
    # Sound on reward
    Sound:
      # Enable or Disable Sound
      Enabled: false
      # Sound to play
      # Uses minecraft names
      Sound: 'entity.player.levelup'
      # Volume
      # Range: 0.0 to 1.0
      Volume: 1.0
      # Pitch
      # Range: 0.0 to 2.0
      Pitch: 1.0
      
    # Play particle effect on reward
    # 1.10 Effects can be found here:
    # https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Effect.html
    Effect:
      Enabled: false
      Effect: 'EXPLOSION_NORMAL'
      # Ususally speed
      Data: 1
      Particles: 10
      Radius: 5
      
    Firework:
      Enabled: false
      Power: 2
      # Colors can be found here:
      # https://hub.spigotmc.org/javadocs/spigot/org/bukkit/DyeColor.html
      Colors:
      - BLUE
      FadeOutColor: 
      - RED
      Trail: true
      Flicker: true
      # Types can be found here:
      # https://hub.spigotmc.org/javadocs/spigot/org/bukkit/FireworkEffect.Type.html
      Types:
      - BALL_LARGE
      
    # Send action bar
    ActionBar:
      Message: '&cThis is an actionbar!'
      # Delay until action bar goes away (in ticks)
      Delay: 30
    
    # Lucky rewards  
      
    OnlyOneLucky: false
    # The example below would give a 1 in 10 chance of receiving an extra $100, and a 1 in 50 chance of an extra $1000.
    Lucky:
      '10':
        Messages:
          Player: 'You were lucky and received an extra $100!'
        Money: 100
      '50':
        Messages:
          Player: 'You were lucky and received an extra $1000!'
        Money: 1000
        
    # Only for some GUI's
    # Required for choice rewards
    # not a reward
    DisplayItem:
      Material: 'DIAMOND'
      Name: '&aAdvancedReward'
      Amount: 1
        
    # Ability for server option
    # Makes sure the correct server gets the reward
    #Server: 'Minecraft Server'
    
    #############################################
    # RECOMMEND using AdvancedPriority
    # as it easier to use
    #############################################
    #
    # Advanced Random Rewards, just ignore this if you don't want fancy chance rewards
    # This is to give random rewards, with fallback
    # Rewards defined in this reward file below are still given regardless of this below
    Random:
      # Chance to give a randomly selected reward below (from list), will only give random reward
      # if lucky (according to chance)
      # Works same as chance above
      Chance: 40
      # If this value is true it will pick a random reward in the Rewards list
      # if false, all rewards are given
      # Value is true if not specified
      # Can also use RandomReward (a few lines below) to give a random reward only
      PickRandom: true
      # Rewards if chance is lucky, can be random depending in option above
      # Don't set this reward as a possible reward, may cause infinite loop
      Rewards: []
      # A list of fall back rewards if chance is unlucky
      # Don't set this reward as a reward, may cause infinite loop
      FallBack: [] 
      
    ################################################
    # REPEAT REWARDS
    # Meant for advanced uses
    # Rewards do not persist on shutdown (unless enabled)
    # Not tested in all situations yet, use at your own risk
    ################################################
    Repeat:
      Enabled: true
      # Time in milliseconds 1000 = 1 second
      TimeBetween: 60000
      # Number of times to repeat
      # set to -1 for no limit
      Amount: -1
      # Start repeating on startup, otherwise it will only repeat when reward is given
      # If true, the reward will not repeat when executed
      # Will execute for every player online at time of execution
      RepeatOnStartup: false
      # If any reward requirement fails to pass, the reward will stop repeating
      AutoStop: truee