# EMA Hourly Continuation — BLUR/USDT P26_50

**Symbol:** BLUR/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 940 |
| net_profit_factor | 0.4912 |
| net_win_rate | 0.4596 |
| gross_profit_factor | 0.8895 |
| gross_win_rate | 0.4798 |
| sharpe_ratio | -6.6523 |
| sortino_ratio | -2.8735 |
| max_drawdown | 0.9715 |
| cagr | -0.7509 |
| net_avg_win | 21.6800 |
| net_avg_loss | -37.5309 |
| avg_hold_time_bars | 4.0649 |
| exposure | 0.1729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
