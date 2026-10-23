# EMA Hourly Continuation — CELR/USDT P50_144

**Symbol:** CELR/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.6433 |
| net_win_rate | 0.4794 |
| gross_profit_factor | 0.9412 |
| gross_win_rate | 0.4897 |
| sharpe_ratio | -2.9156 |
| sortino_ratio | -0.9097 |
| max_drawdown | 0.6634 |
| cagr | -0.3463 |
| net_avg_win | 50.9192 |
| net_avg_loss | -72.8963 |
| avg_hold_time_bars | 14.2840 |
| exposure | 0.3141 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
