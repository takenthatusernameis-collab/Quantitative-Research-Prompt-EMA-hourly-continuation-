# EMA Hourly Continuation — PEPE/USDT P55_100

**Symbol:** PEPE/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.9086 |
| net_win_rate | 0.5377 |
| gross_profit_factor | 1.1545 |
| gross_win_rate | 0.5377 |
| sharpe_ratio | -0.4721 |
| sortino_ratio | -0.1167 |
| max_drawdown | 0.1708 |
| cagr | -0.0551 |
| net_avg_win | 83.9927 |
| net_avg_loss | -107.5015 |
| avg_hold_time_bars | 8.0959 |
| exposure | 0.1075 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
