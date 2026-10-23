# EMA Hourly Continuation — REZ/USDT P12_100

**Symbol:** REZ/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 590 |
| net_profit_factor | 0.8002 |
| net_win_rate | 0.5136 |
| gross_profit_factor | 1.0539 |
| gross_win_rate | 0.5136 |
| sharpe_ratio | -1.7736 |
| sortino_ratio | -0.6170 |
| max_drawdown | 0.5307 |
| cagr | -0.2538 |
| net_avg_win | 68.1083 |
| net_avg_loss | -89.8645 |
| avg_hold_time_bars | 21.8559 |
| exposure | 0.5949 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
