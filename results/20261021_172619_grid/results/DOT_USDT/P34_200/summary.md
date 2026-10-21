# EMA Hourly Continuation — DOT/USDT P34_200

**Symbol:** DOT/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.8840 |
| net_win_rate | 0.5204 |
| gross_profit_factor | 1.0796 |
| gross_win_rate | 0.5204 |
| sharpe_ratio | -0.6121 |
| sortino_ratio | -0.1444 |
| max_drawdown | 0.2175 |
| cagr | -0.0667 |
| net_avg_win | 86.6339 |
| net_avg_loss | -106.3613 |
| avg_hold_time_bars | 44.8067 |
| exposure | 0.5479 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
