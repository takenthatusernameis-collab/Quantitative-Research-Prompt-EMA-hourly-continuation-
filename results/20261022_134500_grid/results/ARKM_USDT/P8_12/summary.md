# EMA Hourly Continuation — ARKM/USDT P8_12

**Symbol:** ARKM/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1896 |
| net_profit_factor | 0.2559 |
| net_win_rate | 0.3782 |
| gross_profit_factor | 0.6072 |
| gross_win_rate | 0.4103 |
| sharpe_ratio | -16.6098 |
| sortino_ratio | -10.3011 |
| max_drawdown | 1.0000 |
| cagr | -0.9957 |
| net_avg_win | 4.7958 |
| net_avg_loss | -11.3983 |
| avg_hold_time_bars | 1.7700 |
| exposure | 0.1525 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
