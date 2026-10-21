# EMA Hourly Continuation — AIOZ/USDT P8_100

**Symbol:** AIOZ/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.8603 |
| net_win_rate | 0.5039 |
| gross_profit_factor | 1.0228 |
| gross_win_rate | 0.5039 |
| sharpe_ratio | -1.1790 |
| sortino_ratio | -0.3836 |
| max_drawdown | 0.4652 |
| cagr | -0.1651 |
| net_avg_win | 86.2532 |
| net_avg_loss | -101.8319 |
| avg_hold_time_bars | 26.4709 |
| exposure | 0.6209 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
