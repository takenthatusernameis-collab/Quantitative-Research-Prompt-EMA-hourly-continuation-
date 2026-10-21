# EMA Hourly Continuation — FIL/USDT P8_26

**Symbol:** FIL/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 612 |
| net_profit_factor | 0.7160 |
| net_win_rate | 0.4951 |
| gross_profit_factor | 0.9765 |
| gross_win_rate | 0.4951 |
| sharpe_ratio | -2.5482 |
| sortino_ratio | -0.9046 |
| max_drawdown | 0.6684 |
| cagr | -0.3386 |
| net_avg_win | 53.7502 |
| net_avg_loss | -73.6108 |
| avg_hold_time_bars | 6.8922 |
| exposure | 0.1917 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
