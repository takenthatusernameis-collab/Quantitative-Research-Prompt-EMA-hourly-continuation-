# EMA Hourly Continuation — LPT/USDT P55_100

**Symbol:** LPT/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.5123 |
| net_win_rate | 0.4184 |
| gross_profit_factor | 0.6877 |
| gross_win_rate | 0.4184 |
| sharpe_ratio | -3.9257 |
| sortino_ratio | -1.0855 |
| max_drawdown | 0.7200 |
| cagr | -0.3945 |
| net_avg_win | 47.3229 |
| net_avg_loss | -66.4599 |
| avg_hold_time_bars | 7.7289 |
| exposure | 0.1335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
