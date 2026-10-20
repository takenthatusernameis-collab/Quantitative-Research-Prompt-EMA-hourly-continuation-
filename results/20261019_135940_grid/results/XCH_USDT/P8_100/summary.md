# EMA Hourly Continuation — XCH/USDT P8_100

**Symbol:** XCH/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 809 |
| net_profit_factor | 0.5514 |
| net_win_rate | 0.4648 |
| gross_profit_factor | 0.8857 |
| gross_win_rate | 0.4784 |
| sharpe_ratio | -4.3691 |
| sortino_ratio | -1.7473 |
| max_drawdown | 0.8803 |
| cagr | -0.5660 |
| net_avg_win | 28.6713 |
| net_avg_loss | -45.1530 |
| avg_hold_time_bars | 17.9098 |
| exposure | 0.6586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
