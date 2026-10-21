# EMA Hourly Continuation — ASTR/USDT P34_200

**Symbol:** ASTR/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.7576 |
| net_win_rate | 0.4843 |
| gross_profit_factor | 0.9483 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -1.5339 |
| sortino_ratio | -0.3688 |
| max_drawdown | 0.3969 |
| cagr | -0.1574 |
| net_avg_win | 78.8997 |
| net_avg_loss | -97.8081 |
| avg_hold_time_bars | 40.6098 |
| exposure | 0.5274 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
