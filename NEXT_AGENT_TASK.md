# NEXT AGENT TASK

## Objective
No active task. EMA hourly continuation research is concluded and **REJECTED**. Stand down — no experiments to run unless the user supplies a new, pre-registered hypothesis.

## Current State
- Decision: **REJECTED** / **CONCLUDED** (no live trading).
- OOS pooled (net-of-costs): 666 trades, net PF 0.6890, net Sharpe -1.9443, max DD 0.6663 from `results/20261019_064215_oos_pooled/summary.json`.
- Per-symbol (net PF): BTC 0.6860, ETH 0.7861, SOL 0.8792, BNB 0.6955, XRP 0.8006 (all < 1).
- All robustness checks negative; cost stress (2x) worsens PF 0.6906 → 0.4691.
- Tests: 16/16 pass (`python -m pytest tests/ -q`).
- Git: tracked tree clean; only untracked `__pycache__/` directories present.
- Artifacts final: `results/FINAL_DECISION.md`, `results/RESEARCH_CONCLUSION.md`, `results/robustness_summary.md`.

## Ground Truth
Research artifacts are immutable unless a new pre-registered hypothesis exists. Do not re-run parameter searches or tune the rejected baseline.

## Handoff Notes
- Independently verified by current agent: tests pass (16/16), tracked git tree clean, OOS metrics match handoff (666 trades, PF 0.6890, Sharpe -1.9443, max DD 0.6663).
- `NEXT_AGENT_TASK.md` marked COMPLETE with verification details.
- No code changes were made.

## Constraints
- Any new work requires a fresh, pre-registered hypothesis card (theoretical rationale + falsifiable acceptance criteria) before implementation (PROMPT.md §3.4; `results/FINAL_DECISION.md`).
- If no new authorized hypothesis is provided, stand down with no changes.

## Validation Command
`python -m pytest tests/ -q`
