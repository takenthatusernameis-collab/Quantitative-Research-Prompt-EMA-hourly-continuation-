# EMA Hourly Continuation — RUNE/USDT P100_144

**Symbol:** RUNE/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.4385 |
| net_win_rate | 0.4422 |
| gross_profit_factor | 0.7799 |
| gross_win_rate | 0.4603 |
| sharpe_ratio | -5.0220 |
| sortino_ratio | -1.4957 |
| max_drawdown | 0.8406 |
| cagr | -0.5149 |
| net_avg_win | 33.5453 |
| net_avg_loss | -60.6341 |
| avg_hold_time_bars | 4.1610 |
| exposure | 0.0834 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
