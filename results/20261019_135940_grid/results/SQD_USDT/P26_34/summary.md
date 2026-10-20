# EMA Hourly Continuation — SQD/USDT P26_34

**Symbol:** SQD/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 976 |
| net_profit_factor | 0.4769 |
| net_win_rate | 0.4303 |
| gross_profit_factor | 0.9522 |
| gross_win_rate | 0.4508 |
| sharpe_ratio | -9.1760 |
| sortino_ratio | -4.1230 |
| max_drawdown | 0.9936 |
| cagr | -0.8754 |
| net_avg_win | 21.5689 |
| net_avg_loss | -34.1642 |
| avg_hold_time_bars | 2.4764 |
| exposure | 0.1136 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
