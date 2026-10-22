# EMA Hourly Continuation — LQTY/USDT P55_144

**Symbol:** LQTY/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.6946 |
| net_win_rate | 0.4640 |
| gross_profit_factor | 0.8729 |
| gross_win_rate | 0.4640 |
| sharpe_ratio | -2.3036 |
| sortino_ratio | -0.6331 |
| max_drawdown | 0.5318 |
| cagr | -0.2528 |
| net_avg_win | 68.0297 |
| net_avg_loss | -84.7884 |
| avg_hold_time_bars | 14.5867 |
| exposure | 0.2475 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
