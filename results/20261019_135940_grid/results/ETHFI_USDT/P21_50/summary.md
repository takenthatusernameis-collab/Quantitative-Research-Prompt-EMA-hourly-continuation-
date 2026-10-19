# EMA Hourly Continuation — ETHFI/USDT P21_50

**Symbol:** ETHFI/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1052 |
| net_profit_factor | 0.5659 |
| net_win_rate | 0.4420 |
| gross_profit_factor | 0.9246 |
| gross_win_rate | 0.4525 |
| sharpe_ratio | -6.9276 |
| sortino_ratio | -3.1592 |
| max_drawdown | 0.9803 |
| cagr | -0.7847 |
| net_avg_win | 27.4385 |
| net_avg_loss | -38.4115 |
| avg_hold_time_bars | 4.5409 |
| exposure | 0.2171 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
