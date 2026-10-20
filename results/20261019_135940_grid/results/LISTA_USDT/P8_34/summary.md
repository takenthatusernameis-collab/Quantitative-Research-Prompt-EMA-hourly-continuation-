# EMA Hourly Continuation — LISTA/USDT P8_34

**Symbol:** LISTA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1149 |
| net_profit_factor | 0.6494 |
| net_win_rate | 0.4613 |
| gross_profit_factor | 0.9924 |
| gross_win_rate | 0.4743 |
| sharpe_ratio | -6.1971 |
| sortino_ratio | -3.0809 |
| max_drawdown | 0.9685 |
| cagr | -0.7659 |
| net_avg_win | 33.7730 |
| net_avg_loss | -44.5273 |
| avg_hold_time_bars | 6.3229 |
| exposure | 0.3552 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
