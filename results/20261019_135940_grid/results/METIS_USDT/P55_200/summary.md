# EMA Hourly Continuation — METIS/USDT P55_200

**Symbol:** METIS/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.6078 |
| net_win_rate | 0.4489 |
| gross_profit_factor | 0.8322 |
| gross_win_rate | 0.4539 |
| sharpe_ratio | -3.1594 |
| sortino_ratio | -0.8908 |
| max_drawdown | 0.6549 |
| cagr | -0.3429 |
| net_avg_win | 56.1097 |
| net_avg_loss | -75.1836 |
| avg_hold_time_bars | 20.2145 |
| exposure | 0.3685 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
