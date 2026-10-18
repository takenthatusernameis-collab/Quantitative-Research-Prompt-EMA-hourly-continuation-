# NEXT AGENT TASK

## Objective
Establish a minimal, reproducible implementation of the EMA hourly continuation strategy per PROMPT.md, with realistic crypto costs and market-cap descending processing.

## Current State
- Repo contains PROMPT.md (full specification), README.md, workflow, and diagnostics state.
- No implementation modules yet (no data, signals, backtest, metrics, universe).
- No tests, no config, no artifacts.

## Task (Prioritize cheapest correct path)
1. **Scaffold modules**: Create `data/`, `signals/`, `backtest/`, `metrics/`, `universe/`, `scripts/`, `tests/` dirs with `__init__.py` and minimal README.
2. **Data ingestion**: Design a simple data interface for hourly OHLCV. For baseline, implement support for:
   - Local CSVs (OHLCV columns: timestamp/close/open/high/low/volume)
   - Document source, timezone, universe selection approach in `data/README.md`
   If free public data access is feasible via ccxt/pycoingecko/yfinance, add minimal code; otherwise add a clear "data fixture" template + instructions in `NEXT_AGENT_TASK.md` for next agent.
3. **Universe by market cap**: Add code to rank symbols by market cap desc. If live market cap fetch unavailable, allow loading from a `universe/mcap_rank.json` file with structure `{ "updated_at": "...", "symbols": ["BTC/USDT", "ETH/USDT", ...] }`. Process in that order.
4. **Indicators & signals**: Implement EMA50/EMA100 (pandas or pure Python). Detect long cross: close[t-1]<=EMA50[t-1] and close[t]>EMA50[t] with bullish regime EMA50>EMA100; mirror for short. Enforce warm-up (>=100 bars).
5. **Backtest engine**: Confirmed closed-bar only. SL/TP at 1:1 RR where risk = |entry - EMA100[t]| on signal bar; skip trade if risk <= 0 or pathological. Long: SL=entry-risk, TP=entry+risk (so SL at EMA100 when entry above). Choose one fill assumption (e.g. signal-bar close fill with next-bar exit logic) and document it. Use high/low for stop/target hits; define conservative same-bar conflict (adverse first). One position per symbol.
6. **Costs**: Baseline costs - taker fee and slippage per side (configurable). Report gross and net. Start with conservative defaults (e.g. 10 bps taker + 2 bps slippage per side) and make them overrideable via config.
7. **Metrics**: Compute net metrics: Sharpe/Sortino (simple returns on equity curve), max drawdown, CAGR, PF, win rate, avg win/loss, trade count, avg hold, exposure. Per-symbol + pooled.
8. **Config + artifacts**: Save run config (JSON), trade blotter (CSV), equity curve (CSV), summary (JSON/Markdown). Include timestamped `results/` folder.
9. **Tests**: Add unit tests for EMA, cross detection, SL/TP geometry, same-bar conflict rule.
10. **Minimal runner**: Add `scripts/run_baseline.py` that runs over top N by mcap and writes all artifacts.

## Acceptance Criteria
- `python -m pytest -v` passes all unit tests.
- Running baseline (even on synthetic/small fixture data) produces: `config.json`, `trades.csv`, `equity.csv`, `summary.json`, `summary.md` in results/<timestamp> with gross and net metrics present.
- Signals use confirmed closed-bar logic; warm-up enforced; no trades when EMAs equal or risk pathological.
- Processing is in market-cap descending order (enforced/documented).
- README documents data source, fill assumption, cost model, timezone, universe selection.

## Validation Commands
```bash
python -m pytest -v
python scripts/run_baseline.py --help 2>/dev/null || echo "add --help"
# If fixture exists: python scripts/run_baseline.py --fixture data/fixtures/sample_hourly.csv --mcap data/universe/mcap_rank.json --n 3
```

## Notes
- Do not invent live market data if unavailable; create a small synthetic fixture + mcap rank so tests run offline.
- Keep changes minimal and testable. Follow existing code style in repo (but repo empty; use clean Python).
