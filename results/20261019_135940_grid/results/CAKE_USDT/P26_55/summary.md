# EMA Hourly Continuation — CAKE/USDT P26_55

**Symbol:** CAKE/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 846 |
| net_profit_factor | 0.3731 |
| net_win_rate | 0.4433 |
| gross_profit_factor | 0.8140 |
| gross_win_rate | 0.4728 |
| sharpe_ratio | -7.6559 |
| sortino_ratio | -3.1510 |
| max_drawdown | 0.9800 |
| cagr | -0.7893 |
| net_avg_win | 15.5533 |
| net_avg_loss | -33.1896 |
| avg_hold_time_bars | 5.0934 |
| exposure | 0.1959 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
