# EMA Hourly Continuation — AURORA/USDT P26_144

**Symbol:** AURORA/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.6117 |
| net_win_rate | 0.4662 |
| gross_profit_factor | 0.9473 |
| gross_win_rate | 0.4728 |
| sharpe_ratio | -3.7096 |
| sortino_ratio | -1.1114 |
| max_drawdown | 0.7500 |
| cagr | -0.4178 |
| net_avg_win | 54.6973 |
| net_avg_loss | -78.0990 |
| avg_hold_time_bars | 21.2462 |
| exposure | 0.4433 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
