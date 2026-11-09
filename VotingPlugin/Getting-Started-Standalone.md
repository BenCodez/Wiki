---
title: Standalone Server Quick Start
description: Install and verify VotingPlugin on a single Paper or Spigot server
published: true
date: 2026-11-09T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2026-11-09T00:00:00.000Z
---

# Standalone Server Quick Start

This walkthrough is for **one Paper/Spigot server**, without Velocity or BungeeCord. By the end, a real vote from one configured website should be received and rewarded.

> **Version:** VotingPlugin **7.1.1**, requiring **Java 21**. You do **not** need MySQL, `BungeeSettings.yml`, or a proxy for this setup; the default `DataStorage: SQLITE` is fine.
{.is-info}

## 1. Install VotingPlugin and a vote listener

1. Download [VotingPlugin](https://www.spigotmc.org/resources/votingplugin.15358/) and [VotifierPlus](https://github.com/BenCodez/VotifierPlus) (or a compatible NuVotifier release).
2. Place the **server** JARs in your Paper/Spigot `plugins/` folder. Do not use a BungeeCord/Velocity JAR on a backend.
3. **Start or fully restart** the server. Check the console to ensure *both plugins loaded without errors*.
4. Find VotingPlugin's generated files in `plugins/VotingPlugin/`, including `Config.yml` and `VoteSites.yml`.

If either plugin fails to load, resolve that before continuing. Check Java/server compatibility and the actual error message, rather than changing random configuration values.

## 2. Make the vote listener reachable

VotifierPlus receives the notification that a server-list website sends. VotingPlugin does **not** listen for public Votifier connections itself.

Open the **generated VotifierPlus listener** `config.yml` (not VotingPlugin's `Config.yml`). Common VotifierPlus defaults are:

```yaml
host: 0.0.0.0
port: 8192
TokenSupport: false
DisableV1: false
```

- `port` is the **listener's TCP port**, **not** the Minecraft game port (usually `25565`). On a managed host, use a port allocated to this server; `8192` is only an example/default.
- `0.0.0.0` means **bind to local interfaces**; it is **never** the address to enter on a voting website.
- Allow inbound TCP traffic to the chosen listener port in your hosting panel/firewall, and forward it if hosting behind a router.
- For a website using **Votifier v1**, provide the public address, port, and contents of `rsa/public.key` from the listener's generated data folder. **Never share `rsa/private.key`.**
- If the website supports **Votifier v2 tokens**, enable `TokenSupport`, restart the listener, and provide the appropriate generated/configured token instead of a public key. Use the protocol your installed listener and the website both support. Leave `DisableV1: false` if any site still requires v1.

**Restart** after listener changes. In your listing site's voting/Votifier settings, enter the server's **public hostname or IP**, the **actual Votifier port**, and the matching key/token. This may require a separate network allocation from your game server.

See [Votifier Troubleshooting](/VotingPlugin/Votifier-Troubleshooting) if the listener cannot bind or a remote test cannot connect.

## 3. Add your first voting site

You have three supported paths. Pick one and test **one site** before adding more.

### Option A — in-game vote-site presets (easiest for supported sites)

As an operator **in game**, run:

```text
/av VotePresets
```

Or search for a matching preset using the real voting-page URL:

```text
/av VotePresets https://your-server-list.example/vote
```

Follow the prompts and review the generated `VoteSites.yml` entry. The URL must include `https://` or `http://`; not every listing has a preset. This 7.1.1 feature needs access to GitHub to load presets. See [VotingPlugin Presets](/VotingPlugin/VotingPlugin-Presets).

### Option B — automatically detect the service-site name

`Config.yml` defaults to:

```yaml
AutoCreateVoteSites: true
```

Send a **real or listener-generated vote** through the configured website and inspect the console or use `/av servicesites`. VotingPlugin can generate a site from a previously unknown service identifier. Open `VoteSites.yml`, replace any generated placeholder `VoteURL`, and review its delay, display item, and rewards.

### Option C — edit `VoteSites.yml` yourself

Use this example **inside** the existing `VoteSites:` section, replacing the placeholders with your real values:

```yaml
VoteSites:
  MyFirstSite:
    Enabled: true
    Name: 'My First Voting Site'
    ServiceSite: 'REPLACE_WITH_RECEIVED_SERVICE'
    VoteURL: 'https://your-server-list.example/vote'
    VoteDelay: 24h
    WaitUntilVoteDelay: false
    DisplayItem:
      Material: DIAMOND
      Amount: 1
    Rewards:
      Messages:
        Player: '&aThanks for voting!'
      Commands:
        - 'give %player% diamond 1'
```

- `MyFirstSite` is an **internal key**. Keep it simple, without spaces or dots.
- `ServiceSite` must match the **actual value sent by the website**; do not assume it is the website domain. Discover it from a real/listener-generated vote or `/av servicesites` and replace the placeholder before testing.
- `VoteURL` is what players click through `/vote`. Replace the example URL.
- `VoteDelay: 24h` controls the displayed next-vote interval; `WaitUntilVoteDelay: false` avoids mistakenly rejecting legitimate votes when a website uses different cooldown rules.
- `Enabled: true` matters. The bundled `ExampleVoteSite` is **disabled by default** and has example values. Edit/replace it or leave it disabled; don't assume it will work unchanged.
- The reward above sends a message and gives one diamond as a simple test. **Inline rewards are enough**; no separate reward file is required.

Do not paste a *second* top-level `VoteSites:` key into the file. Merge the new `MyFirstSite` entry under the existing one, then reload VotingPlugin or restart. See [Service Sites](/VotingPlugin/Service-sites) and [Rewards](/VotingPlugin/Rewards).

## 4. Verify the complete path

1. Join with a known player account and run `/vote`. Verify your site and link appear.
2. Run `/av vote <player> MyFirstSite` (use your internal site key) to check **VotingPlugin's local processing**. Verify the reward/total; this command does **not** test the public listener.
3. From the voting website, send a **real or listener-generated test vote** using the same player name. Verify that VotifierPlus received it, VotingPlugin logged it with the expected `ServiceSite`, and the reward was delivered.
4. If the website delivers a different service name, correct `ServiceSite` before retesting.

See [Verify Your First Vote](/VotingPlugin/Getting-Started-Verification) for example messages and a troubleshooting table.

## 5. Finish safely

- Once **all intended sites** exist and work, set `AutoCreateVoteSites: false` in VotingPlugin's `Config.yml` and reload. This stops unexpected, unknown service identifiers from creating new site entries.
- In **7.1.1**, temporarily re-enable `AutoCreateVoteSites` before adding a new site **through `/av gui`**; direct `VoteSites.yml` editing still works when disabled. See [Service Sites](/VotingPlugin/Service-sites).
- Back up your configurations and test both online and offline rewards before making more complex changes.
- Move on to [Reward Examples](/VotingPlugin/Reward-Examples) or [VoteShop](/VotingPlugin/voteshop).

**Next:** [First-vote verification](/VotingPlugin/Getting-Started-Verification) · [Getting Started index](/VotingPlugin/Getting-Started)
