# EMA Hourly Continuation — MAGIC/USDT P26_144

**Symbol:** MAGIC/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.7297 |
| net_win_rate | 0.4909 |
| gross_profit_factor | 0.9922 |
| gross_win_rate | 0.4932 |
| sharpe_ratio | -2.2675 |
| sortino_ratio | -0.6692 |
| max_drawdown | 0.5920 |
| cagr | -0.2729 |
| net_avg_win | 69.1527 |
| net_avg_loss | -91.3717 |
| avg_hold_time_bars | 26.6667 |
| exposure | 0.5309 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
