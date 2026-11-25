---
title: VotingPlugin Control MCP
description: Connect Codex to a scoped Control grant and review a proposed vote-site change in the WebUI
published: true
date: 2026-11-25T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2026-11-25T00:00:00.000Z
---

# VotingPlugin Control MCP

> **Development builds only:** This guide uses [VotingPlugin Control v1.1.2](https://github.com/BenCodez/VotingPlugin-Control/releases/tag/v1.1.2) with a compatible VotingPlugin development build. The connector is present in development commit `d9d64569` and is unavailable in VotingPlugin 7.1.1. Installing the Control release alone does not add the connector to a 7.1.1 server.
{.is-warning}

Use this guide to let Codex read one named vote site on a backend and prepare a change for you to review. The agent can propose edits and follow their status. You approve and apply the proposal in the Control WebUI.

## Enable access and issue a grant

1. Follow the [Control WebUI guide](/VotingPlugin/Control-WebUI) to host Control and enroll a backend. In Control, confirm that the target backend is online and has accepted `config.files.v1` and `config.quick-setup.v1`.
2. Sign in as the Control owner and open **Access → Agent access**. Select **Enable MCP management**, then **Save MCP access**. Control defaults to disabled unless you opted in at startup or saved a preference. The saved setting takes effect immediately and takes precedence over `CONTROL_MCP_ENABLED`. Keep the Control data directory when upgrading so the setting is retained.
3. Enter the exact backend node ID. For this workflow, select **Discover**, **Read**, **Preview**, and **Track operations**. Leave other actions off. The grant applies to the selected actions on that backend; naming one site in your prompt does not restrict the grant to that site. Use a grant for an entire enrolled proxy network only if you intend to include that network.
4. Choose the shortest lifetime that works for the task. The form defaults to 60 minutes and accepts whole minutes, hours, or days up to 90 days. Select **Issue agent credential** and copy the token when it appears. Grant expiry is an upper limit: restarting Control invalidates its active grants even if they have time left.

## Connect Codex

On the machine running Codex, install Java 17 or newer, make sure `java` is on its PATH, and use a local copy of the Control JAR from the v1.1.2 release. Set `VP_CONTROL_MCP_ORIGIN` to the Control origin using verified HTTPS or literal loopback HTTP, such as `http://127.0.0.1:2150` when that is your local port. Set `VP_CONTROL_MCP_TOKEN` in the client's environment to the credential you just issued. Keep the value out of prompts, tool arguments, shell history, and checked-in configuration.

Add this to your local Codex configuration and replace the JAR path with the actual absolute path:

```toml
[mcp_servers.votingplugin-control]
command = "java"
args = ["-jar", "/absolute/path/votingplugin-control.jar", "mcp"]
env_vars = ["VP_CONTROL_MCP_ORIGIN", "VP_CONTROL_MCP_TOKEN"]
```

Start Codex with both variables available. Run `codex mcp list` to confirm the entry is configured, then ask Codex to list its authorized nodes to verify that the adapter can reach Control and the grant works. For other clients and optional tools, see the [Control v1.1.2 agent setup guide](https://github.com/BenCodez/VotingPlugin-Control/blob/v1.1.2/docs/agent-setup.md).

## Review and apply a vote-site change

1. Give Codex the exact backend node ID and the case-sensitive key under `VoteSites`. Ask it to read the current site and preview the intended change. This guided workflow targets one backend and the main `VoteSites.yml`. The existing and proposed vote URLs must use HTTP or HTTPS without embedded credentials, a query string, or a fragment. Use the existing administrator workflow for split files or sites with URLs that need those components.
2. Sign in to Control and open the returned review path or select **Activity → Review agent preview**. Check the target, the current and proposed values, and all changed paths. The guided preset proposes `DisplayItem.Amount: 1`. If you need to keep a different amount, use the existing administrator workflow.
3. Approve the preview in the browser only if the changes match your intent. Watch the operation until it reports a final result. If the file or node session changed, or the grant expired, obtain a fresh eligible preview and review it again.

## Troubleshoot or end access

| Symptom | What to check |
| --- | --- |
| Codex lists the MCP entry but cannot list nodes | Check that MCP management is enabled, the client inherited both environment variables, and the grant has not expired or been invalidated by a Control restart. |
| Codex can see other nodes but cannot preview on the target | Check the exact node ID, accepted backend capabilities, and the grant's scope and actions. A proxy grant does not automatically add newly reported backends. |
| The review is gone or cannot be approved | Check whether the grant was revoked or expired, or the underlying preview became stale. Request a new preview after correcting the cause. |

When finished, revoke the grant in **Access → Agent access**. Turning off MCP management there revokes all grants and blocks approval of their pending previews. Work you already approved can still complete. To use MCP again, enable it and issue a fresh grant.
