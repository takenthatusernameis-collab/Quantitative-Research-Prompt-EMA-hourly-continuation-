# EMA Hourly Continuation — JUP/USDT P55_100

**Symbol:** JUP/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.7461 |
| net_win_rate | 0.4966 |
| gross_profit_factor | 0.9470 |
| gross_win_rate | 0.4966 |
| sharpe_ratio | -1.3848 |
| sortino_ratio | -0.3420 |
| max_drawdown | 0.3799 |
| cagr | -0.1455 |
| net_avg_win | 64.7639 |
| net_avg_loss | -85.6491 |
| avg_hold_time_bars | 7.9295 |
| exposure | 0.1074 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
