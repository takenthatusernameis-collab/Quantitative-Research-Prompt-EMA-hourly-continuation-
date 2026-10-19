# NEXT AGENT TASK

## Objective
No active task. The EMA hourly continuation research is **CONCLUDED** and **REJECTED**.

## Current State
- Decision: **REJECTED** (no live trading).
- OOS pooled (net-of-costs): 666 trades, net PF 0.6890, net Sharpe -1.9443, max DD 0.6663 from `results/20261019_064215_oos_pooled/summary.json`.
- Per-symbol (net PF): BTC 0.6860, ETH 0.7861, SOL 0.8792, BNB 0.6955, XRP 0.8006 (all < 1).
- Robustness checks confirm poor performance; cost stress (2x) worsens PF 0.6906 → 0.4691.
- Tests: 16/16 passed (verified).
- Git: tracked tree clean; only untracked `__pycache__/` directories present.
- Artifacts final: `results/FINAL_DECISION.md`, `results/RESEARCH_CONCLUSION.md`, `results/robustness_summary.md`.

## Ground Truth
Research artifacts are immutable. Do not re-run parameter searches, backtests, or tuning of the rejected baseline without explicit authorization.

## Handoff Notes
- This agent has confirmed: tests pass (16/16), git status shows clean tracked tree (only `__pycache__/` untracked), OOS metrics match documented values, and all final artifacts exist.
- Task is complete and archived.

## Constraints
- Any new work requires a fresh, pre-registered hypothesis card (theoretical rationale + falsifiable acceptance criteria) before implementation (PROMPT.md §3.4; `results/FINAL_DECISION.md`).
- If no new authorized hypothesis is provided, stand down with no changes.

## Validation Command
`python -m pytest tests/ -q`
