# EMA Hourly Continuation — ONDO/USDT P12_100

**Symbol:** ONDO/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.8568 |
| net_win_rate | 0.5043 |
| gross_profit_factor | 1.0111 |
| gross_win_rate | 0.5043 |
| sharpe_ratio | -1.0034 |
| sortino_ratio | -0.3110 |
| max_drawdown | 0.3765 |
| cagr | -0.1363 |
| net_avg_win | 78.0058 |
| net_avg_loss | -92.6172 |
| avg_hold_time_bars | 23.9551 |
| exposure | 0.5096 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
