# EMA Hourly Continuation — MTL/USDT P89_200

**Symbol:** MTL/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.4679 |
| net_win_rate | 0.4290 |
| gross_profit_factor | 0.7804 |
| gross_win_rate | 0.4536 |
| sharpe_ratio | -4.2345 |
| sortino_ratio | -1.1300 |
| max_drawdown | 0.7551 |
| cagr | -0.4245 |
| net_avg_win | 42.1034 |
| net_avg_loss | -67.5992 |
| avg_hold_time_bars | 14.2240 |
| exposure | 0.2356 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
