# EMA Hourly Continuation — STRK/USDT P21_100

**Symbol:** STRK/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.8148 |
| net_win_rate | 0.4979 |
| gross_profit_factor | 0.9881 |
| gross_win_rate | 0.4979 |
| sharpe_ratio | -1.4174 |
| sortino_ratio | -0.4472 |
| max_drawdown | 0.4529 |
| cagr | -0.1875 |
| net_avg_win | 73.8454 |
| net_avg_loss | -89.8904 |
| avg_hold_time_bars | 16.3601 |
| exposure | 0.3614 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
