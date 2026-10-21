# EMA Hourly Continuation — PHA/USDT P21_200

**Symbol:** PHA/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.7982 |
| net_win_rate | 0.4843 |
| gross_profit_factor | 0.9303 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -1.2728 |
| sortino_ratio | -0.3398 |
| max_drawdown | 0.4112 |
| cagr | -0.1464 |
| net_avg_win | 76.3584 |
| net_avg_loss | -89.8450 |
| avg_hold_time_bars | 35.8718 |
| exposure | 0.5723 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
