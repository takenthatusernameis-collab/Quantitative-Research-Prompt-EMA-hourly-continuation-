# EMA Hourly Continuation — SUPER/USDT P55_144

**Symbol:** SUPER/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.6574 |
| net_win_rate | 0.4990 |
| gross_profit_factor | 1.0077 |
| gross_win_rate | 0.5133 |
| sharpe_ratio | -2.7642 |
| sortino_ratio | -0.8572 |
| max_drawdown | 0.6649 |
| cagr | -0.3381 |
| net_avg_win | 50.7351 |
| net_avg_loss | -76.8638 |
| avg_hold_time_bars | 11.3395 |
| exposure | 0.2520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
