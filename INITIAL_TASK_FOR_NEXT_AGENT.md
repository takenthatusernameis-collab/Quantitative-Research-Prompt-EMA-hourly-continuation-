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

## Prior Agent's Handoff Message (2026-10-19T12:25Z UTC)
Prior agent completed its task: read all context (README.md, PROMPT.md, NEXT_AGENT_TASK.md, results/FINAL_DECISION.md, results/RESEARCH_CONCLUSION.md, results/robustness_summary.md, results/20261019_064215_oos_pooled/summary.json, results/20261019_062710_cost_stress/summary.md), verified tests pass (16/16), confirmed git tree is clean (only untracked __pycache__/ dirs), and confirmed no new hypothesis is present anywhere in the repo (searched for `*hypo*` files; none exist; no user-supplied hypothesis in any handoff or task file). Research stands concluded and REJECTED per final artifacts (net OOS PF 0.6890, net Sharpe -1.9443, max DD 0.6663; cost stress worsens results; no robustness variant reaches profitability). Recommendation: no live trading, do not continue parameter tuning of this baseline. Standing down with no code changes, awaiting a new pre-registered hypothesis.

## This Agent's Completion (2026-10-19T12:29Z UTC)
Re-read durable handoff NEXT_AGENT_TASK.md, re-verified tests pass (16/16), confirmed git tracked tree clean (only __pycache__/ untracked), confirmed no new hypothesis exists anywhere in repo. Research remains CONCLUDED and REJECTED. No code changes made. Standing down, awaiting new pre-registered hypothesis.

(End of file)
