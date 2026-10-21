# EMA Hourly Continuation — EUL/USDT P21_100

**Symbol:** EUL/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.7758 |
| net_win_rate | 0.4897 |
| gross_profit_factor | 0.9440 |
| gross_win_rate | 0.4897 |
| sharpe_ratio | -1.5414 |
| sortino_ratio | -0.4604 |
| max_drawdown | 0.4356 |
| cagr | -0.1913 |
| net_avg_win | 66.8364 |
| net_avg_loss | -82.6720 |
| avg_hold_time_bars | 18.3799 |
| exposure | 0.3651 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
