# EMA Hourly Continuation — ROSE/USDT P12_55

**Symbol:** ROSE/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1044 |
| net_profit_factor | 0.6341 |
| net_win_rate | 0.4655 |
| gross_profit_factor | 0.9932 |
| gross_win_rate | 0.4732 |
| sharpe_ratio | -5.8596 |
| sortino_ratio | -2.6575 |
| max_drawdown | 0.9637 |
| cagr | -0.7226 |
| net_avg_win | 34.2297 |
| net_avg_loss | -47.0182 |
| avg_hold_time_bars | 8.3305 |
| exposure | 0.3953 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
