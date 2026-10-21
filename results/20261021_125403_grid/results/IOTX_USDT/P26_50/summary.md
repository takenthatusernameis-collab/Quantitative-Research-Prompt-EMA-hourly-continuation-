# EMA Hourly Continuation — IOTX/USDT P26_50

**Symbol:** IOTX/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.6719 |
| net_win_rate | 0.4921 |
| gross_profit_factor | 0.9567 |
| gross_win_rate | 0.4921 |
| sharpe_ratio | -2.6222 |
| sortino_ratio | -0.7940 |
| max_drawdown | 0.6108 |
| cagr | -0.3035 |
| net_avg_win | 55.8145 |
| net_avg_loss | -80.4938 |
| avg_hold_time_bars | 6.0202 |
| exposure | 0.1218 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
