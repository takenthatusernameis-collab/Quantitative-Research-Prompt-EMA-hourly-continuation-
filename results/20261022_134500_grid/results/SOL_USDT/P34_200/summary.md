# EMA Hourly Continuation — SOL/USDT P34_200

**Symbol:** SOL/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.5459 |
| net_win_rate | 0.4591 |
| gross_profit_factor | 0.8400 |
| gross_win_rate | 0.4620 |
| sharpe_ratio | -3.2504 |
| sortino_ratio | -0.8452 |
| max_drawdown | 0.6554 |
| cagr | -0.3351 |
| net_avg_win | 49.0946 |
| net_avg_loss | -76.3244 |
| avg_hold_time_bars | 34.4591 |
| exposure | 0.5357 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
