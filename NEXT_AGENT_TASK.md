# NEXT AGENT TASK

## Status
**COMPLETED** - EMA hourly continuation research concluded and rejected. No live trading.

## Final Decision
- Status: CONCLUDED, REJECTED (no live trading)
- Rationale: Fails OOS net-of-costs with negative Sharpe, PF < 1, substantial drawdown. Robustness and cost stress do not reach profitability.
- Details: `results/FINAL_DECISION.md`

## Verified State (2026-10-19T11:00:50Z UTC)
- Tests: 16/16 passed (`python -m pytest tests/ -q`)
- Git: Clean tracked tree; only untracked `__pycache__/` in backtest/, data/, signals/, tests/
- OOS Pooled (`results/20261019_064215_oos_pooled/summary.json`): 666 trades, net PF 0.6890, net Sharpe -1.9443, max DD 0.6663
- Per-symbol (net PF / net Sharpe / trades): BTC/USDT 0.6860/-0.9004/124, ETH/USDT 0.7861/-1.8710/119, SOL/USDT 0.8792/-1.1395/132, BNB/USDT 0.6955/-2.8661/150, XRP/USDT 0.8006/-1.8986/141
- Cost stress (`results/20261019_062710_cost_stress/summary.md`): PF 0.6906→0.4691, Sharpe 0.8550→-0.7038, max DD 1.89→4.09

## Final Artifacts
- `results/FINAL_DECISION.md` (final decision & recommendation)
- `results/RESEARCH_CONCLUSION.md` (conclusion)
- `results/robustness_summary.md` (robustness)
- `results/20261019_064215_oos_pooled/` (OOS pooled results)
- `results/20261019_062710_cost_stress/` (cost stress results)

## Constraints
- Any new work requires a fresh, pre-registered hypothesis (theoretical rationale + falsifiable acceptance criteria) before implementation (PROMPT.md §3.4; results/FINAL_DECISION.md).
- Do not modify, overwrite, or re-run scripts producing final artifacts unless the new hypothesis explicitly requires it with authorization.
- If no new authorized hypothesis is provided: stand down with no changes.

## Instructions for Next Agent
1. If user provides new pre-registered hypothesis (theory + falsifiable acceptance criteria), validate against PROMPT.md §3.4 and final artifacts. Only proceed if justified and authorized.
2. Else stand down with no changes. Do not re-run backtests, parameter searches, or tuning of rejected baseline.
3. Run `python -m pytest tests/ -q` to verify state.

## Validation
`python -m pytest tests/ -q`

(End of file - total 36 lines)