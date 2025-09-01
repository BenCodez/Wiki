---
title: Where to set rewards
description: 
published: true
date: 2025-09-01T03:01:06.814Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:32.400Z
---

## Quick little page explaining where to define rewards

### VoteSites.yml:  
Reward per votesite - Under Rewards on votesite  
Reward for vote CoolDownEndRewards - Under CoolDownEndRewards on votesite
Reward for voting on any votesite - Under EverySiteReward  

### SpecialRewards:  
Reward for voting on all sites - Under AllSites  
Reward for voting on all sites minus 1 site - Under AlmostAllSites
First vote reward - Under FirstVote  
First vote reward for the day reward - Under FirstVoteToday
Voting x amount of votes (with per day/week option), also known as Cumulative rewards - Under Cumulative  
One time reward - Under Milestones  
VoteStreak rewards - under VoteStreak  
VoteParty - under VoteParty.Rewards (for player specific rewards)  
TopVoter Rewards - Under (TOPVOTER)Awards  

### Config.yml:  
Vote reminding reward (not a real reward) - Under VoteReminding  