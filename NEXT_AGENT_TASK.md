# NEXT AGENT TASK

## Objective
No active task. The EMA hourly continuation research is **CONCLUDED** and **REJECTED** (no live trading).

If the user provides no new pre-registered hypothesis, stand down with no changes. Do not re-run backtests, parameter searches, or tuning of the rejected baseline without explicit authorization.

## Current State
- Decision: **REJECTED** / **CONCLUDED** (no live trading).
- OOS pooled (net-of-costs): 666 trades, net PF 0.6890, net Sharpe -1.9443, max DD 0.6663 from `results/20261019_064215_oos_pooled/summary.json`.
- Per-symbol (net PF): BTC 0.6860, ETH 0.7861, SOL 0.8792, BNB 0.6955, XRP 0.8006 (all < 1).
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
- Handoff verified/completed by this session (2026-10-19T12:25:41Z UTC). Tests re-verified (16/16 via `python -m pytest tests/ -q`). Git state: tracked tree clean, only `__pycache__/` untracked. All artifacts verified consistent (OOS pooled 666 trades, net PF 0.6890, net Sharpe -1.9443, max DD 0.6663; per-symbol net PF BTC 0.6860, ETH 0.7861, SOL 0.8792, BNB 0.6955, XRP 0.8006; cost stress 0.6906→0.4691, Sharpe 0.8550→-0.7038, max DD 1.89→4.09).

## Initial Task for Next Agent (copy-ready)
> "No active task. EMA hourly continuation research is CONCLUDED and REJECTED (no live trading). Verified: tests 16/16 pass (`python -m pytest tests/ -q`); git tracked tree clean (only __pycache__/ untracked); final artifacts in results/ (FINAL_DECISION.md, RESEARCH_CONCLUSION.md, robustness_summary.md, 20261019_064215_oos_pooled/summary.json) match OOS metrics (666 trades, net PF 0.6890, net Sharpe -1.9443, max DD 0.6663; per-symbol net PF BTC 0.6860, ETH 0.7861, SOL 0.8792, BNB 0.6955, XRP 0.8006). Cost stress consistent (0.6906→0.4691, Sharpe 0.8550→-0.7038, max DD 1.89→4.09). Decision FINAL and REJECTED per results/FINAL_DECISION.md. Handoff verified 2026-10-19T12:25:41Z UTC. Do NOT run backtests/parameter searches/tuning of the rejected baseline without explicit authorization. If the user provides a new pre-registered hypothesis (theoretical rationale + falsifiable acceptance criteria), start by validating it against PROMPT.md §3.4 and final artifacts; otherwise stand down with no changes. Validation: python -m pytest tests/ -q"

## Validation Command
`python -m pytest tests/ -q`
