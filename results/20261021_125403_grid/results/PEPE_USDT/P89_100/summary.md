# EMA Hourly Continuation — PEPE/USDT P89_100

**Symbol:** PEPE/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 62 |
| net_profit_factor | 1.2748 |
| net_win_rate | 0.6290 |
| gross_profit_factor | 1.6690 |
| gross_win_rate | 0.6290 |
| sharpe_ratio | 0.6285 |
| sortino_ratio | 0.0740 |
| max_drawdown | 0.0690 |
| cagr | 0.0302 |
| net_avg_win | 92.1252 |
| net_avg_loss | -122.5342 |
| avg_hold_time_bars | 5.1290 |
| exposure | 0.0145 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
