# EMA Hourly Continuation — ZEC/USDT P26_144

**Symbol:** ZEC/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 1.0114 |
| net_win_rate | 0.5472 |
| gross_profit_factor | 1.2010 |
| gross_win_rate | 0.5472 |
| sharpe_ratio | 0.1313 |
| sortino_ratio | 0.0361 |
| max_drawdown | 0.2406 |
| cagr | 0.0086 |
| net_avg_win | 97.4616 |
| net_avg_loss | -116.4610 |
| avg_hold_time_bars | 26.6583 |
| exposure | 0.4362 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
