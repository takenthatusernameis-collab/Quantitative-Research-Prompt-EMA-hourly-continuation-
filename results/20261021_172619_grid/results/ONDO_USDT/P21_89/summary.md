# EMA Hourly Continuation — ONDO/USDT P21_89

**Symbol:** ONDO/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.8561 |
| net_win_rate | 0.5056 |
| gross_profit_factor | 1.0352 |
| gross_win_rate | 0.5056 |
| sharpe_ratio | -1.1133 |
| sortino_ratio | -0.3377 |
| max_drawdown | 0.4537 |
| cagr | -0.1460 |
| net_avg_win | 86.1106 |
| net_avg_loss | -102.8615 |
| avg_hold_time_bars | 15.3826 |
| exposure | 0.3125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
