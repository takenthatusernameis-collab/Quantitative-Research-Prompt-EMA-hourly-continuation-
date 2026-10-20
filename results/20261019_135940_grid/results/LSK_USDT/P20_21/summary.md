# EMA Hourly Continuation — LSK/USDT P20_21

**Symbol:** LSK/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 976 |
| net_profit_factor | 0.1984 |
| net_win_rate | 0.3463 |
| gross_profit_factor | 0.7938 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -13.4202 |
| sortino_ratio | -6.1556 |
| max_drawdown | 0.9998 |
| cagr | -0.9650 |
| net_avg_win | 7.3219 |
| net_avg_loss | -19.5495 |
| avg_hold_time_bars | 2.8391 |
| exposure | 0.1260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
