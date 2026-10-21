# EMA Hourly Continuation — ICP/USDT P50_100

**Symbol:** ICP/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.7369 |
| net_win_rate | 0.4972 |
| gross_profit_factor | 0.9778 |
| gross_win_rate | 0.4972 |
| sharpe_ratio | -1.7616 |
| sortino_ratio | -0.4792 |
| max_drawdown | 0.4390 |
| cagr | -0.1973 |
| net_avg_win | 66.3716 |
| net_avg_loss | -89.0702 |
| avg_hold_time_bars | 8.8083 |
| exposure | 0.1441 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
