# EMA Hourly Continuation — SAFE/USDT P8_100

**Symbol:** SAFE/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.7981 |
| net_win_rate | 0.4940 |
| gross_profit_factor | 0.9650 |
| gross_win_rate | 0.4940 |
| sharpe_ratio | -1.5412 |
| sortino_ratio | -0.4928 |
| max_drawdown | 0.4829 |
| cagr | -0.2051 |
| net_avg_win | 70.0171 |
| net_avg_loss | -85.6406 |
| avg_hold_time_bars | 27.9257 |
| exposure | 0.6369 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
