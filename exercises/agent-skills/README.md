# Agent Skills Exercise

This exercise introduces Agent Skills as reusable instruction packages for research workflows.

## Purpose

Participants should learn that `AGENTS.md` describes how an agent should behave in one project, while an Agent Skill packages a reusable workflow that can travel across projects.

## Standard Structure

A minimal skill is a folder with a required `SKILL.md` file:

```text
skill-name/
  SKILL.md
```

`SKILL.md` should contain:

- YAML frontmatter with `name` and `description`
- concise Markdown instructions
- clear trigger guidance so the agent knows when to use the skill

A fuller skill can include:

- `scripts/` for reusable code
- `references/` for supporting documentation loaded only when needed
- `assets/` for templates or files used in outputs

## Workshop Task

Create a small skill for one reproducible research task, such as:

- creating a data inventory
- summarising sources without inventing evidence
- preparing a decision log
- running a small analysis while saving inputs, scripts, outputs, and assumptions

The skill should be short enough to inspect during the workshop. It should focus on what the agent needs to do the task, not on background explanation.
