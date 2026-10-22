# EMA Hourly Continuation — PENDLE/USDT P50_89

**Symbol:** PENDLE/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 702 |
| net_profit_factor | 0.5585 |
| net_win_rate | 0.4786 |
| gross_profit_factor | 0.9080 |
| gross_win_rate | 0.4801 |
| sharpe_ratio | -4.8078 |
| sortino_ratio | -1.7919 |
| max_drawdown | 0.8879 |
| cagr | -0.5797 |
| net_avg_win | 33.3787 |
| net_avg_loss | -54.8659 |
| avg_hold_time_bars | 4.2194 |
| exposure | 0.1346 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
