# EMA Hourly Continuation — CGPT/USDT P34_100

**Symbol:** CGPT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.8238 |
| net_win_rate | 0.5036 |
| gross_profit_factor | 1.0297 |
| gross_win_rate | 0.5036 |
| sharpe_ratio | -1.3591 |
| sortino_ratio | -0.3960 |
| max_drawdown | 0.4322 |
| cagr | -0.1677 |
| net_avg_win | 83.0054 |
| net_avg_loss | -102.2365 |
| avg_hold_time_bars | 12.9637 |
| exposure | 0.2434 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
