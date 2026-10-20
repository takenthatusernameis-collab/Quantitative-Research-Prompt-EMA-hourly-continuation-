# EMA Hourly Continuation — PHA/USDT P144_200

**Symbol:** PHA/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 418 |
| net_profit_factor | 0.4316 |
| net_win_rate | 0.4211 |
| gross_profit_factor | 0.7776 |
| gross_win_rate | 0.4330 |
| sharpe_ratio | -5.1321 |
| sortino_ratio | -1.4908 |
| max_drawdown | 0.8401 |
| cagr | -0.5116 |
| net_avg_win | 36.0134 |
| net_avg_loss | -60.6813 |
| avg_hold_time_bars | 3.6818 |
| exposure | 0.0700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
