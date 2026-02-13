# Step 6: Interview Prep

## Purpose

Generate predicted interview questions and model answers for a specific company,
grounded in career data and web-searched company intelligence. Web search is
REQUIRED to ensure company info is accurate and current.

## Inputs

- `src/applicantinfo.md` — career data
- Target JD — `src/jds/{company}.md` or `src/jd.md`
- Previous resume (if exists) — `outcome/{company}/4-refine/final_resume.md`
- **Web search** — company research (mandatory)

## Procedure

### 1. Web Search Research (REQUIRED — run FIRST)

Before generating any questions, search for:

| Topic | Example Query | Purpose |
|-------|--------------|---------|
| **Company news** | "{company} AI 2026 news" | Latest projects, strategy |
| **Tech blog** | "{company} engineering blog" | Tech stack, culture |
| **Interview reviews** | "{company} AI Engineer interview" | Actual question types |
| **Tech interview trends** | "AI Engineer interview questions 2026" | Current patterns |
| **Company values** | "{company} culture values mission" | Culture-fit prep |

⚠️ Clearly distinguish web-sourced facts from inference.
Use "According to interview reviews..." vs "Generally speaking..."

### 2. Generate Questions by Category

#### A. Technical Interview

Based on JD requirements + web search interview trends:

```markdown
### Q: [Technical question]
**Source**: JD requirement "..." / {company} blog post about "..."
**Model Answer**: (based on actual experience from applicantinfo.md)
**Key Terms**: [keywords the interviewer wants to hear]
**Watch Out**: [common mistakes or traps]
```

Categories:
- System design (e.g., "Design a real-time inference service")
- Coding/algorithms (based on JD-specified technologies)
- Deep-dive (based on your project experience — "Walk me through this")

#### B. Behavioral Interview (STAR Format)

Stories extracted from career data:

```markdown
### Q: [Behavioral question]
**S (Situation)**: Extracted from applicantinfo.md
**T (Task)**: Your specific responsibility
**A (Action)**: What you concretely did
**R (Result)**: Outcome and impact
**Source**: Specific applicantinfo.md entry
```

Common prompts:
- "Most challenging technical problem?"
- "How did you resolve a team conflict?"
- "Tell me about a failure and what you learned"

#### C. Company-Specific Questions

Based on web search findings:

- "What do you know about us?" → answer using latest news/blog
- "Why this company?" → connect JD + company mission + your career
- Opinion on company's latest projects/products

#### D. Questions to Ask (Reverse Interview)

Concrete questions based on web research:

- Team structure, tech stack details
- Questions about recent news/projects ("I read about X, can you tell me more?")
- Growth opportunities, onboarding process

### 3. Answer Quality Verification

Every answer must pass:

| Check | Criteria |
|-------|----------|
| ✅ Fact-based | Grounded in applicantinfo.md? |
| ✅ Metrics accurate | Numbers/dates/scale match source? |
| ✅ Sources cited | Web search info has source URL? |
| ❌ No exaggeration | No "revolutionary", "groundbreaking" fluff |
| ❌ No fabrication | No invented experiences |

### 4. Output

- `outcome/{company}/interview-prep/questions_technical.md`
- `outcome/{company}/interview-prep/questions_behavioral.md`
- `outcome/{company}/interview-prep/questions_company.md`
- `outcome/{company}/interview-prep/questions_to_ask.md`
- `outcome/{company}/interview-prep/research_notes.md` — web research results

## Anti-Hallucination Rules

- All experience/metrics in answers must trace to applicantinfo.md.
  If not available, mark as "specific metric needs confirmation"
- Company info requires web search source: "According to {url}..."
- Interview review data must note timeframe: "Per 2025 reviews..."
- Unknown information: state explicitly, never fabricate
