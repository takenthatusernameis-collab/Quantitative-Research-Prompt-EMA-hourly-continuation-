# EMA Hourly Continuation — RIO/USDT P8_100

**Symbol:** RIO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 875 |
| net_profit_factor | 0.5789 |
| net_win_rate | 0.4343 |
| gross_profit_factor | 0.7617 |
| gross_win_rate | 0.4354 |
| sharpe_ratio | -5.1535 |
| sortino_ratio | -2.1395 |
| max_drawdown | 0.9292 |
| cagr | -0.6439 |
| net_avg_win | 33.3989 |
| net_avg_loss | -44.2915 |
| avg_hold_time_bars | 15.2606 |
| exposure | 0.6130 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
