# EMA Hourly Continuation — CFX/USDT P21_200

**Symbol:** CFX/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.7730 |
| net_win_rate | 0.4839 |
| gross_profit_factor | 0.9334 |
| gross_win_rate | 0.4839 |
| sharpe_ratio | -1.4500 |
| sortino_ratio | -0.3636 |
| max_drawdown | 0.3944 |
| cagr | -0.1542 |
| net_avg_win | 77.9490 |
| net_avg_loss | -94.5397 |
| avg_hold_time_bars | 43.4839 |
| exposure | 0.6127 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
