# EMA Hourly Continuation — CWEB/USDT P21_200

**Symbol:** CWEB/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 270 |
| net_profit_factor | 0.7519 |
| net_win_rate | 0.5074 |
| gross_profit_factor | 1.0596 |
| gross_win_rate | 0.5111 |
| sharpe_ratio | -1.5855 |
| sortino_ratio | -0.3683 |
| max_drawdown | 0.4497 |
| cagr | -0.1626 |
| net_avg_win | 79.5400 |
| net_avg_loss | -108.9697 |
| avg_hold_time_bars | 55.8444 |
| exposure | 0.6854 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
