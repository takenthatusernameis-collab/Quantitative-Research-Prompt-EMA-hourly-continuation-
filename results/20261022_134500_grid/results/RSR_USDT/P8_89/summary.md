# EMA Hourly Continuation — RSR/USDT P8_89

**Symbol:** RSR/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 701 |
| net_profit_factor | 0.6537 |
| net_win_rate | 0.4793 |
| gross_profit_factor | 0.9533 |
| gross_win_rate | 0.4850 |
| sharpe_ratio | -3.5281 |
| sortino_ratio | -1.2993 |
| max_drawdown | 0.8108 |
| cagr | -0.4711 |
| net_avg_win | 44.8296 |
| net_avg_loss | -63.1316 |
| avg_hold_time_bars | 20.0528 |
| exposure | 0.6390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
