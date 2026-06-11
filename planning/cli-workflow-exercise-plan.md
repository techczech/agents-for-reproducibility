# CLI Workflow Exercise Plan

This note surveys the command-line patterns worth teaching in the workshop and proposes a safe participant exercise sequence for Git, GitHub, sample bundles, and Cloudflare publishing.

## Summary

The workshop should teach a **small CLI ladder**, not the full maintainer workflow.

Participants should experience that Codex can:

- inspect the project state before changing files,
- initialise and explain a Git history,
- optionally connect a local folder to GitHub,
- build or package a simple output,
- optionally publish a static folder to Cloudflare Pages,
- record what was done and what remains local-only or account-dependent.

Your full workflow includes extra scaffolding such as backlog capture, repo registry habits, changelog/task-log conventions, co-author commit trailers, generated zip bundles, and Cloudflare deploy checks. Those are useful for facilitator preparation and advanced discussion, but they should not all become participant requirements.

## Observed Local Pattern

Current workshop repo:

- Remote: `https://github.com/techczech/agents-for-reproducibility.git`
- Branch: `main`
- Status pattern: `git status --short --branch`
- Review pattern: `git diff --check` before reporting or committing
- Commit pattern: clear message plus agent co-author trailer when the agent commits
- Bundle pattern: `zip -r -FS workshop-sample-files.zip sample-files -x "*/.DS_Store"`

Available CLI tools on this machine during the survey:

- `git` 2.39.5
- `gh` 2.93.0
- `wrangler` 4.90.0
- `node`, `npm`, `npx`
- `zip`, `unzip`

Wrangler did report its version, but also tried to write a log file under the user home, which the sandbox blocked. This is a useful reminder for the workshop: participants may see harmless environment-specific warnings, so instructions should describe expected outcomes and fallback paths rather than assuming quiet output.

## Maintainer Workflow To Avoid Teaching As Required

Do not make these core participant steps:

- `_BACKLOG` capture.
- `_REPOLOG` registration.
- Private GitHub organisation conventions.
- Automatic pushing to shared remotes.
- Production Cloudflare project names.
- Secrets handling beyond "do not paste or commit secrets".
- Agent co-author trailers as a participant requirement.
- Generated fixture rebuilds unless the exercise is specifically about sample packaging.

These are good facilitator practices, but they will distract from the reproducibility lesson for beginners.

## Participant Exercise Ladder

### 1. Local Git Trace

Everyone can do this, even without GitHub or Cloudflare access.

Participant prompt:

> Ask Codex to initialise Git in this sample project, show the current status, make a first commit, and explain what the commit records.

Expected command family:

```bash
git init
git status --short
git diff --check
git add .
git commit -m "Initial project record"
git log --oneline -3
```

Teaching point: Git is a visible research trace. It records project state and lets participants compare before and after, even when no code is involved.

### 2. GitHub Sync

Use only when the participant has a working GitHub account and is comfortable creating a test repository.

Participant prompt:

> Ask Codex to check whether GitHub CLI is available and authenticated. If it is, create a private GitHub repository for this workshop project and push the first commit. If it is not, explain the local-only fallback.

Expected command family:

```bash
gh --version
gh auth status
gh repo create <your-test-repo-name> --private --source=. --remote=origin --push
git remote -v
```

Safety notes:

- Never use `gh auth status --show-token` in the workshop.
- Ask participants to create private test repos by default.
- If authentication fails, stop at the local Git history.

Teaching point: GitHub is a sharing and backup layer on top of Git. It is not required for the local reproducibility trace.

### 3. Build Or Package An Output

Use this before Cloudflare so participants see what is being published.

Participant prompt:

> Ask Codex to create a simple static documentation page from the sample project and save it in an output folder. Then ask it to explain which files would be published.

Expected command family depends on the artefact:

```bash
ls
find outputs -maxdepth 2 -type f
python3 -m http.server 8000
zip -r project-output.zip outputs
```

Teaching point: publishing should have an inspectable build/output folder. Do not publish a vague working directory.

### 4. Cloudflare Pages Direct Deploy

Use only when the participant has Cloudflare access and the room is ready.

Participant prompt:

> Ask Codex to check whether Wrangler is available and whether Cloudflare authentication works. If it does, deploy the static output folder to a new or existing Cloudflare Pages project. If it does not, keep the output local and record what would be needed.

Expected command family:

```bash
npx wrangler --version
npx wrangler whoami
npx wrangler pages project create <your-test-project-name>
npx wrangler pages deploy <output-directory> --project-name <your-test-project-name>
```

Safety notes:

- Use participant-owned test project names.
- Avoid secrets in the first workshop version.
- Do not ask participants to deploy anything containing private or real research data.
- Treat Cloudflare as optional; the local output plus Git history is still a completed exercise.

Teaching point: Cloudflare is the dissemination layer. It should publish a reviewed static output, not raw source material by accident.

## Recommended Participant Handouts

Create two short handouts rather than one long CLI handout.

### Handout A: Versioning A Project With Git And GitHub

Contents:

- What Git records.
- What GitHub adds.
- Safe prompt to give Codex.
- Minimal commands participants may see.
- Local-only fallback.
- One review checklist: `git status`, `git log`, and "what changed?".

Placement: `participant/git-github-exercise.md`.

### Handout B: Publishing A Static Output With Cloudflare

Contents:

- What is safe to publish.
- Difference between source folder and output folder.
- Safe prompt to give Codex.
- Minimal Wrangler commands participants may see.
- Cloudflare account fallback.
- Review checklist: source files used, output folder inspected, public URL copied, limitations recorded.

Placement: `participant/cloudflare-publishing-exercise.md`.

## Suggested Integration With Existing Materials

- Keep `participant/git-github-exercise.md` and `participant/cloudflare-publishing-exercise.md` as the guided handouts for the CLI and publishing slots.
- Keep `participant/setup-checklist.md` as a setup checklist, not a command tutorial.
- Keep `exercises/website/` as the simple static publishing target.
- Use `sample-files/project-management-sample-project/` as an advanced demonstration of richer project scaffolding, not the first Git exercise.
- Keep `exercises/external-services/` separate; Cloudflare publishing is dissemination, not the external-service/MCP example.

## Sources Checked

- Cloudflare Wrangler Pages command docs: <https://developers.cloudflare.com/workers/wrangler/commands/pages/>
- Cloudflare Wrangler general command docs: <https://developers.cloudflare.com/workers/wrangler/commands/general/>
- GitHub CLI manual, `gh auth status`: <https://cli.github.com/manual/gh_auth_status>
- GitHub CLI manual, `gh repo create`: <https://cli.github.com/manual/gh_repo_create>
- Local repo state and existing workshop planning files.
- Prior deployment memory from the MondAI workflow: `npx wrangler whoami`, local build, and `npx wrangler pages deploy dist --project-name ...`.
