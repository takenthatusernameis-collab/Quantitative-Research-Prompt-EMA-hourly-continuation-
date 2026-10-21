# EMA Hourly Continuation — ORCA/USDT P21_26

**Symbol:** ORCA/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.6317 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0238 |
| gross_win_rate | 0.5034 |
| sharpe_ratio | -2.6037 |
| sortino_ratio | -0.6354 |
| max_drawdown | 0.5584 |
| cagr | -0.2569 |
| net_avg_win | 61.7264 |
| net_avg_loss | -97.7204 |
| avg_hold_time_bars | 5.2329 |
| exposure | 0.0695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
