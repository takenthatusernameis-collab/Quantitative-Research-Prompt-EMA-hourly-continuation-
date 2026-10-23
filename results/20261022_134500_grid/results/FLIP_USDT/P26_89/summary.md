# EMA Hourly Continuation — FLIP/USDT P26_89

**Symbol:** FLIP/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.4615 |
| net_win_rate | 0.4149 |
| gross_profit_factor | 0.7939 |
| gross_win_rate | 0.4419 |
| sharpe_ratio | -5.4111 |
| sortino_ratio | -1.6627 |
| max_drawdown | 0.8767 |
| cagr | -0.5604 |
| net_avg_win | 37.4108 |
| net_avg_loss | -57.4910 |
| avg_hold_time_bars | 15.0892 |
| exposure | 0.3306 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
