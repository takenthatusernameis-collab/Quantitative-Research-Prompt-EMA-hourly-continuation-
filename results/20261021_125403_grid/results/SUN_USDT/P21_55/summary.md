# EMA Hourly Continuation — SUN/USDT P21_55

**Symbol:** SUN/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.4657 |
| net_win_rate | 0.4160 |
| gross_profit_factor | 0.8229 |
| gross_win_rate | 0.4351 |
| sharpe_ratio | -6.4223 |
| sortino_ratio | -2.1036 |
| max_drawdown | 0.9209 |
| cagr | -0.6342 |
| net_avg_win | 36.8223 |
| net_avg_loss | -56.3264 |
| avg_hold_time_bars | 10.8073 |
| exposure | 0.2563 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
