# EMA Hourly Continuation — AEVO/USDT P55_100

**Symbol:** AEVO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 667 |
| net_profit_factor | 0.5636 |
| net_win_rate | 0.4633 |
| gross_profit_factor | 0.9125 |
| gross_win_rate | 0.4753 |
| sharpe_ratio | -4.8476 |
| sortino_ratio | -1.7594 |
| max_drawdown | 0.8853 |
| cagr | -0.5717 |
| net_avg_win | 36.8758 |
| net_avg_loss | -56.4715 |
| avg_hold_time_bars | 5.0990 |
| exposure | 0.1539 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
