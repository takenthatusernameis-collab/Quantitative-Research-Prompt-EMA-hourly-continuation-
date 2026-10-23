# EMA Hourly Continuation — MOVR/USDT P8_100

**Symbol:** MOVR/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 694 |
| net_profit_factor | 0.5916 |
| net_win_rate | 0.4539 |
| gross_profit_factor | 0.8819 |
| gross_win_rate | 0.4597 |
| sharpe_ratio | -4.4965 |
| sortino_ratio | -1.6611 |
| max_drawdown | 0.8646 |
| cagr | -0.5460 |
| net_avg_win | 39.6637 |
| net_avg_loss | -55.7200 |
| avg_hold_time_bars | 21.3631 |
| exposure | 0.6739 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
