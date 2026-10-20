# EMA Hourly Continuation — EUL/USDT P21_100

**Symbol:** EUL/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 623 |
| net_profit_factor | 0.5088 |
| net_win_rate | 0.4462 |
| gross_profit_factor | 0.7473 |
| gross_win_rate | 0.4543 |
| sharpe_ratio | -4.4926 |
| sortino_ratio | -1.5791 |
| max_drawdown | 0.8525 |
| cagr | -0.5290 |
| net_avg_win | 31.6307 |
| net_avg_loss | -50.0968 |
| avg_hold_time_bars | 13.4960 |
| exposure | 0.3822 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
