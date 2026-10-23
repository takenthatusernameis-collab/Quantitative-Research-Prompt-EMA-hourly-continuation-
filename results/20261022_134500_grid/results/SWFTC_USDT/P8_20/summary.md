# EMA Hourly Continuation — SWFTC/USDT P8_20

**Symbol:** SWFTC/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1604 |
| net_profit_factor | 0.2914 |
| net_win_rate | 0.3953 |
| gross_profit_factor | 0.6578 |
| gross_win_rate | 0.4208 |
| sharpe_ratio | -13.7683 |
| sortino_ratio | -7.8016 |
| max_drawdown | 1.0000 |
| cagr | -0.9832 |
| net_avg_win | 6.4870 |
| net_avg_loss | -14.5489 |
| avg_hold_time_bars | 3.0555 |
| exposure | 0.2228 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
