# INITIAL TASK FOR NEXT AGENT

**Status:** No active task. EMA hourly continuation research is CONCLUDED and REJECTED (no live trading).

## Current State
- Tests: 16/16 passed (`python -m pytest tests/ -q`) — verified 2026-10-19T10:51:19Z UTC
- Git: Clean tracked tree; only untracked `__pycache__/` in backtest/, data/, signals/, tests/
- OOS pooled (final): 666 trades, net PF 0.6890, net Sharpe -1.9443, max DD 0.6663
- Per-symbol (net PF): BTC 0.6860, ETH 0.7861, SOL 0.8792, BNB 0.6955, XRP 0.8006
- Cost stress (2x): PF 0.6906→0.4691, Sharpe 0.8550→-0.7038, max DD 1.89→4.09

## Key Artifacts
- `results/FINAL_DECISION.md` — final decision (REJECTED)
- `results/RESEARCH_CONCLUSION.md` — research conclusion
- `results/robustness_summary.md` — robustness checks
- `results/20261019_064215_oos_pooled/summary.json` — OOS pooled results
- `results/20261019_062710_cost_stress/summary.md` — cost stress results

## Instructions
1. If the user provides a new pre-registered hypothesis (theoretical rationale + falsifiable acceptance criteria), validate it against PROMPT.md §3.4 and the final artifacts before proceeding. Only proceed if it justifies work beyond the rejected baseline and is explicitly authorized.
2. Otherwise, **stand down with no changes**. Do not re-run backtests, parameter searches, or tuning of the rejected baseline.
3. Before concluding, verify state with `python -m pytest tests/ -q`.

## Validation Command
`python -m pytest tests/ -q`
