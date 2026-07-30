---
title: VotingPlugin Presets
description: Configure vote sites from maintained VotingPlugin presets
published: true
date: 2026-07-30T22:00:00.000Z
tags:
editor: markdown
dateCreated: 2026-07-30T22:00:00.000Z
---

# VotingPlugin Presets

Vote-site presets provide an in-game setup flow for supported voting websites.
VotingPlugin downloads the available definitions from the
[VotingPlugin-Presets repository](https://github.com/BenCodez/VotingPlugin-Presets),
asks for the values required by the selected site, writes the result to
`VoteSites.yml`, and reloads the vote sites.

## Requirements

- Run the command as a player; the setup uses in-game prompts or dialogs.
- The server must be able to access GitHub and `raw.githubusercontent.com`.
- The player needs `VotingPlugin.Commands.AdminVote.VotePresets` or the
  configured VotingPlugin administrator permission.
- Back up `VoteSites.yml` before applying presets on an established server.

## Browse all presets

```text
/av VotePresets
```

This loads the available preset IDs and prompts you to select one. VotingPlugin
then asks for the preset's configurable values before applying it.

Depending on the preset, values may include:

- display name
- vote URL
- vote delay
- daily-delay behavior
- daily reset hour

The site key and service-site value may be supplied automatically by the
preset.

## Find a preset from a URL

```text
/av VotePresets https://example-voting-site.com/server/example/vote
```

VotingPlugin extracts the hostname and selects a preset whose configured domain
matches it. Include `https://` or `http://`; a hostname without a URL scheme
cannot be matched.

If a preset matches, VotingPlugin opens the same value prompts and applies the
completed configuration.

## What gets changed?

The preset enables or updates an entry in `VoteSites.yml`. A preset may set:

```yaml
VoteSites:
  example_site:
    Enabled: true
    DisplayName: Example Site
    ServiceSite: example.com
    VoteURL: https://example.com/vote
    VoteDelay: 24h
    WaitUntilVoteDelay: false
    VoteDelayDaily: false
    VoteDelayDailyHour: 0
```

If the site has no display item, VotingPlugin adds a basic stone display item.
If it has no rewards, VotingPlugin adds a basic thank-you message. Existing
sections that the preset does not manage are left in place.

After saving, VotingPlugin reloads the vote-site configuration.

## Troubleshooting

### No presets are available

Check that the server can reach GitHub's API and raw-content host. A firewall,
proxy, DNS failure, GitHub outage, or API rate limit can prevent the list from
loading.

### No preset matches the URL

- Include the complete URL with `https://` or `http://`.
- Try `/av VotePresets` and browse the available IDs.
- The voting site may not have a maintained preset yet.

### The wrong service site is detected

The preset supplies the usual service-site value, but voting websites can
change it. Send a test vote and compare the received service site with the
`ServiceSite` value in `VoteSites.yml`.

### The generated configuration needs customization

Presets are starting points. Review the generated site, display item, delay,
and rewards in `VoteSites.yml`, then test the site before advertising it to
players.
