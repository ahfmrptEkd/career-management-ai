# Workflow Installation (Slash Commands)

Workflows enable `/command` triggers in Antigravity.
Skills trigger on natural language; Workflows trigger on `/`.

## Install

```bash
# Global
cp workflows/*.md ~/.gemini/antigravity/workflows/

# Or project-local
mkdir -p .agent/workflows
cp workflows/*.md .agent/workflows/
```

## Claude Code

```bash
mkdir -p .claude/commands
cp workflows/*.md .claude/commands/
```
