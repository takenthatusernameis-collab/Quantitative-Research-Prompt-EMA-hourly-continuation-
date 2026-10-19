# EMA Hourly Continuation — ZBCN/USDT P34_55

**Symbol:** ZBCN/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 947 |
| net_profit_factor | 0.4284 |
| net_win_rate | 0.4298 |
| gross_profit_factor | 0.8080 |
| gross_win_rate | 0.4372 |
| sharpe_ratio | -8.2997 |
| sortino_ratio | -3.5986 |
| max_drawdown | 0.9895 |
| cagr | -0.8414 |
| net_avg_win | 18.2217 |
| net_avg_loss | -32.0553 |
| avg_hold_time_bars | 2.5987 |
| exposure | 0.1139 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
