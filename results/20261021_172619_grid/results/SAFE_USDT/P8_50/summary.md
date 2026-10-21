# EMA Hourly Continuation — SAFE/USDT P8_50

**Symbol:** SAFE/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 680 |
| net_profit_factor | 0.7965 |
| net_win_rate | 0.5015 |
| gross_profit_factor | 0.9983 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -1.8554 |
| sortino_ratio | -0.6957 |
| max_drawdown | 0.5666 |
| cagr | -0.2752 |
| net_avg_win | 63.3175 |
| net_avg_loss | -79.9628 |
| avg_hold_time_bars | 14.2897 |
| exposure | 0.4450 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
