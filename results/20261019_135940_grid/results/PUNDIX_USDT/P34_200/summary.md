# EMA Hourly Continuation — PUNDIX/USDT P34_200

**Symbol:** PUNDIX/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.6930 |
| net_win_rate | 0.4887 |
| gross_profit_factor | 1.0358 |
| gross_win_rate | 0.4962 |
| sharpe_ratio | -2.6375 |
| sortino_ratio | -0.7342 |
| max_drawdown | 0.6050 |
| cagr | -0.3022 |
| net_avg_win | 68.8700 |
| net_avg_loss | -94.9902 |
| avg_hold_time_bars | 27.8070 |
| exposure | 0.5043 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
