# EMA Hourly Continuation — AERO/USDT P20_50

**Symbol:** AERO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.8266 |
| net_win_rate | 0.5097 |
| gross_profit_factor | 1.0427 |
| gross_win_rate | 0.5097 |
| sharpe_ratio | -1.3324 |
| sortino_ratio | -0.4118 |
| max_drawdown | 0.4298 |
| cagr | -0.1739 |
| net_avg_win | 76.9810 |
| net_avg_loss | -96.8222 |
| avg_hold_time_bars | 8.0842 |
| exposure | 0.1701 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
