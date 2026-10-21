# EMA Hourly Continuation — SHIB/USDT P8_144

**Symbol:** SHIB/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.9635 |
| net_win_rate | 0.5468 |
| gross_profit_factor | 1.1946 |
| gross_win_rate | 0.5468 |
| sharpe_ratio | -0.1895 |
| sortino_ratio | -0.0545 |
| max_drawdown | 0.2348 |
| cagr | -0.0310 |
| net_avg_win | 92.7868 |
| net_avg_loss | -116.2076 |
| avg_hold_time_bars | 38.7620 |
| exposure | 0.6960 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
