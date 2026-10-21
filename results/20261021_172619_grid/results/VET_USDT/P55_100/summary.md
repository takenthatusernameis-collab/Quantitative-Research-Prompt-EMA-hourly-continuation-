# EMA Hourly Continuation — VET/USDT P55_100

**Symbol:** VET/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.7012 |
| net_win_rate | 0.5029 |
| gross_profit_factor | 0.9784 |
| gross_win_rate | 0.5029 |
| sharpe_ratio | -1.9246 |
| sortino_ratio | -0.5168 |
| max_drawdown | 0.4645 |
| cagr | -0.2109 |
| net_avg_win | 59.7813 |
| net_avg_loss | -86.2375 |
| avg_hold_time_bars | 7.4571 |
| exposure | 0.1186 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
