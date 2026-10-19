# NEXT AGENT TASK

## Status (Updated)
COMPLETED: Minimal, reproducible implementation of EMA hourly continuation strategy per PROMPT.md.

## Implementation Summary
- Scaffolded modules: data/, signals/, backtest/, metrics/, universe/, scripts/, tests/
- Data: CSV loader with OHLCV normalization (timestamp/open/high/low/close/volume)
- Universe: Market cap ranking via JSON; processed in market-cap descending order
- Signals: EMA50/EMA100, confirmed closed-bar cross detection (close[t-1]<=EMA50[t-1] and close[t]>EMA50[t] for long with EMA50>EMA100; mirror for short). Warm-up enforced (>=100 bars). EMAs equal -> no signals. Risk-based filtering.
- Backtest: SL/TP at 1:1 RR with risk = |entry - EMA100[t]|; skip if risk <= 0/pathological. Long SL=entry-risk, TP=entry+risk. Same-bar conflict: prioritize SL (adverse) when both hit. One position per symbol. Taker fee + slippage per side (configurable; defaults 10 bps + 2 bps). Tracks gross and net PnL.
- Metrics: Sharpe/Sortino, max drawdown, CAGR, profit factor (gross/net), win rate (gross/net), avg win/loss (gross/net), trade count, per-symbol + pooled.
- Artifacts: config.json, trades.csv, equity.csv, summary.json, summary.md in results/<timestamp>
- Runner: scripts/run_baseline.py with --fixture, --mcap, --n, --taker-fee-bps, --slippage-bps

## Acceptance Criteria Met
- python -m pytest -v passes (7/7)
- Baseline produces all required artifacts with gross and net metrics
- Confirmed closed-bar logic; warm-up enforced; no trades when EMAs equal or risk pathological
- Market-cap descending order enforced and documented
- README documents data source, fill assumption, cost model, timezone, universe selection

## Next Agent Task
Focus on robustness, validation, and extensibility:

1. **Parameterization & Config**
- Add YAML/JSON config file (e.g. config/default.yaml) for EMA periods, costs, filters
- Support overriding via CLI and config
- Add validation

2. **Data Quality & Edge Cases**
- Add tests for same-bar conflict (SL vs TP) - current logic prioritizes SL on conflict; make explicit and test
- Add tests for risk=0/pathological cases
- Handle missing data, NaNs, duplicates
- Add data validation

3. **Execution Logic Refinement**
- Verify SL/TP hit logic matches spec exactly (using high/low; confirm entry timing)
- Consider alternative same-bar conflict rules? Document clearly
- Test short-side scenarios more thoroughly

4. **Metrics & Reporting**
- Annualize Sharpe/Sortino properly for hourly bars (or document assumption)
- Add exposure, avg hold time calculation (currently partial)
- Add rolling metrics, drawdown duration
- Improve pooled equity calculation (currently averaged across symbols)

5. **Research Extensions**
- Add walk-forward / rolling window support?
- Add parameter optimization (grid search) with OOS
- Add transaction cost sensitivity analysis
- Generate plots (optional)

## Quick Start
```bash
export PATH=$HOME/.local/bin:$PATH
cd /home/runner/work/Quantitative-Research-Prompt-EMA-hourly-continuation-/Quantitative-Research-Prompt-EMA-hourly-continuation-
PYTHONPATH=$(pwd) python3 -m pytest -v
PYTHONPATH=$(pwd) python3 scripts/run_baseline.py --fixture data/fixtures/sample_hourly.csv --mcap universe/mcap_rank.json --n 3
```

## Notes
- Synthetic fixture available at data/fixtures/sample_hourly.csv
- mcap rank at universe/mcap_rank.json
- All changes are minimal and testable.
