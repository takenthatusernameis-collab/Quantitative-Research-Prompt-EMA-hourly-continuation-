# EMA Hourly Continuation — ENA/USDT P34_100

**Symbol:** ENA/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 602 |
| net_profit_factor | 0.7200 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9810 |
| gross_win_rate | 0.5050 |
| sharpe_ratio | -2.3573 |
| sortino_ratio | -0.8157 |
| max_drawdown | 0.6323 |
| cagr | -0.3222 |
| net_avg_win | 53.2533 |
| net_avg_loss | -73.9642 |
| avg_hold_time_bars | 9.7193 |
| exposure | 0.2660 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
