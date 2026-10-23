# EMA Hourly Continuation — FLIP/USDT P100_200

**Symbol:** FLIP/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 252 |
| net_profit_factor | 0.4401 |
| net_win_rate | 0.4048 |
| gross_profit_factor | 0.6782 |
| gross_win_rate | 0.4127 |
| sharpe_ratio | -3.9239 |
| sortino_ratio | -0.8771 |
| max_drawdown | 0.6624 |
| cagr | -0.3410 |
| net_avg_win | 50.0279 |
| net_avg_loss | -77.2914 |
| avg_hold_time_bars | 18.2738 |
| exposure | 0.2093 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
