# EMA Hourly Continuation — UQC/USDT P50_100

**Symbol:** UQC/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.1613 |
| net_win_rate | 0.2485 |
| gross_profit_factor | 0.3940 |
| gross_win_rate | 0.2754 |
| sharpe_ratio | -8.5807 |
| sortino_ratio | -2.2595 |
| max_drawdown | 0.9525 |
| cagr | -0.7013 |
| net_avg_win | 22.0703 |
| net_avg_loss | -45.2467 |
| avg_hold_time_bars | 26.4581 |
| exposure | 0.4000 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
