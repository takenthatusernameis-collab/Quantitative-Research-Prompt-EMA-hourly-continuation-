# EMA Hourly Continuation — DBR/USDT P8_26

**Symbol:** DBR/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 975 |
| net_profit_factor | 0.5014 |
| net_win_rate | 0.4390 |
| gross_profit_factor | 0.9957 |
| gross_win_rate | 0.4759 |
| sharpe_ratio | -9.1328 |
| sortino_ratio | -4.4961 |
| max_drawdown | 0.9891 |
| cagr | -0.8923 |
| net_avg_win | 23.2294 |
| net_avg_loss | -36.2489 |
| avg_hold_time_bars | 5.3887 |
| exposure | 0.2988 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
