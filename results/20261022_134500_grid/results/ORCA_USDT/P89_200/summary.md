# EMA Hourly Continuation — ORCA/USDT P89_200

**Symbol:** ORCA/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.4821 |
| net_win_rate | 0.4347 |
| gross_profit_factor | 0.7940 |
| gross_win_rate | 0.4480 |
| sharpe_ratio | -4.1624 |
| sortino_ratio | -1.1344 |
| max_drawdown | 0.7683 |
| cagr | -0.4222 |
| net_avg_win | 42.7015 |
| net_avg_loss | -68.1066 |
| avg_hold_time_bars | 13.2373 |
| exposure | 0.2256 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
