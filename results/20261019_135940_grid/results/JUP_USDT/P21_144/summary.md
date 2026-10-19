# EMA Hourly Continuation — JUP/USDT P21_144

**Symbol:** JUP/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 543 |
| net_profit_factor | 0.5772 |
| net_win_rate | 0.4475 |
| gross_profit_factor | 0.8274 |
| gross_win_rate | 0.4530 |
| sharpe_ratio | -3.9731 |
| sortino_ratio | -1.3009 |
| max_drawdown | 0.7970 |
| cagr | -0.4619 |
| net_avg_win | 44.3279 |
| net_avg_loss | -62.2080 |
| avg_hold_time_bars | 20.0939 |
| exposure | 0.4960 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
