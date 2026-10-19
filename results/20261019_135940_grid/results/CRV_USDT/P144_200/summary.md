# EMA Hourly Continuation — CRV/USDT P144_200

**Symbol:** CRV/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.4623 |
| net_win_rate | 0.4525 |
| gross_profit_factor | 0.8261 |
| gross_win_rate | 0.4587 |
| sharpe_ratio | -5.1286 |
| sortino_ratio | -1.5981 |
| max_drawdown | 0.8600 |
| cagr | -0.5412 |
| net_avg_win | 33.7043 |
| net_avg_loss | -60.2557 |
| avg_hold_time_bars | 3.4566 |
| exposure | 0.0760 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
