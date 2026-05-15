# Using AI Agents for Reproducible Research

This repository contains the planning system and reusable workshop materials for **Using AI Agents for Reproducible Research**.

The workshop introduces the use of AI agents to help researchers produce more reproducible research workflows. Codex is the main example. The focus is on how agents combine language models with ordinary computing infrastructure: files, folders, command-line tools, Git, GitHub, Cloudflare, external services, and reusable project instructions.

## What Organisers Can Use Now

- [Public abstract](docs/publicity/abstract.md)
- [Organiser brief](facilitator/organiser-brief.md)
- [Participant setup checklist](participant/setup-checklist.md)
- [Session outline](planning/session-outline.md)
- [Key concepts](planning/key-concepts.md)

## Repository Structure

```text
agents-for-reproducibility/
  README.md                         # Public entry point for organisers and collaborators
  AGENTS.md                         # Instructions for Codex and other agentic tools
  CLAUDE.md                         # Companion instructions for Claude-style agents
  CLOUD.md                          # Cloud, publishing, and external-service notes
  docs/publicity/                   # Public-facing abstract and promotional copy
  planning/                         # Workshop design, outline, concepts, decisions
  facilitator/                      # Organiser and facilitator notes
  participant/                      # Participant setup and workshop-facing materials
  exercises/                        # Exercise designs to be developed
  sample-project/                   # Fictional research project used during the workshop
  website/                          # Future public website or Cloudflare output
  admin/                            # Planning checklists and operational notes
```

## Current Workshop Shape

The first pilot is planned as a full-day, in-person workshop with a smaller group and helper support. A 3-hour version can be developed later as a taster, but the full-day version is the right first pilot because it needs time for Codex setup, project instructions, Git/GitHub, Cloudflare publishing, command-line or MCP integration, and a reproducible data-analysis example.

The workshop is designed for researchers, research students, research support staff, and professional services colleagues. No programming experience is assumed, but participants should be comfortable working with files and folders and should install Codex before attending.

## Core Materials

- `docs/publicity/abstract.md` contains the sober registration-page abstract and 80-word version.
- `planning/session-outline.md` contains the current workshop outline.
- `planning/key-concepts.md` defines model, agent, orchestration harness, tools, `AGENTS.md`, Git, GitHub, Cloudflare, MCP, and reproducible analysis.
- `sample-project/` contains fictional research materials for workshop exercises.
- `participant/setup-checklist.md` lists what participants should install or create before the session.

## Source

This standalone repository was initialised from the planning material in:

```text
/Users/dominiklukes/gitrepos/15_training-presentations/dominiks-session-abstracts-archive/
```

Do not use `codex-token-use-explorer` as a source for this workshop. That was the wrong repository.
