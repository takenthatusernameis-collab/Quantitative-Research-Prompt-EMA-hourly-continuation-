# EMA Hourly Continuation — ATOM/USDT P12_100

**Symbol:** ATOM/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 465 |
| net_profit_factor | 0.8520 |
| net_win_rate | 0.5183 |
| gross_profit_factor | 1.0669 |
| gross_win_rate | 0.5183 |
| sharpe_ratio | -1.0341 |
| sortino_ratio | -0.3208 |
| max_drawdown | 0.3512 |
| cagr | -0.1396 |
| net_avg_win | 75.0948 |
| net_avg_loss | -94.8328 |
| avg_hold_time_bars | 25.9785 |
| exposure | 0.5491 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
