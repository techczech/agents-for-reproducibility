# Versioning A Project With Git And GitHub

This exercise shows how Git can make project work easier to inspect and repeat. GitHub is optional. If GitHub access is not ready, the local Git history is still a useful outcome.

## Before You Start

Use only the workshop sample project or another non-sensitive folder.

Do not use confidential, identifiable, restricted, or embargoed research data.

## Ask Codex

Start with this prompt:

> Initialise Git in this sample project, show me the current status, make a first commit, and explain what has been saved. Before committing, show me what files will be included.

Codex may run commands like:

```bash
git init
git status --short
git diff --check
git add .
git commit -m "Initial project record"
git log --oneline -3
```

## What To Check

Ask Codex:

> Explain the Git history in plain language. Which files are now part of the project record, and which files should I review before doing more work?

Look for:

- a clear first commit,
- no sensitive files,
- no accidental temporary files,
- a short explanation of what changed.

## Optional GitHub Step

Use this only if you have a working GitHub account and are comfortable creating a private test repository.

Ask Codex:

> Check whether GitHub CLI is available and authenticated. If it is, create a private GitHub repository for this workshop project and push the first commit. If it is not, explain the local-only fallback.

Codex may run commands like:

```bash
gh --version
gh auth status
gh repo create <your-test-repo-name> --private --source=. --remote=origin --push
git remote -v
```

Do not run or ask for:

```bash
gh auth status --show-token
```

## Fallback

If GitHub is not ready, stop after the local Git commit.

The important reproducibility point is that the project now has a visible local history. GitHub adds sharing and backup, but it is not required for the exercise.
