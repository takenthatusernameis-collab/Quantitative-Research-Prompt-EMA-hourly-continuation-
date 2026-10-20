# EMA Hourly Continuation — WEMIX/USDT P8_100

**Symbol:** WEMIX/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1123 |
| net_profit_factor | 0.3477 |
| net_win_rate | 0.3188 |
| gross_profit_factor | 0.5481 |
| gross_win_rate | 0.3339 |
| sharpe_ratio | -12.5277 |
| sortino_ratio | -5.9759 |
| max_drawdown | 0.9994 |
| cagr | -0.9482 |
| net_avg_win | 14.8815 |
| net_avg_loss | -20.0283 |
| avg_hold_time_bars | 12.4052 |
| exposure | 0.6332 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
