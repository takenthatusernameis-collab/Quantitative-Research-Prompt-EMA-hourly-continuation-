# EMA Hourly Continuation — SQD/USDT P12_26

**Symbol:** SQD/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1275 |
| net_profit_factor | 0.5559 |
| net_win_rate | 0.4439 |
| gross_profit_factor | 0.9395 |
| gross_win_rate | 0.4580 |
| sharpe_ratio | -8.6592 |
| sortino_ratio | -4.4055 |
| max_drawdown | 0.9952 |
| cagr | -0.8887 |
| net_avg_win | 22.0106 |
| net_avg_loss | -31.6074 |
| avg_hold_time_bars | 3.1663 |
| exposure | 0.1898 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
