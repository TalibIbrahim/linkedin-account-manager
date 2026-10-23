# Profile Audit

## Before you write anything: benchmark + SEO
Don't draft headline/About/Skills from first principles alone.
1. **Benchmark real profiles.** `web_search` (and `web_fetch` the results if useful — expect it to fail outright or return a partial, login-gated view for most profiles; it only reliably works on very high-traffic/cached ones) 3-5 LinkedIn profiles of people who actually do similar client/freelance work and are clearly landing clients, not job-seekers with a generic résumé-style profile. `web_search` snippets alone are often enough for this, don't block on fetch succeeding. Note positioning patterns that repeat: how they frame scope, where they put proof, what they leave out. This is for calibration, not copying — never lift another person's wording or claim their results (same integrity rule as everywhere else in this skill).
2. **Find the real search terms.** Work out what a buyer would actually type into LinkedIn's search or Google to find someone like this user ("AI developer for startups," "Next.js freelancer Lahore," "MVP developer," etc.) — `web_search` to sanity-check these aren't just guesses. Make sure the headline, the first 3 lines of About, and the pinned Skills contain those exact terms naturally (LinkedIn's own search indexes headline/About/Skills/job titles heavily) — not stuffed in as a list, worked into real sentences.

Score each area 1-10 from a client's point of view (a founder landing on the profile for 8 seconds), then fix in priority order.

1. **Headline**: says what they do + for whom, not "Student | Aspiring Developer". Before drafting, ask two quick preferences in one message, with a one-line example of each so the user can just pick:
   - **Style** — keyword-segmented tags (`[Role] | [Specialization/tools + who for] | [value prop]`, best for LinkedIn's own search matching), a conversational sentence, or a mix of both.
   - **Proof in the headline or not** — a specific metric/number right in the headline, or keep the headline pure offer+keywords and let Featured/About carry the proof (headline gets found and passes a 2-second relevance check; proof lands better once someone's already reading).
   Then give 3 options matching what they picked.
2. **Banner**: states the offer visually (editable .pptx, 1584x396). Name, one-line offer, 2-3 proof keywords, site URL. Keep all text/logo out of the bottom-left ~320x396px — that's where the profile photo overlaps, and anything under it gets covered. Build via `/mnt/skills/public/pptx/SKILL.md` if present, else write a JSON spec and run `python scripts/make_pptx.py spec.json banner.pptx`; if that script fails too, hand over the JSON spec as a plain-text build spec.
3. **Photo**: face visible, plain background, good light. Note only if clearly an issue.
4. **About**: first 3 lines (visible before "see more") must state who you help and what result. Then: proof (projects with outcomes), how you work, how to hire you (CTA with email/Calendly). First person, plain language, no buzzword soup.
5. **Featured**: 3 items max: best project demo, case study/write-up, a strong post. Each with a clear title.
6. **Experience/Projects**: outcomes and numbers that are real (users, performance, stack, shipped dates). Each project: problem, what you built, result, link.
7. **Skills & keywords**: match the terms target clients search (e.g. "Next.js developer", "RAG chatbot"). Top 3 pinned skills should be the sellable ones.
8. **Social proof**: recommendations, endorsements, GitHub/site links. Suggest who to ask and a short ask script.
9. **Settings**: custom URL, "Open to work"/services page setup (Services section for freelancers), creator mode only if useful.

Output: score table, top 3 fixes, then full rewritten headline/About/Featured plan ready to paste.

## Credibility Makeover (run after the audit)
Check against `references/proof.md`: GitHub pins and READMEs, portfolio site, live demos, case studies in Featured, recommendations. Output a ranked checklist of gaps with effort (hours) and impact, then turn the top 3 into dated tasks in the state block. Rewrite README intros, the profile README, and site hero copy on request.
