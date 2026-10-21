# EMA Hourly Continuation — EIGEN/USDT P8_100

**Symbol:** EIGEN/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.8759 |
| net_win_rate | 0.5028 |
| gross_profit_factor | 1.0097 |
| gross_win_rate | 0.5028 |
| sharpe_ratio | -0.8696 |
| sortino_ratio | -0.2622 |
| max_drawdown | 0.3384 |
| cagr | -0.1172 |
| net_avg_win | 87.5206 |
| net_avg_loss | -101.0307 |
| avg_hold_time_bars | 32.8343 |
| exposure | 0.6614 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
