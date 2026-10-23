# EMA Hourly Continuation — ANKR/USDT P26_50

**Symbol:** ANKR/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 948 |
| net_profit_factor | 0.4572 |
| net_win_rate | 0.4030 |
| gross_profit_factor | 0.8975 |
| gross_win_rate | 0.4325 |
| sharpe_ratio | -9.6283 |
| sortino_ratio | -4.2045 |
| max_drawdown | 0.9952 |
| cagr | -0.8801 |
| net_avg_win | 21.9405 |
| net_avg_loss | -32.3898 |
| avg_hold_time_bars | 5.3871 |
| exposure | 0.2321 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
