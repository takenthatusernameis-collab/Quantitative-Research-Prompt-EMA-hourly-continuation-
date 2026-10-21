# EMA Hourly Continuation — METIS/USDT P55_100

**Symbol:** METIS/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.6124 |
| net_win_rate | 0.4432 |
| gross_profit_factor | 0.8038 |
| gross_win_rate | 0.4432 |
| sharpe_ratio | -2.9552 |
| sortino_ratio | -0.7880 |
| max_drawdown | 0.6037 |
| cagr | -0.3047 |
| net_avg_win | 60.6289 |
| net_avg_loss | -78.7960 |
| avg_hold_time_bars | 7.8551 |
| exposure | 0.1257 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
