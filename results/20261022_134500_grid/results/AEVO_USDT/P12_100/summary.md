# EMA Hourly Continuation — AEVO/USDT P12_100

**Symbol:** AEVO/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 586 |
| net_profit_factor | 0.7201 |
| net_win_rate | 0.4863 |
| gross_profit_factor | 1.0179 |
| gross_win_rate | 0.4932 |
| sharpe_ratio | -2.9162 |
| sortino_ratio | -0.9956 |
| max_drawdown | 0.7262 |
| cagr | -0.3753 |
| net_avg_win | 62.7330 |
| net_avg_loss | -82.4806 |
| avg_hold_time_bars | 23.3379 |
| exposure | 0.6189 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
