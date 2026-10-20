# EMA Hourly Continuation — RIO/USDT P34_100

**Symbol:** RIO/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 794 |
| net_profit_factor | 0.5260 |
| net_win_rate | 0.4106 |
| gross_profit_factor | 0.7404 |
| gross_win_rate | 0.4118 |
| sharpe_ratio | -6.3292 |
| sortino_ratio | -2.5098 |
| max_drawdown | 0.9561 |
| cagr | -0.7032 |
| net_avg_win | 32.3834 |
| net_avg_loss | -42.8823 |
| avg_hold_time_bars | 6.6612 |
| exposure | 0.2428 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
