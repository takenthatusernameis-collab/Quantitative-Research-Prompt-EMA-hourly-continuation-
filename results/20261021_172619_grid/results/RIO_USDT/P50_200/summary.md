# EMA Hourly Continuation — RIO/USDT P50_200

**Symbol:** RIO/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 319 |
| net_profit_factor | 0.7523 |
| net_win_rate | 0.4608 |
| gross_profit_factor | 0.8516 |
| gross_win_rate | 0.4608 |
| sharpe_ratio | -1.5993 |
| sortino_ratio | -0.4069 |
| max_drawdown | 0.4315 |
| cagr | -0.1722 |
| net_avg_win | 77.4674 |
| net_avg_loss | -88.0012 |
| avg_hold_time_bars | 22.3574 |
| exposure | 0.3274 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
