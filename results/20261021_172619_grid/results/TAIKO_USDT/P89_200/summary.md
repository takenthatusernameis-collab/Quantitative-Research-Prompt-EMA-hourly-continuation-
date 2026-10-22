# EMA Hourly Continuation — TAIKO/USDT P89_200

**Symbol:** TAIKO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 222 |
| net_profit_factor | 0.7157 |
| net_win_rate | 0.4820 |
| gross_profit_factor | 0.9289 |
| gross_win_rate | 0.4820 |
| sharpe_ratio | -1.6174 |
| sortino_ratio | -0.3537 |
| max_drawdown | 0.3389 |
| cagr | -0.1499 |
| net_avg_win | 75.3603 |
| net_avg_loss | -97.9665 |
| avg_hold_time_bars | 16.2568 |
| exposure | 0.1734 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
