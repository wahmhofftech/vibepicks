# New AI tool releases for builders
> Verified AI tool and model launches that matter to people shipping apps, newest first, each with its source link. Curated by VibePicks.

Page: https://vibepicks.ai/releases/
RSS: https://vibepicks.ai/releases/feed.xml
JSON Feed: https://vibepicks.ai/releases/feed.json
Last updated: 2026-11-07

## 2026-11-07: OpenCode Browse
OpenCode Browse is an MCP server and Chromium extension that lets coding agents drive your real browser — including signed-in tabs and extensions — in background tabs, then hands the tab back to you for a login, 2FA prompt or payment
- Category: coding-agents
- Source: https://opencode.ai/product/browse

## 2026-11-06: Claude Code
Claude Code 2.1.319 backgrounds MCP tool calls that run as tasks instead of waiting inside the turn, adds permissions.denyInsteadOfPrompting so unattended runs deny a permission prompt and continue, and adds /claude-api latency-optimize
- Category: coding-agents
- Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.319

## 2026-11-06: Cursor
Cursor now lets you talk with your agents in a realtime voice call, in the Agents Window, the IDE, on web and in Cursor for iOS: describe a change out loud, the voice agent hands coding work to the agent in your chat, and it speaks short progress notes while it works. Powered by Grok Voice, and separate from dictation
- Category: coding-agents
- Source: https://cursor.com/changelog/voice-chat

## 2026-11-06: Vercel AI Gateway
Vercel AI Gateway now offers DeepSeek Search (page titles, URLs and summaries) and DeepSeek Fetch (page content as Markdown) for any tool-calling model behind one AI Gateway API key, with no separate DeepSeek account. Each costs $0.75 per 1,000 billable requests; failed, timed-out and empty results have no tool charge
- Category: llm-apis
- Source: https://vercel.com/changelog/ai-gateway-adds-deepseek-search-and-fetch-tools

## 2026-11-06: GitHub Copilot
You can now manage GitHub Copilot code review settings through the REST and GraphQL APIs, from enterprise policy down to individual repositories, and Copilot's review overview comment is more compact. Available on Copilot Pro, Pro+, Max, Business and Enterprise
- Category: code-review
- Source: https://github.blog/changelog/2026-11-06-copilot-code-review-api-management-and-review-overview-updates/

## 2026-11-06: OpenCode
OpenCode v2.2.6 lets MCP servers share one connection across projects with pool: true, adds opencode run -w to start a session in a new git worktree, and --archived so scripted and CI sessions stay out of your inbox
- Category: coding-agents
- Source: https://github.com/anomalyco/opencode/releases/tag/v2.2.6

## 2026-11-06: OpenRouter
OpenRouter rebuilt its Auto Router and added Auto Code (openrouter/auto-code), a router tuned for coding harnesses that picks a model per request; OpenRouter says it scores in line with Claude Opus 5.5 at 74% lower cost per task
- Category: llm-apis
- Source: https://openrouter.ai/blog/announcements/auto-and-auto-code-routers/

## 2026-11-06: GitHub Copilot
@GitHub in Slack and Microsoft Teams is generally available: investigate bugs, create issues and open pull requests from a chat, with Canvas in Teams for reviewing plans, diffs and previews alongside the conversation
- Category: coding-agents
- Source: https://github.blog/changelog/2026-11-06-github-copilot-in-slack-and-teams-is-generally-available/

## 2026-11-06: Vercel Tracing
Vercel Tracing is generally available on all plans: a new Traces page with KQL search, vercel traces search in the CLI, tracing on by default for new Next.js 16.5 projects, and longer retention (3 days Hobby, 14 days Pro)
- Category: hosting
- Source: https://vercel.com/changelog/vercel-tracing-is-now-generally-available

## 2026-11-06: Replit Agent
Replit Agent can now troubleshoot platform problems in chat by checking incidents, docs and known issues, and on Pro it files the support ticket for you with debugging details attached
- Category: app-builders
- Source: https://docs.replit.com/updates

## 2026-11-05: Codex CLI (OpenAI)
Codex CLI 0.167.0 opens an agent command center with codex agents --no-daemon, marks unread results, lets you switch backends without losing drafts, and adds a Google Cloud Vertex AI setup wizard
- Category: coding-agents
- Source: https://github.com/openai/codex/releases/tag/rust-v0.167.0

## 2026-11-05: Cursor
Cursor can now build live apps and share them with a link: describe the tool you want, and Cursor scaffolds the web app, sets up a Postgres database and auth behind Cursor SSO when needed, runs deterministic and agentic security checks, and deploys to a URL you pick. Available on all paid plans with cloud agents enabled
- Category: coding-agents
- Source: https://cursor.com/changelog/build-live-apps

## 2026-11-05: Kiro
Kiro bots are generally available in Kiro Crew: named, long-running agents with their own memory, notes, tools and permissions that coordinate parallel worker sessions, keep a single ongoing chat for direction and results, and can run on schedules for recurring work like issue triage, build monitoring or release readiness
- Category: coding-agents
- Source: https://kiro.dev/blog/crew-bots/

## 2026-11-05: Evergreen
Carta released Evergreen for other companies: a multiplayer cloud coding platform where teammates and agents share sessions, agents push PRs on their own, and it runs on Claude, Codex, Grok and Muse with isolated sessions, scoped access, audit logs and spending caps. 7-day free trial
- Category: coding-agents
- Source: https://evergreen.carta.com/blog/introducing-evergreen

## 2026-11-05: Vercel Schedules
Vercel Schedules is in public beta on all plans: define recurring or one-time schedules in vercel.json or at runtime that target a private Function, HTTP path or Queue topic, enable/disable/run on demand without redeploying. Successor to Cron Jobs; Hobby includes 5,000 runs/month, Pro/Enterprise from $5 per 1M runs
- Category: hosting
- Source: https://vercel.com/changelog/vercel-schedules-is-now-in-public-beta

## 2026-11-05: Gemini Omni 1.2 Flash
Google's Gemini Omni 1.2 Flash is on Vercel AI Gateway as google/gemini-omni-1.2-flash: generate 3–15 second videos with native audio from text (or edit source clips with up to six reference images) via one API key with no separate Google account, using generateText or streamText in the AI SDK
- Category: ai-video
- Source: https://vercel.com/changelog/gemini-omni-1-2-flash-now-available-on-ai-gateway

## 2026-11-05: Kimi Hosted Agents
Moonshot AI launched Kimi Hosted Agents, a managed Harness-as-a-Service for long-running and multi-agent workloads: isolated cloud sandboxes, network controls, stoppable sessions, audit logs, 140+ Skills and 30+ plugins, plus finance Agent templates. Sign up at platform.kimi.com; usage-based pricing (sandbox-hours plus model tokens and plugin calls)
- Category: automations
- Source: https://www.kimi.com/news/kimi-hosted-agents

## 2026-11-04: Devin
Cognition released SWE-2 Flash, a smaller coding model (276B total, 12B active parameters) that runs at about 200 tokens a second, 3x faster than SWE-2 at one-fifth the price, and scores 89.9 on SWE-Bench Pro v2 Hard against SWE-2's 90.6. It's available now in Devin Desktop and the Devin CLI; weights aren't public yet, only through a planned partner program
- Category: coding-agents
- Source: https://cognition.com/blog/swe-2-flash

## 2026-11-04: Atlassian Code Reviewer
Atlassian Code Reviewer is generally available with paid Jira and Teamwork Collection plans: an AI agent that reviews pull requests in Bitbucket Cloud and GitHub (GitLab coming), leaves inline comments with fixes you can apply, and checks each PR against the acceptance criteria in its linked Jira work item. It starts in manual mode (reviews only when the author asks) and uses Rovo credits
- Category: code-review
- Source: https://www.atlassian.com/blog/development/code-reviewer

## 2026-11-04: GitHub Copilot
GitHub Copilot now works inside Xcode's built-in coding assistant, in public preview from Xcode 27.3 beta on macOS Tahoe 26.6 or later. Turn it on in Xcode > Settings > Intelligence; every Copilot plan is supported, and the separate Copilot for Xcode extension still works
- Category: coding-agents
- Source: https://github.blog/changelog/2026-11-04-github-copilot-is-now-available-in-xcodes-coding-assistant/

## 2026-11-04: Lovable
Lovable now runs "Dreaming" on paid plans: in the background it checks its project memory and your AGENTS.md rules against your code and chat, then rewrites or removes notes that no longer apply, while keeping rules you asked for. It never touches your app's code, shows AGENTS.md edits in chat and version history, and uses no credits
- Category: app-builders
- Source: https://docs.lovable.dev/changelog

## 2026-11-03: Claude Code
Claude Code 2.1.318 shows when your stored claude.ai sign-in expires (claude auth status and claude -p JSON) and warns in claude -p output 10 days before it ends, lets a mod's side job run at low effort, and fixes --continue losing earlier conversation, macOS sessions stalling with many Bash commands, and keys typed right after sending a message answering permission prompts. It also stops auto-installing the IDE extension from IDE terminals
- Category: coding-agents
- Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.318

## 2026-11-03: Vercel Security Review
Vercel Security Review is in public beta for Pro and Enterprise teams: every push to a connected GitHub repo (including direct pushes to production) gets an AI scan of the changed code for issues like missing auth checks or exposed secrets, with findings in a Vulnerabilities dashboard, a GitHub check and PR comments. Vercel Agent can open a fix PR, or pull findings into your own coding agent with vercel security vulnerabilities. Reviews are free until Nov 10, 2026, then billed at the Vercel Agent token rate
- Category: hosting
- Source: https://vercel.com/changelog/vercel-security-review-public-beta

## 2026-11-03: Vercel CLI
vercel doctor checks your Vercel CLI version and install, login, team, project link and vercel.json, reports Vercel status incidents, and prints the exact command that fixes each problem. It never prompts or logs in, and --json gives structured output, so coding agents can run it before guessing at a fix
- Category: hosting
- Source: https://vercel.com/changelog/vercel-cli-now-diagnoses-setup-problems-with-vercel-doctor

## 2026-11-03: Tencent Hy4
Tencent's Hy4, the first Hy model with vision and computer use, is on Vercel AI Gateway as tencent/hy4 at 50% off through Dec 31, 2026 (about $0.42 in / $1.25 out per million tokens): 1M-token context, tool calling, structured outputs and image input, and usable from Claude Code, Codex or Cursor via the gateway
- Category: llm-apis
- Source: https://vercel.com/changelog/tencent-hy4-now-available-on-ai-gateway

## 2026-11-03: GitHub Copilot
GitHub Copilot now works inside JetBrains Air: pick Copilot in Air's agent picker to delegate tasks on your existing Copilot subscription, track several agent sessions in parallel and review changes next to your code, or run cloud tasks in isolated containers through Air Teams billed to your Copilot plan rather than JetBrains AI credits
- Category: coding-agents
- Source: https://github.blog/changelog/2026-11-03-github-copilot-is-now-available-in-jetbrains-air/

## 2026-11-03: Replit Agent
Replit Agent now works in Slack: mention @Replit in a channel or DM to build a prototype, work on an existing project, ask questions about your codebase or pull data from connected tools like Linear and Notion; each thread is its own Replit chat and uses the linked user's own permissions
- Category: app-builders
- Source: https://x.com/Replit/status/2117689305019887899

## 2026-11-03: Bolt
Bolt for Microsoft Teams is live on the Microsoft Marketplace: describe what you want inside Teams or Copilot, get a build plan, and ship the app without leaving the chat
- Category: app-builders
- Source: https://x.com/boltdotnew/status/2117648022737682467

## 2026-11-02: Claude Code
Claude Code 2.1.317 now asks before a web or shell tool call sends your account email address out, warns when a new /schedule cloud task picks up connectors you did not ask for, and lets Agent SDK hooks use onFailure: "block" so a failing check stops the action instead of letting it run. It also fixes project MCP servers dropping after the first turn in some desktop sessions and claude auth status signing you out after a slow token refresh
- Category: coding-agents
- Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.317

## 2026-11-02: Vercel
Vercel now blocks known-malicious npm package versions before and during dependency installs on every plan, with no setup: it checks your lockfile (including cached dependencies) and stops bad downloads, so a poisoned install script can't run in your build. If one is found the deploy fails and names the package and version; bump it, update the lockfile and redeploy
- Category: hosting
- Source: https://vercel.com/changelog/blocking-malicious-npm-packages-before-and-during-installation

## 2026-11-02: Vercel
Projects can now be configured with vercel.toml, which takes every setting vercel.json does but allows comments and has a flatter layout. Use only one config file per project: vercel.toml, vercel.json or vercel.ts
- Category: hosting
- Source: https://vercel.com/changelog/projects-can-now-be-configured-with-vercel-toml

## 2026-11-02: Vercel MCP
Vercel MCP now shows your deployments as a live card inside ChatGPT and other chat apps that support MCP Apps, with build status, build logs, commit details and a Visit button, so you can paste logs into the chat and debug a failed deploy with the model without opening the dashboard
- Category: hosting
- Source: https://vercel.com/changelog/monitor-vercel-deployments-in-chatgpt

## 2026-11-02: LongCat 2.5 (Meituan)
Meituan's LongCat 2.5, a model built for coding agents and image-based programming with a 1M-token context and text plus image input, is now on Vercel AI Gateway as meituan/longcat-2.5, so you can try it in Claude Code, Codex or Cursor through one AI Gateway key without opening a Meituan account
- Category: llm-apis
- Source: https://vercel.com/changelog/longcat-2-5-now-available-on-ai-gateway

## 2026-11-02: Supabase CLI
Supabase CLI v3.0.0 is a major release: commands like db push, db pull, gen types and storage now target your local stack by default, one --remote flag replaces --linked, --project-ref and --db-url, and every change to a hosted project asks for confirmation, with No as the default answer (pass --yes in CI or agent runs). Read the v2 to v3 migration guide before upgrading scripts. It also points to the experimental local stack that gives each project, git worktree or agent its own local Supabase, with or without Docker
- Category: databases
- Source: https://github.com/supabase/cli/releases/tag/v3.0.0

## 2026-10-31: DeepSeek dsh-superagent
DeepSeek open-sourced dsh-superagent (MIT), a research prototype of a proactive coding agent for one GitHub repository: when an allowed person asks for work in an issue thread (or optionally Feishu), it opens a work item, does the job in its own session and directory and answers back, often with a pull request, plus a web panel for what needs a human. It runs as a DeepSeek Harness bundle; DeepSeek says it is not an official product, so try it on a side repo
- Category: coding-agents
- Source: https://github.com/deepseek-ai/dsh-superagent-prototype

## 2026-10-30: Claude Code
v2.1.316 adds CLAUDE_CODE_SUBAGENT_EFFORT, so subagents that only search and read files can run at a lower effort level than your main session instead of inheriting it, plus CLAUDE_CODE_DISABLE_ULTRATHINK to turn the ultrathink keyword off. Fast mode for Opus 4.8 is deprecated and will be removed on November 30, 2026, after which those requests error instead of falling back; Anthropic says to move to Opus 5.5
- Category: coding-agents
- Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.316

## 2026-10-30: OpenCode
OpenCode v2.2.3 lets you use Claude Code inside OpenCode: install Claude Code, run claude auth login, then pick Claude Agent in /connect to use your Claude Code login and models. v2.2.4 and v2.2.5 the same day added persistent desktop terminals, experimental HTML artifact publishing and a compaction buffer you can set as a percentage of the model's context window
- Category: coding-agents
- Source: https://github.com/anomalyco/opencode/releases/tag/v2.2.3

## 2026-10-30: Claude (Anthropic)
Anthropic renamed its Max plans: Max 5x is now just Max ($100/month) and Max 20x is now Ultra ($200/month), with no change in price and nothing for subscribers to do. Verified Ultra accounts also lose the 5-hour usage limit, starting with most existing subscribers; newer accounts keep a temporary limit until verified, and weekly limits stay the same. Claude Code is included in Pro, Max and Ultra
- Category: coding-agents
- Source: https://x.com/claudeai/status/2116220869479428500

## 2026-10-30: Gemini API
The Gemini API's Computer Use tool is generally available in both the Interactions and GenerateContent APIs, so you can build agents that operate a browser, phone or desktop app by clicking and typing, now with production support instead of preview
- Category: llm-apis
- Source: https://ai.google.dev/gemini-api/docs/changelog

## 2026-10-30: Supabase
Explorer, the new Supabase query editor, runs SQL against both your database and your logs in one place, and Notebooks save those queries plus Markdown notes as a file in your supabase folder that you, a teammate or your coding agent can rerun (supabase notebooks pull/push in the beta CLI). Feature preview on every project: turn it on under Feature Previews
- Category: databases
- Source: https://supabase.com/blog/explorer-and-notebooks-investigations-your-team-can-rerun

## 2026-10-30: Vercel
Data Cache is leaving beta and merging into Runtime Cache: Next.js fetch caching and unstable_cache switch over with no code changes and get 8x more storage on Pro, but reads and writes that were free become billed (from $0.40 per million reads and $4 per million writes). Hobby gets 1M reads and 200K writes free a month and migrates November 29, 2026; new teams use Runtime Cache from today
- Category: hosting
- Source: https://vercel.com/changelog/data-cache-is-moving-to-runtime-cache

## 2026-10-30: Convex
Convex 1.49.0 adds npx convex plugins install, which installs the Convex plugin for Claude Code and Codex (CLI, desktop apps and VS Code) on macOS and Linux, plus a v.function() validator for function handles. It drops Node.js 20, so update to Node 22 or newer
- Category: databases
- Source: https://github.com/get-convex/convex-js/blob/main/CHANGELOG.md

## 2026-10-29: Mistral Large 4 (Mistral AI)
Mistral released the open weights of Mistral Large 4 (Le Chonk), its 1-trillion-parameter multimodal model, after extra training that Mistral says makes it the top open-weight model on FrontierCode and Terminal-Bench 4.0 (41%) while using about 47% fewer tokens per task than GLM-5.3. It adds Low, Medium and High reasoning modes. Use it in Mistral Studio, the Mistral API or OpenRouter, or download the weights from Hugging Face and run it with vLLM or SGLang; benchmarks are Mistral's own
- Category: llm-apis
- Source: https://mistral.ai/news/mistral-large-4-oss/

## 2026-10-29: Codex CLI (OpenAI)
Codex CLI 0.166.0 adds keyboard transcript selection and search in the terminal UI, GPT-6.1 Terra in the bundled, Vertex AI and Amazon Bedrock model lists, codex queue --resume to pick unloaded threads back up, and codex doctor --network-only for quick connection checks
- Category: coding-agents
- Source: https://github.com/openai/codex/releases/tag/rust-v0.166.0

## 2026-10-29: Claude Code
v2.1.314 adds permissions.blockWritesOutsideWorkingDirectories: turn it on and Claude Code's Write and Edit tools refuse any file outside your project folders in every permission mode, a good safety net for unattended or CI runs. Also: claude -p now exits with an error instead of silently succeeding when startup fails, and long idle chats in VS Code and the desktop Code tab get compacted
- Category: coding-agents
- Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.314

## 2026-10-29: Google Jules
Google is shutting down Jules, its background AI coding agent, to fold the idea into Antigravity: you can keep finishing sessions until November 11, then Jules goes read-only and winds down December 31, 2026. Export your settings, environment variables, scheduled tasks, memories, setup scripts and session history first with the Jules Tools CLI (npm install -g @google/jules); your code, branches and pull requests stay in GitHub
- Category: coding-agents
- Source: https://jules.google/docs/changelog/2026-10-29/

## 2026-10-29: Google Antigravity
Antigravity now has a Plugin Marketplace in the Antigravity app and CLI: one-click plugins that bundle skills, MCP servers, rules, hooks and custom agents, so you no longer wire up each MCP server by hand. Launch partners include Atlassian, Canva, Datadog, Dropbox, Figma, Stripe and Unity, plus a Vercel plugin
- Category: coding-agents
- Source: https://antigravity.google/blog/plugin-marketplace-in-antigravity/

## 2026-10-29: Factory Droid
Factory released Droid 1.0, a rebuilt coding-agent harness whose default Script mode lets the model write a small sandboxed JavaScript program that runs many tool calls in one request instead of one call at a time. Factory says that cuts cost about 15% on Claude Opus 5.5 and turned one 312-call cleanup into 2 requests; its benchmark wins are self-reported. On desktop, CLI and an SDK
- Category: coding-agents
- Source: https://factory.com/news/frontier-harness

## 2026-10-29: OpenCode
OpenCode v2.2.1 adds /goal: give the session an objective and it keeps working until an automatic review confirms it is done, with /goal pause, resume and clear. Also new: opt-in scheduled prompts (/schedule), an opt-in image_generate tool, live background-shell output in Desktop and a redesigned model picker
- Category: coding-agents
- Source: https://github.com/anomalyco/opencode/releases/tag/v2.2.1

## 2026-10-29: Vercel
Node.js 26 LTS is generally available on Vercel for builds and Functions and is now the default for new projects. Built-in fetch uses HTTP/2 by default (set VERCEL_FETCH_DISABLE_H2=1 to keep HTTP/1.1), and you get the Temporal date API. Existing projects move to 26 on the next deploy if engines.node allows it, e.g. >=20
- Category: hosting
- Source: https://vercel.com/changelog/node-js-26-lts-is-now-generally-available-on-vercel

## 2026-10-29: Vercel
Vercel Firewall can now treat AI crawlers (bots that collect pages for indexing and model training) and AI assistants (bots fetching a page to answer someone's question) separately, so you can block training crawlers but still let ChatGPT-style assistants read and cite your site. In the AI Bots managed ruleset, on all plans
- Category: hosting
- Source: https://vercel.com/changelog/block-ai-crawlers-and-assistants-independently-with-managed-rules

## 2026-10-28: GitHub Copilot
Copilot Memory is generally available on paid Copilot plans: tell Copilot a preference once (like how to start your PR descriptions) or let it learn your repo's test command, and it carries that across the Copilot app, CLI, VS Code, cloud agent and code review. Copilot Dreaming, in public preview, reviews past sessions and proposes changes to your skills and instruction files as pull requests
- Category: coding-agents
- Source: https://github.blog/changelog/2026-10-28-github-intelligence-puts-your-code-context-and-history-to-work/

## 2026-10-28: Vercel
Vercel CI is in beta for Turborepo repos: tag tasks like lint or test with ci in turbo.json and they run on every push, only for code that changed, with remote caching and dependencies installed once per run. Vercel says its own push-to-green time got 2 to 6 times shorter
- Category: hosting
- Source: https://vercel.com/changelog/vercel-ci-is-now-in-beta

## 2026-10-28: GitHub Replica
GitHub Design open-sourced Replica (MIT license), an AI prototyping tool that turns plain-English ideas into interactive prototypes built from your own design system's components, driven from the GitHub Copilot app, with an optional self-hosted Replica Hub for sharing and comments
- Category: design-to-code
- Source: https://github.blog/changelog/2026-10-28-introducing-replica-an-open-source-ai-prototyping-tool/

## 2026-10-28: GitHub Copilot
Copilot Fusion is generally available: pick Fusion in the model picker and Copilot routes and combines models for each task instead of you choosing one, with Standard, High and Max effort levels. GitHub says Fusion Max scored within two points of Claude Code with Opus 5.5 Max on the Artificial Analysis Coding Agent Index at about half the cost. On all Copilot plans in VS Code, the Copilot app, Copilot CLI and JetBrains
- Category: coding-agents
- Source: https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion/

## 2026-10-28: GitHub Copilot
Copilot cloud sessions now follow you everywhere: start a cloud agent task on github.com, GitHub Mobile, Copilot CLI, the Copilot app, VS Code, Slack or Teams and pick it up on any of the others while it keeps running in a cloud sandbox. Sandbox time can come out of your included Actions minutes. Generally available on paid Copilot plans, rolling out from Oct 28; Copilot Projects for multi-repo goals are in public preview
- Category: coding-agents
- Source: https://github.blog/changelog/2026-10-28-work-from-anywhere-with-a-new-connected-copilot-cloud-experience/

## 2026-10-28: GitHub Agentic Workflows
GitHub Agentic Workflows is generally available: write an automation (issue triage, CI failure analysis, docs updates, test writing) as a plain-English Markdown file and it compiles to a normal GitHub Actions workflow run by Copilot or your own coding agent, read-only by default and sandboxed. On GitHub Free, Team and Enterprise; the default Copilot CLI engine needs a Copilot license
- Category: automations
- Source: https://github.blog/changelog/2026-10-28-github-agentic-workflows-generally-available/

## 2026-10-28: Supabase
OrioleDB is in public beta on every Supabase plan: an open-source Postgres storage engine built for tables with lots of updates and deletes, cutting the table bloat and VACUUM tuning the default engine needs. Choose it when you create a project; billed like standard Postgres, backups and read replicas work, but not ready for production yet
- Category: databases
- Source: https://supabase.com/blog/orioledb-public-beta

## 2026-10-28: Vercel
The Vercel Plugin now works in OpenCode 2: install it with opencode plugin add github:vercel/vercel-plugin to get Vercel skills (AI SDK, Functions, Workflow), /vercel:deploy and /vercel:env commands, and the Vercel MCP server so the agent can see your projects, deployments and logs
- Category: hosting
- Source: https://vercel.com/changelog/vercel-plugin-now-available-in-opencode

## 2026-10-27: Supabase
Supabase Compute is in private alpha: run AI agents, background jobs and APIs (Node, Deno or any Dockerfile) inside your Supabase project, next to your Postgres data, for minutes or hours instead of the 400-second Edge Function limit. Deploy with supabase compute push (CLI v2.120.0+); free during the alpha, us-west-2 projects only, waitlist required and not for production yet
- Category: databases
- Source: https://supabase.com/blog/supabase-compute-private-alpha

## 2026-10-27: Replit
Replit Cloud Agents let anyone on a team describe a change in plain English, watch it in a live preview of the running app, and have the agent open a tested pull request on GitHub (or merge request on GitLab) that follows the team's guidelines and keeps fixing it as review comments come in. Engineers still approve what ships. Available now on Pro and Enterprise
- Category: app-builders
- Source: https://replit.com/blog/anyone-can-bring-ideas-to-company-codebase

## 2026-10-27: Cursor
Cursor design mode adds Annotate: give the agent visual prompts by editing elements, drawing right on the page, and reviewing your design at different screen sizes
- Category: coding-agents
- Source: https://x.com/cursor_ai/status/2115159585548021814

## 2026-10-27: Gemini API
Google released the Gemini API CLI (gemini-api) in beta, a stateless, zero-dependency command-line client built for AI coding agents, scripts and CI pipelines. It uses the Interactions API to generate text and media, analyze files and run Gemini managed agents
- Category: llm-apis
- Source: https://ai.google.dev/gemini-api/docs/changelog

## 2026-10-27: Ramp Inspect
Ramp opened early access to Inspect, the cloud coding agent its own teams use: hand it a task from Slack, GitHub, Linear, the web or your phone (even a screenshot with "@inspect fix this") and it returns a visually checked, reviewed pull request. Sessions are multiplayer so teammates can jump in and steer. Ramp says it now writes 74% of the company's merged PRs
- Category: coding-agents
- Source: https://ramp.com/blog/introducing-inspect

## 2026-10-27: Vercel
Vercel Observability now shows AI traffic: requests by each verified AI bot, the pages AI crawlers hit most, pages AI assistants fetch in answer to a user's question, Markdown requests, and pages that return errors to bots. Find it under Observability > AI Traffic; querying it from the CLI with vercel metrics needs Observability Plus
- Category: hosting
- Source: https://vercel.com/changelog/ai-traffic-insights-now-available-in-vercel-observability

## 2026-10-27: OpenCode
OpenCode v2.2.0 adds experimental desktop plugins you can create, install and share, a refreshed desktop app, experimental image-generation APIs for plugins, keyed session instructions that survive compaction without busting the prompt cache, and prompt-cache lifetimes you can set per provider and model. Heads-up: the OpenCode GitHub Action is no longer published, so remove it from your workflows
- Category: coding-agents
- Source: https://github.com/anomalyco/opencode/releases/tag/v2.2.0

## 2026-10-26: GPT-6.1 Terra (OpenAI)
OpenAI released GPT-6.1 Terra, a fast, lower-cost model for computer use, visual reasoning and writing. On the API as gpt-6.1-terra at $1 per million input tokens and $5 per million output (half the price of GPT-6.1 Sol), with a 1M-token context; also in ChatGPT and Codex for paid plans, and generally available in GitHub Copilot
- Category: llm-apis
- Source: https://openai.com/index/introducing-gpt-6-1-terra/

## 2026-10-26: Cursor
Cursor's Agent SDK is generally available: define an agent as a folder (instructions.md for the prompt, tools/ in TypeScript, skills, MCP connections), test it with built-in evals, and deploy it to Cursor with agent-sdk deploy or run it on your own servers. Agents can wake on GitHub, GitLab or Bitbucket events, Slack messages, webhooks or a schedule
- Category: coding-agents
- Source: https://cursor.com/blog/agent-sdk

## 2026-10-26: GitHub Copilot
Assisted permissions are generally available in Copilot CLI, the Copilot app and VS Code: an AI model checks each command, file path or URL Copilot asks to use, lets clearly safe ones run, and still asks you about the rest. It's a middle ground between approving everything by hand and Allow All
- Category: coding-agents
- Source: https://github.blog/changelog/2026-10-26-github-copilot-assisted-permissions-generally-available/

## 2026-10-26: Claude Code
v2.1.311 fixes long sessions stopping with "Usage credits required for 1M context" past 200K tokens (it now compacts and keeps going), fixes multi-thousand-line edits stalling for up to 5 seconds, lets subagents use MCP servers that connect late, and typing ultrathink mid-turn now raises effort for the rest of that turn
- Category: coding-agents
- Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.311

## 2026-10-26: Entire
Former GitHub CEO Thomas Dohmke's Entire launched a Git hosting platform built for coding agents: Trails replace pull requests with agent-scored checks on every push, Continuous Memory saves agent sessions into the repo so agents can search past work, and Buildkite and Depot handle CI. Open to every developer today, with private repos only for now
- Category: code-review
- Source: https://entire.com/news/entire-launches-an-independent-git-forge-for-agent-human-collaboration

## 2026-10-26: Gemini API
New paid-tier projects now store Generate Content API requests by default (store=true), matching the Interactions API; opt out per request with store=false or in Logs and Datasets settings
- Category: llm-apis
- Source: https://ai.google.dev/gemini-api/docs/changelog

## 2026-10-26: Vercel
Faster pnpm installs: dependency verification is reused across deployments, cutting average install time 14% on Pro, automatic on all plans
- Category: hosting
- Source: https://vercel.com/changelog/faster-pnpm-installs

## 2026-10-26: Replit
Replit now works fully in Japanese, from the interface to prompts and agent output
- Category: app-builders
- Source: https://x.com/Replit/status/2114587332137664535

## 2026-10-25: Cloudflare WAF
Cloudflare added two emergency Managed Ruleset rules for the Node.js Brotli decoder flaw CVE-2026-111497 (memory leak or code execution when decoding attacker-controlled Brotli data): one matches Brotli-encoded request bodies, one matches the Next.js image optimizer path /_next/image. Both default to Log, not Block. If you self-host Next.js or any Node app, upgrade Node.js to 22.23.4, 24.22.1 or 26.12.1
- Category: hosting
- Source: https://developers.cloudflare.com/changelog/post/2026-10-25-emergency-waf-release/

## 2026-10-23: Vercel Connect
Vercel Connect can now create a separate restricted Stripe API key for each agent or task (Managed API Key method), limited to the permissions you pick, so an agent never holds your full-access secret key. Vercel stores the key, and you can rotate it without redeploying
- Category: payments-email
- Source: https://vercel.com/changelog/vercel-connect-adds-managed-stripe-api-keys

## 2026-10-23: GitHub Copilot
The new GitHub app for Microsoft Teams combines notifications with Copilot: @mention GitHub on a bug report in a channel or chat and it investigates, fixes the bug and opens a pull request for review. The legacy app is renamed GitHub (deprecated) and retires November 16
- Category: coding-agents
- Source: https://github.blog/changelog/2026-10-23-turn-notifications-into-code-with-github-copilot-in-teams/

## 2026-10-23: Cursor
Cursor agents can now control your computer: Computer Use lets them click and type across desktop apps, not just the browser, such as driving the iOS Simulator to test the features they build. Cursor uses it on its own when a task needs it, or you can @-mention Computer Use; update Cursor to get it
- Category: coding-agents
- Source: https://x.com/cursor_ai/status/2113661506634305834

## 2026-10-23: Kimi K3.1 Pro (Moonshot AI)
Moonshot AI released Kimi K3.1 Pro, a 2.8T-parameter MoE model (104B active) with a 1M-token context and image input, aimed at full-project coding and long agent runs. It is live on the Kimi API and Vercel AI Gateway (moonshotai/kimi-k3.1-pro, plus a faster Highspeed version), with open weights planned by November 4
- Category: llm-apis
- Source: https://vercel.com/changelog/kimi-k3-1-pro-and-kimi-k3-1-pro-highspeed-are-available-now-in-ai-gateway

## 2026-10-23: Replit
Replit launched Monitoring Agent, an on-call agent that investigates production issues from your app's logs and metrics, then attempts and validates fixes (with optional auto-fix and experimental auto-republish). Also new: Agent-made reusable skills, chat and asset sharing, Stripe Atlas incorporation at 20% off, and published apps that keep running at zero credits for eligible top-up customers
- Category: app-builders
- Source: https://docs.replit.com/updates/2026/10/23/changelog

## 2026-10-23: Chroma
Chroma, the open-source vector database, signed a deal to join Replit. Chroma Cloud is winding down: writes stop November 22, 2026 and reads stop December 22, 2026, so cloud users need to export and migrate. Open-source ChromaDB stays Apache 2.0
- Category: databases
- Source: https://www.trychroma.com/blog/chroma-joins-replit

## 2026-10-23: Codex CLI
Codex CLI 0.164.0 lets you save reusable prompts and slash commands in ten numbered /presets slots, set the model and permissions inline with /model and /permissions, preview images in the terminal, and mask credentials in remote Bash commands
- Category: coding-agents
- Source: https://github.com/openai/codex/releases/tag/rust-v0.164.0

## 2026-10-23: TanStack AI
TanStack AI hits 1.0 with stable core APIs: an open-source, no-lock-in toolkit for adding chat, tools, MCP, media and agents to your app, with 23 provider adapters, eight UI frameworks and a new experimental agent harness
- Category: llm-apis
- Source: https://tanstack.com/blog/tanstack-ai-1-0

## 2026-10-22: Vercel CLI
You can now deploy to Vercel without an account: run vercel deploy --temporary (or point it at a single file) to get a shareable tmp.now URL for a prototype. Temporary deployments expire after one hour unless you open the claim link and sign in
- Category: hosting
- Source: https://vercel.com/changelog/deploy-without-an-account-using-vercel-cli

## 2026-10-22: Amp
You can now self-host Amp orbs: run amp orb provider on your own machines (Docker, E2B, Modal, Vercel Sandbox, Daytona or Kubernetes) so agents run inside your own network; free for individuals and teams, and free for every workspace until Oct 29
- Category: coding-agents
- Source: https://ampcode.com/news/self-hosted-orbs

## 2026-10-22: Agent Skills
Anthropic donated Agent Skills, the open SKILL.md standard used by 70+ agent platforms including ChatGPT, Cursor, GitHub Copilot and VS Code, to the Linux Foundation's Agentic AI Foundation, so skills you write stay vendor-neutral
- Category: coding-agents
- Source: https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation

## 2026-10-22: OpenAI Decisions API
The Decisions API is now generally available: you define a question and its allowed answers and get fast, low-cost classification, routing and next-action picks for apps and agents, up to 10x faster than GPT-6 Luna through the Responses API, now with prompt caching, JSON and image inputs and up to 400 questions per request
- Category: llm-apis
- Source: https://openai.com/index/decisions-api/

## 2026-10-22: Cloudflare Agents SDK
Agents SDK v0.30.0 runs PiHarness on Pi 1.4, so agents can hibernate while tasks sleep, park tasks that keep crashing, and recover from storage errors and cut-off model streams; the upgrade can't be rolled back past Pi 1.4
- Category: hosting
- Source: https://developers.cloudflare.com/changelog/post/2026-10-22-pi-harness-pi-1-4/

## 2026-10-21: Recursive Flint
Recursive released Flint, a free Apache 2.0 coding model that runs on a laptop (40B mixture-of-experts, about 2.5B active), downloadable on Hugging Face so you can code offline and keep your code private
- Category: coding-agents
- Source: https://techcrunch.com/2026/10/21/recursive-launches-flint-a-laptop-coding-model-it-says-was-largely-built-by-ai/

## 2026-10-21: GemDB Code
GemDB launched GemDB Code, a free VS Code extension where your code is the database schema, so a coding agent can change objects without writing migrations; Python only at launch, with a built-in MCP server for plain-English data questions
- Category: databases
- Source: https://www.businesswire.com/news/home/20261021228398/en/GemDB-Makes-Code-the-Schema-Eliminating-Database-Migration-Bottlenecks-to-Accelerate-AI-Driven-Development

## 2026-10-21: Cloudflare Agents SDK
New createAI function in the agents package gives the AI SDK one provider for Workers AI models, AI Gateway catalog models, dynamic routes and vendor models, with fallbacks, caching and stream resume; workers-ai-provider and ai-gateway-provider are now deprecated
- Category: hosting
- Source: https://developers.cloudflare.com/changelog/

## 2026-10-20: OpenAI API
You can now choose 12-hour prompt caching in the Responses API, so shared instructions, tools and context stay cached at the lower cached-input rate even when requests are hours apart; 12-hour cache writes cost 2.5x the input token price
- Category: llm-apis
- Source: https://developers.openai.com/api/docs/changelog

## 2026-10-20: Vercel
WebSocket support in Vercel Functions is now generally available, for AI chat, streaming and realtime multiplayer apps, at the same limits and pricing as other Function invocations (CPU billed only while processing messages)
- Category: hosting
- Source: https://vercel.com/changelog/websocket-support-is-now-generally-available

## 2026-10-20: Supabase
Your coding agent can now query your Supabase logs, and a new Supabase skill points it to the signals to watch: error spikes, security issues, slow queries and growing usage, on a schedule you choose
- Category: databases
- Source: https://x.com/supabase/status/2112578077872050470

## 2026-10-19: Claude Code
v2.1.304 adds /auto-mode-setup, a guided setup that reads your project and recent sessions to teach auto mode about your setup, warns Pro and Max users when resuming an old conversation would use a noticeable share of their 5-hour limit, and fixes claude --worktree deleting a worktree and its branch at exit without asking, which could lose commits
- Category: coding-agents
- Source: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md

## 2026-10-19: Mercury 3 (Inception)
Inception's Mercury 3, a diffusion LLM that writes 1,000+ tokens per second with a 1M-token context, is live on Inception's OpenAI-compatible API (new keys get 100M free tokens) and on OpenRouter, Baseten and Vercel AI Gateway; launch price is $0.10/$0.35 per million tokens, 50% off its $0.20/$0.70 list price
- Category: llm-apis
- Source: https://www.inceptionlabs.ai/blog/introducing-mercury-3

## 2026-10-19: Cloudflare Workers AI
Clairic, a new extraction model in preview on Workers AI (@cf/cloudflare/clairic), pulls typed values like invoice totals, dates and lists out of text or up to four images, with a confidence score on every answer, for $0.10 per million input tokens and no output charge; open weights are planned
- Category: hosting
- Source: https://developers.cloudflare.com/changelog/post/2026-10-19-clairic-workers-ai/

## 2026-10-19: MiniMax M3.1 Flash
MiniMax's new fast model for coding, agent work and visual reasoning (74% on DeepSWE) is live on the MiniMax API at a flat $0.15/$0.60 per million tokens, about 1/3 the cost of M3 at 3x the speed; open weights arrive Oct 23
- Category: llm-apis
- Source: https://x.com/MiniMax_AI/status/2112150867868541221

## 2026-10-18: Vercel
AI Gateway logs now have a Sessions view that groups requests by conversation and shows which coding agent ran it (Claude Code, Codex, Cursor), plus its cost, models and cache hit rate
- Category: hosting
- Source: https://vercel.com/changelog/ai-gateway-logs-now-show-session-affinity

## 2026-10-17: Replit
OpenAI is now the preferred partner powering Replit Agent's default experience, CEO Amjad Masad says; Replit stays model-agnostic, so you can still pick Anthropic's Claude and other supported models
- Category: app-builders
- Source: https://x.com/amasad/status/2111494912562888939

## 2026-10-17: DeepSeek API
DeepSeek-V4.1-Flash-1017 now powers the deepseek-flash API model (open weights on Hugging Face), and DeepSeek's Search and Fetch web APIs are open to all developers at $0.75 per 1,000 calls
- Category: llm-apis
- Source: https://api-docs.deepseek.com/news/news261017

## 2026-10-16: Claude Code
v2.1.302 turns on fork subagents by default in claude -p, the Agent SDK, the desktop app and VS Code (CLAUDE_CODE_FORK_SUBAGENT=0 turns them off), adds an idle-compaction toggle in /config, and warns that standalone Claude Design (claude.ai/design) closes by December 14, 2026
- Category: coding-agents
- Source: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md

## 2026-10-16: Amp
You can now see and control your macOS or Linux runner's desktop from Amp, handy for trying native apps (like iOS apps) that Amp builds for you; turn on Share This Mac's Display or run amp --no-tui --desktop
- Category: coding-agents
- Source: https://ampcode.com/news/runner-desktop

## 2026-10-16: Glimpse (Elorian)
New visual-reasoning model that keeps re-checking images and video while it thinks (it can crop, pull frames and run code); research preview with API access at $0.60/$3 per million tokens, also on OpenRouter
- Category: llm-apis
- Source: https://elorian.ai/blog/introducing-glimpse

## 2026-10-16: ChatGPT
ChatGPT Slides: build a deck from a chat, files or an outline, edit it with teammates in real time, present from ChatGPT, or export to PowerPoint, PDF or Google Slides; rolling out to Pro, Business and Enterprise users with Space access
- Category: writing
- Source: https://help.openai.com/en/articles/6825453-chatgpt-release-notes

## 2026-10-16: Beam (Reflection)
Beam, a 501B-parameter (23B active) open-weight model for coding and agents, is out under Apache 2.0 with the open-source Mirror CLI; free to start on Reflection's API and also on OpenRouter, Vercel, Ollama and other partners
- Category: llm-apis
- Source: https://reflection.ai/blog/beam-is-available

## 2026-10-16: Cursor
Cloud agents can now build interactive canvases (dashboards, reports) you share with a link; Environments API in beta; cloud environments now hold up to 300 repos and large ones load 5x faster
- Category: coding-agents
- Source: https://cursor.com/changelog/cloud-agent-canvases-and-environments

## 2026-10-16: Junie Local (JetBrains)
JetBrains' free on-device coding agent runs on NVIDIA RTX Spark at launch, and Windows support is now stable on RTX cards with 24 GB+ VRAM: no token bill, and your code never leaves the machine
- Category: coding-agents
- Source: https://blog.jetbrains.com/junie/2026/10/junie-local-rtx-spark/

## 2026-10-16: Google AI Studio
Google AI Pro subscribers can now build apps with Gemini 4 Argon in AI Studio Build and the playground
- Category: app-builders
- Source: https://x.com/GoogleAIStudio/status/2111240722426802258

## 2026-10-16: HeyGen
HeyGen Video 1, its video generation model, is now available in the HeyGen MCP server, so you can ask your AI agent for a video and get it back in seconds
- Category: ai-video
- Source: https://x.com/HeyGenDev/status/2111151435778039811

## 2026-10-16: Clerk
New Agents section in your Clerk app config with setup for adding auth to your MCP server, plus a ready-made agent prompt for building a new MCP server
- Category: auth
- Source: https://x.com/clerk/status/2111193502587752702

## 2026-10-15: Claude Code
Code Review is generally available on Claude Team and Enterprise: automatic reviews on new GitHub pull requests, about 3x faster than the preview (6-10 minutes), with Quick, Standard or Deep review levels per repo
- Category: code-review
- Source: https://claude.com/resources/articles/code-review-is-now-generally-available

## 2026-10-15: Claude API (Anthropic)
Fast mode for Claude Opus 5.5 is out of research preview: up to 2.5x faster output, no waitlist or beta header, $8/$40 per million tokens
- Category: llm-apis
- Source: https://platform.claude.com/docs/en/release-notes/overview

## 2026-10-15: Neon
Neon Realtime in public beta: subscribe to any read-only SQL query and your app updates live, with React hooks and a coding-agent skill; free during beta
- Category: databases
- Source: https://neon.com/blog/neon-now-has-realtime

## 2026-10-15: Figma
Code layers enter open beta (code-backed prototypes on the canvas, all plans), plus Specs for Markdown context you can hand to coding agents via Figma MCP
- Category: design-to-code
- Source: https://www.figma.com/blog/build-by-design/

## 2026-10-15: Nemotron 3.5 (NVIDIA)
Open 120B Nemotron 3.5 Super VL (text, image, video; up to 1M context) and Bolt 74B-A9B, a local agent model that fits in 24GB; on Hugging Face and OpenRouter
- Category: llm-apis
- Source: https://blogs.nvidia.com/blog/nemotron-3-5-super-vl/

## 2026-10-15: FLUX 3 Image Klein (Black Forest Labs)
Open-weights 5.6B image model with native 4K and up to 10 reference images; runs on consumer GPUs, API from $0.009 per 1K image
- Category: ai-images
- Source: https://bfl.ai/blog/flux-3-image-klein

## 2026-10-15: Krea 3
New image editing model: most edits under 8 seconds at native 2K, keeps products and characters consistent; $0.06 per 2K image, also on fal, Replicate and OpenRouter
- Category: ai-images
- Source: https://www.krea.ai/blog/introducing-krea-3

## 2026-10-15: Attie (Bluesky)
Bluesky's Attie now lets anyone describe and build small shareable sites, games, quizzes and polls with no code, with Bluesky sign-in built in
- Category: app-builders
- Source: https://techcrunch.com/2026/10/15/bluesky-expands-its-ai-powered-attie-app-to-let-anyone-build-websites-games-and-more/

## 2026-10-15: Muse Spark Open (Meta)
Open-weight version of Muse Spark for self-hosted agentic coding, 1M context
- Category: llm-apis
- Source: https://dev.meta.ai/resources/blog/build-with-muse-spark-open

## 2026-10-13: Gemini 4 Argon (Google)
Google's newest frontier model is now available to developers via the paid Gemini API tier and AI Studio
- Category: llm-apis
- Source: https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-4-argon/

## 2026-10-13: GitHub Copilot
Gemini 4 Argon now generally available in Copilot (Pro+, Max, Business, Enterprise)
- Category: coding-agents
- Source: https://github.blog/changelog/2026-10-13-gemini-4-argon-in-github-copilot/

## 2026-10-12: Muse Wonder (Meta)
New model on Muse Code and Meta Model API at $4/$20 per million tokens
- Category: llm-apis
- Source: https://dev.meta.ai/resources/blog/build-with-muse-wonder

All categories: https://vibepicks.ai/llms.txt
Full directory: https://vibepicks.ai/llms-full.txt
