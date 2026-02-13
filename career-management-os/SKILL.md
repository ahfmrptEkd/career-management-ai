---
name: career-management-os
description: >
  A career management system with 7 commands: resume pipeline (sync, draft,
  verify, review, refine), career planning, and interview prep. Optionally
  syncs with claw-log to auto-import daily dev records. Trigger when user
  mentions: resumes, CVs, career docs, job applications, cover letters,
  경력기술서, 이력서, 면접 준비, 커리어 플랜, claw-log, or wants to prepare
  application materials. Also trigger on: "draft resume", "update my resume",
  "tailor resume to JD", "sync claw-log", "career plan", "interview prep",
  "면접 질문", "커리어 로드맵", "career OS".
  Commands: /sync-claw-log, /draft-resume, /verify-resume, /review-resume,
  /refine-resume, /career-plan, /prep-interview.
---

# Career Management OS

A personal career management system that produces high-quality, hallucination-free
resumes through a structured pipeline. Each step writes versioned output for full
audit trail.

## Why a Pipeline?

LLMs hallucinate numbers, fabricate titles, and drift in tone when writing resumes
in a single pass. Splitting work into discrete stages with narrow mandates keeps
every claim traceable and quality consistently high.

---

## Quick Start

### 1. Inputs

| Input | Description | File |
|-------|-------------|------|
| **Career data** | Work history, projects, metrics — the raw truth | `src/applicantinfo.md` |
| **Target JD(s)** | One or multiple company JDs | `src/jd.md` or `src/jds/*.md` |
| **Example resume** *(optional)* | Tone/format reference | `src/resume_example.md` |

If none exist, help user create them interactively.

**Multi-JD support**: Store per-company JDs in `src/jds/`. When user says
"make resume for company_a", use `src/jds/company_a.md`. If only one JD, use
`src/jd.md`. If `src/jds/` has multiple files and no company specified, list
and ask.

### 2. Workspace Structure

```
project/
├── src/
│   ├── applicantinfo.md          # Career data (auto-updated by claw-log sync)
│   ├── jd.md                     # Single JD mode
│   ├── jds/                      # Multi JD mode
│   │   ├── company_a.md
│   │   └── company_b.md
│   └── resume_example.md         # (optional)
├── instruction/
│   └── resume_workflow.md
└── outcome/
    ├── 0-sync/                   # Sync report
    ├── company_a/                # Per-company outputs (multi JD)
    │   ├── 1-draft/
    │   ├── 2-verify/
    │   ├── 3-review/
    │   ├── 4-refine/
    │   └── interview-prep/
    ├── career-plan/              # Career plan outputs
    └── (or 1-draft/ ... 4-refine/ for single JD mode)
```

### 3. Run Pipeline

Full resume pipeline: `/sync-claw-log` → `/draft-resume` → `/verify-resume` → `/review-resume` → `/refine-resume`

Step 0 (Sync) is optional — only for claw-log users. Without claw-log, start at Step 1.

---

## Steps

Read the reference file for each step before executing.

### Step 0: Sync Claw-Log (`/sync-claw-log`) — Optional

> Reference: `references/step0-sync.md`

**Requires**: [claw-log](https://github.com/WooHyucks/claw-log) (`pipx install claw-log`)
**Input**: claw-log log files (daily auto-generated dev records)
**Output**: `outcome/0-sync/sync_report.md` + updated `src/applicantinfo.md`

Reads claw-log logs, extracts Resume Bullet Points per project, compares with
existing applicantinfo.md, and merges intelligently:
- Duplicate → skip
- Similar (same project, same tech) → update existing entry to be richer
- New → add in refined form

Without claw-log installed, skip to Step 1.

### Step 1: Draft (`/draft-resume`)

> Reference: `references/step1-draft.md`

**Input**: `src/applicantinfo.md` + target JD + (optional) `src/resume_example.md`
**Output**: `outcome/1-draft/` or `outcome/{company}/1-draft/` (multi JD)

**JD selection**:
- User specifies company → use `src/jds/{company}.md`, output to `outcome/{company}/`
- No company specified → use `src/jd.md`, output to `outcome/` root
- Multiple JDs exist but none specified → list and ask

Generate **3 distinct resume versions**:
- **V1 — Impact-First**: Leads with measurable business outcomes
- **V2 — Narrative-Arc**: Coherent career story
- **V3 — Skills-Match**: Optimized for ATS keyword alignment

Rule: Every number and claim MUST come from applicantinfo.md. Never invent.

### Step 2: Verify (`/verify-resume`)

> Reference: `references/step2-verify.md`

**Input**: Drafts from Step 1 + `src/applicantinfo.md`
**Output**: `outcome/2-verify/` — verification report + corrected drafts

Line-by-line fact-check against source data:
- ✅ VERIFIED — exact match
- ⚠️ MODIFIED — semantically equivalent, reworded
- ❌ HALLUCINATED — no source basis, must remove/rewrite
- 🔍 UNVERIFIABLE — plausible but not in source, ask user

### Step 3: Review (`/review-resume`)

> Reference: `references/step3-review.md`

**Input**: Verified drafts from Step 2
**Output**: `outcome/3-review/review_report.md`

Expert evaluation on 5 dimensions (A–D grade each):
Relevance | Impact | Clarity | Differentiation | ATS Readiness

Cross-version analysis: best section, weakest section, cherry-pick recommendations.

### Step 4: Refine (`/refine-resume`)

> Reference: `references/step4-refine.md`

**Input**: Review report + verified drafts
**Output**: `outcome/4-refine/final_resume.md` + `changelog.md`

Merge best elements from all versions into one final resume.
Final self-check: every claim traceable, consistent tone, no hallucinations.

### Step 5: Career Plan (`/career-plan`)

> Reference: `references/step5-career-plan.md`

**Input**: `src/applicantinfo.md` + `src/jds/*.md` + **web search (required)**
**Output**: `outcome/career-plan/`

Analyzes gap between current skills and target positions. Web search is REQUIRED
for: industry trends, salary data, job market, tech roadmap, certifications.
Produces short/mid/long-term roadmap with concrete resources.

⚠️ No guessing trends. All data must cite web search sources.

### Step 6: Interview Prep (`/prep-interview`)

> Reference: `references/step6-prep-interview.md`

**Input**: `src/applicantinfo.md` + target JD + (optional) final resume + **web search (required)**
**Output**: `outcome/{company}/interview-prep/`

Web search FIRST: company news, tech blog, interview reviews, culture.
Then generate: technical Q&A, behavioral STAR answers, company-specific questions,
questions to ask the interviewer.

⚠️ All experience/metrics from applicantinfo.md only. Company info requires web sources.

---

## Command Summary

| Command | Function | Web Search |
|---------|----------|------------|
| `/sync-claw-log` | claw-log → applicantinfo merge | ❌ |
| `/draft-resume` | 3-version resume drafts | ❌ |
| `/verify-resume` | Fact-check (hallucination removal) | ❌ |
| `/review-resume` | Expert evaluation | ❌ |
| `/refine-resume` | Final resume generation | ❌ |
| `/career-plan` | Career roadmap with gap analysis | ✅ Required |
| `/prep-interview` | Interview Q&A generation | ✅ Required |

**Resume pipeline** (sequential): `/sync-claw-log` → `/draft-resume` → `/verify-resume` → `/review-resume` → `/refine-resume`

**Standalone**: `/career-plan` and `/prep-interview` can run independently anytime.

---

## Iteration & Refinement

- **Add info** → update applicantinfo.md, re-run from Step 1
- **Switch company** → "make resume for company_b" → same data, different JD
- **Re-run single step** → e.g., just `/review-resume` after manual edits
- **Targeted edits** → inline editor for tone/nuance, then re-verify

Previous outputs are preserved; re-runs build on them.

---

## Extension Skills (Future)

| Skill | Purpose |
|-------|---------|
| `/generate-cover-letter` | Tailored cover letter from same source + JD |
| `/tailor-for-jd` | Quick-adapt existing resume for new JD |
| `/portfolio-gen` | Portfolio page from applicantinfo + projects |

Daily career event logging is handled by claw-log automatically.
Manual events (promotions, awards, certs) go directly into `src/applicantinfo.md`.

---

## Language & Tone

- Working language: match user's language (Korean or English)
- Resume language: ask user — many prefer English resumes even in Korean context
- Skill internals: English for token efficiency
- Be direct and actionable — avoid vague praise

---

## Key Principles

1. **Source data is sacred** — Never invent metrics, titles, dates, or company names
2. **One job per step** — Sync collects, Draft creates, Verify checks, Review evaluates, Refine synthesizes
3. **Everything is a file** — All outputs are markdown in `outcome/` for traceability
4. **Iterate, don't restart** — Build on previous runs
5. **Human stays in control** — System handles structure and facts; user owns nuance and voice
6. **Daily records compound** — Small daily claw-log entries become the strongest resume source over time
7. **Web search over guessing** — Career plan and interview prep must use real data, never fabricate
