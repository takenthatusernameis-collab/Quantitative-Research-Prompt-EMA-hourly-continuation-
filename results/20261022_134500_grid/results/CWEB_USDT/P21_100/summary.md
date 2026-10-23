# EMA Hourly Continuation — CWEB/USDT P21_100

**Symbol:** CWEB/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.5610 |
| net_win_rate | 0.4404 |
| gross_profit_factor | 0.9111 |
| gross_win_rate | 0.4500 |
| sharpe_ratio | -4.9805 |
| sortino_ratio | -1.5898 |
| max_drawdown | 0.8652 |
| cagr | -0.5448 |
| net_avg_win | 48.0787 |
| net_avg_loss | -67.4386 |
| avg_hold_time_bars | 19.3558 |
| exposure | 0.4575 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
