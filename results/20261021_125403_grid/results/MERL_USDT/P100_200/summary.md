# EMA Hourly Continuation — MERL/USDT P100_200

**Symbol:** MERL/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 262 |
| net_profit_factor | 0.7069 |
| net_win_rate | 0.4542 |
| gross_profit_factor | 0.8464 |
| gross_win_rate | 0.4542 |
| sharpe_ratio | -1.8751 |
| sortino_ratio | -0.4310 |
| max_drawdown | 0.3997 |
| cagr | -0.1806 |
| net_avg_win | 79.5982 |
| net_avg_loss | -93.7089 |
| avg_hold_time_bars | 12.9237 |
| exposure | 0.1543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
