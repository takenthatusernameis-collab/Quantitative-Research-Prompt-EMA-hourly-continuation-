# EMA Hourly Continuation — ORDI/USDT P12_89

**Symbol:** ORDI/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 777 |
| net_profit_factor | 0.5951 |
| net_win_rate | 0.4453 |
| gross_profit_factor | 0.8870 |
| gross_win_rate | 0.4582 |
| sharpe_ratio | -5.0075 |
| sortino_ratio | -1.9604 |
| max_drawdown | 0.9093 |
| cagr | -0.6094 |
| net_avg_win | 38.4634 |
| net_avg_loss | -51.8909 |
| avg_hold_time_bars | 14.7773 |
| exposure | 0.5219 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
