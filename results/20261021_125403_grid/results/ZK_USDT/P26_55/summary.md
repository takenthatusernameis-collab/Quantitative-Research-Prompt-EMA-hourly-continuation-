# EMA Hourly Continuation — ZK/USDT P26_55

**Symbol:** ZK/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.7849 |
| net_win_rate | 0.4988 |
| gross_profit_factor | 1.0095 |
| gross_win_rate | 0.4988 |
| sharpe_ratio | -1.7550 |
| sortino_ratio | -0.5396 |
| max_drawdown | 0.4913 |
| cagr | -0.2195 |
| net_avg_win | 75.0685 |
| net_avg_loss | -95.1989 |
| avg_hold_time_bars | 7.0256 |
| exposure | 0.1469 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
