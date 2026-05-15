# Participant Tasks

Work through these tasks with Codex. The aim is not to get the agent to produce a perfect answer. The aim is to make the research process visible and to see how Codex combines a language model with files, folders, command-line tools, versioning, and external services.

## 1. Inspect the Project

Ask Codex to inspect the folder and list:

- what files exist
- what each file appears to contain
- what documentation is missing
- what it should not edit

## 2. Improve the README

Ask Codex to improve `README.md` using only the files in the project. It should not invent extra data, participants, dates, or findings.

## 3. Complete the Data Inventory

Ask Codex to fill in `docs/data-inventory.md` from the files in `data/raw/`.

## 4. Create Project Instructions

Ask Codex to draft or revise `AGENTS.md` so that it supports reproducible work. It should include instructions about:

- reading before editing
- not changing raw data
- logging decisions
- naming source files
- saving scripts and outputs
- recording uncertainty

## 5. Create a Versioned Project

Ask Codex to initialise a Git repository, make a first commit, and explain what has been saved. If GitHub access is available, ask Codex to prepare or carry out the GitHub sync.

## 6. Publish a Simple Output

Ask Codex to create a simple documentation page or website from the project materials. If Cloudflare access is available, ask Codex to prepare the project for publication through Cloudflare.

## 7. Try an External-Service Workflow

Use a facilitator-provided example to show how Codex can work with a command-line tool or MCP server. The first pilot may use Sketch Engine if the setup is ready, or a simpler command-line service if that is more reliable.

## 8. Run a Small Data-Analysis Task

Ask Codex to inspect `data/raw/survey-responses.csv` and propose a small script that counts tool-use categories and concern categories. Save the script in `scripts/` and any output in `outputs/`.

## 9. Produce a Short Report

Ask Codex to draft a short report in `outputs/short-report.md` that separates:

- what the materials show
- what remains uncertain
- what a researcher should check before using the findings

## 10. Record Decisions and Review the Trace

Ask Codex to update `notes/decision-log.md` with the choices made during the exercise.

Compare the project before and after the agent work. Identify what changed, why it changed, and which claims still need human review.
