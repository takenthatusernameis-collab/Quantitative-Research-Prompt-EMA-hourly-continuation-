# EMA Hourly Continuation — PROM/USDT P50_100

**Symbol:** PROM/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.5772 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8413 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -3.3279 |
| sortino_ratio | -0.9548 |
| max_drawdown | 0.6873 |
| cagr | -0.3572 |
| net_avg_win | 49.4671 |
| net_avg_loss | -71.4177 |
| avg_hold_time_bars | 9.3980 |
| exposure | 0.1739 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
