# EMA Hourly Continuation — WEMIX/USDT P21_26

**Symbol:** WEMIX/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 152 |
| net_profit_factor | 0.3933 |
| net_win_rate | 0.3355 |
| gross_profit_factor | 0.5477 |
| gross_win_rate | 0.3355 |
| sharpe_ratio | -3.7866 |
| sortino_ratio | -0.6647 |
| max_drawdown | 0.5505 |
| cagr | -0.2677 |
| net_avg_win | 68.9893 |
| net_avg_loss | -88.5700 |
| avg_hold_time_bars | 9.1118 |
| exposure | 0.0630 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
