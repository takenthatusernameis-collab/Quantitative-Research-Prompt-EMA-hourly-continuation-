# EMA Hourly Continuation — STRAX/USDT P50_100

**Symbol:** STRAX/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 420 |
| net_profit_factor | 0.6231 |
| net_win_rate | 0.4619 |
| gross_profit_factor | 0.9006 |
| gross_win_rate | 0.4643 |
| sharpe_ratio | -3.3790 |
| sortino_ratio | -0.9894 |
| max_drawdown | 0.6912 |
| cagr | -0.3663 |
| net_avg_win | 57.9278 |
| net_avg_loss | -79.8051 |
| avg_hold_time_bars | 8.9738 |
| exposure | 0.1723 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
