# EMA Hourly Continuation — REZ/USDT P26_89

**Symbol:** REZ/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.7211 |
| net_win_rate | 0.4890 |
| gross_profit_factor | 1.0069 |
| gross_win_rate | 0.4978 |
| sharpe_ratio | -2.9239 |
| sortino_ratio | -1.0918 |
| max_drawdown | 0.7408 |
| cagr | -0.4012 |
| net_avg_win | 55.6503 |
| net_avg_loss | -73.8549 |
| avg_hold_time_bars | 10.6779 |
| exposure | 0.3365 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
