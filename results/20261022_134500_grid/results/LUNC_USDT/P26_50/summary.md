# EMA Hourly Continuation — LUNC/USDT P26_50

**Symbol:** LUNC/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1043 |
| net_profit_factor | 0.2963 |
| net_win_rate | 0.4132 |
| gross_profit_factor | 0.6964 |
| gross_win_rate | 0.4430 |
| sharpe_ratio | -10.1255 |
| sortino_ratio | -4.6654 |
| max_drawdown | 0.9970 |
| cagr | -0.9005 |
| net_avg_win | 9.7375 |
| net_avg_loss | -23.1478 |
| avg_hold_time_bars | 3.1879 |
| exposure | 0.1511 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
