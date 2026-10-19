# EMA Hourly Continuation — JUP/USDT P21_100

**Symbol:** JUP/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 666 |
| net_profit_factor | 0.5801 |
| net_win_rate | 0.4444 |
| gross_profit_factor | 0.8281 |
| gross_win_rate | 0.4474 |
| sharpe_ratio | -4.6455 |
| sortino_ratio | -1.6854 |
| max_drawdown | 0.8738 |
| cagr | -0.5519 |
| net_avg_win | 40.4495 |
| net_avg_loss | -55.7869 |
| avg_hold_time_bars | 13.0826 |
| exposure | 0.3960 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
