# EMA Hourly Continuation — GLM/USDT P26_55

**Symbol:** GLM/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 869 |
| net_profit_factor | 0.4064 |
| net_win_rate | 0.4568 |
| gross_profit_factor | 0.7455 |
| gross_win_rate | 0.4684 |
| sharpe_ratio | -6.8887 |
| sortino_ratio | -2.8683 |
| max_drawdown | 0.9702 |
| cagr | -0.7524 |
| net_avg_win | 16.7267 |
| net_avg_loss | -34.6190 |
| avg_hold_time_bars | 5.2474 |
| exposure | 0.2073 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
