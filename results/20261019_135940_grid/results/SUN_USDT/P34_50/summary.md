# EMA Hourly Continuation — SUN/USDT P34_50

**Symbol:** SUN/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 806 |
| net_profit_factor | 0.1415 |
| net_win_rate | 0.2928 |
| gross_profit_factor | 0.6601 |
| gross_win_rate | 0.3933 |
| sharpe_ratio | -14.1529 |
| sortino_ratio | -6.1155 |
| max_drawdown | 0.9998 |
| cagr | -0.9646 |
| net_avg_win | 6.9843 |
| net_avg_loss | -20.4318 |
| avg_hold_time_bars | 3.6687 |
| exposure | 0.1338 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
