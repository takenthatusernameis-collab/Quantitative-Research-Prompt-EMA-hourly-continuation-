# EMA Hourly Continuation — SUSHI/USDT P21_50

**Symbol:** SUSHI/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 512 |
| net_profit_factor | 0.6940 |
| net_win_rate | 0.4746 |
| gross_profit_factor | 0.9232 |
| gross_win_rate | 0.4746 |
| sharpe_ratio | -2.7849 |
| sortino_ratio | -0.8979 |
| max_drawdown | 0.6519 |
| cagr | -0.3372 |
| net_avg_win | 60.2714 |
| net_avg_loss | -78.4492 |
| avg_hold_time_bars | 7.4551 |
| exposure | 0.1727 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
