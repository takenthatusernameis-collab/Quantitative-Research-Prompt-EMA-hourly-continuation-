# EMA Hourly Continuation — ORDI/USDT P144_200

**Symbol:** ORDI/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.5136 |
| net_win_rate | 0.4683 |
| gross_profit_factor | 0.8845 |
| gross_win_rate | 0.4878 |
| sharpe_ratio | -3.8219 |
| sortino_ratio | -1.0876 |
| max_drawdown | 0.7345 |
| cagr | -0.4076 |
| net_avg_win | 40.2325 |
| net_avg_loss | -68.9891 |
| avg_hold_time_bars | 4.4707 |
| exposure | 0.0833 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
