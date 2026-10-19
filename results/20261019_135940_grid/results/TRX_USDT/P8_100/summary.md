# EMA Hourly Continuation — TRX/USDT P8_100

**Symbol:** TRX/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.4432 |
| net_win_rate | 0.4315 |
| gross_profit_factor | 0.9665 |
| gross_win_rate | 0.4875 |
| sharpe_ratio | -7.5406 |
| sortino_ratio | -2.6844 |
| max_drawdown | 0.9706 |
| cagr | -0.7539 |
| net_avg_win | 27.8840 |
| net_avg_loss | -47.7481 |
| avg_hold_time_bars | 22.0202 |
| exposure | 0.6426 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
