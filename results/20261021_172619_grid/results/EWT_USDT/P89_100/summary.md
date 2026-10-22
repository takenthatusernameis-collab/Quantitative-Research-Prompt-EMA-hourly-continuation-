# EMA Hourly Continuation — EWT/USDT P89_100

**Symbol:** EWT/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 98 |
| net_profit_factor | 0.4521 |
| net_win_rate | 0.3776 |
| gross_profit_factor | 0.5835 |
| gross_win_rate | 0.3776 |
| sharpe_ratio | -2.2970 |
| sortino_ratio | -0.3211 |
| max_drawdown | 0.3353 |
| cagr | -0.1387 |
| net_avg_win | 69.7517 |
| net_avg_loss | -93.5835 |
| avg_hold_time_bars | 9.4490 |
| exposure | 0.0421 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
