# EMA Hourly Continuation — BIGTIME/USDT P26_200

**Symbol:** BIGTIME/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.9604 |
| net_win_rate | 0.5309 |
| gross_profit_factor | 1.1272 |
| gross_win_rate | 0.5309 |
| sharpe_ratio | -0.1727 |
| sortino_ratio | -0.0436 |
| max_drawdown | 0.1868 |
| cagr | -0.0248 |
| net_avg_win | 91.3850 |
| net_avg_loss | -107.7043 |
| avg_hold_time_bars | 43.5603 |
| exposure | 0.6052 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
