---
title: Vote Reminding
description: 
published: true
date: 2025-09-01T02:59:31.350Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:29.070Z
---

Vote reminding applies to players with permission "VotingPlugin.Player" (Given by default) or "VotingPlugin.Login.RemindVotes"  

The vote reminding won't apply if player has permission "VotingPlugin.NoRemind"  

By default players will be reminded if they can vote on any website (This changed from requiring allsites in 6.5+)  

If player has the permissison "VotingPlugin.Login.RemindVotes.All" then the reminding only runs if they can vote on all vote sites  

You can also remind players to vote when cool down ends for each site in VoteSites.yml under each site, CoolDownEndRewards.

Full default config options (Config.yml):

    # ------------------------------------------------
    # VoteReminding
    # ------------------------------------------------

    # Configuration for VoteReminding
    # By default this should be all setup to work
    # as long as vote delays are done properly in votesites.yml
    VoteReminding:
      # Enable vote reminding
      # This will remind player when he can vote on all sites
      # Requires VoteDelays to be setup properly
      # Use /vote next to see when you can be reminded
      # Players require the perm "VotingPlugin.Login.RemindVotes" or "VotingPlugin.Player"
      # To remind if all votesites are available (rather than any) use the permission "VotingPlugin.Login.RemindVotes.All"
      Enabled: true

      # Will remind player on login if he can vote
      RemindOnLogin: true
      
      # Whether or not to remind only once when the player can vote
      # Does not apply to login reminds.
      RemindOnlyOnce: true

      # Delay to remind votes in minutes
      # Set to -1 to disable
      RemindDelay: 30

      # Run rewards
      # and have the default message
      # Can add titles and more in the reward
      # This can also be edited via /av gui
      Rewards:
        Messages:
          Player: '&aYou have %sitesavailable% to vote on still!'
        Title:
          Enabled: false
          Title: '&cRemember to vote!'
          SubTitle: '&aType /vote'
          FadeIn: 10
          ShowTime: 50
          FadeOut: 10
        ActionBar:
          Message: '&cRemember to vote'
          Delay: 30