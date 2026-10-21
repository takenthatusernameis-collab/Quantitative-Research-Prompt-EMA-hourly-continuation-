# EMA Hourly Continuation — CRV/USDT P50_144

**Symbol:** CRV/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.8125 |
| net_win_rate | 0.5041 |
| gross_profit_factor | 1.0133 |
| gross_win_rate | 0.5041 |
| sharpe_ratio | -1.2418 |
| sortino_ratio | -0.3421 |
| max_drawdown | 0.3425 |
| cagr | -0.1464 |
| net_avg_win | 76.4012 |
| net_avg_loss | -95.5787 |
| avg_hold_time_bars | 13.8645 |
| exposure | 0.2325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
