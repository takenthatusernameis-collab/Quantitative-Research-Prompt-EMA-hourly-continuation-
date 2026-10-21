# EMA Hourly Continuation — ERG/USDT P21_100

**Symbol:** ERG/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.6818 |
| net_win_rate | 0.4668 |
| gross_profit_factor | 0.8563 |
| gross_win_rate | 0.4668 |
| sharpe_ratio | -2.3903 |
| sortino_ratio | -0.7111 |
| max_drawdown | 0.5791 |
| cagr | -0.2792 |
| net_avg_win | 58.8791 |
| net_avg_loss | -75.6097 |
| avg_hold_time_bars | 17.9771 |
| exposure | 0.3571 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
