# EMA Hourly Continuation — STRAX/USDT P34_100

**Symbol:** STRAX/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.6093 |
| net_win_rate | 0.4495 |
| gross_profit_factor | 0.8442 |
| gross_win_rate | 0.4515 |
| sharpe_ratio | -3.7384 |
| sortino_ratio | -1.1736 |
| max_drawdown | 0.7532 |
| cagr | -0.4183 |
| net_avg_win | 53.0478 |
| net_avg_loss | -71.0806 |
| avg_hold_time_bars | 11.7237 |
| exposure | 0.2600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
