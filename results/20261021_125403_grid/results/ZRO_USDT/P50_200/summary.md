# EMA Hourly Continuation — ZRO/USDT P50_200

**Symbol:** ZRO/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 276 |
| net_profit_factor | 0.8451 |
| net_win_rate | 0.4964 |
| gross_profit_factor | 0.9818 |
| gross_win_rate | 0.4964 |
| sharpe_ratio | -0.8917 |
| sortino_ratio | -0.2198 |
| max_drawdown | 0.2653 |
| cagr | -0.0981 |
| net_avg_win | 85.2679 |
| net_avg_loss | -99.4440 |
| avg_hold_time_bars | 24.3116 |
| exposure | 0.3284 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
