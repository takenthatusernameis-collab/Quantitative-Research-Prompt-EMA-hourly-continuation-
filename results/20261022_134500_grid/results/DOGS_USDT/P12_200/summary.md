# EMA Hourly Continuation — DOGS/USDT P12_200

**Symbol:** DOGS/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.6050 |
| net_win_rate | 0.4514 |
| gross_profit_factor | 0.8477 |
| gross_win_rate | 0.4571 |
| sharpe_ratio | -3.3329 |
| sortino_ratio | -0.9402 |
| max_drawdown | 0.6337 |
| cagr | -0.3650 |
| net_avg_win | 60.4518 |
| net_avg_loss | -82.2240 |
| avg_hold_time_bars | 39.0371 |
| exposure | 0.7248 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
