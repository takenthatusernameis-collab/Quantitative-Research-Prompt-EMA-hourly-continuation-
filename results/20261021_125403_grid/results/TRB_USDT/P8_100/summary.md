# EMA Hourly Continuation — TRB/USDT P8_100

**Symbol:** TRB/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.7076 |
| net_win_rate | 0.4722 |
| gross_profit_factor | 0.8692 |
| gross_win_rate | 0.4722 |
| sharpe_ratio | -2.1366 |
| sortino_ratio | -0.6305 |
| max_drawdown | 0.5580 |
| cagr | -0.2513 |
| net_avg_win | 61.4608 |
| net_avg_loss | -77.7192 |
| avg_hold_time_bars | 34.1343 |
| exposure | 0.6673 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
