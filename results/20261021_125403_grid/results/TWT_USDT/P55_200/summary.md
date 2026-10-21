# EMA Hourly Continuation — TWT/USDT P55_200

**Symbol:** TWT/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.7523 |
| net_win_rate | 0.4967 |
| gross_profit_factor | 0.9822 |
| gross_win_rate | 0.4967 |
| sharpe_ratio | -1.5430 |
| sortino_ratio | -0.3864 |
| max_drawdown | 0.3998 |
| cagr | -0.1630 |
| net_avg_win | 72.0048 |
| net_avg_loss | -94.4686 |
| avg_hold_time_bars | 26.2712 |
| exposure | 0.3654 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
