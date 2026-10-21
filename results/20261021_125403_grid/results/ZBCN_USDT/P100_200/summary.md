# EMA Hourly Continuation — ZBCN/USDT P100_200

**Symbol:** ZBCN/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 270 |
| net_profit_factor | 0.8711 |
| net_win_rate | 0.5148 |
| gross_profit_factor | 1.0426 |
| gross_win_rate | 0.5148 |
| sharpe_ratio | -0.6289 |
| sortino_ratio | -0.1499 |
| max_drawdown | 0.2570 |
| cagr | -0.0689 |
| net_avg_win | 78.5014 |
| net_avg_loss | -95.6228 |
| avg_hold_time_bars | 11.3704 |
| exposure | 0.1420 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
