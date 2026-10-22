# EMA Hourly Continuation — ZBCN/USDT P34_200

**Symbol:** ZBCN/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 511 |
| net_profit_factor | 0.6973 |
| net_win_rate | 0.4912 |
| gross_profit_factor | 0.9540 |
| gross_win_rate | 0.4912 |
| sharpe_ratio | -2.5875 |
| sortino_ratio | -0.8261 |
| max_drawdown | 0.6473 |
| cagr | -0.3286 |
| net_avg_win | 57.4435 |
| net_avg_loss | -79.5231 |
| avg_hold_time_bars | 18.1487 |
| exposure | 0.4291 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
