# EMA Hourly Continuation — JUP/USDT P89_200

**Symbol:** JUP/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.7004 |
| net_win_rate | 0.4701 |
| gross_profit_factor | 0.8610 |
| gross_win_rate | 0.4701 |
| sharpe_ratio | -1.6812 |
| sortino_ratio | -0.3917 |
| max_drawdown | 0.4110 |
| cagr | -0.1647 |
| net_avg_win | 67.4530 |
| net_avg_loss | -85.4592 |
| avg_hold_time_bars | 13.3657 |
| exposure | 0.1628 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
