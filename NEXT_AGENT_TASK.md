# NEXT AGENT TASK

## Objective
No active task. The EMA hourly continuation research is **CONCLUDED** and **REJECTED** (no live trading).

If the user provides no new pre-registered hypothesis, stand down with no changes. Do not re-run backtests, parameter searches, or tuning of the rejected baseline without explicit authorization.

## Current State
- Decision: **REJECTED** / **CONCLUDED** (no live trading).
- OOS pooled (net-of-costs): 666 trades, net PF 0.6890, net Sharpe -1.9443, max DD 0.6663 from `results/20261019_064215_oos_pooled/summary.json`.
- Per-symbol (net PF / Sharpe): BTC/USDT 0.6860 / -0.9004, ETH/USDT 0.7861 / -1.8710, SOL/USDT 0.8792 / -1.1395, BNB/USDT 0.6955 / -2.8661, XRP/USDT 0.8006 / -1.8986.
- Cost stress (2x): base 0.6906 → 0.4691, Sharpe 0.8550 → -0.7038, max DD 1.89 → 4.09 (from `results/20261019_062710_cost_stress/summary.md`).
- Tests: 16/16 pass (`python -m pytest tests/ -q`).
- Tracked git tree clean; only untracked `__pycache__/` directories present.
- Final artifacts (immutable): `results/FINAL_DECISION.md`, `results/RESEARCH_CONCLUSION.md`, `results/robustness_summary.md`, `results/20261019_064215_oos_pooled/summary.json`.

## Constraints (Critical)
- Any new work requires a fresh, pre-registered hypothesis card (theoretical rationale + falsifiable acceptance criteria) before implementation (PROMPT.md §3.4; `results/FINAL_DECISION.md`).
- Do not modify, overwrite, or re-run scripts that produced final artifacts unless the new hypothesis explicitly requires it and you have explicit authorization.
- If no new authorized hypothesis is provided, stand down with no changes.

## Ground Truth
Research artifacts are immutable. The decision is final. Only work on the repo if the user supplies a new pre-registered hypothesis card.

## Handoff Notes
- Verified 2026-10-19T12:29:25Z UTC: Read durable handoff, re-verified tests 16/16 (`python -m pytest tests/ -q`), confirmed git tracked tree clean (only `__pycache__/` untracked), validated OOS metrics (666 trades, net PF 0.6890, Sharpe -1.9443, max DD 0.6663; per-symbol values match). Decision remains CONCLUDED and REJECTED. No code changes made. Standing down; awaiting new pre-registered hypothesis.

## Validation Command
`python -m pytest tests/ -q`
