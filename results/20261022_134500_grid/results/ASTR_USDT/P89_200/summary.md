# EMA Hourly Continuation — ASTR/USDT P89_200

**Symbol:** ASTR/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.6636 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0144 |
| gross_win_rate | 0.5056 |
| sharpe_ratio | -2.4109 |
| sortino_ratio | -0.6451 |
| max_drawdown | 0.5746 |
| cagr | -0.2635 |
| net_avg_win | 59.2603 |
| net_avg_loss | -89.2962 |
| avg_hold_time_bars | 14.2905 |
| exposure | 0.2315 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
