# Agent Instructions

This repository is:

```text
/Users/dominiklukes/gitrepos/15_training-presentations/agents-for-reproducibility/
```

It is a standalone public planning and materials repository for the workshop **Using AI Agents for Reproducible Research**.

## Purpose

Use this repository to develop, organise, and publish workshop materials for organisers, facilitators, and participants. The workshop uses Codex as the main example of an AI agent and focuses on reproducible research workflows.

## What Is In This Repository

- `docs/publicity/` - public abstract and promotional copy for organisers.
- `planning/` - workshop outline, key concepts, decisions, and future session design.
- `facilitator/` - organiser and helper guidance.
- `participant/` - setup checklist and participant-facing materials.
- `exercises/` - workshop exercises and activity designs.
- `sample-project/` - fictional research project used during hands-on work.
- `website/` - future Cloudflare or static-site output.
- `admin/` - operational planning notes.

## Working Principles

- Keep the repository self-describing. Every top-level area should explain what it is for.
- Keep organiser-facing material separate from facilitator notes and participant exercises.
- Write in a sober, practical workshop tone. Avoid editorial openings, hype, and overclaiming.
- Treat reproducibility as a practice made of documentation, versioning, logging, review, and shareable outputs.
- Codex is the main workshop agent unless a planning note explicitly says otherwise.
- Do not use real participant data or sensitive research material in examples.
- Keep sample data fictional and clearly marked as fictional.
- Record decisions in `planning/decision-log.md` when they affect the workshop design.
- If adding generated outputs, make clear which files and prompts or instructions produced them.

## Editing Rules

- Prefer Markdown for all planning and participant materials.
- Use British spelling.
- Keep file names lowercase and hyphenated.
- Do not hand-edit generated website output once a generator exists; update the source instead.
- Do not add secrets, API keys, tokens, or private account details.
- Before committing, run:

```bash
git status --short
git diff --check
```

## Source Boundary

The source archive is:

```text
/Users/dominiklukes/gitrepos/15_training-presentations/dominiks-session-abstracts-archive/
```

Do not look in or reuse material from `codex-token-use-explorer` for this workshop.
