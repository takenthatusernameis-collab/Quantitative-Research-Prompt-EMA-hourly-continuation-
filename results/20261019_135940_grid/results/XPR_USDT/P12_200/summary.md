# EMA Hourly Continuation — XPR/USDT P12_200

**Symbol:** XPR/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.5674 |
| net_win_rate | 0.4688 |
| gross_profit_factor | 0.8363 |
| gross_win_rate | 0.4728 |
| sharpe_ratio | -3.4781 |
| sortino_ratio | -1.0855 |
| max_drawdown | 0.7434 |
| cagr | -0.4087 |
| net_avg_win | 41.2528 |
| net_avg_loss | -64.1637 |
| avg_hold_time_bars | 29.0443 |
| exposure | 0.6561 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
