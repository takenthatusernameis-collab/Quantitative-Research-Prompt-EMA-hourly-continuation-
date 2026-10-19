# EMA Hourly Continuation — SAND/USDT P20_21

**Symbol:** SAND/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1170 |
| net_profit_factor | 0.1004 |
| net_win_rate | 0.2573 |
| gross_profit_factor | 0.5678 |
| gross_win_rate | 0.3538 |
| sharpe_ratio | -19.1713 |
| sortino_ratio | -10.3376 |
| max_drawdown | 1.0000 |
| cagr | -0.9971 |
| net_avg_win | 3.7073 |
| net_avg_loss | -12.7916 |
| avg_hold_time_bars | 1.5282 |
| exposure | 0.0813 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
