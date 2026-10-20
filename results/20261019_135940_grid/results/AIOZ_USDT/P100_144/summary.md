# EMA Hourly Continuation — AIOZ/USDT P100_144

**Symbol:** AIOZ/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 543 |
| net_profit_factor | 0.5350 |
| net_win_rate | 0.4494 |
| gross_profit_factor | 0.9314 |
| gross_win_rate | 0.4659 |
| sharpe_ratio | -5.3463 |
| sortino_ratio | -1.7599 |
| max_drawdown | 0.8931 |
| cagr | -0.5759 |
| net_avg_win | 41.6844 |
| net_avg_loss | -63.5830 |
| avg_hold_time_bars | 3.7330 |
| exposure | 0.0921 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
