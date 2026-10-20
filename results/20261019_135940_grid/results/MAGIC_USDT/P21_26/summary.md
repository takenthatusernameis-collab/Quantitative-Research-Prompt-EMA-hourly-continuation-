# EMA Hourly Continuation — MAGIC/USDT P21_26

**Symbol:** MAGIC/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1159 |
| net_profit_factor | 0.3373 |
| net_win_rate | 0.4003 |
| gross_profit_factor | 0.9474 |
| gross_win_rate | 0.4607 |
| sharpe_ratio | -11.8489 |
| sortino_ratio | -5.7809 |
| max_drawdown | 0.9994 |
| cagr | -0.9485 |
| net_avg_win | 10.9609 |
| net_avg_loss | -21.6979 |
| avg_hold_time_bars | 2.4193 |
| exposure | 0.1275 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
