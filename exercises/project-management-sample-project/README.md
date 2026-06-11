# Sample Project: Change Request Impact Review

This fictional project is a small project-management workspace for the workshop **Using AI Agents for Reproducible Research**.

It shows how an agent-ready project can keep source material, working tasks, decisions, and change history separate. Participants can inspect the folder before asking an agent to produce a change-impact brief.

## Scenario

A service team is preparing a pilot booking workflow. The service owner has asked whether online payments should be added to the first pilot release.

The agent's job is not to invent missing evidence. It should assess the request against the available materials, name gaps, and produce a sponsor-ready recommendation.

## Suggested Participant Task

Ask the agent:

> Assess the change request against the baseline plan. Produce a decision summary, impacts, options with pros and cons, a recommended decision, and sponsor-ready wording. Be clear where the evidence is insufficient.

## Folder Guide

- `source-material/` contains the fictional source files copied from the PM9 scenario.
- `outputs/` is where generated briefs, tables, or sponsor wording should go.
- `notes/` holds working notes and human-readable decision notes.
- `_TASK-LOG/` records operational work, one resumable task at a time.
- `_CHANGELOG/` records meaningful changes, backlog items, and decisions.
- `_AGENT-INSTRUCTIONS/` holds agent-only procedures and helper scripts.
- `AGENTS.md` gives the short operational rules for agents entering this sample project.

## Reproducibility Rule

Do not overwrite the source material. Any assessment, recommendation, or decision must leave a trace in `outputs/`, `notes/`, `_TASK-LOG/`, or `_CHANGELOG/`.
