# EMA Hourly Continuation — RIO/USDT P55_100

**Symbol:** RIO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 732 |
| net_profit_factor | 0.4850 |
| net_win_rate | 0.3948 |
| gross_profit_factor | 0.7124 |
| gross_win_rate | 0.3989 |
| sharpe_ratio | -7.1085 |
| sortino_ratio | -2.6993 |
| max_drawdown | 0.9664 |
| cagr | -0.7374 |
| net_avg_win | 31.4189 |
| net_avg_loss | -42.2576 |
| avg_hold_time_bars | 4.2746 |
| exposure | 0.1437 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
