# EMA Hourly Continuation — FLIP/USDT P12_50

**Symbol:** FLIP/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.6413 |
| net_win_rate | 0.4683 |
| gross_profit_factor | 0.9159 |
| gross_win_rate | 0.4741 |
| sharpe_ratio | -3.5720 |
| sortino_ratio | -1.1545 |
| max_drawdown | 0.7500 |
| cagr | -0.4195 |
| net_avg_win | 54.5772 |
| net_avg_loss | -74.9660 |
| avg_hold_time_bars | 17.1766 |
| exposure | 0.4068 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
