# EMA Hourly Continuation — AERO/USDT P8_26

**Symbol:** AERO/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1539 |
| net_profit_factor | 0.4021 |
| net_win_rate | 0.4457 |
| gross_profit_factor | 0.7201 |
| gross_win_rate | 0.4594 |
| sharpe_ratio | -9.3117 |
| sortino_ratio | -5.1161 |
| max_drawdown | 0.9984 |
| cagr | -0.9219 |
| net_avg_win | 9.7885 |
| net_avg_loss | -19.5760 |
| avg_hold_time_bars | 3.6777 |
| exposure | 0.2573 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
