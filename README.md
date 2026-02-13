# Career Management OS

**An AI-powered system for managing your career credentials, from daily logs to final polished resumes.**

This project implements a structured pipeline to draft, verify, review, and refine resumes, ensuring they are hallucination-free and impactful.

## 💡 The Power of Claw-log

While **Career Management OS** functions perfectly as a standalone tool, it is designed to synergize with **[claw-log](https://github.com/ahfmrptEkd/claw-log)**.

- **Without claw-log**: You provide your career history manually.
- **With claw-log**: typically, developers forget 90% of their daily problem-solving details. `claw-log` captures these daily tasks. This OS then consumes those rich daily logs to generate highly detailed, evidence-backed achievements that you might have otherwise forgotten. **It turns your daily grind into career gold.**

---

# Usage Guide

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/career-management-os.git
cd career-management-os
```

### Antigravity IDE

```bash
# Skills (natural language trigger)
cp -r career-management-os ~/.gemini/antigravity/skills/

# Workflows (slash commands)
cp career-management-os/workflows/*.md ~/.gemini/antigravity/workflows/
```

or Ask a gemini to apply this github repository skill

### Claude Code

```bash
cp -r career-management-os ~/.claude/skills/
cp career-management-os/workflows/*.md .claude/commands/
```

or Ask a claude to apply this github repository skill

or Add this repository as a plugin

```bash
/plugin marketplace add ahfmrptEkd/career-management-ai

/plugin install career-management-os@career-management-os
```

### Cursor

```bash
cp -r career-management-os .cursor/skills/
```

After installation, restart your agent session.

---

## Project Setup

Run the setup script or create manually:

```bash
python career-management-os/scripts/setup_project.py
```

This creates:

```
project/
├── src/
│   ├── applicantinfo.md    ← Your career data (fill this in)
│   ├── jds/                ← Target company JDs
│   │   └── (add JDs here)
│   └── resume_example.md   ← (optional) tone/format reference
├── instruction/
│   └── resume_workflow.md
└── outcome/                ← All outputs go here
```

---

## Commands (7 total)

### Resume Pipeline (run in order)

| #   | Command          | What it does                                               |
| --- | ---------------- | ---------------------------------------------------------- |
| 0   | `/sync-claw-log` | Imports claw-log dev records → applicantinfo.md (optional) |
| 1   | `/draft-resume`  | Generates 3 strategic resume versions                      |
| 2   | `/verify-resume` | Fact-checks every claim against source data                |
| 3   | `/review-resume` | Expert evaluation on 5 dimensions                          |
| 4   | `/refine-resume` | Merges best elements into final resume                     |

### Standalone (run anytime)

| Command           | What it does                     | Requires web search |
| ----------------- | -------------------------------- | ------------------- |
| `/career-plan`    | Gap analysis + career roadmap    | ✅ Yes              |
| `/prep-interview` | Interview Q&A for target company | ✅ Yes              |

---

## Typical Workflows

### First-time resume creation

```
1. Fill in src/applicantinfo.md (your career data)
2. Add target JD to src/jds/company_a.md
3. /draft-resume company_a
4. /verify-resume
5. /review-resume
6. /refine-resume
→ Final resume at outcome/company_a/4-refine/final_resume.md
```

### With claw-log (daily dev tracking)

```
1. Install claw-log: pipx install claw-log
2. Let it run daily (auto-generates dev records)
3. When ready: /sync-claw-log
4. Review updated applicantinfo.md
5. Continue with /draft-resume ...
```

### Multiple companies

```
src/jds/
├── naver_ai.md
├── kakao_brain.md
└── samsung_sds.md

/draft-resume naver_ai     → outcome/naver_ai/
/draft-resume kakao_brain   → outcome/kakao_brain/
(same applicantinfo.md, different JDs)
```

### Career planning

```
/career-plan
→ Web-searches industry trends, salary data, skill demand
→ Produces gap analysis + roadmap at outcome/career-plan/
```

### Interview prep

```
/prep-interview company_a
→ Web-searches company news, tech blog, interview reviews
→ Produces Q&A sets at outcome/company_a/interview-prep/
```

---

## File Structure After Full Run

```
outcome/
├── 0-sync/
│   └── sync_report.md
├── company_a/
│   ├── 1-draft/
│   │   ├── draft_v1.md          (Impact-First)
│   │   ├── draft_v2.md          (Narrative-Arc)
│   │   ├── draft_v3.md          (Skills-Match)
│   │   └── jd_analysis.md
│   ├── 2-verify/
│   │   ├── verification_report.md
│   │   └── draft_v{1,2,3}_verified.md
│   ├── 3-review/
│   │   └── review_report.md
│   ├── 4-refine/
│   │   ├── final_resume.md      ← YOUR FINAL RESUME
│   │   └── changelog.md
│   └── interview-prep/
│       ├── questions_technical.md
│       ├── questions_behavioral.md
│       ├── questions_company.md
│       ├── questions_to_ask.md
│       └── research_notes.md
└── career-plan/
    ├── career_plan.md
    ├── gap_analysis.md
    └── research_sources.md
```

---

## Key Rules

1. **Source data is sacred** — No invented metrics, titles, or dates
2. **One job per step** — Each command has a single responsibility
3. **Everything is a file** — Full audit trail in `outcome/`
4. **Web search over guessing** — `/career-plan` and `/prep-interview` always search first
5. **Human stays in control** — System handles structure; you own voice and nuance

---

## Tips

- **Re-run single steps**: After manual edits, just run `/verify-resume` again
- **Iterate**: Each run preserves previous outputs
- **Language**: System instructions are in English (token-efficient). Resume output language is your choice — just tell the agent
- **claw-log**: Daily records compound over time into powerful resume material
- **Token efficiency**: All skill internals are English to minimize token usage; user-facing content (resume, Q&A) follows your preferred language

---

## 🔗 References & Inspiration

This project was created with inspiration from the following resource:

- **Core Concept**: [Documentation-driven Resume Engineering (LinkedIn Post)](https://www.linkedin.com/feed/update/urn:li:activity:7427324639552581632/?originTrackingId=BhCxOmnK57swQPBhWx%2F5Hw%3D%3D)

**Claw-log Repositories:**

- **[ahfmrptEkd/claw-log](https://github.com/ahfmrptEkd/claw-log)**: The customized fork used in this workflow (Recommended).
- **[WooHyucks/claw-log](https://github.com/WooHyucks/claw-log)**: The original project.
