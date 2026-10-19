# EMA Hourly Continuation Strategy

A quantitative research implementation of an EMA hourly continuation strategy on cryptocurrency markets.

## Components

- `data/`: Data ingestion and management
- `signals/`: EMA indicators and signal generation (confirmed closed-bar only)
- `backtest/`: Backtesting engine with costs, slippage, and execution logic
- `metrics/`: Performance metrics (net and gross)
- `universe/`: Market cap-based universe selection
- `scripts/`: Run scripts and utilities
- `tests/`: Unit tests

## Data Source

By default, this implementation uses local CSV files for offline reproducibility. Data fixtures should contain hourly OHLCV with columns: `timestamp` (or `date`/`time`), `open`, `high`, `low`, `close`, `volume`. Timezone must be documented per dataset. If live data is needed, the interface can be extended (see data/README.md).

## Fill Assumption

Confirmed closed-bar only. Signals are generated after bar `t` closes (using close[t], EMA50[t], EMA100[t] with comparison to t-1). Entry is taken at the signal bar's close price (close[t]) by default, with next-bar exit logic for stop/target hits checked against high/low. Same-bar conflict resolution: if both stop and target would be hit on the same bar, treat as adverse first (see backtest implementation). One position per symbol.

## Cost Model

Trading costs include taker fees and slippage per side, configurable. Defaults: 10 bps taker fee + 2 bps slippage per side (i.e., 0.0010 + 0.0002 per trade side). Report both gross and net metrics.

## Universe Selection

Symbols are processed in market cap descending order. Market cap can be loaded from `universe/mcap_rank.json` with structure: `{"updated_at": "...", "symbols": ["BTC/USDT", ...]}`. If live market cap fetch is unavailable, use fixture files.

## Processing Order

All symbols are processed in market cap descending order as specified in the strategy.
