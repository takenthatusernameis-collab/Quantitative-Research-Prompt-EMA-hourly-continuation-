# EMA Hourly Continuation — CAKE/USDT P20_55

**Symbol:** CAKE/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 512 |
| net_profit_factor | 0.6503 |
| net_win_rate | 0.4785 |
| gross_profit_factor | 0.9086 |
| gross_win_rate | 0.4785 |
| sharpe_ratio | -3.0070 |
| sortino_ratio | -0.9730 |
| max_drawdown | 0.6807 |
| cagr | -0.3605 |
| net_avg_win | 51.1977 |
| net_avg_loss | -72.2468 |
| avg_hold_time_bars | 9.8477 |
| exposure | 0.2292 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
