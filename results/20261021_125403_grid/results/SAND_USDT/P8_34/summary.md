# EMA Hourly Continuation — SAND/USDT P8_34

**Symbol:** SAND/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 710 |
| net_profit_factor | 0.7042 |
| net_win_rate | 0.4873 |
| gross_profit_factor | 0.9490 |
| gross_win_rate | 0.4873 |
| sharpe_ratio | -2.9132 |
| sortino_ratio | -1.1108 |
| max_drawdown | 0.7279 |
| cagr | -0.3987 |
| net_avg_win | 49.6282 |
| net_avg_loss | -66.9897 |
| avg_hold_time_bars | 9.4380 |
| exposure | 0.3046 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
