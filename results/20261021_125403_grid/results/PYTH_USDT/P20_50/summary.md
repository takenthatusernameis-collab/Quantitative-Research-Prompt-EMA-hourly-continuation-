# EMA Hourly Continuation — PYTH/USDT P20_50

**Symbol:** PYTH/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.7814 |
| net_win_rate | 0.4980 |
| gross_profit_factor | 0.9934 |
| gross_win_rate | 0.4980 |
| sharpe_ratio | -1.7574 |
| sortino_ratio | -0.5642 |
| max_drawdown | 0.4968 |
| cagr | -0.2287 |
| net_avg_win | 68.5006 |
| net_avg_loss | -86.9707 |
| avg_hold_time_bars | 7.6873 |
| exposure | 0.1754 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
