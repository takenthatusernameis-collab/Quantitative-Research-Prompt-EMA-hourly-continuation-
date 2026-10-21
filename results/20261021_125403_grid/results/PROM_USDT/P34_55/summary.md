# EMA Hourly Continuation — PROM/USDT P34_55

**Symbol:** PROM/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.5650 |
| net_win_rate | 0.4491 |
| gross_profit_factor | 0.8527 |
| gross_win_rate | 0.4517 |
| sharpe_ratio | -3.6110 |
| sortino_ratio | -1.0076 |
| max_drawdown | 0.7076 |
| cagr | -0.3738 |
| net_avg_win | 52.2083 |
| net_avg_loss | -75.3221 |
| avg_hold_time_bars | 6.1201 |
| exposure | 0.1065 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
