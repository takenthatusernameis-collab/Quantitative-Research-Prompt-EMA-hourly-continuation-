# EMA Hourly Continuation — MERL/USDT P20_100

**Symbol:** MERL/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.7950 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.9348 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -1.6487 |
| sortino_ratio | -0.5026 |
| max_drawdown | 0.5118 |
| cagr | -0.2078 |
| net_avg_win | 78.2504 |
| net_avg_loss | -90.5705 |
| avg_hold_time_bars | 20.2516 |
| exposure | 0.4219 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
