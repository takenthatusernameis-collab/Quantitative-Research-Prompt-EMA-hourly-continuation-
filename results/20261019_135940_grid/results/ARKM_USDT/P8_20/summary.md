# EMA Hourly Continuation — ARKM/USDT P8_20

**Symbol:** ARKM/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1726 |
| net_profit_factor | 0.4360 |
| net_win_rate | 0.4061 |
| gross_profit_factor | 0.7918 |
| gross_win_rate | 0.4218 |
| sharpe_ratio | -12.4200 |
| sortino_ratio | -7.2548 |
| max_drawdown | 0.9999 |
| cagr | -0.9740 |
| net_avg_win | 11.0287 |
| net_avg_loss | -17.2976 |
| avg_hold_time_bars | 2.8094 |
| exposure | 0.2204 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
