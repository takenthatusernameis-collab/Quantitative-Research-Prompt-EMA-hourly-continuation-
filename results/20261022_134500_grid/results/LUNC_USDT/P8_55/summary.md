# EMA Hourly Continuation — LUNC/USDT P8_55

**Symbol:** LUNC/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1157 |
| net_profit_factor | 0.4525 |
| net_win_rate | 0.4339 |
| gross_profit_factor | 0.8219 |
| gross_win_rate | 0.4486 |
| sharpe_ratio | -8.2282 |
| sortino_ratio | -3.9452 |
| max_drawdown | 0.9921 |
| cagr | -0.8528 |
| net_avg_win | 16.3283 |
| net_avg_loss | -27.6571 |
| avg_hold_time_bars | 9.0674 |
| exposure | 0.4769 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
