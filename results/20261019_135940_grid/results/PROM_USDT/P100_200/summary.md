# EMA Hourly Continuation — PROM/USDT P100_200

**Symbol:** PROM/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.3331 |
| net_win_rate | 0.3737 |
| gross_profit_factor | 0.6632 |
| gross_win_rate | 0.4127 |
| sharpe_ratio | -6.7727 |
| sortino_ratio | -2.1040 |
| max_drawdown | 0.9323 |
| cagr | -0.6504 |
| net_avg_win | 25.4859 |
| net_avg_loss | -45.6538 |
| avg_hold_time_bars | 8.5380 |
| exposure | 0.1890 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
