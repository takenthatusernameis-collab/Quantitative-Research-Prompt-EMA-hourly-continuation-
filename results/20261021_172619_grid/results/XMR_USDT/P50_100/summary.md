# EMA Hourly Continuation — XMR/USDT P50_100

**Symbol:** XMR/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.5288 |
| net_win_rate | 0.4214 |
| gross_profit_factor | 0.7335 |
| gross_win_rate | 0.4214 |
| sharpe_ratio | -3.3840 |
| sortino_ratio | -0.8319 |
| max_drawdown | 0.6238 |
| cagr | -0.3178 |
| net_avg_win | 54.9809 |
| net_avg_loss | -75.7265 |
| avg_hold_time_bars | 8.9532 |
| exposure | 0.1217 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
