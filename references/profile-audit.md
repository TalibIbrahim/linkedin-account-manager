# Profile Audit

Score each area 1-10 from a client's point of view (a founder landing on the profile for 8 seconds), then fix in priority order.

1. **Headline**: says what they do + for whom + proof/outcome, not "Student | Aspiring Developer". Formula: `[What you build] for [who] | [proof point or stack]`. Give 3 options.
2. **Banner**: states the offer visually (editable .pptx, 1584x396). Name, one-line offer, 2-3 proof keywords, site URL. Build via `/mnt/skills/public/pptx/SKILL.md` if present, else write a JSON spec and run `python scripts/make_pptx.py spec.json banner.pptx`; if that script fails too, hand over the JSON spec as a plain-text build spec.
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
