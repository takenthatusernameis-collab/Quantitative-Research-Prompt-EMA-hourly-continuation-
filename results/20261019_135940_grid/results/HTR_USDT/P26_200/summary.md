# EMA Hourly Continuation — HTR/USDT P26_200

**Symbol:** HTR/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.5739 |
| net_win_rate | 0.4318 |
| gross_profit_factor | 0.8250 |
| gross_win_rate | 0.4379 |
| sharpe_ratio | -4.6501 |
| sortino_ratio | -1.4238 |
| max_drawdown | 0.8414 |
| cagr | -0.5114 |
| net_avg_win | 53.0063 |
| net_avg_loss | -70.1862 |
| avg_hold_time_bars | 23.9287 |
| exposure | 0.5340 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
