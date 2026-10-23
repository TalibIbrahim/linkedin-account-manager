# Pipeline (outreach to closed project)

## Target list
30-50 accounts: ideal clients (founders, CTOs, product leads at early-stage startups/agencies in the target market) and peers who attract them. Table: name | role | company | why relevant | last touch | status | next step | due.

## Daily 15 minutes
1. Comment thoughtfully on 3-5 target posts (2-4 sentences, a specific point or question, never "Great post!").
2. Reply to all comments on own posts within a few hours.
3. 3-5 personalized connection requests.

## Templates (3 variants each, tailored to the brief; never mass-send)
- **Connection note** (<300 chars): something specific they posted/built + why connect. No pitch.
- **After accept:** thanks + one relevant question or useful resource. No pitch.
- **Soft offer** (only after real interaction): what you noticed, one concrete idea, low-pressure next step.
- **Inbound reply:** answer first, then propose a short call.
- **Follow-up cadence:** 3 touches over ~3 weeks, each adding value, then park the lead.

## Discovery call (30 min)
Goals, current situation, problem cost, timeline, budget range, decision makers, past attempts. Script questions, a "what happens if you do nothing" prompt, and a clear next step. End by summarizing back.

## Proposal (1-2 pages)
Problem in their words → proposed solution → scope in/out → timeline/milestones → price + payment terms (deposit) → next step. Optional: 2 tiers. Generate as a doc on request.

## Objections
Price, "we'll build in-house", "you're a student/junior", trust, timing. Give honest replies built on real proof, scope control, and a small paid first step; never bluff experience.

## Lead tracker
Keep leads in `leads.csv` via `python scripts/lead_tracker.py` (`add`, `update`, `list`, `export`): name/lead | source | last contact | stage (cold, warm, call, proposal, won, lost) | next step | due | value. CSV always works; `export` also writes a styled `.xlsx` via openpyxl when it's installed, otherwise it says so and the CSV is the deliverable. Review weekly.
