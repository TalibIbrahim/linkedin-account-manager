# Post Studio

## 1. Topic
- User gave a topic: go to 2.
- Otherwise `web_search` 4-6 queries for the last 7 days (today's real date) across AI releases, dev tools, big-tech moves, open source. Fetch the best 1-2 pages if snippets are thin.
- Show 5-6 candidates: headline, what happened, why the target audience cares, and which of the user's real projects/experience connects. Ask which to pick (or let them type their own). Stop and wait.

## 2. Angle
Use a real experience from the brief if one fits. None fits? Write an opinionated take with a concrete trade-off. Never invent anecdotes or numbers. Verify every factual claim against retrieved sources; paraphrase, don't copy.

## 3. Write (human, not corny)
- 120-220 words. Hook = first line, specific, under ~12 words. Mixed paragraph lengths, not one sentence per line.
- One opinion, one real trade-off, one concrete detail (a number, tool, thing that broke).
- Plain words, contractions, first person. End on a point; a question only if genuinely wanted. 0-3 hashtags, no emoji bullets, at most one emoji.
- Banned phrases/patterns: see `references/banned-phrases.md` (living list — when a judge flags a new one in step 5, add it there before the session ends).
- Suggest the source link for the first comment.

## 4. Image
Single-slide editable `.pptx`, 1080x1350, real text boxes/shapes. One idea: short headline or key number + small handle/source line. Clean, high contrast, whitespace, one accent color. Build via `/mnt/skills/public/pptx/SKILL.md` if present; otherwise write the layout as a JSON spec (shapes, positions, colors) and run `python scripts/make_pptx.py spec.json post.pptx`. If the script fails too, present the same spec as a plain-text build spec instead. Render and check for overflow/legibility before presenting.

## 5. Judges
3 subagents in parallel if available; otherwise 3 sequential passes (say so). Each gets only the post text, image text, and its persona, not the drafting reasoning.
1. **Skeptical senior engineer**: cringe detector; flags fake, hype, vague, wrong.
2. **Potential client (founder/hiring manager)**: would I trust and DM this person for paid work?
3. **LinkedIn editor**: hook, scannability, text+image fit, earns the read.
Each returns 1-10 for `stops_the_scroll`, `credibility`, `non_cringe`, `would_contact` (client only), one-line verdict, biggest fix.
If any `credibility` or `non_cringe` < 7: apply fixes, re-run judges once. No further loops.

## 6. Final output
Post text (copy-ready) | image (.pptx) | judge table | overall confidence (average) | sources | best time/day to post per strategy | one line that scores are opinions.
