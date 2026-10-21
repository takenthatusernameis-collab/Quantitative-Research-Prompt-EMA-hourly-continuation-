# EMA Hourly Continuation — GALA/USDT P12_55

**Symbol:** GALA/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 604 |
| net_profit_factor | 0.7199 |
| net_win_rate | 0.4752 |
| gross_profit_factor | 0.9060 |
| gross_win_rate | 0.4752 |
| sharpe_ratio | -2.5977 |
| sortino_ratio | -0.9101 |
| max_drawdown | 0.6815 |
| cagr | -0.3419 |
| net_avg_win | 58.2487 |
| net_avg_loss | -73.2524 |
| avg_hold_time_bars | 12.1987 |
| exposure | 0.3349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
