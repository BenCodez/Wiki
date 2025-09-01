---
title: Delayed reward command
description: 
published: true
date: 2025-09-01T02:55:45.221Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:07.057Z
---

In this example fly will be enabled with /fly and disable with /fly one hour later. Works with any reward

    Rewards:
      Commands:
      - fly %player%
      # Can chain rewards within rewards
      # Executes as a different reward
      Rewards:
        Delayed:
          Enabled: true
          Hours: 1
          Minutes: 0
          Seconds: 0
        Commands:
        - fly %player%