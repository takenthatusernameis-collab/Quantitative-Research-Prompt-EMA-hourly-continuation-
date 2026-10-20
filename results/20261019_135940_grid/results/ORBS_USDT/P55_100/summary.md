# EMA Hourly Continuation — ORBS/USDT P55_100

**Symbol:** ORBS/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 668 |
| net_profit_factor | 0.4462 |
| net_win_rate | 0.4147 |
| gross_profit_factor | 0.9241 |
| gross_win_rate | 0.4431 |
| sharpe_ratio | -7.6882 |
| sortino_ratio | -2.8354 |
| max_drawdown | 0.9701 |
| cagr | -0.7516 |
| net_avg_win | 28.2109 |
| net_avg_loss | -44.7871 |
| avg_hold_time_bars | 5.7784 |
| exposure | 0.1755 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
