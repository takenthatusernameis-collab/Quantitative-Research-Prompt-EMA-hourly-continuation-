# EMA Hourly Continuation — ALT/USDT P144_200

**Symbol:** ALT/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 248 |
| net_profit_factor | 0.6914 |
| net_win_rate | 0.4879 |
| gross_profit_factor | 0.9314 |
| gross_win_rate | 0.4879 |
| sharpe_ratio | -1.7382 |
| sortino_ratio | -0.3912 |
| max_drawdown | 0.4247 |
| cagr | -0.1649 |
| net_avg_win | 67.3809 |
| net_avg_loss | -92.8529 |
| avg_hold_time_bars | 8.7661 |
| exposure | 0.0988 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
