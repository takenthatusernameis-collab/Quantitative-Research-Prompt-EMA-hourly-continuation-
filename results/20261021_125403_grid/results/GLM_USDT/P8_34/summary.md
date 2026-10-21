# EMA Hourly Continuation — GLM/USDT P8_34

**Symbol:** GLM/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 852 |
| net_profit_factor | 0.6764 |
| net_win_rate | 0.4777 |
| gross_profit_factor | 0.9517 |
| gross_win_rate | 0.4789 |
| sharpe_ratio | -4.1342 |
| sortino_ratio | -1.7248 |
| max_drawdown | 0.8724 |
| cagr | -0.5480 |
| net_avg_win | 44.3611 |
| net_avg_loss | -59.9853 |
| avg_hold_time_bars | 8.4953 |
| exposure | 0.3290 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
