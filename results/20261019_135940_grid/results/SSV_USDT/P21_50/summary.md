# EMA Hourly Continuation — SSV/USDT P21_50

**Symbol:** SSV/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1067 |
| net_profit_factor | 0.5210 |
| net_win_rate | 0.4396 |
| gross_profit_factor | 0.8513 |
| gross_win_rate | 0.4564 |
| sharpe_ratio | -7.4064 |
| sortino_ratio | -3.4069 |
| max_drawdown | 0.9846 |
| cagr | -0.8073 |
| net_avg_win | 22.8303 |
| net_avg_loss | -34.3652 |
| avg_hold_time_bars | 4.7198 |
| exposure | 0.2279 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
