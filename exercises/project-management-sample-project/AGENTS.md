# Agent Instructions

## Project

- Mode: project management sample; content/training support.
- Audience: workshop participants exploring agent-ready project setup.
- Status: fictional, safe teaching project; source copied from PM9 change-request scenario.
- Task: assess an online-payments change request for a booking-workflow pilot.

## First Move

- Create/update `_TASK-LOG/` record before multi-step work.
- Read `source-material/` before drafting recommendations.

## Routing

- Source evidence: `source-material/`; never edit source files.
- Generated briefs/tables: `outputs/`.
- Human-readable working notes: `notes/`.
- Operational task state: `_TASK-LOG/`.
- Changes/decisions: `_CHANGELOG/` (project-changelog rules).
- Detailed agent procedure/cache: `_AGENT-INSTRUCTIONS/`.
- Hard-to-reverse decisions -> `docs/adr/` via `grill-with-docs` only if the sample grows beyond this exercise.

## Working Rules

- Treat all project data as fictional.
- Do not add real people, organisations, private paths, or external claims.
- Separate evidence, analysis, recommendation, and sponsor wording.
- Name insufficient evidence instead of filling gaps.
- Use British spelling.
- Keep participant-facing prose sober, practical, and clear.
- Change entries tag the decisions they touch; new durable decisions get a thin cross-link in `_CHANGELOG/decisions/`.

## Self-Healing

On user correction: classify, route, optionally promote.
Protocol: `_AGENT-INSTRUCTIONS/self-healing.md`.

## Verification

- `python3 _AGENT-INSTRUCTIONS/scripts/new-task.py "Task title"` creates task records.
- `python3 "$HOME/gitrepos/02_workskills/project-changelog/scripts/build_index.py" --changelog-dir _CHANGELOG` validates changelog entries.
- Before reporting done: `git diff --check` from the workshop repo root.
