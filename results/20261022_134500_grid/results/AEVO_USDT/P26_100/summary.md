# EMA Hourly Continuation — AEVO/USDT P26_100

**Symbol:** AEVO/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 673 |
| net_profit_factor | 0.6771 |
| net_win_rate | 0.4889 |
| gross_profit_factor | 0.9958 |
| gross_win_rate | 0.4978 |
| sharpe_ratio | -3.4186 |
| sortino_ratio | -1.2527 |
| max_drawdown | 0.7824 |
| cagr | -0.4459 |
| net_avg_win | 49.3560 |
| net_avg_loss | -69.7175 |
| avg_hold_time_bars | 12.2214 |
| exposure | 0.3722 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
