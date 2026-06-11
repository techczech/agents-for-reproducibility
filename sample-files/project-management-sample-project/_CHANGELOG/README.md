# Project Changelog

This folder records meaningful project changes, backlog items, and durable decisions for the sample project.

It is separate from `_TASK-LOG/`:

- `_TASK-LOG/` records the operational state of work.
- `_CHANGELOG/` records durable change history and project decisions.

## Buckets

- `changes/` — completed changes or migrations.
- `decisions/` — durable decisions that future agents should not silently contradict.
- `backlog/` — proposed or active work with explicit status.
- `logs/worklog.jsonl` — compact machine-readable run notes.

Validate with:

```bash
python3 "$HOME/gitrepos/02_workskills/project-changelog/scripts/build_index.py" --changelog-dir _CHANGELOG
```
