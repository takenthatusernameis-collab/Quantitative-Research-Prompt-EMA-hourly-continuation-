# EMA Hourly Continuation — GRT/USDT P89_100

**Symbol:** GRT/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 577 |
| net_profit_factor | 0.2501 |
| net_win_rate | 0.4021 |
| gross_profit_factor | 0.7375 |
| gross_win_rate | 0.4489 |
| sharpe_ratio | -8.8052 |
| sortino_ratio | -3.0529 |
| max_drawdown | 0.9827 |
| cagr | -0.7990 |
| net_avg_win | 14.1236 |
| net_avg_loss | -37.9771 |
| avg_hold_time_bars | 1.9116 |
| exposure | 0.0499 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
