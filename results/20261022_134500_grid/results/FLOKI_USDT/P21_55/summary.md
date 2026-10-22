# EMA Hourly Continuation — FLOKI/USDT P21_55

**Symbol:** FLOKI/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1026 |
| net_profit_factor | 0.5323 |
| net_win_rate | 0.4513 |
| gross_profit_factor | 0.8730 |
| gross_win_rate | 0.4620 |
| sharpe_ratio | -7.3142 |
| sortino_ratio | -3.2581 |
| max_drawdown | 0.9850 |
| cagr | -0.8076 |
| net_avg_win | 24.1923 |
| net_avg_loss | -37.3744 |
| avg_hold_time_bars | 5.0692 |
| exposure | 0.2364 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
