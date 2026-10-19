# NEXT AGENT TASK

## Status: OPEN

## Ground Truth
Baseline EMA hourly continuation is **REJECTED** — no live trading.
- `results/FINAL_DECISION.md`: pooled OOS 666 trades, net PF 0.6890, net Sharpe -1.9443, max DD 0.6663. Cost stress worsens results; no robustness variant reaches profitability.
- Tests: 16/16 pass (`python -m pytest tests/`).
- Git: clean, up to date with `origin/main`.

## Objective for Next Agent
Decide whether to (a) pursue a **new, pre-specified hypothesis** for crypto hourly research, or (b) conclude research. Do NOT re-run parameter searches on the rejected baseline.

## Key Files to Review
- `PROMPT.md` (strategy specification & research process)
- `README.md` (project context, data source, fill assumption, cost model)
- `results/FINAL_DECISION.md` (final decision — REJECTED, with robustness detail)
- `results/robustness_summary.md` (tuned config sweep, walk-forward, OOS)
- `backtest/`, `scripts/`, `tests/`, `signals/`, `metrics/`, `data/`, `universe/` (implementation)
- `data/fixtures/` (real hourly OHLCV, tracked — keep as-is)
- `config/default.json` (configuration)

## Instructions
1. Read `FINAL_DECISION.md` and `PROMPT.md` sections 3 (research process) and 5 (extensions) before any new work.
2. If pursuing new work, formulate **one** new pre-specified hypothesis **before** implementing:
   - Clear theoretical rationale (mechanism + why it might work)
   - Falsifiable acceptance criteria, pre-registered (e.g. specific net PF / net Sharpe / max DD / trade-count thresholds on OOS)
   - Justification for any signal/filter/exit change vs the baseline
   - Document the hypothesis card in `results/` (new file) before implementation
3. Do NOT continue tuning the rejected EMA 50/100 baseline. Only test the new hypothesis.
4. Keep data/fixtures as-is (tracked). Do not fabricate market data, metrics, or sources.
5. Run tests to validate any changes: `python -m pytest tests/ -v`
6. Record parent config → child config → delta metrics for each controlled mutation (PROMPT.md §5).
7. Persist reproducible artifacts (config, trade blotter, equity/returns, summary metrics, reproduce commands) and leave a narrow `NEXT_AGENT_TASK.md` handoff with acceptance criteria and validation commands when done.

## Acceptance Criteria (for any new hypothesis to be considered complete)
- Hypothesis card written and pre-registered in `results/` before testing.
- Net-of-costs OOS metrics reported (gross + net), per-symbol and pooled.
- Acceptance criteria met or explicitly falsified with evidence.
- Tests pass: `python -m pytest tests/ -q`
- Handoff updated (`NEXT_AGENT_TASK.md`) with result and next steps.

## Validation Command
`python -m pytest tests/ -q`

## Handoff Date
2026-10-19T07:00:40Z
