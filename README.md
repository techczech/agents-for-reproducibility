# Using AI Agents for Reproducible Research

This repository contains the workshop materials, planning notes, participant setup, exercises, fictional sample project, and website draft for **Using AI Agents for Reproducible Research**.

The workshop introduces AI agents as practical tools for making research work easier to inspect, repeat, document, and share. Codex is the main example because it can work with ordinary project folders, files, commands, Git, GitHub, publishing tools, reusable project instructions, and Agent Skills.

## Workshop Abstract

This workshop introduces the use of AI agents to help researchers produce more reproducible research workflows from data management to data analysis - for both qualitative and quantitative data. Using Codex as the main example of a coding agent, it will show how agents fit into ordinary computer work and how they can make documentation, data management, versioning, reusable agent instructions, and dissemination practices easier to apply consistently.

Participants will learn the difference between the language model inside an agent and the surrounding computing infrastructure: files, folders, command-line tools, Git, GitHub, cloud services, external tools, `AGENTS.md`, and Agent Skills. The workshop shows how to use Codex to organise research materials, inspect data, create project documentation, and set up instructions that ask the agent to log decisions, preserve evidence, reuse tested workflows, and support reproducibility throughout the research process.

The workshop is suitable for researchers, research students and research support staff who work with documents, transcripts, spreadsheets, notes, or small datasets. No programming experience is required, but participants should be comfortable working with files and folders on their own laptop and should install Codex before attending.

## What Participants Will Do

- Set up a local research-project folder.
- Use Codex to inspect, organise, and document fictional research materials.
- Create project instructions in `AGENTS.md`.
- Create a small Agent Skill using the standard `SKILL.md` structure.
- Record decisions, uncertainties, source files, scripts, and outputs.
- Put the project under version control with Git and GitHub.
- Publish a simple documentation output.
- Try a small data-analysis task with saved inputs, code, outputs, and notes.
- Discuss which parts of their own research workflows are suitable for agent support.

## Current Session Plan

The first version is planned as a full-day, in-person workshop. The day gives participants time to install and use Codex, work with a sample project, write project instructions, create a small Agent Skill, use Git and GitHub, publish a simple output, connect to an external tool where appropriate, and complete a small reproducible analysis exercise.

See [planning/session-outline.md](planning/session-outline.md) for the current structure.

## About the Facilitator

Dominik is an AI Consultant at the Oxford e-Research Centre and part of the University's AI Competency Centre. His work connects applied AI, academic practice, linguistics, education technology, accessibility, and research workflows. He designs practical training and tools that help researchers use generative AI with clearer documentation, evidence, and review.

More at [dominiklukes.net](https://dominiklukes.net).

## Prepare Before the Workshop

Participants should bring a laptop with working internet access and permission to install or use software. They should install Codex, install or confirm Git, create or confirm access to a GitHub account, and avoid using sensitive, confidential, identifiable, restricted, or embargoed research data during the exercises.

See [participant/setup-checklist.md](participant/setup-checklist.md) for the setup checklist.

## Repository Structure

```text
agents-for-reproducibility/
  README.md                         # Repository entry point
  AGENTS.md                         # Instructions for agentic tools working in this repo
  planning/                         # Workshop design, page copy, concepts, decisions
  participant/                      # Participant-facing setup and materials
  sample-files/                     # Downloadable sample file bundles
  exercises/                        # Exercises, fictional sample project, website draft
  admin/                            # Operational planning notes
```

## Core Materials

- [Workshop page copy](planning/workshop-page.md)
- [Session outline](planning/session-outline.md)
- [Participant setup checklist](participant/setup-checklist.md)
- [Git and GitHub exercise](participant/git-github-exercise.md)
- [Cloudflare publishing exercise](participant/cloudflare-publishing-exercise.md)
- [Workshop sample files](sample-files/)
- [Key concepts](planning/key-concepts.md)
- [Exercise folder](exercises/)
- [Agent Skills exercise](exercises/agent-skills/)
- [Fictional sample project](exercises/sample-project/)
- [Project-management sample project](sample-files/project-management-sample-project/)
- [Static website draft](exercises/website/)
