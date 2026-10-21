# EMA Hourly Continuation — MLK/USDT P8_21

**Symbol:** MLK/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.3633 |
| net_win_rate | 0.3600 |
| gross_profit_factor | 0.6067 |
| gross_win_rate | 0.3620 |
| sharpe_ratio | -6.7847 |
| sortino_ratio | -2.1460 |
| max_drawdown | 0.9241 |
| cagr | -0.6384 |
| net_avg_win | 29.2635 |
| net_avg_loss | -45.3083 |
| avg_hold_time_bars | 6.2860 |
| exposure | 0.1422 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
