# INITIAL TASK FOR NEXT AGENT

**Status:** No active task. EMA hourly continuation research is CONCLUDED and REJECTED (no live trading). Last verified 2026-10-19T12:10:48Z UTC.

## Current State
- Tests: 16/16 passed (`python -m pytest tests/ -q`) — verified 2026-10-19T12:10:48Z UTC
- Git: Clean tracked tree; only untracked `__pycache__/` in backtest/, data/, signals/, tests/
- OOS pooled (final): 666 trades, net PF 0.6890, net Sharpe -1.9443, max DD 0.6663 (`results/20261019_064215_oos_pooled/summary.json`)
- Per-symbol (net PF): BTC 0.6860, ETH 0.7861, SOL 0.8792, BNB 0.6955, XRP 0.8006
- Cost stress (2x): PF 0.6906→0.4691, Sharpe 0.8550→-0.7038, max DD 1.89→4.09 (`results/20261019_062710_cost_stress/summary.md`)

## Key Artifacts
- `results/FINAL_DECISION.md` — final decision (REJECTED) and recommendation (no live trading)
- `results/RESEARCH_CONCLUSION.md` — research conclusion
- `results/robustness_summary.md` — robustness checks performed
- `results/20261019_064215_oos_pooled/summary.json` — final OOS pooled results
- `results/20261019_062710_cost_stress/summary.md` — cost stress results

## Instructions
1. If the user provides a new pre-registered hypothesis (theoretical rationale + falsifiable acceptance criteria), validate it against PROMPT.md §3.4 and the final artifacts before proceeding. Only proceed if it justifies work beyond the rejected baseline and is explicitly authorized.
2. Otherwise, **stand down with no changes**. Do not re-run backtests, parameter searches, or tuning of the rejected baseline.
3. Before concluding, verify state with `python -m pytest tests/ -q`.

## Validation Command
`python -m pytest tests/ -q`

---

# CLEAR INITIAL TASK MESSAGE FOR THE NEXT AGENT

**Task:** Stand by. No active work is authorized. The EMA hourly continuation research is concluded and rejected (no live trading); do not re-run backtests, parameter searches, or tuning of the rejected baseline unless the user supplies a new authorized pre-registered hypothesis.

**Context to read first:**
- `README.md` — project overview, components, cost model, fill assumptions, universe selection
- `PROMPT.md` — research protocol, including §3.4 (hypothesis registration and validation rules)
- `NEXT_AGENT_TASK.md` — durable handoff with full session history and constraints
- `results/FINAL_DECISION.md` — the final decision (REJECTED) and recommendation
- `results/RESEARCH_CONCLUSION.md` — research conclusion
- `results/robustness_summary.md` — robustness checks performed

**Current state (re-verified this session):**
- Tests: 16/16 passed (`python -m pytest tests/ -q`)
- Git: Clean tracked tree (only untracked `__pycache__/` directories)
- Research outcome: CONCLUDED, REJECTED — no live trading recommended
- Final OOS pooled: 666 trades, net PF 0.6890, net Sharpe -1.9443, max DD 0.6663
- Cost stress (2x): PF 0.6906→0.4691, Sharpe 0.8550→-0.7038, max DD 1.89→4.09

**What to do:**
1. Check for a new, user-provided pre-registered hypothesis (must include theoretical rationale + falsifiable acceptance criteria).
2. If **none** is present: stand down with no code changes. Report the state above (tests pass, research concluded/rejected). Do not re-run backtests, parameter searches, or tuning of the rejected baseline.
3. If a hypothesis **is** provided: validate it against PROMPT.md §3.4 and the final artifacts. Only proceed if it is justified, falsifiable, and explicitly authorized. Do not modify or re-run scripts producing final artifacts unless the hypothesis explicitly requires it with authorization.
4. Verify state with `python -m pytest tests/ -q` before concluding.
5. Update `NEXT_AGENT_TASK.md` with the outcome (or keep it in standby). Do not commit unless explicitly requested.

**Constraints (from PROMPT.md §3.4 and FINAL_DECISION.md):**
- Any new work requires a fresh, pre-registered hypothesis before implementation.
- Do not modify, overwrite, or re-run scripts producing final artifacts without explicit authorization tied to the new hypothesis.
- If no new authorized hypothesis is provided: stand down with no changes.
