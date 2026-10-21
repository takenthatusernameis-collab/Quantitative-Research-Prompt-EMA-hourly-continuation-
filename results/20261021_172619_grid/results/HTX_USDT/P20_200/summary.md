# EMA Hourly Continuation — HTX/USDT P20_200

**Symbol:** HTX/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.6403 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 0.9580 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -2.7033 |
| sortino_ratio | -0.6638 |
| max_drawdown | 0.5721 |
| cagr | -0.2694 |
| net_avg_win | 68.1031 |
| net_avg_loss | -98.1217 |
| avg_hold_time_bars | 47.7450 |
| exposure | 0.6439 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
