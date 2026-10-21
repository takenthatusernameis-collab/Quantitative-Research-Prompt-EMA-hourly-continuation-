# EMA Hourly Continuation — BSV/USDT P21_50

**Symbol:** BSV/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.6550 |
| net_win_rate | 0.4894 |
| gross_profit_factor | 0.9468 |
| gross_win_rate | 0.4894 |
| sharpe_ratio | -2.9546 |
| sortino_ratio | -0.9656 |
| max_drawdown | 0.6708 |
| cagr | -0.3561 |
| net_avg_win | 50.0088 |
| net_avg_loss | -73.1746 |
| avg_hold_time_bars | 7.2408 |
| exposure | 0.1708 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
