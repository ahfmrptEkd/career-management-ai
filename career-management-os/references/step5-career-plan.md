# Step 5: Career Plan

## Purpose

Analyze the gap between current skills and target positions, then produce
a realistic, actionable career roadmap. Web search is REQUIRED to ground
all trend/salary/market claims in real data.

## Inputs

- `src/applicantinfo.md` — current capabilities
- `src/jds/` — target positions
- **Web search** — industry data (mandatory)

## Procedure

### 1. Current Capability Analysis

Extract from applicantinfo.md:
- Core tech stack inventory
- Years of experience and seniority level
- Domain expertise (e.g., real-time AI, MLOps)
- Leadership / management experience

### 2. Target Position Analysis

Extract common patterns across JDs:
- Top 10 repeatedly required skills
- Required experience level
- Common keywords and role scope

### 3. Web Search Research (REQUIRED)

Search for the following BEFORE generating any plan:

| Topic | Example Query | Why |
|-------|--------------|-----|
| **Tech trends** | "AI Engineer skills demand 2026" | Which skills are rising/declining |
| **Salary range** | "AI Engineer salary [country] 2026" | Set realistic expectations |
| **Job market** | "AI Engineer hiring trends" | Market conditions |
| **Tech roadmap** | "TensorRT vs vLLM inference 2026" | Technology direction |
| **Certifications** | "MLOps certification value 2026" | Worth investing in? |

⚠️ NEVER guess trends without web search evidence.
Cite sources. If search returns nothing, state "needs verification."

### 4. Gap Analysis

| Dimension | Current (applicantinfo) | Target (JD common) | Gap |
|-----------|------------------------|--------------------|----|
| Tech stack | Owned skills | Required skills | Missing skills |
| Experience | N years | Required level | Experience gap |
| Domain | Current domain | Target domain | Transition needed? |
| Soft skills | Current | Required | Leadership/communication |

### 5. Roadmap Generation

Time-based action plan:

```markdown
## Short-term (1-3 months)
- [ ] Immediately actionable items
- [ ] Quick-to-learn missing skills

## Mid-term (3-6 months)
- [ ] Build project experience
- [ ] Complete certifications/courses

## Long-term (6-12 months)
- [ ] Ready to apply for target positions
- [ ] Portfolio complete
```

Each item includes **specific resources** (courses, certs, open-source
projects found via web search).

### 6. Output

- `outcome/career-plan/career_plan.md` — full roadmap
- `outcome/career-plan/gap_analysis.md` — detailed gap analysis
- `outcome/career-plan/research_sources.md` — web search sources

## Anti-Hallucination Rules

- Salary data: must cite web search source, never guess
- Tech trends: cite specific sources, not "it is known that..."
- Job market: use latest data, flag stale information
- Unverifiable claims: tag as "needs verification"
