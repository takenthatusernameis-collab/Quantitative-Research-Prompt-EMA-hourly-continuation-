# EMA Hourly Continuation — VR/USDT P50_100

**Symbol:** VR/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 250 |
| net_profit_factor | 0.5575 |
| net_win_rate | 0.4200 |
| gross_profit_factor | 0.7363 |
| gross_win_rate | 0.4200 |
| sharpe_ratio | -2.9789 |
| sortino_ratio | -0.6661 |
| max_drawdown | 0.5385 |
| cagr | -0.2650 |
| net_avg_win | 64.6127 |
| net_avg_loss | -83.9244 |
| avg_hold_time_bars | 11.5920 |
| exposure | 0.1317 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
