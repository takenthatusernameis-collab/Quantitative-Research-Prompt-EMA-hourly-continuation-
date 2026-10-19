# EMA Hourly Continuation — SAND/USDT P8_55

**Symbol:** SAND/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 983 |
| net_profit_factor | 0.4897 |
| net_win_rate | 0.4334 |
| gross_profit_factor | 0.8233 |
| gross_win_rate | 0.4446 |
| sharpe_ratio | -7.0075 |
| sortino_ratio | -3.0681 |
| max_drawdown | 0.9775 |
| cagr | -0.7788 |
| net_avg_win | 22.0139 |
| net_avg_loss | -34.3836 |
| avg_hold_time_bars | 10.9980 |
| exposure | 0.4914 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
