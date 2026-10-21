# EMA Hourly Continuation — EIGEN/USDT P26_100

**Symbol:** EIGEN/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.7957 |
| net_win_rate | 0.4860 |
| gross_profit_factor | 0.9295 |
| gross_win_rate | 0.4860 |
| sharpe_ratio | -1.3928 |
| sortino_ratio | -0.4161 |
| max_drawdown | 0.3326 |
| cagr | -0.1757 |
| net_avg_win | 73.2509 |
| net_avg_loss | -87.0563 |
| avg_hold_time_bars | 15.2542 |
| exposure | 0.3039 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
