# EMA Hourly Continuation — AGLD/USDT P55_144

**Symbol:** AGLD/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.6927 |
| net_win_rate | 0.4563 |
| gross_profit_factor | 0.8779 |
| gross_win_rate | 0.4563 |
| sharpe_ratio | -2.6418 |
| sortino_ratio | -0.7604 |
| max_drawdown | 0.6088 |
| cagr | -0.2947 |
| net_avg_win | 70.2076 |
| net_avg_loss | -85.0633 |
| avg_hold_time_bars | 13.5825 |
| exposure | 0.2532 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
