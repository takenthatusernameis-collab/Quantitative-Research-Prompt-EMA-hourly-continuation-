# EMA Hourly Continuation — ARKM/USDT P55_200

**Symbol:** ARKM/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.7928 |
| net_win_rate | 0.4904 |
| gross_profit_factor | 0.9499 |
| gross_win_rate | 0.4904 |
| sharpe_ratio | -1.2056 |
| sortino_ratio | -0.3050 |
| max_drawdown | 0.3404 |
| cagr | -0.1318 |
| net_avg_win | 74.2623 |
| net_avg_loss | -90.1541 |
| avg_hold_time_bars | 23.5605 |
| exposure | 0.3363 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
