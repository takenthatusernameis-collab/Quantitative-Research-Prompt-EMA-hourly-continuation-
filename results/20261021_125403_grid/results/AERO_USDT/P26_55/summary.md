# EMA Hourly Continuation — AERO/USDT P26_55

**Symbol:** AERO/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.7604 |
| net_win_rate | 0.4963 |
| gross_profit_factor | 0.9700 |
| gross_win_rate | 0.4963 |
| sharpe_ratio | -1.6453 |
| sortino_ratio | -0.4732 |
| max_drawdown | 0.4401 |
| cagr | -0.1952 |
| net_avg_win | 66.7038 |
| net_avg_loss | -86.4253 |
| avg_hold_time_bars | 6.8734 |
| exposure | 0.1259 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
