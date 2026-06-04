# Continuation Prompt

Use this prompt to continue work on the **Using AI Agents for Reproducible Research** workshop repository.

Before using it, edit the sections marked `EDIT IF NEEDED`.

## Copy-Paste Prompt

```text
FOR ME

Continue work in this repository:

/Users/dominiklukes/gitrepos/15_training-presentations/agents-for-reproducibility

Context:

This is the public materials repository for the full-day in-person workshop "Using AI Agents for Reproducible Research". The workshop is for researchers, research students, and research support staff. The main teaching example is Codex as an agent that works with local project folders, files, commands, Git, GitHub, documentation, simple scripts, reusable project instructions, and Agent Skills.

The repository is already cloned locally and pushed to GitHub:

https://github.com/techczech/agents-for-reproducibility

Current known state:

- Latest pushed commit from the previous work session: 9120af1, "Align workshop timing and setup materials".
- `planning/session-outline.md` now has the agreed 9.30 start time and a full-day outline with timings.
- `participant/setup-checklist.md` now has a more participant-ready setup checklist.
- `planning/decision-log.md` records the 9.30 start and the decision to treat Cloudflare/external-service work as conditional.
- `admin/next-steps.md` lists the remaining work queue.

Important constraints:

- Follow `AGENTS.md`.
- Write for workshop participants first, then for colleagues helping to run the session.
- Keep internal planning separate from participant-facing instructions.
- Use British spelling.
- Keep the tone sober, practical, and clear. Avoid hype.
- Do not include private paths, private transcript URLs, participant data, API keys, secrets, or sensitive research material in public workshop materials.
- Keep sample data fictional and clearly marked as fictional.
- Treat reproducibility as documentation, versioning, logging, review, shareable outputs, and human-checkable traces.
- Before committing, run `git status --short` and `git diff --check`.
- If committing, add an agent co-author trailer.

EDIT IF NEEDED: Choose the next work slice.

Default next slice:

Build the Codex Explorer exercise.

Goal:

Turn `exercises/codex-explorer/README.md` from a scaffold into a usable hands-on exercise that helps participants distinguish:

- what the language model contributes,
- what local files contribute,
- what command-line tools contribute,
- what the orchestration harness contributes,
- what the researcher must still check.

Preferred shape:

- Keep it simple enough for a mixed-experience room.
- Use the existing fictional sample project where possible.
- Make the exercise usable even if GitHub, Cloudflare, or external services are not working.
- Include participant instructions and facilitator notes.
- Add any repo-map or next-steps updates needed.

Alternative slices if I ask for one:

1. Polish `participant/setup-checklist.md` into final participant setup copy.
2. Turn `exercises/agent-skills/README.md` into a tested hands-on skill-building exercise.
3. Test and improve `exercises/sample-project/participant-tasks.md`.
4. Decide and document the fallback path for participants who cannot connect GitHub, Cloudflare, or external services.
5. Decide whether `exercises/website/` should become the published workshop page.

How to start:

1. Run `git status --short --branch`.
2. Read `AGENTS.md`, `README.md`, `planning/session-outline.md`, `admin/next-steps.md`, and the files relevant to the chosen slice.
3. Make a short plan.
4. Implement the chosen slice directly.
5. Validate with `git diff --check`.
6. Summarise changed files and remaining open decisions.

Do not ask me broad questions before inspecting the repo. Ask only if a missing choice would materially change the work.
```

## Editable Notes For Dominik

Change these before pasting the prompt if the next session should go in a different direction.

- Next slice:
- Deadline or timebox:
- Must-have output:
- Things to avoid:
- Whether to commit and push:

## Current Best Next Slice

Build the Codex Explorer exercise.

Reason:

The current workshop spine depends on participants understanding that Codex is not "just a chatbot". The Codex Explorer exercise is the bridge between the conceptual introduction and the hands-on project work. It is also currently the least developed core exercise.

## Useful Local Files

- `AGENTS.md`
- `README.md`
- `planning/session-outline.md`
- `planning/key-concepts.md`
- `planning/decision-log.md`
- `admin/next-steps.md`
- `participant/setup-checklist.md`
- `exercises/codex-explorer/README.md`
- `exercises/sample-project/participant-tasks.md`
- `exercises/sample-project/README.md`
- `exercises/agent-skills/README.md`
- `exercises/reproducible-analysis/README.md`

## Recent Work Completed

- Repo cloned locally from `techczech/agents-for-reproducibility`.
- Full-day outline updated with 9.30 start, breaks, checkpoints, and local-only fallback paths.
- Participant setup checklist made more realistic and less brittle.
- Admin next steps updated so already-settled timing work is no longer listed as open.
- Decision log updated with timing and conditional-path decisions.

## Open Decisions

- What exact Codex Explorer activity to use.
- How much of the day should depend on GitHub account readiness.
- Whether Cloudflare publishing should be live, demonstrated only, or optional.
- Whether Sketch Engine via MCP is worth the setup risk for the first pilot.
- How much facilitator support will be available in the room.
