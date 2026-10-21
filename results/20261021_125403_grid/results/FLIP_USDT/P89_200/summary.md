# EMA Hourly Continuation — FLIP/USDT P89_200

**Symbol:** FLIP/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 216 |
| net_profit_factor | 0.5365 |
| net_win_rate | 0.4306 |
| gross_profit_factor | 0.7491 |
| gross_win_rate | 0.4352 |
| sharpe_ratio | -2.7206 |
| sortino_ratio | -0.5659 |
| max_drawdown | 0.4974 |
| cagr | -0.2288 |
| net_avg_win | 59.6426 |
| net_avg_loss | -84.0514 |
| avg_hold_time_bars | 23.3380 |
| exposure | 0.2291 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
