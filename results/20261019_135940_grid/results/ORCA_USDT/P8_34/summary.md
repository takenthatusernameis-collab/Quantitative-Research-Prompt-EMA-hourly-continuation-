# EMA Hourly Continuation — ORCA/USDT P8_34

**Symbol:** ORCA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1239 |
| net_profit_factor | 0.6363 |
| net_win_rate | 0.4770 |
| gross_profit_factor | 1.0233 |
| gross_win_rate | 0.4964 |
| sharpe_ratio | -5.9572 |
| sortino_ratio | -2.9469 |
| max_drawdown | 0.9737 |
| cagr | -0.7599 |
| net_avg_win | 28.7815 |
| net_avg_loss | -41.2528 |
| avg_hold_time_bars | 6.3446 |
| exposure | 0.3573 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
