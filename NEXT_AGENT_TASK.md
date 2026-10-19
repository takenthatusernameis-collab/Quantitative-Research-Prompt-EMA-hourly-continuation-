# NEXT AGENT TASK

## Prior Task Status
**COMPLETED**. The EMA hourly continuation research is **CONCLUDED** and **REJECTED** (no live trading).

## Current State (Verified)
- Tests: 16/16 passed (`python -m pytest tests/ -q`).
- Git: tracked tree clean; only untracked `__pycache__/` directories present.
- Final artifacts (immutable):
  - `results/FINAL_DECISION.md` (decision: REJECTED; no live trading)
  - `results/RESEARCH_CONCLUSION.md` (research concluded; no further experiments without new hypothesis)
  - `results/robustness_summary.md`
  - `results/20261019_064215_oos_pooled/summary.json`
- OOS pooled (net-of-costs): 666 trades, net PF 0.6890, net Sharpe -1.9443, max DD 0.6663.
- Per-symbol (net PF): BTC 0.6860, ETH 0.7861, SOL 0.8792, BNB 0.6955, XRP 0.8006 (all < 1).
- Cost stress (2x): base 0.6906 → 0.4691; Sharpe 0.8550 → -0.7038; max DD 1.89 → 4.09.
- ATR grid (OOS): atr 0.5 (826 tr, PF 0.6354, Sharpe -2.1419), atr 1.0 (517 tr, PF 0.6501, Sharpe -2.0586), atr 1.5 (302 tr, PF 0.7922, Sharpe -1.2193).
- Same-bar exit delta: PF 0.6890→0.6952, Sharpe -1.9443→-1.9169 (negligible).

## Handoff Notes
- Prior agent task fully completed. Validation performed: tests 16/16 pass, git tracked clean (only `__pycache__/` untracked), OOS metrics match `results/20261019_064215_oos_pooled/summary.json`, cost stress consistent, and all final artifacts exist and are consistent with `results/FINAL_DECISION.md`.
- Research artifacts are immutable. Decision is FINAL and REJECTED per `results/FINAL_DECISION.md`.
- No further experiments authorized for the rejected baseline.

## Next Task (for next agent)
No active task. Stand down.
- Do NOT re-run backtests, parameter searches, or tuning of the rejected baseline.
- If the user provides a new pre-registered hypothesis (theoretical rationale + falsifiable acceptance criteria), start by validating it against `PROMPT.md` §3.4 and the final artifacts above. Only then proceed with implementation, with explicit authorization as required.
- If no new authorized hypothesis is provided, stand down with no changes.

## Initial Task Message (copy-ready for next agent)
```
No active task. EMA hourly continuation research is CONCLUDED and REJECTED (no live trading).
Verified: tests 16/16 pass (python -m pytest tests/ -q); git tracked tree clean (only __pycache__ untracked); final artifacts in results/ (FINAL_DECISION.md, RESEARCH_CONCLUSION.md, robustness_summary.md, 20261019_064215_oos_pooled/summary.json) match OOS metrics (666 trades, net PF 0.6890, net Sharpe -1.9443, max DD 0.6663; per-symbol net PF BTC 0.6860, ETH 0.7861, SOL 0.8792, BNB 0.6955, XRP 0.8006). Cost stress consistent (0.6906→0.4691, Sharpe 0.8550→-0.7038, max DD 1.89→4.09).
Do NOT run backtests/parameter searches/tuning of the rejected baseline. If the user provides a new pre-registered hypothesis (theoretical rationale + falsifiable acceptance criteria), start by validating it against PROMPT.md §3.4 and final artifacts; otherwise stand down with no changes.
```

## Validation Command
`python -m pytest tests/ -q`
