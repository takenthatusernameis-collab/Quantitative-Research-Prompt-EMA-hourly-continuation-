# EMA Hourly Continuation — COMP/USDT P8_100

**Symbol:** COMP/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 567 |
| net_profit_factor | 0.6154 |
| net_win_rate | 0.4956 |
| gross_profit_factor | 0.9951 |
| gross_win_rate | 0.5097 |
| sharpe_ratio | -3.2545 |
| sortino_ratio | -1.0879 |
| max_drawdown | 0.7452 |
| cagr | -0.4071 |
| net_avg_win | 41.6116 |
| net_avg_loss | -66.4396 |
| avg_hold_time_bars | 27.8113 |
| exposure | 0.7168 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
