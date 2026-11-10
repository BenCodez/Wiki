---
title: Vote Site Catalog and Preset Verification
description: Verify vote-site identifiers and preserve the runtime-consumed mapping format
published: true
date: 2026-11-09T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2026-11-09T00:00:00.000Z
---

# Vote-site catalog and preset verification

**Important:** The [Minecraft Server Lists](/VotingPlugin/Minecraft-Server-Lists) page is **a runtime input to VotingPlugin**, not only human-readable documentation. The `ServiceSiteHandler` fetches its Markdown (or HTML-rendered mirrors) and parses simple `domain - service site` list entries, then can persist the resulting mappings into `ServerData.yml`. Keep that original page in its existing bullet-list format. Do not convert it into a table.

The mapping list is a convenience reference, not a guarantee that a voting website's currently transmitted `ServiceSite` is unchanged. This companion page carries editorial guidance so the machine-readable source stays intact.

## Verify the actual site identifier

1. Configure VotifierPlus/NuVotifier, then send a **real or listener-generated vote** through your actual voting website.
2. Check the received service name in console output, or use `/av servicesites` after the vote.
3. Compare that exact value with the enabled `VoteSites.yml` entry's `ServiceSite`. Matching is case-insensitive, but do not guess a value from the public voting URL.
4. Use `/av VotePresets` to generate a starting configuration for supported websites, then verify its suggested service name against the real vote. `/av vote <player> <site>` is an internal test and does not verify the name sent by the external website.
5. After configuring all intended sites, set `AutoCreateVoteSites: false` to prevent unknown services from automatically creating new entries.

## Presets are starting points

The [VotingPlugin-Presets repository](https://github.com/BenCodez/VotingPlugin-Presets/tree/main/presets/votesites) maintains configuration templates. Some template metadata includes `"verified": false`. For example:

| Website | Preset metadata |
|---|---|
| MinecraftServers.org | [Preset JSON](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/minecraftservers-org.meta.json) |
| Minecraft Server List | [Preset JSON](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/minecraft-server-list-com.meta.json) |
| PlanetMinecraft | [Preset JSON](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/planetminecraft-com.meta.json) |
| CraftVote | [Preset JSON](https://github.com/BenCodez/VotingPlugin-Presets/blob/main/presets/votesites/craftvote_com.meta.json) |

Neither a preset nor a historical wiki mapping takes precedence over an actual received vote.

## Editing the machine-readable list

The original list contains **26 mappings** as of this review. Preserve one plain Markdown bullet per mapping, without extra links, labels, or metadata on the mapping line:

```text
* example.com - ExampleServiceName
```

Avoid adding unrelated `name - value` lines, tables, or other ambiguous text to that page. That content may be fetched directly by a running server. Use this companion page for longer explanations and provide evidence from a real received vote when proposing corrections.

The existing `AdvancedServiceSiteHandling` option uses these mappings to help resolve service identifiers. Incorrect entries can affect vote-site matching. Do not change the mapping values merely to align them with unverified preset defaults.

## Related documentation

[Runtime-consumed Minecraft Server Lists](/VotingPlugin/Minecraft-Server-Lists) · [Vote-site Presets](/VotingPlugin/VotingPlugin-Presets) · [Service Sites](/VotingPlugin/Service-sites) · [Votifier Troubleshooting](/VotingPlugin/Votifier-Troubleshooting)
