# EMA Hourly Continuation — QI/USDT P21_200

**Symbol:** QI/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.8147 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9973 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.1540 |
| sortino_ratio | -0.2983 |
| max_drawdown | 0.3346 |
| cagr | -0.1296 |
| net_avg_win | 79.1848 |
| net_avg_loss | -97.1976 |
| avg_hold_time_bars | 39.0823 |
| exposure | 0.5801 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
