# EMA Hourly Continuation — ICP/USDT P100_200

**Symbol:** ICP/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.5560 |
| net_win_rate | 0.4820 |
| gross_profit_factor | 0.9548 |
| gross_win_rate | 0.4916 |
| sharpe_ratio | -3.7195 |
| sortino_ratio | -1.0669 |
| max_drawdown | 0.7447 |
| cagr | -0.4069 |
| net_avg_win | 45.5282 |
| net_avg_loss | -76.1948 |
| avg_hold_time_bars | 8.7698 |
| exposure | 0.1662 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
