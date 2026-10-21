# EMA Hourly Continuation — AR/USDT P50_55

**Symbol:** AR/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 128 |
| net_profit_factor | 0.6341 |
| net_win_rate | 0.4688 |
| gross_profit_factor | 0.8551 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -1.4980 |
| sortino_ratio | -0.2419 |
| max_drawdown | 0.2504 |
| cagr | -0.1052 |
| net_avg_win | 70.3564 |
| net_avg_loss | -97.8960 |
| avg_hold_time_bars | 5.9297 |
| exposure | 0.0345 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
