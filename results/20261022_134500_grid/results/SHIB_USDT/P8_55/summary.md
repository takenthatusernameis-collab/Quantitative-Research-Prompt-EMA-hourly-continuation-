# EMA Hourly Continuation — SHIB/USDT P8_55

**Symbol:** SHIB/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1093 |
| net_profit_factor | 0.4958 |
| net_win_rate | 0.4410 |
| gross_profit_factor | 0.8232 |
| gross_win_rate | 0.4547 |
| sharpe_ratio | -7.9824 |
| sortino_ratio | -3.6809 |
| max_drawdown | 0.9906 |
| cagr | -0.8441 |
| net_avg_win | 20.2078 |
| net_avg_loss | -32.1541 |
| avg_hold_time_bars | 9.4931 |
| exposure | 0.4716 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
