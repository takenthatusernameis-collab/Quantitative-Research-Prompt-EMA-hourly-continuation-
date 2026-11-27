# EMA Hourly Continuation — SHR/USDT P34_100

**Symbol:** SHR/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 888 |
| net_profit_factor | 0.4171 |
| net_win_rate | 0.3457 |
| gross_profit_factor | 0.5804 |
| gross_win_rate | 0.3457 |
| sharpe_ratio | -8.6455 |
| sortino_ratio | -3.5840 |
| max_drawdown | 0.9882 |
| cagr | -0.8259 |
| net_avg_win | 23.0261 |
| net_avg_loss | -29.1694 |
| avg_hold_time_bars | 6.4932 |
| exposure | 0.2609 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
