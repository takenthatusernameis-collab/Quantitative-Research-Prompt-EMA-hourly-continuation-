# EMA Hourly Continuation — XPR/USDT P34_200

**Symbol:** XPR/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.5271 |
| net_win_rate | 0.4639 |
| gross_profit_factor | 0.8313 |
| gross_win_rate | 0.4685 |
| sharpe_ratio | -3.7086 |
| sortino_ratio | -1.0690 |
| max_drawdown | 0.7499 |
| cagr | -0.4115 |
| net_avg_win | 41.2151 |
| net_avg_loss | -67.6579 |
| avg_hold_time_bars | 22.4476 |
| exposure | 0.4377 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
