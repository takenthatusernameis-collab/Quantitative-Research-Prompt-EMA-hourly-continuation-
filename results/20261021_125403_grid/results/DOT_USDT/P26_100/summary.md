# EMA Hourly Continuation — DOT/USDT P26_100

**Symbol:** DOT/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.8369 |
| net_win_rate | 0.5160 |
| gross_profit_factor | 1.0645 |
| gross_win_rate | 0.5160 |
| sharpe_ratio | -1.1752 |
| sortino_ratio | -0.3537 |
| max_drawdown | 0.4362 |
| cagr | -0.1518 |
| net_avg_win | 76.8833 |
| net_avg_loss | -97.9373 |
| avg_hold_time_bars | 17.6233 |
| exposure | 0.3509 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
