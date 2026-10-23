# LinkedIn Account Manager (Claude Code skill)

Turns a developer's LinkedIn into a client-winning channel: profile audit, offer/pricing, proof (case studies, GitHub, portfolio), content strategy, Post Studio (research → draft → `.pptx` image → judge scoring), outreach/pipeline, and weekly review. See `SKILL.md` for the full flow.

## Install

This directory *is* the skill — `SKILL.md` at the root, supporting detail in `references/`, helper scripts in `scripts/`.

- **Project-local (this repo only):** keep it where it is; a Claude Code session opened in this directory picks it up automatically.
- **Available in every project:** copy the whole folder into `~/.claude/skills/linkedin-account-manager/` (create the parent dir if it doesn't exist).

## Requirements

Core skill: none — it's prompt-only.

Optional scripts (only needed if `/mnt/skills/public/pptx/SKILL.md` isn't available in your environment, or you want the lead tracker exported to `.xlsx`):

```
pip install python-pptx   # scripts/make_pptx.py
pip install openpyxl      # scripts/lead_tracker.py export (CSV always works without it)
```

## State across sessions

The skill writes `linkedin-state.md` to this project directory at the end of every session (stage, pipeline, open tasks) and reads it back at the start of the next one — no need to paste it back in, unless you're running in a context with no file-write access, in which case it prints the block for you to save yourself. Leads live in `leads.csv` next to it, managed via `scripts/lead_tracker.py`.

## Scripts

- **`scripts/make_pptx.py`** — fallback `.pptx` renderer. Takes a JSON layout spec (canvas size, text/shape boxes with position/color/copy) and produces a real, editable `.pptx`. Used for banners, Post Studio images, and case-study carousels when the bundled pptx skill isn't present.
  ```
  python scripts/make_pptx.py spec.json output.pptx
  ```
- **`scripts/lead_tracker.py`** — lead pipeline tracker backed by `leads.csv` (no dependencies), with an `export` command that also writes a styled `.xlsx` if `openpyxl` is installed.
  ```
  python scripts/lead_tracker.py add --name "Jane Doe" --source "commented on their launch post" --stage cold --next-step "send connection note" --due 2026-11-01 --value 2000
  python scripts/lead_tracker.py list
  python scripts/lead_tracker.py export
  ```

## Example output

Prompt: `check in` (with `linkedin-state.md` already in the project dir, stage 2, two overdue posts).

> **Manager check-in — 2026-10-23**
> Stage 2 (Visibility). Profile and offer are converting; proof assets are done (2 case studies, Featured set).
> Done this week: 2/3 posts shipped, 12 target-list comments logged.
> Overdue: Thursday's build-in-public post (2 days late) and the weekly-review numbers pull.
> Biggest blocker: no inbound DMs yet despite steady impressions — funnel gap is profile→DM, not content.
> Top 3 this week: (1) ship the overdue post today, 20 min; (2) add a direct CTA line to About and Featured, 15 min; (3) run Weekly Review once Thursday's post has 48h of data, 20 min.
> State file updated and saved to `linkedin-state.md`.

(Illustrative — actual output depends on the real state file and profile content; integrity rules mean no invented metrics or client names.)
