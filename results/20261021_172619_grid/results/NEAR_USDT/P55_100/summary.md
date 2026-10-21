# EMA Hourly Continuation — NEAR/USDT P55_100

**Symbol:** NEAR/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.7126 |
| net_win_rate | 0.4832 |
| gross_profit_factor | 0.9171 |
| gross_win_rate | 0.4832 |
| sharpe_ratio | -1.7311 |
| sortino_ratio | -0.4272 |
| max_drawdown | 0.3940 |
| cagr | -0.1778 |
| net_avg_win | 66.8414 |
| net_avg_loss | -87.7145 |
| avg_hold_time_bars | 6.6846 |
| exposure | 0.0905 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
