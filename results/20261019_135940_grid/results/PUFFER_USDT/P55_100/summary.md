# EMA Hourly Continuation — PUFFER/USDT P55_100

**Symbol:** PUFFER/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.5128 |
| net_win_rate | 0.4397 |
| gross_profit_factor | 0.7919 |
| gross_win_rate | 0.4482 |
| sharpe_ratio | -4.7708 |
| sortino_ratio | -1.6299 |
| max_drawdown | 0.7953 |
| cagr | -0.5396 |
| net_avg_win | 40.0120 |
| net_avg_loss | -61.2494 |
| avg_hold_time_bars | 6.8605 |
| exposure | 0.1836 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
