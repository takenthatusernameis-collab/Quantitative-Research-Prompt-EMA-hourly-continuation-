# EMA Hourly Continuation — LPT/USDT P26_100

**Symbol:** LPT/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.6666 |
| net_win_rate | 0.4560 |
| gross_profit_factor | 0.8399 |
| gross_win_rate | 0.4560 |
| sharpe_ratio | -3.0026 |
| sortino_ratio | -0.9527 |
| max_drawdown | 0.6783 |
| cagr | -0.3559 |
| net_avg_win | 58.6474 |
| net_avg_loss | -73.7442 |
| avg_hold_time_bars | 14.0340 |
| exposure | 0.3190 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
