# EMA Hourly Continuation — BICO/USDT P55_100

**Symbol:** BICO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 597 |
| net_profit_factor | 0.5833 |
| net_win_rate | 0.4757 |
| gross_profit_factor | 0.9192 |
| gross_win_rate | 0.4841 |
| sharpe_ratio | -3.8477 |
| sortino_ratio | -1.3341 |
| max_drawdown | 0.7995 |
| cagr | -0.4652 |
| net_avg_win | 39.0594 |
| net_avg_loss | -60.7535 |
| avg_hold_time_bars | 6.8911 |
| exposure | 0.1870 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
