# EMA Hourly Continuation — CELO/USDT P8_144

**Symbol:** CELO/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.8870 |
| net_win_rate | 0.5148 |
| gross_profit_factor | 1.0585 |
| gross_win_rate | 0.5148 |
| sharpe_ratio | -0.7651 |
| sortino_ratio | -0.2108 |
| max_drawdown | 0.3630 |
| cagr | -0.0958 |
| net_avg_win | 92.1915 |
| net_avg_loss | -110.2924 |
| avg_hold_time_bars | 45.2264 |
| exposure | 0.7593 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
