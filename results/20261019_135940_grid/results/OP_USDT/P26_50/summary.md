# EMA Hourly Continuation — OP/USDT P26_50

**Symbol:** OP/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 963 |
| net_profit_factor | 0.4460 |
| net_win_rate | 0.4694 |
| gross_profit_factor | 0.8918 |
| gross_win_rate | 0.4787 |
| sharpe_ratio | -6.8081 |
| sortino_ratio | -2.9891 |
| max_drawdown | 0.9749 |
| cagr | -0.7661 |
| net_avg_win | 17.3446 |
| net_avg_loss | -34.4021 |
| avg_hold_time_bars | 3.3707 |
| exposure | 0.1475 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
