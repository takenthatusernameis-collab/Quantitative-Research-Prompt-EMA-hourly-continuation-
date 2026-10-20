# EMA Hourly Continuation — DEEP/USDT P21_55

**Symbol:** DEEP/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 679 |
| net_profit_factor | 0.6860 |
| net_win_rate | 0.4934 |
| gross_profit_factor | 1.0162 |
| gross_win_rate | 0.5007 |
| sharpe_ratio | -3.8617 |
| sortino_ratio | -1.5869 |
| max_drawdown | 0.7914 |
| cagr | -0.5304 |
| net_avg_win | 51.0213 |
| net_avg_loss | -72.4241 |
| avg_hold_time_bars | 5.8115 |
| exposure | 0.2234 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
