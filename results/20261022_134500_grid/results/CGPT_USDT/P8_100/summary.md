# EMA Hourly Continuation — CGPT/USDT P8_100

**Symbol:** CGPT/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 621 |
| net_profit_factor | 0.7245 |
| net_win_rate | 0.5024 |
| gross_profit_factor | 1.0342 |
| gross_win_rate | 0.5089 |
| sharpe_ratio | -2.6327 |
| sortino_ratio | -0.9237 |
| max_drawdown | 0.6875 |
| cagr | -0.3577 |
| net_avg_win | 56.5603 |
| net_avg_loss | -78.8252 |
| avg_hold_time_bars | 24.0161 |
| exposure | 0.6779 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
