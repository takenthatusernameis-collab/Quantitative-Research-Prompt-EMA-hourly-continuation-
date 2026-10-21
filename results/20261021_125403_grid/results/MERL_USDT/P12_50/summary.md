# EMA Hourly Continuation — MERL/USDT P12_50

**Symbol:** MERL/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.8011 |
| net_win_rate | 0.4876 |
| gross_profit_factor | 0.9573 |
| gross_win_rate | 0.4876 |
| sharpe_ratio | -1.8530 |
| sortino_ratio | -0.6723 |
| max_drawdown | 0.5883 |
| cagr | -0.2679 |
| net_avg_win | 69.5285 |
| net_avg_loss | -82.5814 |
| avg_hold_time_bars | 11.6211 |
| exposure | 0.3411 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
