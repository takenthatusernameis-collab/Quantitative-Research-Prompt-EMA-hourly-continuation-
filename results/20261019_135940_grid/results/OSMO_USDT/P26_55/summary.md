# EMA Hourly Continuation — OSMO/USDT P26_55

**Symbol:** OSMO/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 881 |
| net_profit_factor | 0.4391 |
| net_win_rate | 0.4075 |
| gross_profit_factor | 0.8549 |
| gross_win_rate | 0.4222 |
| sharpe_ratio | -8.5686 |
| sortino_ratio | -3.5983 |
| max_drawdown | 0.9886 |
| cagr | -0.8319 |
| net_avg_win | 21.5619 |
| net_avg_loss | -33.7685 |
| avg_hold_time_bars | 5.1067 |
| exposure | 0.2045 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
