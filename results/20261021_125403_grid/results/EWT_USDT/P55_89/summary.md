# EMA Hourly Continuation — EWT/USDT P55_89

**Symbol:** EWT/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 235 |
| net_profit_factor | 0.7162 |
| net_win_rate | 0.4851 |
| gross_profit_factor | 0.9423 |
| gross_win_rate | 0.4851 |
| sharpe_ratio | -1.6243 |
| sortino_ratio | -0.3556 |
| max_drawdown | 0.3911 |
| cagr | -0.1515 |
| net_avg_win | 74.8555 |
| net_avg_loss | -98.4702 |
| avg_hold_time_bars | 8.0426 |
| exposure | 0.0859 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
