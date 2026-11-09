---
title: Minecraft Server Lists
description: Historical vote service identifiers and maintained preset metadata for setup verification
published: true
date: 2026-11-09T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2025-08-30T22:18:13.937Z
---

# Minecraft Server Lists — service-site reference

This table helps server administrators recognize voting websites and find available VotingPlugin presets. **It is not a live or verified registry of current site identifiers.** The website chooses the Votifier service name sent to your listener, and websites can change that name without notifying VotingPlugin.

**The safest source is your own received vote:** send one real/listener-generated test, read the service name in your console or use `/av servicesites`, and copy that value into `VoteSites.yml`. [Service Sites](/VotingPlugin/Service-sites) explains matching and automatic creation.

## Presets vs. confirmed service names

A **preset** is a convenience template, not proof that a service-site value is correct today. For example, the maintained [MinecraftServers.org preset](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/minecraftservers-org.meta.json) provides a default `ServiceSite` and has `"verified": false` in its metadata as checked November 2026. The sampled PlanetMinecraft, MCSL, and CraftVote presets also have `verified: false`; **do not interpret the presence of a preset as independent verification**.

For supported websites, try `/av VotePresets` in game or `/av VotePresets https://example.com/your-vote-page` (using your **real** page URL), review the result, and confirm the actual incoming vote before setting rewards. See [VotingPlugin Presets](/VotingPlugin/VotingPlugin-Presets).

## Historical mapping table

The values below come from the existing VotingPlugin community reference. They are **historical suggestions**, not freshly verified responses from each live voting website. Preset links point to maintained *metadata files* (not a guarantee the external site is active).

| Website/domain (reference) | Historical suggested `ServiceSite` | Available preset metadata |
|---|---|---|
| minecraftservers-list.com | `MinecraftServersList` | [Preset metadata](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/minecraftservers-list_com.meta.json) |
| minecraft-server-list.com | `MCSL` | [Preset metadata](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/minecraft-server-list-com.meta.json) |
| minecraftservers.org | `MinecraftServers.org` | [Preset metadata](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/minecraftservers-org.meta.json) |
| Minecraft-MP.com | `Minecraft-MP.com` | [Preset metadata](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/minecraft-mp-com.meta.json) |
| Minecraft-Server.net | `Minecraft-Server.net` | [Preset metadata](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/minecraft-server-net.meta.json) |
| PlanetMinecraft.com | `PlanetMinecraft.com` | [Preset metadata](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/planetminecraft-com.meta.json) |
| topminecraftservers.org | `TopMinecraftServers` | [Preset metadata](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/topminecraftservers-org.meta.json) |
| minecraft.buzz | `Minecraft.Buzz` | [Preset metadata](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/minecraft-buzz.meta.json) |
| servers-minecraft.net | `Servers-Minecraft` | [Preset metadata](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/servers-minecraft-net.meta.json) |
| mc-lists.org | `MC-Lists` | [Preset metadata](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/mc-lists-org.meta.json) |
| crafty.gg | `crafty.gg` | [Preset metadata](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/crafty-gg.meta.json) |
| mc-servers.com | `MC-Servers.com` | [Preset metadata](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/mc-servers-com.meta.json) |
| bestservers.com | `BestServers.com` | [Preset metadata](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/bestservers-com.meta.json) |
| minestatus.net | `minestatus.net` | [Preset metadata](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/minestatus-net.meta.json) |
| blockatlas.net | `blockatlas` | [Preset metadata](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/blockatlas-net.meta.json) |
| liste-serveurs.fr | `Liste-Serveurs` | [Preset metadata](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/liste-serveurs-fr.meta.json) |
| best-minecraft-servers.co | `Best Minecraft Servers` | [Preset metadata](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/best-minecraft-servers-co.meta.json) |
| minecraftbestservers.com | `Minecraft Server List` | [Preset metadata](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/minecraftbestservers-com.meta.json) |
| curseforge.com | `curseforge` | [Preset metadata](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/curseforge-com.meta.json) |
| minecraft.menu | `Minecraft Menu` | [Preset metadata](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/minecraft-menu.meta.json) |
| minecraft-serverlist.com | `minecraft-serverlist-com` | [Preset metadata](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/minecraft-serverlist-com.meta.json) |
| play-minecraft-servers.com | `play-minecraft-servers.com` | [Preset metadata](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/play-minecraft-servers-com.meta.json) |
| minecraftservers.blog | `minecraftservers.blog` | [Preset metadata](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/minecraftservers-blog.meta.json) |
| top-mcservers.com | `TOPMCSERVERS` | [Preset metadata](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/top-mcservers_com.meta.json) |
| 9minecraftserver.com | `9minecraftserver.com` | [Preset metadata](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/9minecraftserver_com.meta.json) |
| craftvote.com | `CraftVote` | [Preset metadata](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/craftvote_com.meta.json) |

A preset may contain a different proposed site key, display name, or default service identifier from this historical list. If they disagree, **do not guess**: use a real received vote as the authority. If a site has no preset, you can still configure it manually or let VotingPlugin detect it with `AutoCreateVoteSites: true` while setting up.

## Applying the actual received name

Example: after the listener receives a vote from `ExampleService`, edit an existing entry under `VoteSites:`:

```yaml
VoteSites:
  MyListing:
    Enabled: true
    Name: 'My Listing'
    ServiceSite: 'ExampleService'
    VoteURL: 'https://replace-with-real-listing.example/vote'
    VoteDelay: 24h
    DisplayItem:
      Material: DIAMOND
      Amount: 1
    Rewards:
      Messages:
        Player: '&aThanks for voting!'
```

This is an illustrative block: merge the `MyListing` key into the **existing** `VoteSites:`, replace the placeholder URL, and use the exact name confirmed in the logs. Internal site keys should be simple and without spaces/dots.

## If a reference seems wrong

1. Verify the incoming Votifier `ServiceSite` with a real test; `/av vote` does not verify the website's public protocol or the real incoming service name.
2. Compare it to `VoteSites.yml` and the preset's proposed default value.
3. Verify the website is still active and its real voting URL is not a placeholder.
4. Propose a change in [BenCodez/VotingPlugin-Presets](https://github.com/BenCodez/VotingPlugin-Presets) with **non-secret evidence** of the actual received name, or open a documentation issue for the historical table.
5. Do not paste token/public-key material, private keys, IP restrictions, or full unredacted configuration into an issue.

Helpful pages: [Service Sites](/VotingPlugin/Service-sites) · [Vote-Site Presets](/VotingPlugin/VotingPlugin-Presets) · [Votifier Troubleshooting](/VotingPlugin/Votifier-Troubleshooting).
