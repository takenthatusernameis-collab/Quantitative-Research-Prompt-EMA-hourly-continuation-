# EMA Hourly Continuation — CTC/USDT P21_50

**Symbol:** CTC/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 951 |
| net_profit_factor | 0.4245 |
| net_win_rate | 0.4385 |
| gross_profit_factor | 0.8584 |
| gross_win_rate | 0.4627 |
| sharpe_ratio | -7.9465 |
| sortino_ratio | -3.4519 |
| max_drawdown | 0.9876 |
| cagr | -0.8219 |
| net_avg_win | 17.4549 |
| net_avg_loss | -32.1114 |
| avg_hold_time_bars | 5.5478 |
| exposure | 0.2398 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
