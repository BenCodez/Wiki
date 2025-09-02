---
title: Votifier Troubleshooting
description: 
published: true
date: 2025-09-02T00:53:08.993Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:29.993Z
---

> In order to verify votifier is working you should get this in console: 
[VotingPlugin] Received a vote from service site 'SERVICESITEHERE' by player 'BenCodez'!
This message will appear regardless of VotingPlugin configuration if votifier is working
{.is-info}



[VotifierPlus setup guide](https://github.com/BenCodez/VotifierPlus/wiki/Setup-guide) or any other votifier plugin like NuVotifier


## Testing sites:  
https://mctools.org/votifier-tester   
https://mcservertime.com/votifier-tester  
https://votifier.bencodez.com  

Use a testing service such as above or the actual voting website and do a test vote. Even though it may say that it successfully sent a test vote doesn't mean it's working properly. When doing a vote you will receive a message in console similar to this (If you get this it generally means votifier is working):

`[19:01:21] [Votifier I/O/INFO]: [VotifierPlus] Debug: Received vote record -> Vote (from:SERVICESITEHERE username:BenCodez address:Address timeStamp:TestVote)`  
`[19:01:21] [Server thread/INFO]: [VotingPlugin] Received a vote from service site 'SERVICESITEHERE' by player 'BenCodez'!`

SERVICESITEHERE text is what you set the service site in the votesites.yml for that specific site, so the plugin knows which votesite to link to what. Make sure this is done correctly or rewards may not work as expected

> If you get this message, then your good to go. If you don't set the service site on a votesite the plugin will autogenerate the votesite for you.
{.is-success}


## Steps to try if you don't get the console message:
- Verify votifier is running on an open ip/port (port is not in use, common on shared hosts), may need to contact your host for this
- No firewall or something blocking connections outside of the network. Some Basic steps:
```
To disable the firewall for an additional port on your server, you will need to configure the firewall settings to allow traffic on that specific port. Here are the general steps to do this:

Access your server's control panel or use a remote desktop connection to log in to your server.

Navigate to the firewall settings or firewall management tool on your server.

Look for the option to add a new rule or allow traffic on a specific port.

Create a new rule to allow inbound or outbound traffic on the additional port that you want to disable the firewall for.

Specify the protocol (TCP or UDP) and the port number that you want to allow.

Save the changes and apply the new firewall rule.

Please note that the exact steps to configure the firewall settings may vary depending on the operating system and the firewall management tool used on your server.
```

- Some cases deleting the RSA folder and generating new keys fixes the issues if not use an online site [here](https://www.devglan.com/online-tools/rsa-encryption-decryption) to manually generate keys if needed, just set 2048 bit  
- Use the correct ip for votifier, this heavily depends on your setup (Most cases it's the server ip or 0.0.0.0)

The above methods are from experience and are the most common solutions. There could be other solutions as well, really varies on your specific setup. 

> Please note, unless you get the specific message above in console VotingPlugin will not function, don't blame this on VotingPlugin
