# EMA Hourly Continuation — TNSR/USDT P89_200

**Symbol:** TNSR/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.6683 |
| net_win_rate | 0.4752 |
| gross_profit_factor | 0.9558 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -2.5041 |
| sortino_ratio | -0.6945 |
| max_drawdown | 0.5617 |
| cagr | -0.2763 |
| net_avg_win | 61.7315 |
| net_avg_loss | -83.6396 |
| avg_hold_time_bars | 13.6240 |
| exposure | 0.2361 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
