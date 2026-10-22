# EMA Hourly Continuation — RIO/USDT P34_50

**Symbol:** RIO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 203 |
| net_profit_factor | 0.6277 |
| net_win_rate | 0.4286 |
| gross_profit_factor | 0.7537 |
| gross_win_rate | 0.4286 |
| sharpe_ratio | -2.1089 |
| sortino_ratio | -0.4267 |
| max_drawdown | 0.4248 |
| cagr | -0.1787 |
| net_avg_win | 74.9960 |
| net_avg_loss | -89.6134 |
| avg_hold_time_bars | 6.0394 |
| exposure | 0.0563 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
