# EMA Hourly Continuation — REQ/USDT P55_100

**Symbol:** REQ/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.6062 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 0.9728 |
| gross_win_rate | 0.4777 |
| sharpe_ratio | -3.4589 |
| sortino_ratio | -0.9692 |
| max_drawdown | 0.6816 |
| cagr | -0.3599 |
| net_avg_win | 57.3135 |
| net_avg_loss | -85.5597 |
| avg_hold_time_bars | 8.0472 |
| exposure | 0.1394 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
