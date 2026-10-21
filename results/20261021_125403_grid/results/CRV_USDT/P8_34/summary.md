# EMA Hourly Continuation — CRV/USDT P8_34

**Symbol:** CRV/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 693 |
| net_profit_factor | 0.7702 |
| net_win_rate | 0.5022 |
| gross_profit_factor | 0.9846 |
| gross_win_rate | 0.5022 |
| sharpe_ratio | -1.9868 |
| sortino_ratio | -0.7499 |
| max_drawdown | 0.6033 |
| cagr | -0.2926 |
| net_avg_win | 55.9450 |
| net_avg_loss | -73.2650 |
| avg_hold_time_bars | 8.3261 |
| exposure | 0.2623 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
