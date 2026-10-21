# EMA Hourly Continuation — GMX/USDT P50_55

**Symbol:** GMX/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 228 |
| net_profit_factor | 0.5338 |
| net_win_rate | 0.4605 |
| gross_profit_factor | 0.8406 |
| gross_win_rate | 0.4605 |
| sharpe_ratio | -2.8754 |
| sortino_ratio | -0.6229 |
| max_drawdown | 0.5232 |
| cagr | -0.2498 |
| net_avg_win | 56.0479 |
| net_avg_loss | -89.6398 |
| avg_hold_time_bars | 5.0263 |
| exposure | 0.0521 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
