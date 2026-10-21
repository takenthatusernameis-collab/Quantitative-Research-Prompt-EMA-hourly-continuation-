# EMA Hourly Continuation — AURORA/USDT P55_100

**Symbol:** AURORA/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.5611 |
| net_win_rate | 0.4490 |
| gross_profit_factor | 0.8114 |
| gross_win_rate | 0.4490 |
| sharpe_ratio | -3.1597 |
| sortino_ratio | -0.7987 |
| max_drawdown | 0.6075 |
| cagr | -0.3073 |
| net_avg_win | 54.6143 |
| net_avg_loss | -79.3254 |
| avg_hold_time_bars | 9.5828 |
| exposure | 0.1368 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
