# EMA Hourly Continuation — ORCA/USDT P21_34

**Symbol:** ORCA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.6289 |
| net_win_rate | 0.4839 |
| gross_profit_factor | 0.9722 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -3.2150 |
| sortino_ratio | -0.9584 |
| max_drawdown | 0.6895 |
| cagr | -0.3589 |
| net_avg_win | 54.2760 |
| net_avg_loss | -80.9077 |
| avg_hold_time_bars | 5.6452 |
| exposure | 0.1114 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
