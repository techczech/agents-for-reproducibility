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

## Skills

Skills are reusable instructions or procedures that help an agent carry out a repeated workflow. The workshop will introduce the idea of skill files as a way to make reproducible practices easier to repeat.

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
