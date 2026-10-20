# EMA Hourly Continuation — ALT/USDT P20_55

**Symbol:** ALT/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 824 |
| net_profit_factor | 0.5495 |
| net_win_rate | 0.4369 |
| gross_profit_factor | 0.8549 |
| gross_win_rate | 0.4454 |
| sharpe_ratio | -5.8293 |
| sortino_ratio | -2.3581 |
| max_drawdown | 0.9442 |
| cagr | -0.6749 |
| net_avg_win | 31.8704 |
| net_avg_loss | -44.9969 |
| avg_hold_time_bars | 6.8896 |
| exposure | 0.2580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
