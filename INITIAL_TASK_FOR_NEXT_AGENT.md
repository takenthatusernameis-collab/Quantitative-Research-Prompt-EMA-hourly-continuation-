# INITIAL TASK FOR NEXT AGENT

## Context
This is a quantitative research repo (EMA hourly continuation). Previous research has concluded and was REJECTED per final artifacts:
- results/FINAL_DECISION.md (REJECT)
- results/RESEARCH_CONCLUSION.md
- results/robustness_summary.md

## Objective
Determine if there is a new, pre-registered hypothesis to test. If not, stand down.

## Required Actions
1. Read context: README.md, PROMPT.md, NEXT_AGENT_TASK.md, and final artifacts in results/.
2. Check for new input: Look for a user-provided hypothesis (theoretical rationale + falsifiable acceptance criteria). If none present → stand down with no code changes. Report state (tests pass, research concluded/rejected).
3. If hypothesis provided: Validate against PROMPT.md §3.4. Only proceed if justified, falsifiable, and authorized. Do not re-run baseline/tuning unless hypothesis explicitly requires it.
4. Verify: Run `python -m pytest tests/ -q` and report result.
5. Handoff: Update NEXT_AGENT_TASK.md with outcome (or keep standby). Do not commit unless explicitly requested.

## Constraints
- Any new work requires fresh, pre-registered hypothesis before implementation.
- Do not modify/overwrite/re-run scripts producing final artifacts unless new hypothesis explicitly requires it with authorization.
- If no new authorized hypothesis provided: stand down with no changes.

## Validation
```bash
python -m pytest tests/ -q
```
