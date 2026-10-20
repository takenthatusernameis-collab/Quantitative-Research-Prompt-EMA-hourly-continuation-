# EMA Hourly Continuation — AEVO/USDT P8_200

**Symbol:** AEVO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 263 |
| net_profit_factor | 0.6557 |
| net_win_rate | 0.4677 |
| gross_profit_factor | 0.8786 |
| gross_win_rate | 0.4715 |
| sharpe_ratio | -2.0967 |
| sortino_ratio | -0.4718 |
| max_drawdown | 0.4637 |
| cagr | -0.2058 |
| net_avg_win | 68.2504 |
| net_avg_loss | -91.4491 |
| avg_hold_time_bars | 72.0722 |
| exposure | 0.8577 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
