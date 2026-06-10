# Project Manager Scenario Fixtures

This folder contains repeatable project-management tasks for estimating token use across ordinary knowledge-work patterns. Each numbered folder is designed to be started in a fresh session and measured afterwards from the usage report.

## How to run one scenario

1. Open a new session.
2. Paste the prompt from that scenario's `README.md`.
3. Attach or point the agent at the files in the same folder.
4. Do not give extra clarifications unless the scenario asks for a follow-up variant.
5. After completion, record the total tokens, cached tokens, elapsed time, tool calls, and whether the output would be usable by a project manager.

## Context Variants

Run each scenario at one of these levels:

- `S`: Only the scenario prompt and files in that folder.
- `M`: Scenario prompt, files, and one organisational style rule such as "write for a senior sponsor, keep it under 400 words".
- `L`: Scenario prompt, files, organisational style rule, and a reusable project background paragraph from `shared-project-background.md`.
- `XL`: Same as `L`, plus ask the agent to inspect the public template file included in the folder before producing the answer.

## Source Policy

Downloaded examples are kept in `_sources/` and copied into scenario folders when useful. The working data inside each scenario is synthetic, but modelled on normal project artefacts: messy notes, meeting fragments, task exports, change requests, and stakeholder updates. This keeps the test realistic without embedding private material.

## Scenario Index

- `PM1-weekly-status-brief`: turn mixed weekly notes and a task export into a concise sponsor update.
- `PM2-meeting-prep-pack`: prepare a meeting brief from agenda notes, background, and a sample minutes format.
- `PM3-transcript-to-actions`: extract decisions, actions, risks, and unresolved questions from a transcript.
- `PM4-risk-register`: build or update a risk register from project notes and an open project-log template.
- `PM5-stakeholder-update-email`: draft segmented stakeholder updates from status notes and a communications-plan template.
- `PM6-task-triage`: prioritise a noisy task list and produce a next-week execution plan.
- `PM7-project-plan-from-brief`: turn a rough project brief into a project plan outline.
- `PM8-compare-proposals`: compare two supplier proposals against evaluation criteria.
- `PM9-change-request-impact`: assess scope, time, cost, risk, and comms impact of a proposed change.
- `PM10-lessons-learned`: synthesize a closure note from retrospective notes and an incident log.

