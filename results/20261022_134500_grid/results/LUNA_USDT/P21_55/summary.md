# EMA Hourly Continuation — LUNA/USDT P21_55

**Symbol:** LUNA/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1074 |
| net_profit_factor | 0.4608 |
| net_win_rate | 0.4274 |
| gross_profit_factor | 0.8973 |
| gross_win_rate | 0.4441 |
| sharpe_ratio | -9.2601 |
| sortino_ratio | -4.2628 |
| max_drawdown | 0.9956 |
| cagr | -0.8849 |
| net_avg_win | 18.5406 |
| net_avg_loss | -30.0264 |
| avg_hold_time_bars | 4.2970 |
| exposure | 0.2098 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
