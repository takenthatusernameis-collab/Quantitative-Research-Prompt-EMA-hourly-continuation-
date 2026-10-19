# EMA Hourly Continuation — EIGEN/USDT P26_100

**Symbol:** EIGEN/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 557 |
| net_profit_factor | 0.6525 |
| net_win_rate | 0.4650 |
| gross_profit_factor | 0.8983 |
| gross_win_rate | 0.4722 |
| sharpe_ratio | -3.7402 |
| sortino_ratio | -1.3757 |
| max_drawdown | 0.7402 |
| cagr | -0.4797 |
| net_avg_win | 53.5274 |
| net_avg_loss | -71.2932 |
| avg_hold_time_bars | 10.4578 |
| exposure | 0.3241 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
