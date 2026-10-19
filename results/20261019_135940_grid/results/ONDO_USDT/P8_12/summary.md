# EMA Hourly Continuation — ONDO/USDT P8_12

**Symbol:** ONDO/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1813 |
| net_profit_factor | 0.2389 |
| net_win_rate | 0.3894 |
| gross_profit_factor | 0.6350 |
| gross_win_rate | 0.4203 |
| sharpe_ratio | -16.7174 |
| sortino_ratio | -10.2100 |
| max_drawdown | 1.0000 |
| cagr | -0.9959 |
| net_avg_win | 4.4453 |
| net_avg_loss | -11.8685 |
| avg_hold_time_bars | 1.7579 |
| exposure | 0.1449 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
