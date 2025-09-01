---
title: PlaceHolderAPI placeholders
description: 
published: true
date: 2025-09-01T02:56:18.667Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:20.126Z
---

#### There is a placeholderapi expansion available to be downloaded on the expansion cloud of the plugin [PlaceHolderAPI](https://www.spigotmc.org/resources/placeholderapi.6245/), this is only required before 6.14. List of placeholders below. These can be used in other plugins that have placeholderapi support.

"No player" - Using a player placeholder without a player to reference  
".." - Using a placeholder that is not cached, should return a value once pulled again from cache (if enabled)  
"." or "..." - Using a placeholder that is not cached for the specific player, should almost never happen  

### Placeholder controls
- Add _process to end of placeholder to force a return value rather than . or .. if no cached value is ready, best option if you always need a value returned, do not use on main thread
- Add _nocache to end of placeholder to skip cache and retrive a live value, uses a direct mysql connection, do not use on main thread

### 
    # ---------------------------------------
    # Placeholderapi placeholders settings
    # ---------------------------------------

    # When enabled the command /vote setprimaryaccount (playername)
    # will be shown (after restart)
    # Primary account will be used instead of the players account to get
    # placeholder and other data such as vote reminding
    # Mainly to be used for alts and such
    UsePrimaryAccountForPlaceholders: false

    # Valid Options:
    # AUTO - Auto cache after they have been used (Recommended)
    # SPECIFIC - Only cache certain placeholders 
    # NONE - Don't cache any placeholders
    PlaceholderCacheLevel: AUTO

    # Placeholder controls
    # Add _process to end of placeholder to force a return value rather than . or .. if no cached value is ready
    # Add _nocache to end of placeholder to skip cache and retrive a live value, uses a direct mysql connection, do not use on main thread
    #

    # Set which placeholders to cache at all times
    # Use for placeholders to are pulled constantly or on the main thread
    # Mainly aimed for scoreboards that pull placeholders often
    # Placeholders may auto cache in certain conditions (if enabled above)
    # Will use additional memory, but not a lot
    # Still in early stages, please report bugs
    # Please remove VotingPlugin_ from the placeholder listed here
    CachedPlaceholders: []
    #- Total_AllTime

    # Custom placeholder returns
    # For the example below use %votingplugin_custom_enoughpoints_5%
    # DO NOT USE ON MAIN THREAD IF POSSIBLE
    # Keep everything lowercase
    #CustomPlaceholderReturns:
    #  'enoughpoints_5':
    #    'true': 'User has enough points'
    #    'false': 'User does not have enough points'

#### View up to date placeholders in game with /av placeholders and /av placeholdersplayer (player) to get the list with all values.

#### PlaceHolders:  
    votingplugin_total - Month total
    votingplugin_alltimetotal - Alltime total
    votingplugin_lastmonthtotal - Last month total
    votingplugin_disablebroadcast - Returns true/false if user has broadcast disabled
    votingplugin_disablereminders - Returns true/false if user has reminders disabled
    votingplugin_milestonecount - User milestonecount
    votingplugin_milestone_numberofvotesuntil_20 - Get number of votes until milestone
    votingplugin_milestone_numberofvotesuntil_1 - Get number of votes until milestone
    votingplugin_nextmilestone_votes_required - Get number of votes required for next available milestone
    votingplugin_nextmilestone_votes_until - Get number of votes until next available milestone
    votingplugin_lastmilestone_votes_since - Get number of votes since last milestone
    votingplugin_total_alltime - User total for AllTime
    votingplugin_total_monthly - User total for Monthly
    votingplugin_total_weekly - User total for Weekly
    votingplugin_total_daily - User total for Daily
    votingplugin_bestdailytotal - Best daily total
    votingplugin_bestweeklytotal - Best weekly total
    votingplugin_bestmonthlytotal - Best monthly total
    votingplugin_dailyvotestreak - Current daily votestreak
    votingplugin_weeklyvotestreak - Current weekly votestreak
    votingplugin_monthvotestreak - Current month votestreak
    votingplugin_bestdailyvotestreak - Best daily votestreak
    votingplugin_bestweeklyvotestreak - Best weekly votestreak
    votingplugin_bestmonthvotestreak - Best month votestreak
    votingplugin_points - User points
    votingplugin_points_format - User points
    votingplugin_canvote - Return true/false if player can vote on all sites
    votingplugin_canvotesites - Return number of votesites available
    votingplugin_next_anysite - How long until user can vote on anysite
    votingplugin_sitesavailable - Get number of sites available to be voted on
    votingplugin_sitesavailabletotal - Get total number of sites available to be voted on
    votingplugin_next_anysite - How long until user can vote on anysite
    VotingPlugin_Next_VOTESITE - How long until user can vote on VOTESITE
    VotingPlugin_Last_VOTESITE - How long ago user voted on VOTESITE
    VotingPlugin_CanVote_VOTESITE - Whether or not player can vote on VOTESITE
    votingplugin_top_all_position - Get user top voter position
    votingplugin_enoughpoints_# - Return true/false if player has said points
    votingplugin_top_month_position - Get user top voter position
    votingplugin_top_lastmonth_position - Get user top voter position for lastmonth
    votingplugin_top_week_position - Get user top voter position
    votingplugin_top_daily_position - Get user top voter position
    votingplugin_votepartycontributedvotes - See vote party placeholders contributed
    votingplugin_top_allvotes_# - Get user votes at position in top voter
    votingplugin_top_all_# - Get username at postion in top voter
    votingplugin_top_lastmonth_# - Get user at position in last month top voter
    votingplugin_top_lastmonthvotes_# - Get user votes at position in last month top voter
    votingplugin_top_month_# - Get username at position in top voter
    votingplugin_top_monthvotes_# - Get user votes at position in top voter
    votingplugin_top_week_# - Get username at postion in top voter
    votingplugin_top_weekvotes_# - Get user votes at position in top voter
    votingplugin_top_daily_# - Get username at postion in top voter
    votingplugin_top_dailyvotes_# - Get user votes at position in top voter
    votingplugin_votepartyvotescurrent - Current amount of voteparty votes
    votingplugin_votepartyvotesneeded - Voteparty votes needed
    votingplugin_votepartyvotesrequired - Amount of votes needed for voteparty
    votingplugin_bungeevotepartyvotescurrent - Current amount of bungee voteparty votes
    votingplugin_bungeevotepartyvotesneeded - Voteparty bungee votes needed
    votingplugin_bungeevotepartyvotesrequired - Amount of votes needed for bungee  voteparty
    votingplugin_globalmonthtotal - Global month total
    votingplugin_globalalltimetotal - Global alltime total
    votingplugin_globalweeklytotal - Global weekly total
    votingplugin_globaldailytotal - Global daily total
    votingplugin_timeuntildayreset - Time until plugin time day changes
    votingplugin_timeuntilweekreset - Time until plugin time week changes
    votingplugin_timeuntilmonthreset - Time until plugin time month changes

## 6.11.3 and below

#### Placeholder return codes:  
"No player" - Using a player placeholder without a player to reference  
".." - Using a placeholder on the main thread that isn't cached and AlwaysWaitForCache set to false  
"...." - Using a placeholder that isn't just cached yet and with AlwaysProcessPlaceholders set to false  

#### Default cache options:
Note: These are most performance efficient settings (without using cache), however placeholders can sometimes return values like the ones above instead of the intended value. If you get the other values as shown above set AlwaysWaitForCache and AlwaysProcessPlaceholders to true, that will always return a value. Just note it can crash the server if using with scoreboards.

        # ---------------------------------------
        # Placeholderapi placeholders settings
        # ---------------------------------------

        # When enabled the command /vote setprimaryaccount (playername)
        # will be shown (after restart)
        # Primary account will be used instead of the players account to get
        # placeholder and other data such as vote reminding
        # Mainly to be used for alts and such
        UsePrimaryAccountForPlaceholders: false

        # Always force placeholders to return value if the value isn't cached
        # This should prevent server from crashing when pulling placeholders on main thread
        # Only affects placeholderapi placeholders
        AlwaysWaitForCachePlaceholders: false

        # Always force placeholders to be processed and return a proper value
        # This has small chance of crashing the server (mainly with mysql and using placeholders on main thread)
        AlwaysProcessPlaceholders: false

        # Enable auto caching placeholders
        # Generally this works well, but if you need to cache placeholders manually set them below
        AutoCachePlaceholders: false

        # Set which placeholders to cache at all times
        # Use for placeholders to are pulled constantly or on the main thread
        # Mainly aimed for scoreboards
        # Placeholders may auto cache in certain conditions
        # Will use additional memory, but not a lot
        # Still in early stages, please report bugs
        # Please remove VotingPlugin_ from the placeholder listed here
        CachedPlaceholders: []
        #- Total_AllTime

