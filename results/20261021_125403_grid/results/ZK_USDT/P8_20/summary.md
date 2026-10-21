# EMA Hourly Continuation — ZK/USDT P8_20

**Symbol:** ZK/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 582 |
| net_profit_factor | 0.6574 |
| net_win_rate | 0.4691 |
| gross_profit_factor | 0.8731 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -3.2730 |
| sortino_ratio | -1.1670 |
| max_drawdown | 0.7261 |
| cagr | -0.4141 |
| net_avg_win | 50.1906 |
| net_avg_loss | -67.4492 |
| avg_hold_time_bars | 4.8746 |
| exposure | 0.1383 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
