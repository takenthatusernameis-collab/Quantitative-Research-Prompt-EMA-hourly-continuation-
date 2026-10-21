# EMA Hourly Continuation — ONDO/USDT P50_100

**Symbol:** ONDO/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.6291 |
| net_win_rate | 0.4509 |
| gross_profit_factor | 0.7991 |
| gross_win_rate | 0.4509 |
| sharpe_ratio | -2.5315 |
| sortino_ratio | -0.6690 |
| max_drawdown | 0.5472 |
| cagr | -0.2639 |
| net_avg_win | 58.3611 |
| net_avg_loss | -76.1649 |
| avg_hold_time_bars | 8.8699 |
| exposure | 0.1395 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
