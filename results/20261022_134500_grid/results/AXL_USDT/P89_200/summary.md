# EMA Hourly Continuation — AXL/USDT P89_200

**Symbol:** AXL/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.6136 |
| net_win_rate | 0.4535 |
| gross_profit_factor | 0.8608 |
| gross_win_rate | 0.4626 |
| sharpe_ratio | -3.3314 |
| sortino_ratio | -0.9812 |
| max_drawdown | 0.6969 |
| cagr | -0.3722 |
| net_avg_win | 54.8637 |
| net_avg_loss | -74.1991 |
| avg_hold_time_bars | 11.6689 |
| exposure | 0.2329 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
