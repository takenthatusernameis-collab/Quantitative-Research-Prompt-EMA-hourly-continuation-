# EMA Hourly Continuation — ROSE/USDT P12_26

**Symbol:** ROSE/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1489 |
| net_profit_factor | 0.4049 |
| net_win_rate | 0.4385 |
| gross_profit_factor | 0.8430 |
| gross_win_rate | 0.4567 |
| sharpe_ratio | -10.3373 |
| sortino_ratio | -5.6305 |
| max_drawdown | 0.9991 |
| cagr | -0.9396 |
| net_avg_win | 10.4105 |
| net_avg_loss | -20.0830 |
| avg_hold_time_bars | 2.7643 |
| exposure | 0.1871 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
