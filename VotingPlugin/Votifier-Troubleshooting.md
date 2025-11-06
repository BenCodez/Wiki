---
title: Votifier Troubleshooting
description: 
published: true
date: 2025-11-06T02:39:42.423Z
tags: 
editor: markdown
dateCreated: 2025-08-30T22:18:29.993Z
---

## Verify Votifier Is Working

> ℹ️ If Votifier is working, you will see this in **console** (even if VotingPlugin isn’t fully configured yet):  
> `[VotingPlugin] Received a vote from service site 'SERVICESITEHERE' by player 'BenCodez'!`
{.is-info}

**Votifier plugins:**  
- [VotifierPlus setup guide](https://github.com/BenCodez/VotifierPlus/wiki/Setup-guide) (recommended)  
- NuVotifier (also supported)

### Testing Sites
- https://mctools.org/votifier-tester  
- https://mcservertime.com/votifier-tester  
- https://votifier.bencodez.com

Run a test vote (tester or a real site). A healthy setup typically shows **both** lines:
- From your votifier: `Debug: Received vote record -> Vote (from:SERVICESITEHERE username:BenCodez …)`
- From VotingPlugin: `[VotingPlugin] Received a vote from service site 'SERVICESITEHERE' by player 'BenCodez'!`

**About `SERVICESITEHERE`:**  
This must match the `ServiceSite` you set in `VoteSites.yml` so VotingPlugin links the incoming vote to the correct site.  
If no site is set, VotingPlugin can auto-generate one automatically.

> ✅ If you see the VotingPlugin message above, your votifier is working and VotingPlugin is receiving votes.
{.is-success}

---

## If You **Don’t** See the Console Message

- **Votifier is not listening or port is blocked**
  - Ensure the votifier plugin is loaded (check `/plugins` or `plugins` command).
  - Confirm the **host/IP** and **port** are correct and **not used** by anything else.
  - Open the port on your host/provider firewall and any OS firewall.

- **Keys / Token mismatch**
  - If using token mode (NuVotifier), make sure the vote site or tester uses the **same token**.
  - If using RSA keys, regenerate (2048-bit) and update the public key on the voting site.
  - If keys become corrupted, delete the RSA folder and let the plugin regenerate them.

- **Wrong bind address**
  - On shared hosts or containers, set Votifier to bind to the actual interface or `0.0.0.0` depending on your host setup.

- **Proxy networks**
  - Votifier should only run **on the proxy (Bungee/Velocity)**.  
  - Backend servers do **not** need Votifier.
  - Make sure your tester sends to the **proxy’s IP and port**, not a backend.

- **ServiceSite mismatch**
  - Use `/av servicesites` after a test vote to view the exact service name received.
  - Match that string exactly in `VoteSites.yml -> ServiceSite`.

- **Player / UUID edge cases**
  - If using Floodgate/Bedrock, ensure `BedrockPlayerPrefix` is configured correctly.
  - Check that your `OnlineMode` and `AllowUnJoined` settings match your player setup.

- **Still no luck?**
  - Enable debug mode in Votifier or VotingPlugin.
  - Retry a test vote and check console output for “Received vote record” or connection issues.

> ⚠️ **Note:** VotingPlugin will not function without a working Votifier setup.  
> If you don’t see the specific VotingPlugin message above, fix Votifier first before troubleshooting VotingPlugin.
{.is-warning}
