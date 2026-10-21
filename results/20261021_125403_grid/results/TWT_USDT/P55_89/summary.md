# EMA Hourly Continuation — TWT/USDT P55_89

**Symbol:** TWT/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.5814 |
| net_win_rate | 0.4713 |
| gross_profit_factor | 0.9068 |
| gross_win_rate | 0.4713 |
| sharpe_ratio | -3.2279 |
| sortino_ratio | -0.8639 |
| max_drawdown | 0.6405 |
| cagr | -0.3274 |
| net_avg_win | 53.4150 |
| net_avg_loss | -81.8815 |
| avg_hold_time_bars | 6.1322 |
| exposure | 0.0970 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
