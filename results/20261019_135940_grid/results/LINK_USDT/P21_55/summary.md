# EMA Hourly Continuation — LINK/USDT P21_55

**Symbol:** LINK/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 847 |
| net_profit_factor | 0.5346 |
| net_win_rate | 0.4475 |
| gross_profit_factor | 0.9296 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -7.2214 |
| sortino_ratio | -2.9455 |
| max_drawdown | 0.9755 |
| cagr | -0.7690 |
| net_avg_win | 29.5455 |
| net_avg_loss | -44.7551 |
| avg_hold_time_bars | 5.7698 |
| exposure | 0.2221 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
