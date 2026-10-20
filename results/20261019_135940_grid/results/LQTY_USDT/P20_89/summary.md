# EMA Hourly Continuation — LQTY/USDT P20_89

**Symbol:** LQTY/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 694 |
| net_profit_factor | 0.6097 |
| net_win_rate | 0.4539 |
| gross_profit_factor | 0.8795 |
| gross_win_rate | 0.4611 |
| sharpe_ratio | -4.3259 |
| sortino_ratio | -1.6106 |
| max_drawdown | 0.8564 |
| cagr | -0.5287 |
| net_avg_win | 42.1531 |
| net_avg_loss | -57.4646 |
| avg_hold_time_bars | 13.6499 |
| exposure | 0.4287 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
