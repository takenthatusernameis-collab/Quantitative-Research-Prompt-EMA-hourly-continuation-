# EMA Hourly Continuation — CPOOL/USDT P21_50

**Symbol:** CPOOL/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.8078 |
| net_win_rate | 0.5021 |
| gross_profit_factor | 0.9924 |
| gross_win_rate | 0.5021 |
| sharpe_ratio | -1.4024 |
| sortino_ratio | -0.4356 |
| max_drawdown | 0.4362 |
| cagr | -0.1831 |
| net_avg_win | 70.9382 |
| net_avg_loss | -88.5665 |
| avg_hold_time_bars | 7.0043 |
| exposure | 0.1496 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
