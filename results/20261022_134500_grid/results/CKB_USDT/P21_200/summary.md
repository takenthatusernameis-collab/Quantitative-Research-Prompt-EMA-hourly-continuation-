# EMA Hourly Continuation — CKB/USDT P21_200

**Symbol:** CKB/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.6134 |
| net_win_rate | 0.4688 |
| gross_profit_factor | 0.8515 |
| gross_win_rate | 0.4734 |
| sharpe_ratio | -3.0412 |
| sortino_ratio | -0.8918 |
| max_drawdown | 0.6665 |
| cagr | -0.3457 |
| net_avg_win | 51.2248 |
| net_avg_loss | -73.7041 |
| avg_hold_time_bars | 30.9353 |
| exposure | 0.6089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
