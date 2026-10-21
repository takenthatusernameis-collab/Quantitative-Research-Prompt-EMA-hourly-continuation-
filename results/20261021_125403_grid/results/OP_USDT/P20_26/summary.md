# EMA Hourly Continuation — OP/USDT P20_26

**Symbol:** OP/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 155 |
| net_profit_factor | 0.7455 |
| net_win_rate | 0.5097 |
| gross_profit_factor | 1.0298 |
| gross_win_rate | 0.5097 |
| sharpe_ratio | -1.1001 |
| sortino_ratio | -0.1971 |
| max_drawdown | 0.2328 |
| cagr | -0.0864 |
| net_avg_win | 75.2940 |
| net_avg_loss | -104.9883 |
| avg_hold_time_bars | 4.4774 |
| exposure | 0.0315 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
