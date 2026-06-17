---
description: Initialize the Difference-in-Differences for Corpus Linguistics project environment
---

# Difference-in-Differences for Corpus Linguistics Project Initialization

This workflow orients you to the project. Use it at the start of any new session.

## Quick Start (Returning Session)

1. **Scan the repo for orientation docs**
   ```
   ls -la
   ```

2. **Read orchestration + status files**
   ```
   cat AGENTS.md
   cat STATUS.md
   cat DECISIONS.md
   cat notes/source-verification.md
   ```

3. **Check house style (if present)**
   ```
   [ -f .house-style/style-guide.md ] && cat .house-style/style-guide.md
   [ -f .house-style/style-rules.yaml ] && cat .house-style/style-rules.yaml
   ```

4. **Identify the build entrypoint**
   ```
   ls -la *.tex 2>/dev/null || true
   [ -f Makefile ] && sed -n '1,160p' Makefile
   ```

## Key Retrieval Points

**For argument/outline:**
- `STATUS.md`, `DECISIONS.md`, `notes/source-verification.md`, `sections/`

**For current draft:**
- `main.tex` and `sections/*.tex`

**For bibliography:**
- `references.bib` (central symlink) and `references-local.bib` (verified project-specific entries only)

**For figures/data:**
- none yet; create `figures/`, `data/`, or `analysis/` only when a worked example is chosen

**For source PDFs (if present):**
- central `../../literature/` and verified project-local sources only if needed

Search PDFs quickly:
```
pdftotext "PATH/filename.pdf" - | rg -n "keyword"
```

## Full Initialization (New to Project)

1. **Read `CLAUDE.md`, `STATUS.md`, and `DECISIONS.md`** -- project role, build commands, and live state
2. **Skim `main.tex` and `sections/*.tex`** for structure and macro conventions
3. **Read `notes/source-verification.md` before adding citations**
4. **Run a quick build** (optional, if you have TeX installed)
   - `make quick` or `make`
   - otherwise: `latexmk -pdf main.tex`

## Process Reminders

**For drafting/revision:**
1. Start from an outline and the target venue constraints
2. Make one coherent pass at a time (structure → prose → citations)
3. Keep changes small enough to review

**For citation work:**
1. Verify sources against authoritative records before adding BibTeX
2. Use central `references.bib` keys when available
3. Add only verified project-specific entries to `references-local.bib`
4. Rebuild after citation edits to catch missing keys

**Git:**
- Commit after each logical unit of work; use `/git-hygiene` if you need reminders

## Other Workflows

- `/git-hygiene` — Reminders for clean commits and branch management
- `/multi-agent-review` — Spawn independent LLM agents (Codex, Gemini) for parallel advisory board reviews of the draft. Useful for getting diverse, unbiased feedback.
