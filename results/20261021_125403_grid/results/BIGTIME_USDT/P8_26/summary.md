# EMA Hourly Continuation — BIGTIME/USDT P8_26

**Symbol:** BIGTIME/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 731 |
| net_profit_factor | 0.6486 |
| net_win_rate | 0.4610 |
| gross_profit_factor | 0.8599 |
| gross_win_rate | 0.4610 |
| sharpe_ratio | -4.0026 |
| sortino_ratio | -1.5382 |
| max_drawdown | 0.8320 |
| cagr | -0.5057 |
| net_avg_win | 45.5056 |
| net_avg_loss | -60.0118 |
| avg_hold_time_bars | 7.3051 |
| exposure | 0.2417 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
