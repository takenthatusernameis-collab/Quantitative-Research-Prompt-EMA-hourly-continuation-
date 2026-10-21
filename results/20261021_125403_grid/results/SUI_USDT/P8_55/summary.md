# EMA Hourly Continuation — SUI/USDT P8_55

**Symbol:** SUI/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 605 |
| net_profit_factor | 0.8744 |
| net_win_rate | 0.5207 |
| gross_profit_factor | 1.0791 |
| gross_win_rate | 0.5207 |
| sharpe_ratio | -1.0298 |
| sortino_ratio | -0.3645 |
| max_drawdown | 0.3970 |
| cagr | -0.1583 |
| net_avg_win | 77.6523 |
| net_avg_loss | -96.4582 |
| avg_hold_time_bars | 15.7107 |
| exposure | 0.4320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
