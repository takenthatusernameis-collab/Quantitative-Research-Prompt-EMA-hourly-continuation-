# EMA Hourly Continuation — BRETT/USDT P20_55

**Symbol:** BRETT/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.8261 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9984 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.3743 |
| sortino_ratio | -0.4428 |
| max_drawdown | 0.4390 |
| cagr | -0.1862 |
| net_avg_win | 76.8409 |
| net_avg_loss | -93.0215 |
| avg_hold_time_bars | 8.3389 |
| exposure | 0.1918 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
