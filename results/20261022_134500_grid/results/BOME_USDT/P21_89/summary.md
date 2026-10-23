# EMA Hourly Continuation — BOME/USDT P21_89

**Symbol:** BOME/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 660 |
| net_profit_factor | 0.5790 |
| net_win_rate | 0.4591 |
| gross_profit_factor | 0.8136 |
| gross_win_rate | 0.4636 |
| sharpe_ratio | -3.9574 |
| sortino_ratio | -1.4347 |
| max_drawdown | 0.8339 |
| cagr | -0.4930 |
| net_avg_win | 37.1425 |
| net_avg_loss | -54.4490 |
| avg_hold_time_bars | 12.9591 |
| exposure | 0.3888 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
