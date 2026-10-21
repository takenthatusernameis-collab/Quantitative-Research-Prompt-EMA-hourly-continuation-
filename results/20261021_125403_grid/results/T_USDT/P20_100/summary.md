# EMA Hourly Continuation — T/USDT P20_100

**Symbol:** T/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.7571 |
| net_win_rate | 0.5042 |
| gross_profit_factor | 1.0401 |
| gross_win_rate | 0.5042 |
| sharpe_ratio | -2.0791 |
| sortino_ratio | -0.6491 |
| max_drawdown | 0.5735 |
| cagr | -0.2584 |
| net_avg_win | 68.4919 |
| net_avg_loss | -91.9897 |
| avg_hold_time_bars | 18.6946 |
| exposure | 0.4044 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
