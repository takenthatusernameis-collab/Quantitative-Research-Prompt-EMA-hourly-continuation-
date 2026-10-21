# EMA Hourly Continuation — G/USDT P26_200

**Symbol:** G/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 252 |
| net_profit_factor | 0.6070 |
| net_win_rate | 0.4286 |
| gross_profit_factor | 0.7355 |
| gross_win_rate | 0.4286 |
| sharpe_ratio | -2.6182 |
| sortino_ratio | -0.6297 |
| max_drawdown | 0.5142 |
| cagr | -0.2537 |
| net_avg_win | 67.2497 |
| net_avg_loss | -83.0927 |
| avg_hold_time_bars | 44.9087 |
| exposure | 0.5951 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
