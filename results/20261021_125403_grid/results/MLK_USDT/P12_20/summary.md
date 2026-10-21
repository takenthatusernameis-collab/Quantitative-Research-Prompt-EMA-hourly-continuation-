# EMA Hourly Continuation — MLK/USDT P12_20

**Symbol:** MLK/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.3083 |
| net_win_rate | 0.3166 |
| gross_profit_factor | 0.5470 |
| gross_win_rate | 0.3284 |
| sharpe_ratio | -6.5070 |
| sortino_ratio | -1.6992 |
| max_drawdown | 0.8722 |
| cagr | -0.5557 |
| net_avg_win | 36.2791 |
| net_avg_loss | -54.5011 |
| avg_hold_time_bars | 5.8462 |
| exposure | 0.0894 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
