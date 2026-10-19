# EMA Hourly Continuation — AERO/USDT P26_50

**Symbol:** AERO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 869 |
| net_profit_factor | 0.4126 |
| net_win_rate | 0.4384 |
| gross_profit_factor | 0.7199 |
| gross_win_rate | 0.4476 |
| sharpe_ratio | -7.0607 |
| sortino_ratio | -2.9406 |
| max_drawdown | 0.9730 |
| cagr | -0.7617 |
| net_avg_win | 17.9316 |
| net_avg_loss | -33.9330 |
| avg_hold_time_bars | 3.7066 |
| exposure | 0.1464 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
