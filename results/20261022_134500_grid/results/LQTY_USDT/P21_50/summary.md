# EMA Hourly Continuation — LQTY/USDT P21_50

**Symbol:** LQTY/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1015 |
| net_profit_factor | 0.5031 |
| net_win_rate | 0.4591 |
| gross_profit_factor | 0.8676 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -6.6788 |
| sortino_ratio | -3.0041 |
| max_drawdown | 0.9746 |
| cagr | -0.7637 |
| net_avg_win | 21.1540 |
| net_avg_loss | -35.6924 |
| avg_hold_time_bars | 5.1901 |
| exposure | 0.2384 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
