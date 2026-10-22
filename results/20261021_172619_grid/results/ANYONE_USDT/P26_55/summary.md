# EMA Hourly Continuation — ANYONE/USDT P26_55

**Symbol:** ANYONE/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.5818 |
| net_win_rate | 0.4190 |
| gross_profit_factor | 0.7106 |
| gross_win_rate | 0.4190 |
| sharpe_ratio | -3.5699 |
| sortino_ratio | -1.0628 |
| max_drawdown | 0.6733 |
| cagr | -0.3893 |
| net_avg_win | 55.6275 |
| net_avg_loss | -68.9385 |
| avg_hold_time_bars | 7.7406 |
| exposure | 0.1568 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
