# EMA Hourly Continuation — AIOZ/USDT P50_100

**Symbol:** AIOZ/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.9895 |
| net_win_rate | 0.5552 |
| gross_profit_factor | 1.2384 |
| gross_win_rate | 0.5552 |
| sharpe_ratio | -0.0130 |
| sortino_ratio | -0.0036 |
| max_drawdown | 0.2504 |
| cagr | -0.0087 |
| net_avg_win | 101.8629 |
| net_avg_loss | -128.5207 |
| avg_hold_time_bars | 10.1713 |
| exposure | 0.1674 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
