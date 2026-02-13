# Step 1: Draft Resume

## Purpose

Generate 3 strategically different resume versions from career data and target JD.
Goal is exploration — wide net so later steps can pick the best elements.

## Procedure

1. **Read source files**
   - `src/applicantinfo.md` — single source of truth
   - Target JD — determined by user request:
     - Specific company: `src/jds/{company}.md`
     - Default: `src/jd.md`
     - If `src/jds/` has multiple and none specified: list and ask
   - `src/resume_example.md` (if exists) — tone/format reference
   - Multi-JD mode outputs go to `outcome/{company}/1-draft/`

2. **Analyze JD**
   - Extract: required skills, preferred skills, seniority, industry, key responsibilities
   - Rank top 5 qualifications
   - Note unusual requirements

3. **Map source data to JD**
   - For each requirement, find strongest matching experience
   - Identify gaps; find transferable experiences for gaps

4. **Generate 3 versions**

   **V1 — Impact-First**: Lead with measurable outcomes (revenue, cost, scale).
   Best for: data-driven companies, leadership roles.

   **V2 — Narrative-Arc**: Coherent career story with logical progression.
   Best for: career changers, senior roles, culture-fit companies.

   **V3 — Skills-Match**: Maximum keyword overlap with JD.
   Best for: large companies with ATS, roles with specific technical requirements.

5. **Self-check**
   - Every number/metric must exist in applicantinfo.md
   - Missing source → use qualitative description or flag `[NEEDS SOURCE]`
   - Verify all dates, titles, company names match source exactly

6. **Save**: `outcome/1-draft/draft_v1.md`, `draft_v2.md`, `draft_v3.md`, `jd_analysis.md`
