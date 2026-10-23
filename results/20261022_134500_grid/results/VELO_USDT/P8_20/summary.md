# EMA Hourly Continuation — VELO/USDT P8_20

**Symbol:** VELO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1736 |
| net_profit_factor | 0.5352 |
| net_win_rate | 0.4453 |
| gross_profit_factor | 0.8865 |
| gross_win_rate | 0.4585 |
| sharpe_ratio | -10.4234 |
| sortino_ratio | -6.1124 |
| max_drawdown | 0.9995 |
| cagr | -0.9513 |
| net_avg_win | 14.8889 |
| net_avg_loss | -22.3303 |
| avg_hold_time_bars | 2.6498 |
| exposure | 0.2091 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
