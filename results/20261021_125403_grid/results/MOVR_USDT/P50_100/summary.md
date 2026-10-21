# EMA Hourly Continuation — MOVR/USDT P50_100

**Symbol:** MOVR/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.5950 |
| net_win_rate | 0.4349 |
| gross_profit_factor | 0.7798 |
| gross_win_rate | 0.4349 |
| sharpe_ratio | -3.2356 |
| sortino_ratio | -0.8994 |
| max_drawdown | 0.6718 |
| cagr | -0.3388 |
| net_avg_win | 56.8421 |
| net_avg_loss | -73.5221 |
| avg_hold_time_bars | 8.7630 |
| exposure | 0.1530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
