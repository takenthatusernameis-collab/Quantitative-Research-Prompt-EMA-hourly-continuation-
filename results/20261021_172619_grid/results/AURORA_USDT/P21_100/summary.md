# EMA Hourly Continuation — AURORA/USDT P21_100

**Symbol:** AURORA/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.7616 |
| net_win_rate | 0.4932 |
| gross_profit_factor | 0.9813 |
| gross_win_rate | 0.4932 |
| sharpe_ratio | -1.6951 |
| sortino_ratio | -0.4643 |
| max_drawdown | 0.4494 |
| cagr | -0.1919 |
| net_avg_win | 73.1419 |
| net_avg_loss | -93.4549 |
| avg_hold_time_bars | 24.3515 |
| exposure | 0.4062 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
