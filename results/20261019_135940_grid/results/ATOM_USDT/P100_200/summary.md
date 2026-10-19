# EMA Hourly Continuation — ATOM/USDT P100_200

**Symbol:** ATOM/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.4477 |
| net_win_rate | 0.4414 |
| gross_profit_factor | 0.8018 |
| gross_win_rate | 0.4523 |
| sharpe_ratio | -4.4940 |
| sortino_ratio | -1.2136 |
| max_drawdown | 0.7777 |
| cagr | -0.4492 |
| net_avg_win | 38.8537 |
| net_avg_loss | -68.5739 |
| avg_hold_time_bars | 9.2262 |
| exposure | 0.1539 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
