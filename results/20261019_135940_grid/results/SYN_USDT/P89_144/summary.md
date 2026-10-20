# EMA Hourly Continuation — SYN/USDT P89_144

**Symbol:** SYN/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.5352 |
| net_win_rate | 0.4625 |
| gross_profit_factor | 0.8763 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -4.1620 |
| sortino_ratio | -1.2856 |
| max_drawdown | 0.7970 |
| cagr | -0.4617 |
| net_avg_win | 40.9248 |
| net_avg_loss | -65.7926 |
| avg_hold_time_bars | 5.8500 |
| exposure | 0.1276 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
