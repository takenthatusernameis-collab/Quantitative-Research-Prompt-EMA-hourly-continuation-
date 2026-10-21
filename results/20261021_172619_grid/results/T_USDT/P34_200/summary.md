# EMA Hourly Continuation — T/USDT P34_200

**Symbol:** T/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 319 |
| net_profit_factor | 0.7626 |
| net_win_rate | 0.4984 |
| gross_profit_factor | 1.0073 |
| gross_win_rate | 0.5047 |
| sharpe_ratio | -1.5140 |
| sortino_ratio | -0.3853 |
| max_drawdown | 0.3823 |
| cagr | -0.1628 |
| net_avg_win | 72.9584 |
| net_avg_loss | -95.0751 |
| avg_hold_time_bars | 33.2884 |
| exposure | 0.4805 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
