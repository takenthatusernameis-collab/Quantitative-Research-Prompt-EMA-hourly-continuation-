# EMA Hourly Continuation — MLK/USDT P8_20

**Symbol:** MLK/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1950 |
| net_profit_factor | 0.1726 |
| net_win_rate | 0.2374 |
| gross_profit_factor | 0.5754 |
| gross_win_rate | 0.2610 |
| sharpe_ratio | -23.0307 |
| sortino_ratio | -14.8290 |
| max_drawdown | 1.0000 |
| cagr | -0.9996 |
| net_avg_win | 4.5054 |
| net_avg_loss | -8.1278 |
| avg_hold_time_bars | 2.9128 |
| exposure | 0.2570 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
