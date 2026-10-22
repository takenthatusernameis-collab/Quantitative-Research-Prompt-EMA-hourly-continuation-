# EMA Hourly Continuation — ENA/USDT P20_200

**Symbol:** ENA/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.7498 |
| net_win_rate | 0.4897 |
| gross_profit_factor | 0.9481 |
| gross_win_rate | 0.4948 |
| sharpe_ratio | -1.6462 |
| sortino_ratio | -0.4589 |
| max_drawdown | 0.4705 |
| cagr | -0.1938 |
| net_avg_win | 65.9008 |
| net_avg_loss | -84.3433 |
| avg_hold_time_bars | 35.7088 |
| exposure | 0.6298 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
