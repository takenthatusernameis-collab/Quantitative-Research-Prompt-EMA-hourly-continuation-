# EMA Hourly Continuation — PUFFER/USDT P21_144

**Symbol:** PUFFER/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 315 |
| net_profit_factor | 1.0769 |
| net_win_rate | 0.5587 |
| gross_profit_factor | 1.2606 |
| gross_win_rate | 0.5587 |
| sharpe_ratio | 0.5246 |
| sortino_ratio | 0.1513 |
| max_drawdown | 0.1070 |
| cagr | 0.0595 |
| net_avg_win | 98.3237 |
| net_avg_loss | -115.6049 |
| avg_hold_time_bars | 30.1968 |
| exposure | 0.5383 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
