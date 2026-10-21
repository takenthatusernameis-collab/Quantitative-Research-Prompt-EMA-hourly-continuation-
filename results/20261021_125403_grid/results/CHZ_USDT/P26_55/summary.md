# EMA Hourly Continuation — CHZ/USDT P26_55

**Symbol:** CHZ/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.7412 |
| net_win_rate | 0.4989 |
| gross_profit_factor | 1.0148 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -2.0995 |
| sortino_ratio | -0.6358 |
| max_drawdown | 0.5306 |
| cagr | -0.2525 |
| net_avg_win | 66.8699 |
| net_avg_loss | -89.8196 |
| avg_hold_time_bars | 7.3685 |
| exposure | 0.1490 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
