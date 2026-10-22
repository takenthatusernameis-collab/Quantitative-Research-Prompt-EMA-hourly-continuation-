# EMA Hourly Continuation — RIO/USDT P21_55

**Symbol:** RIO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.8053 |
| net_win_rate | 0.4844 |
| gross_profit_factor | 0.9422 |
| gross_win_rate | 0.4844 |
| sharpe_ratio | -1.4799 |
| sortino_ratio | -0.4500 |
| max_drawdown | 0.4347 |
| cagr | -0.1888 |
| net_avg_win | 76.9593 |
| net_avg_loss | -89.8005 |
| avg_hold_time_bars | 8.6667 |
| exposure | 0.1790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
