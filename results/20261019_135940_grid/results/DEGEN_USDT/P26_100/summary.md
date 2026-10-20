# EMA Hourly Continuation — DEGEN/USDT P26_100

**Symbol:** DEGEN/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.7592 |
| net_win_rate | 0.4969 |
| gross_profit_factor | 1.0370 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.6524 |
| sortino_ratio | -0.9516 |
| max_drawdown | 0.7040 |
| cagr | -0.3637 |
| net_avg_win | 66.7976 |
| net_avg_loss | -86.9028 |
| avg_hold_time_bars | 11.3913 |
| exposure | 0.3340 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
