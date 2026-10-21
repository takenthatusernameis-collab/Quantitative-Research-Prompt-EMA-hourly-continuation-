# EMA Hourly Continuation — ENA/USDT P55_100

**Symbol:** ENA/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.7222 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 0.8740 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -1.7537 |
| sortino_ratio | -0.4300 |
| max_drawdown | 0.4377 |
| cagr | -0.1791 |
| net_avg_win | 73.0834 |
| net_avg_loss | -89.0273 |
| avg_hold_time_bars | 7.8788 |
| exposure | 0.1064 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
