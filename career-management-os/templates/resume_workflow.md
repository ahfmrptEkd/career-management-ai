# Resume Workflow Checklist

## Before Starting
- [ ] `src/applicantinfo.md` filled with career data
- [ ] Target JD in `src/jd.md` or `src/jds/{company}.md`
- [ ] (Optional) Example resume in `src/resume_example.md`

## Pipeline
- [ ] Step 0: `/sync-claw-log` (if using claw-log)
- [ ] Step 1: `/draft-resume` → 3 versions generated
- [ ] Step 2: `/verify-resume` → fact-checked, hallucinations removed
- [ ] Step 3: `/review-resume` → expert evaluation complete
- [ ] Step 4: `/refine-resume` → final resume ready

## Standalone (anytime)
- [ ] `/career-plan` → roadmap generated
- [ ] `/prep-interview` → Q&A ready

## Final Check
- [ ] All claims traceable to applicantinfo.md
- [ ] Resume language matches target (Korean/English)
- [ ] Format suitable for submission method (PDF, web form, etc.)
