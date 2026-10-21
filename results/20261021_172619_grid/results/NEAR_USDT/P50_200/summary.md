# EMA Hourly Continuation — NEAR/USDT P50_200

**Symbol:** NEAR/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.8453 |
| net_win_rate | 0.5053 |
| gross_profit_factor | 1.0072 |
| gross_win_rate | 0.5053 |
| sharpe_ratio | -0.7995 |
| sortino_ratio | -0.1922 |
| max_drawdown | 0.2650 |
| cagr | -0.0863 |
| net_avg_win | 78.0511 |
| net_avg_loss | -94.3318 |
| avg_hold_time_bars | 29.0391 |
| exposure | 0.3709 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
