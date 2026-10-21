# EMA Hourly Continuation — CAKE/USDT P8_26

**Symbol:** CAKE/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.7552 |
| net_win_rate | 0.5208 |
| gross_profit_factor | 1.0914 |
| gross_win_rate | 0.5208 |
| sharpe_ratio | -2.3975 |
| sortino_ratio | -0.8958 |
| max_drawdown | 0.6495 |
| cagr | -0.3366 |
| net_avg_win | 56.6838 |
| net_avg_loss | -81.5888 |
| avg_hold_time_bars | 7.3155 |
| exposure | 0.2235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
