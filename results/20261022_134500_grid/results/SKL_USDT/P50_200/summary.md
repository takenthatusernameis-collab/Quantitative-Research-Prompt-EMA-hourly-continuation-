# EMA Hourly Continuation — SKL/USDT P50_200

**Symbol:** SKL/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.6613 |
| net_win_rate | 0.4777 |
| gross_profit_factor | 0.9128 |
| gross_win_rate | 0.4832 |
| sharpe_ratio | -2.4270 |
| sortino_ratio | -0.6452 |
| max_drawdown | 0.5848 |
| cagr | -0.2653 |
| net_avg_win | 61.5281 |
| net_avg_loss | -85.0864 |
| avg_hold_time_bars | 26.8464 |
| exposure | 0.4369 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
