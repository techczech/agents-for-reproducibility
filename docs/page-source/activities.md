---
title: Using AI Agents for Reproducible Research
subtitle: Activity guide and workshop links
source: Presentation sequence from agents-for-research-reproducibility-outline.md
---

# Using AI Agents for Reproducible Research

This page is the practical activity guide for the workshop. It follows the slide sequence and gathers the links, folders, prompts, and checks participants need during the day.

Start here if you are in the room and need the shortest route through the activities.

## Getting Started

Use these links first.

- Public handout page: [dominiks-handouts.pages.dev/oa8c](https://dominiks-handouts.pages.dev/oa8c)
- Repository: [github.com/techczech/agents-for-reproducibility](https://github.com/techczech/agents-for-reproducibility)
- Download sample files: [workshop-sample-files.zip](https://github.com/techczech/agents-for-reproducibility/raw/main/workshop-sample-files.zip)
- Codex access check: [bit.ly/ox-codex-access](https://bit.ly/ox-codex-access)
- Participant setup checklist: [participant/setup-checklist.md](https://github.com/techczech/agents-for-reproducibility/blob/main/participant/setup-checklist.md)

Copy this if you are asking Codex to orient itself after opening a sample folder:

```text
Inspect this folder before making changes. Tell me what files are here, what they appear to contain, what you should not edit, and what you recommend doing first.
```

## Activity 1: Getting Ready

Time: 9:30-10:00

Goal: confirm that everyone can open Codex, find the sample files, and work in a safe folder.

Links:

- Setup checklist: [participant/setup-checklist.md](https://github.com/techczech/agents-for-reproducibility/blob/main/participant/setup-checklist.md)
- Sample files overview: [sample-files/README.md](https://github.com/techczech/agents-for-reproducibility/blob/main/sample-files/README.md)
- Zip download: [workshop-sample-files.zip](https://github.com/techczech/agents-for-reproducibility/raw/main/workshop-sample-files.zip)

Checklist:

- Open Codex.
- Download or extract the sample files.
- Use only fictional workshop material.
- Do not add real participant data, restricted research data, API keys, or private account information.

## Activity 2: How Agents Work

Time: 10:00-11:00

Goal: understand the difference between a chatbot and an agent before asking Codex to work on files.

Key ideas:

- A chatbot mostly responds to prompts and uploaded context.
- An agent can work in a loop with tools, files, commands, permissions, and feedback.
- Codex works in a local folder and can inspect or change files inside its sandbox.
- The chat is not the archive. Save sources, notes, instructions, scripts, outputs, and decisions into files.

Keep this question in mind:

```text
What did the model infer, what did it actually inspect, and what did the computer do?
```

## Activity 3: First Agent Task

Time: 11:00-11:15

Folder: `sample-files/messy-research-archive/`

Goal: use Codex to inspect a messy folder without immediately changing it.

Detailed handout: [participant/first-agent-task-messy-folder.md](https://github.com/techczech/agents-for-reproducibility/blob/main/participant/first-agent-task-messy-folder.md)

Copy this prompt:

```text
Inspect this folder and tell me what is in it. Group the files into likely categories, flag duplicates or confusing names, and suggest a safer folder structure. Do not move, rename, or edit files yet.
```

Check:

- Did Codex read files before making claims?
- Did it separate evidence from guesses?
- Did it propose changes before making them?
- Which permissions did you approve?

## Activity 4: Debrief Permissions

Time: 11:15-11:30

Goal: review what happened in the first task and connect it to reproducible work.

Copy this follow-up prompt:

```text
What did you inspect, what did you infer, and what would you change only after human approval?
```

Discuss:

- Which folder did Codex have access to?
- What did it do well?
- What did it assume?
- What should a researcher check before accepting its plan?
- What would have been risky in a real research folder?

## Activity 5: Project Instructions With AGENTS.md

Time: 11:30-12:30

Folder: `sample-files/project-management-sample-project/`

Goal: see how project instructions change what the agent does.

Detailed handout: [participant/project-management-agents-exploration.md](https://github.com/techczech/agents-for-reproducibility/blob/main/participant/project-management-agents-exploration.md)

Inspect these files and folders:

- `AGENTS.md`
- `CLAUDE.md`
- `_TASK-LOG/`
- `_CHANGELOG/`
- `_AGENT-INSTRUCTIONS/`
- `source-material/`
- `outputs/`
- `notes/`

Copy this prompt:

```text
Read the project instructions and source material in this folder. Create an HTML project-status report in outputs/ that explains the current change request, the available evidence, the main risks, the missing information, and the recommended next decision. Do not invent facts that are not in the source material.
```

Afterwards, ask:

```text
Which project instructions affected your work?
```

## Activity 6: From AGENTS.md To SKILL.md

Time: 12:00-14:15

Goal: distinguish project instructions from reusable skills.

Links:

- AGENTS.md site: [agents.md](https://agents.md/)
- Agent Skills overview: [AgentSkills.io](https://agentskills.io)
- Agent Skills exercise: [exercises/agent-skills/README.md](https://github.com/techczech/agents-for-reproducibility/blob/main/exercises/agent-skills/README.md)
- Public skill examples: [anthropics/skills](https://github.com/anthropics/skills)
- Public skill examples: [mattpocock/skills](https://github.com/mattpocock/skills)
- Dominik's public skills catalogue: [techczech/dominiks-agent-skills](https://github.com/techczech/dominiks-agent-skills)

Copy this prompt when you want Codex to propose a small skill:

```text
Suggest one small Agent Skill that would help with a repeated research task in this folder. The skill should be narrow, source-grounded, and useful across more than one project. Do not create files yet; first explain the trigger and the workflow.
```

## Activity 7: Git And GitHub

Time: 14:15-15:00

Goal: use Git as a visible project-history layer. GitHub is optional.

Detailed handout: [participant/git-github-exercise.md](https://github.com/techczech/agents-for-reproducibility/blob/main/participant/git-github-exercise.md)

Copy this prompt:

```text
Initialise Git in this sample project, show me the current status, make a first commit, and explain what has been saved. Before committing, show me what files will be included.
```

Commands you may see:

```bash
git init
git status --short
git diff --check
git add .
git commit -m "Initial project record"
git log --oneline -3
```

Optional GitHub prompt:

```text
Check whether GitHub CLI is available and authenticated. If it is, create a private GitHub repository for this workshop project and push the first commit. If it is not, explain the local-only fallback.
```

## Activity 8: Working With Data

Time: 15:15-16:00

Folder: `sample-files/research-data-for-replication/`

Goal: set up a small reproducible analysis with source data, instructions, code, outputs, and assumptions.

Links:

- Data folder README: [sample-files/research-data-for-replication/README.md](https://github.com/techczech/agents-for-reproducibility/blob/main/sample-files/research-data-for-replication/README.md)
- Reproducible analysis exercise: [exercises/reproducible-analysis/README.md](https://github.com/techczech/agents-for-reproducibility/blob/main/exercises/reproducible-analysis/README.md)

Copy this prompt:

```text
Inspect these CSV files, create a short data inventory, identify key variables and missing values, and propose one simple analysis that can be reproduced from the raw files. Save any code, outputs, and assumptions in separate files.
```

Check:

- Are inputs preserved?
- Is there a script?
- Are outputs saved separately?
- Are assumptions and uncertainties recorded?
- Can another person inspect what happened?

## Activity 9: Cloudflare Publishing

Time: 16:00-16:30, optional

Goal: publish a reviewed static output, not raw source material.

Detailed handout: [participant/cloudflare-publishing-exercise.md](https://github.com/techczech/agents-for-reproducibility/blob/main/participant/cloudflare-publishing-exercise.md)

Copy this prompt:

```text
Create a simple static documentation page from this sample project and save it in an output folder. Then explain which files would be published and which source files you used.
```

If Cloudflare and Wrangler are ready, use:

```text
Check whether Wrangler is available and whether Cloudflare authentication works. If it does, deploy the static output folder to a Cloudflare Pages test project. If it does not, keep the output local and record what would be needed.
```

Do not publish:

- raw source material by accident,
- real participant data,
- sensitive research data,
- API keys or account details.

## Activity 10: Safety, Cost, And Next Steps

Time: 16:00-16:30

Goal: connect the day back to real research practice.

Questions:

- What work is safe to do with fictional or public data?
- What would require ethics, data protection, or local policy review?
- What should stay local?
- What costs matter: money, time, attention, review effort, and risk?
- Which part of your own research workflow would benefit from agent support first?

Copy this reflection prompt:

```text
Based on what we did today, help me identify one low-risk research workflow where an agent could help. Include what files I would prepare, what instructions I would write, what outputs I would save, and what a human would still need to review.
```

## Extended And Backup Activities

Use these if setup varies across the room or you want more practice.

- Extended sample-project route: [exercises/sample-project/participant-tasks.md](https://github.com/techczech/agents-for-reproducibility/blob/main/exercises/sample-project/participant-tasks.md)
- External services exercise: [exercises/external-services/README.md](https://github.com/techczech/agents-for-reproducibility/blob/main/exercises/external-services/README.md)
- Static website draft: [exercises/website/README.md](https://github.com/techczech/agents-for-reproducibility/blob/main/exercises/website/README.md)
