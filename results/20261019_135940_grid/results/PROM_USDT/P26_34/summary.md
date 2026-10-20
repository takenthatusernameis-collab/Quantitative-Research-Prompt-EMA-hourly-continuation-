# EMA Hourly Continuation — PROM/USDT P26_34

**Symbol:** PROM/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1084 |
| net_profit_factor | 0.2762 |
| net_win_rate | 0.3662 |
| gross_profit_factor | 0.7480 |
| gross_win_rate | 0.4253 |
| sharpe_ratio | -13.0394 |
| sortino_ratio | -6.1735 |
| max_drawdown | 0.9997 |
| cagr | -0.9630 |
| net_avg_win | 9.6087 |
| net_avg_loss | -20.1050 |
| avg_hold_time_bars | 2.5046 |
| exposure | 0.1234 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
