# Agent Instructions

This repository contains planning notes, participant materials, exercises, and a static website draft for the workshop **Using AI Agents for Reproducible Research**.

## Working Principles

- Write for workshop participants first, then for colleagues helping to run the session.
- Keep the tone sober, practical, and clear. Avoid hype and overclaiming.
- Use British spelling.
- Keep internal planning separate from participant-facing instructions.
- Do not include private source paths, archive locations, internal provenance notes, or sensitive information in workshop materials.
- Treat reproducibility as a practice made of documentation, versioning, logging, review, and shareable outputs.
- Use Codex as the main workshop agent unless a planning note says otherwise.
- Keep sample data fictional and clearly marked as fictional.
- Do not add real participant data, sensitive research material, secrets, API keys, or private account details.

## Repository Shape

- `README.md` is the repository entry point.
- `planning/` holds workshop design notes, page copy, session outlines, decisions, and repository structure.
- `participant/` holds participant-facing setup and workshop materials.
- `docs/page-source/` holds Markdown source for the GitHub Pages activity guide.
- `docs/index.html` is generated from `docs/page-source/activities.md` by `tools/build-github-pages.py`.
- `exercises/` holds workshop activities, the fictional sample project, and the static website draft.
- `admin/` holds operational notes that are not participant-facing.

## Editing Rules

- Prefer Markdown for planning and participant materials.
- Keep file names lowercase and hyphenated.
- Record workshop design decisions in `planning/decision-log.md`.
- Do not hand-edit generated website output once a generator exists; update the source and rerun the generator instead.
- Before committing, run `git status --short` and `git diff --check`.
