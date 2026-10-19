# EMA Hourly Continuation — RAY/USDT P55_200

**Symbol:** RAY/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.6717 |
| net_win_rate | 0.4854 |
| gross_profit_factor | 0.9804 |
| gross_win_rate | 0.5013 |
| sharpe_ratio | -2.3513 |
| sortino_ratio | -0.6428 |
| max_drawdown | 0.6032 |
| cagr | -0.2643 |
| net_avg_win | 60.0622 |
| net_avg_loss | -84.3536 |
| avg_hold_time_bars | 19.8011 |
| exposure | 0.3393 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
