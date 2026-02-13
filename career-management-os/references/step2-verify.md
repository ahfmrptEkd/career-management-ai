# Step 2: Verify Resume

## Purpose

Line-by-line fact-check every claim in drafts against source data.
This is the hallucination firewall.

## What LLMs Get Wrong in Resumes

- Inflate percentages (source says "improved" → draft says "improved by 15%")
- Invent plausible metrics
- Merge experiences from different roles
- Subtly upgrade titles ("contributed to" → "led")
- Add unmentioned skills

## Procedure

1. Load drafts from `outcome/1-draft/` and `src/applicantinfo.md`

2. Extract every factual claim (numbers, titles, companies, dates, projects, skills, team sizes)

3. Compare against source:

   | Verdict | Criteria | Action |
   |---------|----------|--------|
   | ✅ VERIFIED | Exact/near-exact match | Keep |
   | ⚠️ MODIFIED | Semantically equivalent, reworded | Flag for awareness |
   | ❌ HALLUCINATED | No basis in source | Remove or rewrite from source |
   | 🔍 UNVERIFIABLE | Plausible but not in source | Ask user to confirm |

4. Produce verification report with table per draft

5. Produce corrected drafts with all ❌ items fixed

6. Summary stats at top:
   ```
   Total claims: X
   ✅ Verified: X (Y%)
   ⚠️ Modified: X (Y%)
   ❌ Hallucinated: X (Y%)
   🔍 Unverifiable: X (Y%)
   ```

7. Save to `outcome/2-verify/`

## Rules

- When in doubt → 🔍 UNVERIFIABLE, not ✅ VERIFIED
- Never fix a hallucination by inventing a different number — use qualitative language
- Preserve each draft's strategy and structure
