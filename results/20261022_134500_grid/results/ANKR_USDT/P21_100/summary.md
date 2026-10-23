# EMA Hourly Continuation — ANKR/USDT P21_100

**Symbol:** ANKR/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 661 |
| net_profit_factor | 0.5312 |
| net_win_rate | 0.4372 |
| gross_profit_factor | 0.8604 |
| gross_win_rate | 0.4463 |
| sharpe_ratio | -5.5867 |
| sortino_ratio | -2.0069 |
| max_drawdown | 0.9195 |
| cagr | -0.6286 |
| net_avg_win | 35.9499 |
| net_avg_loss | -52.5762 |
| avg_hold_time_bars | 15.2557 |
| exposure | 0.4584 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
