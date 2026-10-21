# EMA Hourly Continuation — FET/USDT P26_50

**Symbol:** FET/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.7969 |
| net_win_rate | 0.5030 |
| gross_profit_factor | 1.0114 |
| gross_win_rate | 0.5030 |
| sharpe_ratio | -1.3191 |
| sortino_ratio | -0.3459 |
| max_drawdown | 0.4016 |
| cagr | -0.1475 |
| net_avg_win | 77.1119 |
| net_avg_loss | -97.9270 |
| avg_hold_time_bars | 6.5299 |
| exposure | 0.0991 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
