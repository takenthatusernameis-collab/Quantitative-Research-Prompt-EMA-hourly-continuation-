# EMA Hourly Continuation — GALA/USDT P50_89

**Symbol:** GALA/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 690 |
| net_profit_factor | 0.4583 |
| net_win_rate | 0.4348 |
| gross_profit_factor | 0.7810 |
| gross_win_rate | 0.4406 |
| sharpe_ratio | -6.3984 |
| sortino_ratio | -2.3687 |
| max_drawdown | 0.9481 |
| cagr | -0.6871 |
| net_avg_win | 26.6728 |
| net_avg_loss | -44.7729 |
| avg_hold_time_bars | 4.9783 |
| exposure | 0.1561 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
