# EMA Hourly Continuation — DEEP/USDT P8_55

**Symbol:** DEEP/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.9150 |
| net_win_rate | 0.5182 |
| gross_profit_factor | 1.0701 |
| gross_win_rate | 0.5182 |
| sharpe_ratio | -0.6742 |
| sortino_ratio | -0.2470 |
| max_drawdown | 0.3103 |
| cagr | -0.1145 |
| net_avg_win | 86.6659 |
| net_avg_loss | -101.8882 |
| avg_hold_time_bars | 15.6526 |
| exposure | 0.4617 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
