# EMA Hourly Continuation — IO/USDT P89_100

**Symbol:** IO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 103 |
| net_profit_factor | 0.8096 |
| net_win_rate | 0.5146 |
| gross_profit_factor | 1.0535 |
| gross_win_rate | 0.5146 |
| sharpe_ratio | -0.6715 |
| sortino_ratio | -0.1012 |
| max_drawdown | 0.1348 |
| cagr | -0.0456 |
| net_avg_win | 83.6663 |
| net_avg_loss | -109.5486 |
| avg_hold_time_bars | 5.4660 |
| exposure | 0.0273 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
