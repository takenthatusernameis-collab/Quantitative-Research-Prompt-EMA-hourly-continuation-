# EMA Hourly Continuation — KAS/USDT P21_100

**Symbol:** KAS/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 717 |
| net_profit_factor | 0.5766 |
| net_win_rate | 0.4840 |
| gross_profit_factor | 0.9475 |
| gross_win_rate | 0.4923 |
| sharpe_ratio | -4.2467 |
| sortino_ratio | -1.5995 |
| max_drawdown | 0.8581 |
| cagr | -0.5375 |
| net_avg_win | 33.5877 |
| net_avg_loss | -54.6284 |
| avg_hold_time_bars | 11.9289 |
| exposure | 0.3888 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
