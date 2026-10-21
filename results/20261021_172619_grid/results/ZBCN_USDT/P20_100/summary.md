# EMA Hourly Continuation — ZBCN/USDT P20_100

**Symbol:** ZBCN/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.9564 |
| net_win_rate | 0.5324 |
| gross_profit_factor | 1.1246 |
| gross_win_rate | 0.5324 |
| sharpe_ratio | -0.2412 |
| sortino_ratio | -0.0781 |
| max_drawdown | 0.2708 |
| cagr | -0.0431 |
| net_avg_win | 85.9717 |
| net_avg_loss | -102.3413 |
| avg_hold_time_bars | 15.0486 |
| exposure | 0.3439 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
