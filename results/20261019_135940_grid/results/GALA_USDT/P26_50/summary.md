# EMA Hourly Continuation — GALA/USDT P26_50

**Symbol:** GALA/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1000 |
| net_profit_factor | 0.4428 |
| net_win_rate | 0.4320 |
| gross_profit_factor | 0.8092 |
| gross_win_rate | 0.4460 |
| sharpe_ratio | -8.0138 |
| sortino_ratio | -3.6091 |
| max_drawdown | 0.9882 |
| cagr | -0.8232 |
| net_avg_win | 18.1571 |
| net_avg_loss | -31.1882 |
| avg_hold_time_bars | 3.5210 |
| exposure | 0.1600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
