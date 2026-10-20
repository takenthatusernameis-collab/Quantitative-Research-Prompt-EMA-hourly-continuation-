# EMA Hourly Continuation — CKB/USDT P34_55

**Symbol:** CKB/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 907 |
| net_profit_factor | 0.4219 |
| net_win_rate | 0.4123 |
| gross_profit_factor | 0.7823 |
| gross_win_rate | 0.4366 |
| sharpe_ratio | -9.3168 |
| sortino_ratio | -3.9762 |
| max_drawdown | 0.9938 |
| cagr | -0.8667 |
| net_avg_win | 19.3872 |
| net_avg_loss | -32.2465 |
| avg_hold_time_bars | 2.9559 |
| exposure | 0.1219 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
