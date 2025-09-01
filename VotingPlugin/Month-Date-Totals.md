---
title: Month Date Totals
description: 
published: true
date: 2025-08-31T03:44:23.945Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:14.680Z
---

# Month Date Totals
## This feature is still a WIP, but stable

By defaut VotingPlugin uses MonthTotal to store month totals, and has to reset that each month.

Using month date totals solves a few issues with that. When enabled the format is MonthTotal-MONTH-YEAR, e.g. Month-DECEMBER-2024. This will ensure month totals reset instantly and keep a history of month totals.

MonthTotal will still stay in sync and reset as it should as if this feature is disabled.

When enabled /vote previousmonthtotals will show all previous months (that there is data for)

More details to come



    ###########################################
    # Month Date Totals
    # Experimental feature
    # Same options for proxy
    ###########################################

    # Experimental
    # Stores month votes with date formatting
    # MonthTotal-MONTH-YEAR
    # This setting only enables setting totals, not using them
    # Enabling this is pretty safe and harmless with just this setting
    # Essentially will just copy MonthTotal to MonthTotal-MONTH-YEAR
    StoreMonthTotalsWithDate: false

    # Experimental
    # This setting uses month votes with date formatting
    # If using this StoreMonthTotalsWithDate must be enabled
    # This setting may be very buggy as it's in early stages
    UseMonthDateTotalsAsPrimaryTotal: false