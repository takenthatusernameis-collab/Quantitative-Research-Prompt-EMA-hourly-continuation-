# EMA Hourly Continuation — KCS/USDT P20_200

**Symbol:** KCS/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.6113 |
| net_win_rate | 0.4563 |
| gross_profit_factor | 0.9291 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -3.1148 |
| sortino_ratio | -0.7815 |
| max_drawdown | 0.5991 |
| cagr | -0.3010 |
| net_avg_win | 66.1597 |
| net_avg_loss | -90.8297 |
| avg_hold_time_bars | 43.6731 |
| exposure | 0.6134 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
