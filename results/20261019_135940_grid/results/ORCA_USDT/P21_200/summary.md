# EMA Hourly Continuation — ORCA/USDT P21_200

**Symbol:** ORCA/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.6611 |
| net_win_rate | 0.4828 |
| gross_profit_factor | 0.9066 |
| gross_win_rate | 0.4855 |
| sharpe_ratio | -2.3734 |
| sortino_ratio | -0.6472 |
| max_drawdown | 0.5812 |
| cagr | -0.2692 |
| net_avg_win | 58.0980 |
| net_avg_loss | -82.0574 |
| avg_hold_time_bars | 36.9789 |
| exposure | 0.6370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
