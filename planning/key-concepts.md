# Key Concepts

## Model

The language model is the component that interprets instructions and generates text or code. In the workshop, participants should distinguish what comes from the model from what comes from the surrounding agent environment.

## Agent

An agent is a tool-using system that can work across files, commands, and tasks. Codex is the main example for this workshop.

## Orchestration Harness

The orchestration harness is the surrounding system that gives the model access to tools, permissions, files, commands, and feedback loops.

## Local Project Folder

The local project folder is the unit of reproducible work. It should contain the sources, documentation, scripts, outputs, and records needed to inspect or repeat the process.

## AGENTS.md

`AGENTS.md` describes how the agent should behave in a project. In this workshop, it is used to require good research habits: read before editing, do not change raw data, log decisions, name sources, preserve scripts, and record uncertainty.

## Agent Skills

Agent Skills are reusable instruction packages that help an agent carry out a repeated workflow. They are useful when a research practice should be repeatable across projects rather than written into one project's `AGENTS.md`.

The standard unit is a skill folder with a required `SKILL.md` file. `SKILL.md` contains YAML frontmatter with a clear `name` and `description`, followed by concise Markdown instructions. A skill can also include optional `scripts/`, `references/`, and `assets/` folders for reusable code, supporting documentation, and templates or files used in outputs.

In this workshop, skills are presented as a way to package reproducible practices: for example, how to create a data inventory, prepare a decision log, summarise sources without inventing evidence, or run a simple analysis while preserving inputs, scripts, outputs, and assumptions.

## Git

Git records changes to files over time. Used well, it can function as a practical record of research project states.

## GitHub

GitHub provides remote hosting for Git repositories. In the workshop, it supports backup, sharing, and visibility.

## Cloudflare

Cloudflare is used as an example of publishing a simple static output or documentation site from a project folder.

## Command-Line Tools

Command-line tools let agents use traditional computing infrastructure. This is one of the key differences between a chatbot interaction and an agentic workflow.

## MCP and External Services

MCP servers and command-line tools can connect an agent to external services such as Sketch Engine. The first pilot should include a simple, reliable example of this.

## Reproducible Analysis

A reproducible analysis should preserve the inputs, script, outputs, and decisions so that a researcher can inspect what happened later.
