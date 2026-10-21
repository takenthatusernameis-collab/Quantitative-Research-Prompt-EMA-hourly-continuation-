# EMA Hourly Continuation — NEAR/USDT P26_200

**Symbol:** NEAR/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.9985 |
| net_win_rate | 0.5373 |
| gross_profit_factor | 1.1552 |
| gross_win_rate | 0.5373 |
| sharpe_ratio | 0.0439 |
| sortino_ratio | 0.0104 |
| max_drawdown | 0.1406 |
| cagr | -0.0008 |
| net_avg_win | 91.0503 |
| net_avg_loss | -105.8958 |
| avg_hold_time_bars | 49.2463 |
| exposure | 0.5999 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
