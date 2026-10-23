# EMA Hourly Continuation — LPT/USDT P34_100

**Symbol:** LPT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 686 |
| net_profit_factor | 0.5599 |
| net_win_rate | 0.4461 |
| gross_profit_factor | 0.8524 |
| gross_win_rate | 0.4665 |
| sharpe_ratio | -4.9872 |
| sortino_ratio | -1.8400 |
| max_drawdown | 0.8907 |
| cagr | -0.5840 |
| net_avg_win | 36.9812 |
| net_avg_loss | -53.1866 |
| avg_hold_time_bars | 8.7332 |
| exposure | 0.2723 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
