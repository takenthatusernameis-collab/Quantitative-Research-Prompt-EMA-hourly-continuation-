# EMA Hourly Continuation — XAI/USDT P21_50

**Symbol:** XAI/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1074 |
| net_profit_factor | 0.6206 |
| net_win_rate | 0.4497 |
| gross_profit_factor | 0.9557 |
| gross_win_rate | 0.4655 |
| sharpe_ratio | -6.9346 |
| sortino_ratio | -3.1920 |
| max_drawdown | 0.9809 |
| cagr | -0.7869 |
| net_avg_win | 33.1645 |
| net_avg_loss | -43.6759 |
| avg_hold_time_bars | 4.9004 |
| exposure | 0.2392 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
