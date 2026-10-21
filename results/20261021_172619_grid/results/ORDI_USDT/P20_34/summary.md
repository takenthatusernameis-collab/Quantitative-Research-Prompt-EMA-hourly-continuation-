# EMA Hourly Continuation — ORDI/USDT P20_34

**Symbol:** ORDI/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 325 |
| net_profit_factor | 0.7044 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9399 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -2.0223 |
| sortino_ratio | -0.5217 |
| max_drawdown | 0.4552 |
| cagr | -0.2128 |
| net_avg_win | 68.5528 |
| net_avg_loss | -90.9509 |
| avg_hold_time_bars | 4.7508 |
| exposure | 0.0702 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
