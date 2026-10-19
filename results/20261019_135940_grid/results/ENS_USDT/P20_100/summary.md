# EMA Hourly Continuation — ENS/USDT P20_100

**Symbol:** ENS/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 639 |
| net_profit_factor | 0.6453 |
| net_win_rate | 0.4789 |
| gross_profit_factor | 0.9441 |
| gross_win_rate | 0.4883 |
| sharpe_ratio | -3.6545 |
| sortino_ratio | -1.3007 |
| max_drawdown | 0.8121 |
| cagr | -0.4631 |
| net_avg_win | 46.9747 |
| net_avg_loss | -66.8973 |
| avg_hold_time_bars | 15.9327 |
| exposure | 0.4628 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
