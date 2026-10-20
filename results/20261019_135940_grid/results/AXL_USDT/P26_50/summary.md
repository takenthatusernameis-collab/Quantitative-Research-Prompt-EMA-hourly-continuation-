# EMA Hourly Continuation — AXL/USDT P26_50

**Symbol:** AXL/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1012 |
| net_profit_factor | 0.5003 |
| net_win_rate | 0.4200 |
| gross_profit_factor | 0.8884 |
| gross_win_rate | 0.4308 |
| sharpe_ratio | -8.2561 |
| sortino_ratio | -3.6972 |
| max_drawdown | 0.9895 |
| cagr | -0.8357 |
| net_avg_win | 23.3057 |
| net_avg_loss | -33.7307 |
| avg_hold_time_bars | 3.8893 |
| exposure | 0.1781 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
