# EMA Hourly Continuation — CELR/USDT P55_100

**Symbol:** CELR/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 634 |
| net_profit_factor | 0.5040 |
| net_win_rate | 0.4527 |
| gross_profit_factor | 0.8435 |
| gross_win_rate | 0.4685 |
| sharpe_ratio | -5.0413 |
| sortino_ratio | -1.7940 |
| max_drawdown | 0.8861 |
| cagr | -0.5739 |
| net_avg_win | 31.2935 |
| net_avg_loss | -51.3510 |
| avg_hold_time_bars | 5.4937 |
| exposure | 0.1576 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
