# Publishing A Static Output With Cloudflare

This exercise shows how a project output can be published after it has been inspected. Cloudflare is optional. If Cloudflare access is not ready, the local output folder is still a useful outcome.

## Before You Start

Publish only a static workshop output, not raw source material.

Use fictional workshop data or non-sensitive content only. Do not publish confidential, identifiable, restricted, or embargoed research data.

## Create An Output First

Ask Codex:

> Create a simple static documentation page from this sample project and save it in an output folder. Then explain which files would be published.

Codex may create or inspect files in a folder such as:

```text
outputs/
  index.html
  styles.css
```

Ask Codex to explain:

- which source files it used,
- what is included in the output folder,
- what is not included,
- what a human should check before publication.

## Optional Cloudflare Step

Use this only if you have a working Cloudflare account and Wrangler authentication is ready.

Ask Codex:

> Check whether Wrangler is available and whether Cloudflare authentication works. If it does, deploy the static output folder to a Cloudflare Pages test project. If it does not, keep the output local and record what would be needed.

Codex may run commands like:

```bash
npx wrangler --version
npx wrangler whoami
npx wrangler pages project create <your-test-project-name>
npx wrangler pages deploy <output-directory> --project-name <your-test-project-name>
```

## What To Check

Before publishing, ask:

> Confirm that the output folder contains only files that are safe to publish.

After publishing, ask:

> Record the public URL, the source files used, and anything that cannot be reproduced without Cloudflare access.

## Fallback

If Cloudflare is not ready, ask Codex to package or describe the local output instead:

```bash
zip -r project-output.zip outputs
```

The important reproducibility point is that the output is inspectable and linked back to its source materials. A public URL is useful, but it is not required for the exercise.
