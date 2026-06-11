# Explore `AGENTS.md` In A Sample Project

This exercise shows how project instructions shape an agent's behaviour.

Use the fictional `project-management-sample-project/` folder from the workshop sample files.

## Open The Folder

Open this folder in Codex:

```text
sample-files/project-management-sample-project/
```

Before asking for output, inspect the folder yourself. Notice:

- `AGENTS.md`
- `CLAUDE.md`
- `_TASK-LOG/`
- `_CHANGELOG/`
- `_AGENT-INSTRUCTIONS/`
- `source-material/`
- `outputs/`
- `notes/`

## Ask Codex

Start with this prompt:

> Read the project instructions and source material in this folder. Create an HTML project-status report in `outputs/` that explains the current change request, the available evidence, the main risks, the missing information, and the recommended next decision. Do not invent facts that are not in the source material.

## What To Check

Ask Codex:

> Which project instructions affected your work?

Look for:

- whether it read `AGENTS.md`,
- whether it avoided editing `source-material/`,
- whether it saved output in `outputs/`,
- whether it recorded uncertainty,
- whether it used `_TASK-LOG/` or `_CHANGELOG/` only for the right kind of record.

## Why This Matters

`AGENTS.md` is project context that follows the folder. It helps the agent remember what the project is for, what it should create, what it should not touch, and how to leave a trace.

This is different from a reusable `SKILL.md`. `AGENTS.md` belongs to one project. A skill packages a repeated workflow so it can be used across projects.
