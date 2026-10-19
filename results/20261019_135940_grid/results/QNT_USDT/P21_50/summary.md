# EMA Hourly Continuation — QNT/USDT P21_50

**Symbol:** QNT/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1124 |
| net_profit_factor | 0.3357 |
| net_win_rate | 0.4279 |
| gross_profit_factor | 0.7434 |
| gross_win_rate | 0.4511 |
| sharpe_ratio | -9.6463 |
| sortino_ratio | -4.5705 |
| max_drawdown | 0.9969 |
| cagr | -0.8990 |
| net_avg_win | 10.4751 |
| net_avg_loss | -23.3390 |
| avg_hold_time_bars | 3.8345 |
| exposure | 0.1959 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
