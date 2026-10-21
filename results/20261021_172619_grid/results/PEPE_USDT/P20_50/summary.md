# EMA Hourly Continuation — PEPE/USDT P20_50

**Symbol:** PEPE/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.7310 |
| net_win_rate | 0.4801 |
| gross_profit_factor | 0.9195 |
| gross_win_rate | 0.4801 |
| sharpe_ratio | -2.0361 |
| sortino_ratio | -0.6005 |
| max_drawdown | 0.5084 |
| cagr | -0.2407 |
| net_avg_win | 66.1714 |
| net_avg_loss | -83.5867 |
| avg_hold_time_bars | 8.4379 |
| exposure | 0.1638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
