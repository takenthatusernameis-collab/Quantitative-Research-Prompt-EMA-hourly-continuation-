# EMA Hourly Continuation — KCS/USDT P26_200

**Symbol:** KCS/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.5484 |
| net_win_rate | 0.4401 |
| gross_profit_factor | 0.8380 |
| gross_win_rate | 0.4401 |
| sharpe_ratio | -3.5406 |
| sortino_ratio | -0.8873 |
| max_drawdown | 0.6415 |
| cagr | -0.3353 |
| net_avg_win | 57.2821 |
| net_avg_loss | -82.1092 |
| avg_hold_time_bars | 39.3948 |
| exposure | 0.5533 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
