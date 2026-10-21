# EMA Hourly Continuation — SQD/USDT P8_55

**Symbol:** SQD/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 665 |
| net_profit_factor | 0.8603 |
| net_win_rate | 0.5038 |
| gross_profit_factor | 1.0158 |
| gross_win_rate | 0.5038 |
| sharpe_ratio | -1.2762 |
| sortino_ratio | -0.4792 |
| max_drawdown | 0.4879 |
| cagr | -0.2021 |
| net_avg_win | 77.5614 |
| net_avg_loss | -91.5248 |
| avg_hold_time_bars | 13.1338 |
| exposure | 0.4105 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
