# EMA Hourly Continuation — TWT/USDT P21_50

**Symbol:** TWT/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1047 |
| net_profit_factor | 0.3652 |
| net_win_rate | 0.4460 |
| gross_profit_factor | 0.8077 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -8.6278 |
| sortino_ratio | -3.9221 |
| max_drawdown | 0.9938 |
| cagr | -0.8640 |
| net_avg_win | 12.2374 |
| net_avg_loss | -26.9797 |
| avg_hold_time_bars | 4.4651 |
| exposure | 0.2125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
