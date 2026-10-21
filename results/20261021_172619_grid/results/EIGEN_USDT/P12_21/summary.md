# EMA Hourly Continuation — EIGEN/USDT P12_21

**Symbol:** EIGEN/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 254 |
| net_profit_factor | 0.7043 |
| net_win_rate | 0.4724 |
| gross_profit_factor | 0.8964 |
| gross_win_rate | 0.4724 |
| sharpe_ratio | -1.9901 |
| sortino_ratio | -0.5006 |
| max_drawdown | 0.4297 |
| cagr | -0.2061 |
| net_avg_win | 74.8371 |
| net_avg_loss | -95.1607 |
| avg_hold_time_bars | 4.4370 |
| exposure | 0.0627 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
