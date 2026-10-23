# EMA Hourly Continuation — BAND/USDT P21_200

**Symbol:** BAND/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.7383 |
| net_win_rate | 0.5014 |
| gross_profit_factor | 1.0120 |
| gross_win_rate | 0.5095 |
| sharpe_ratio | -1.7188 |
| sortino_ratio | -0.4620 |
| max_drawdown | 0.4451 |
| cagr | -0.1974 |
| net_avg_win | 65.2884 |
| net_avg_loss | -88.9113 |
| avg_hold_time_bars | 37.9891 |
| exposure | 0.6309 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
