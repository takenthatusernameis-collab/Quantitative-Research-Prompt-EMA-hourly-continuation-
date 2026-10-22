# EMA Hourly Continuation — CATI/USDT P50_100

**Symbol:** CATI/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 270 |
| net_profit_factor | 0.6745 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.8815 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -2.3667 |
| sortino_ratio | -0.6073 |
| max_drawdown | 0.4957 |
| cagr | -0.2443 |
| net_avg_win | 72.6871 |
| net_avg_loss | -94.2941 |
| avg_hold_time_bars | 10.2185 |
| exposure | 0.1512 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
