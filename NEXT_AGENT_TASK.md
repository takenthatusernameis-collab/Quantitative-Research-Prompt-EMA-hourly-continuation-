# NEXT AGENT TASK

## Objective
Stand down. The EMA hourly continuation research is **CONCLUDED** and **REJECTED** (no live trading). No active work to perform.

## Decision (Final)
- **Status**: CONCLUDED, REJECTED (no live trading)
- **Rationale**: Fails on OOS net-of-costs with negative Sharpe, PF < 1, and substantial drawdown; robustness/cost stress do not reach profitability.
- **Source**: `results/FINAL_DECISION.md`

## Current Verified State (2026-10-19T10:39:30Z UTC)
- **Tests**: 16/16 passed (`python -m pytest tests/ -q`)
- **Git**: Tracked tree clean; only untracked `__pycache__/` directories (backtest/, data/, signals/, tests/)
- **OOS Pooled** (`results/20261019_064215_oos_pooled/summary.json`): 666 trades, net PF 0.6890, net Sharpe -1.9443, max DD 0.6663
- **Per-symbol (net PF / net Sharpe / trades)**: BTC/USDT 0.6860 / -0.9004 / 124; ETH/USDT 0.7861 / -1.8710 / 119; SOL/USDT 0.8792 / -1.1395 / 132; BNB/USDT 0.6955 / -2.8661 / 150; XRP/USDT 0.8006 / -1.8986 / 141
- **Cost stress** (`results/20261019_062710_cost_stress/summary.md`): base PF 0.6906 → stress 0.4691; Sharpe 0.8550 → -0.7038; max DD 1.89 → 4.09
- **Final artifacts** (immutable): `results/FINAL_DECISION.md`, `results/RESEARCH_CONCLUSION.md`, `results/robustness_summary.md`, `results/20261019_064215_oos_pooled/summary.json`, `results/20261019_062710_cost_stress/summary.md`

## Constraints (Critical)
- Any new work requires a fresh, pre-registered hypothesis card (theoretical rationale + falsifiable acceptance criteria) before implementation (PROMPT.md §3.4; `results/FINAL_DECISION.md`).
- Do not modify, overwrite, or re-run scripts that produced final artifacts unless the new hypothesis explicitly requires it and you have explicit authorization.
- If no new authorized hypothesis is provided, **stand down with no changes**.

## Instructions for Next Agent
1. If the user provides a new pre-registered hypothesis (theoretical rationale + falsifiable acceptance criteria), start by validating it against PROMPT.md §3.4 and the final artifacts listed above. Only proceed if it justifies work beyond the rejected baseline and has explicit authorization.
2. Otherwise, stand down with no changes. Do not re-run backtests, parameter searches, or tuning of the rejected baseline.
3. Verify state with `python -m pytest tests/ -q` before concluding.

## Validation Command
`python -m pytest tests/ -q`
