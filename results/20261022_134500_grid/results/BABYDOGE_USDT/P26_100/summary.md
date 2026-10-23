# EMA Hourly Continuation — BABYDOGE/USDT P26_100

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 51 |
| net_profit_factor | 1.2095 |
| net_win_rate | 0.5686 |
| gross_profit_factor | 1.3044 |
| gross_win_rate | 0.5686 |
| sharpe_ratio | 0.4503 |
| sortino_ratio | 0.0470 |
| max_drawdown | 0.0617 |
| cagr | 0.0194 |
| net_avg_win | 98.8621 |
| net_avg_loss | -107.7421 |
| avg_hold_time_bars | 33.7059 |
| exposure | 0.0778 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
