# EMA Hourly Continuation — SQD/USDT P89_100

**Symbol:** SQD/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 131 |
| net_profit_factor | 0.6464 |
| net_win_rate | 0.4504 |
| gross_profit_factor | 0.8390 |
| gross_win_rate | 0.4504 |
| sharpe_ratio | -1.6222 |
| sortino_ratio | -0.2678 |
| max_drawdown | 0.2751 |
| cagr | -0.1161 |
| net_avg_win | 80.2203 |
| net_avg_loss | -101.7011 |
| avg_hold_time_bars | 5.0458 |
| exposure | 0.0311 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
