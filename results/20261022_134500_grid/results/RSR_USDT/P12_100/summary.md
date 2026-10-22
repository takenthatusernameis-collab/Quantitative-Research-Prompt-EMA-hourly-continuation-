# EMA Hourly Continuation — RSR/USDT P12_100

**Symbol:** RSR/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 698 |
| net_profit_factor | 0.6769 |
| net_win_rate | 0.4756 |
| gross_profit_factor | 0.9427 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -3.4048 |
| sortino_ratio | -1.2641 |
| max_drawdown | 0.7925 |
| cagr | -0.4512 |
| net_avg_win | 49.1204 |
| net_avg_loss | -65.8260 |
| avg_hold_time_bars | 17.3152 |
| exposure | 0.5494 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
