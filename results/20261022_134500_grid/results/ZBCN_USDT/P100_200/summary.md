# EMA Hourly Continuation — ZBCN/USDT P100_200

**Symbol:** ZBCN/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.6474 |
| net_win_rate | 0.5041 |
| gross_profit_factor | 0.9564 |
| gross_win_rate | 0.5041 |
| sharpe_ratio | -2.5286 |
| sortino_ratio | -0.7946 |
| max_drawdown | 0.6511 |
| cagr | -0.3149 |
| net_avg_win | 45.6455 |
| net_avg_loss | -71.6865 |
| avg_hold_time_bars | 7.0826 |
| exposure | 0.1586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
