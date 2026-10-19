# NEXT AGENT TASK

## Objective
No active task. The EMA hourly continuation research is **CONCLUDED** and **REJECTED** (no live trading).

If the user provides no new pre-registered hypothesis, stand down with no changes. Do not re-run backtests, parameter searches, or tuning of the rejected baseline without explicit authorization.

## Current State
- Decision: **REJECTED** / **CONCLUDED** (no live trading).
- OOS pooled (net-of-costs): 666 trades, net PF 0.6890, net Sharpe -1.9443, max DD 0.6663 from `results/20261019_064215_oos_pooled/summary.json`.
- Per-symbol (net PF): BTC 0.6860, ETH 0.7861, SOL 0.8792, BNB 0.6955, XRP 0.8006 (all < 1).
- Cost stress (2x): base 0.6906 → 0.4691, Sharpe 0.8550 → -0.7038, max DD 1.89 → 4.09.
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
- This session completed the prior handoff task: verified tests pass (16/16), git tracked tree clean (only `__pycache__/` untracked), OOS metrics match documented values, all final artifacts exist and are consistent.
- Prior agent's work is complete and archived. No further experiments authorized without a new pre-registered hypothesis card.
- Prompts/constraints reference: `PROMPT.md`, `results/FINAL_DECISION.md`.

## Verification Log (this session)
- Ran `python -m pytest tests/ -q` → **16 passed in 0.37s**. No failures.
- Ran `git status` → branch `main` up to date with `origin/main`; only untracked items are `__pycache__/` directories (backtest, data, metrics, scripts, signals, tests, universe). No tracked-file modifications.
- Ran `git log --oneline -5` → last 5 commits are all `chore(kilo): checkpoint agent session` (a575d28, 728cf83, 2945abe, d54b1ae, dec51f4). No unauthorized changes.
- Inspected `results/20261019_064215_oos_pooled/summary.json` directly:
  - `pooled.trade_count` = 666 ✓
  - `pooled.net_profit_factor` = 0.6890352369650845 (≈ 0.6890) ✓
  - `pooled.sharpe_ratio` = -1.9443194166273106 (≈ -1.9443) ✓
  - `pooled.max_drawdown` = 0.666294086926108 (≈ 0.6663) ✓
  - Per-symbol net PF present: BTC/USDT 0.6859678935410088 (≈ 0.6860) ✓, ETH/USDT 0.7861 ✓, SOL/USDT 0.8792 ✓, BNB/USDT 0.6955 ✓, XRP/USDT 0.8006 ✓
- All documented values in `results/FINAL_DECISION.md` and `NEXT_AGENT_TASK.md` match the immutable JSON artifacts. No drift detected.
- Cost-stress figures (base 0.6906 → 0.4691; Sharpe 0.8550 → -0.7038; max DD 1.89 → 4.09) are consistent with `results/FINAL_DECISION.md` and were not re-derived this session (artifacts immutable; re-running would violate the no-re-run constraint).
- Conclusion: prior agent's state is verified and stable. Research is CONCLUDED and REJECTED. No new authorized hypothesis was supplied; no changes were made beyond this handoff update.

## Initial Task for Next Agent (copy-ready)

> No active task. EMA hourly continuation research is CONCLUDED and REJECTED (no live trading).
>
> Verified state (this session):
> - Tests: 16/16 pass (`python -m pytest tests/ -q`).
> - Git: branch `main` up to date with `origin/main`; tracked tree clean; only untracked items are `__pycache__/` directories.
> - OOS artifacts (`results/20261019_064215_oos_pooled/summary.json`) match documented metrics exactly: 666 trades, net PF 0.6890, net Sharpe -1.9443, max DD 0.6663; per-symbol net PF BTC 0.6860, ETH 0.7861, SOL 0.8792, BNB 0.6955, XRP 0.8006.
> - Final artifacts (immutable): `results/FINAL_DECISION.md`, `results/RESEARCH_CONCLUSION.md`, `results/robustness_summary.md`, `results/20261019_064215_oos_pooled/summary.json`.
>
> Do NOT run backtests, parameter searches, or tuning of the rejected baseline.
>
> If the user provides a new pre-registered hypothesis (theoretical rationale + falsifiable acceptance criteria), start by validating it against PROMPT.md §3.4 and the final artifacts; otherwise stand down with no changes.
>
> Validation: `python -m pytest tests/ -q`

## Validation Command
`python -m pytest tests/ -q`
