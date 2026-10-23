# EMA Hourly Continuation — CELR/USDT P34_50

**Symbol:** CELR/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 913 |
| net_profit_factor | 0.4137 |
| net_win_rate | 0.4294 |
| gross_profit_factor | 0.8497 |
| gross_win_rate | 0.4469 |
| sharpe_ratio | -8.2412 |
| sortino_ratio | -3.5341 |
| max_drawdown | 0.9875 |
| cagr | -0.8221 |
| net_avg_win | 17.7665 |
| net_avg_loss | -32.3150 |
| avg_hold_time_bars | 3.3844 |
| exposure | 0.1398 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
