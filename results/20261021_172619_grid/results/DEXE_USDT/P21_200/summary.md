# EMA Hourly Continuation — DEXE/USDT P21_200

**Symbol:** DEXE/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 254 |
| net_profit_factor | 0.9970 |
| net_win_rate | 0.5433 |
| gross_profit_factor | 1.1689 |
| gross_win_rate | 0.5433 |
| sharpe_ratio | 0.0364 |
| sortino_ratio | 0.0084 |
| max_drawdown | 0.2248 |
| cagr | -0.0014 |
| net_avg_win | 82.7391 |
| net_avg_loss | -98.7300 |
| avg_hold_time_bars | 60.8110 |
| exposure | 0.7021 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
