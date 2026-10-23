# EMA Hourly Continuation — OSMO/USDT P34_50

**Symbol:** OSMO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 895 |
| net_profit_factor | 0.2966 |
| net_win_rate | 0.3754 |
| gross_profit_factor | 0.7337 |
| gross_win_rate | 0.4123 |
| sharpe_ratio | -10.6458 |
| sortino_ratio | -4.5676 |
| max_drawdown | 0.9970 |
| cagr | -0.9003 |
| net_avg_win | 12.5130 |
| net_avg_loss | -25.3556 |
| avg_hold_time_bars | 3.3855 |
| exposure | 0.1377 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
