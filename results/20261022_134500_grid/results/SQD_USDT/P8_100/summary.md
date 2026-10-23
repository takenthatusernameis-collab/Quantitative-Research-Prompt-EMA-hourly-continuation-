# EMA Hourly Continuation — SQD/USDT P8_100

**Symbol:** SQD/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 754 |
| net_profit_factor | 0.7119 |
| net_win_rate | 0.4907 |
| gross_profit_factor | 0.9597 |
| gross_win_rate | 0.4934 |
| sharpe_ratio | -2.9162 |
| sortino_ratio | -1.1544 |
| max_drawdown | 0.7422 |
| cagr | -0.4169 |
| net_avg_win | 48.7712 |
| net_avg_loss | -66.0065 |
| avg_hold_time_bars | 16.0995 |
| exposure | 0.5706 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
