# EMA Hourly Continuation — FIL/USDT P26_89

**Symbol:** FIL/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.6854 |
| net_win_rate | 0.4685 |
| gross_profit_factor | 0.8790 |
| gross_win_rate | 0.4685 |
| sharpe_ratio | -2.4573 |
| sortino_ratio | -0.7245 |
| max_drawdown | 0.5815 |
| cagr | -0.2832 |
| net_avg_win | 61.4061 |
| net_avg_loss | -78.9837 |
| avg_hold_time_bars | 14.9953 |
| exposure | 0.2924 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
