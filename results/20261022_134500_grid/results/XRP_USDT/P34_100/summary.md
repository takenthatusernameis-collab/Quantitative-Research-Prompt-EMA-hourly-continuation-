# EMA Hourly Continuation — XRP/USDT P34_100

**Symbol:** XRP/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 655 |
| net_profit_factor | 0.3989 |
| net_win_rate | 0.4305 |
| gross_profit_factor | 0.8949 |
| gross_win_rate | 0.4641 |
| sharpe_ratio | -6.8491 |
| sortino_ratio | -2.4810 |
| max_drawdown | 0.9585 |
| cagr | -0.7070 |
| net_avg_win | 22.4573 |
| net_avg_loss | -42.5591 |
| avg_hold_time_bars | 9.2901 |
| exposure | 0.2766 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
