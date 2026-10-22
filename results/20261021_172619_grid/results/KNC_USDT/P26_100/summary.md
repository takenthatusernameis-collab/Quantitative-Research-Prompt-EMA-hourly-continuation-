# EMA Hourly Continuation — KNC/USDT P26_100

**Symbol:** KNC/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.7287 |
| net_win_rate | 0.4913 |
| gross_profit_factor | 0.9918 |
| gross_win_rate | 0.4913 |
| sharpe_ratio | -2.4401 |
| sortino_ratio | -0.7499 |
| max_drawdown | 0.6414 |
| cagr | -0.2919 |
| net_avg_win | 68.6067 |
| net_avg_loss | -90.9428 |
| avg_hold_time_bars | 17.6602 |
| exposure | 0.3709 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
