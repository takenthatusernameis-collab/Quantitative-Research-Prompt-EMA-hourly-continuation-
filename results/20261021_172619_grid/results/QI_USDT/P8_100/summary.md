# EMA Hourly Continuation — QI/USDT P8_100

**Symbol:** QI/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 488 |
| net_profit_factor | 0.7939 |
| net_win_rate | 0.4939 |
| gross_profit_factor | 0.9778 |
| gross_win_rate | 0.4939 |
| sharpe_ratio | -1.6400 |
| sortino_ratio | -0.5167 |
| max_drawdown | 0.5210 |
| cagr | -0.2123 |
| net_avg_win | 72.2814 |
| net_avg_loss | -88.8389 |
| avg_hold_time_bars | 29.0041 |
| exposure | 0.6405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
