# EMA Hourly Continuation — BABYDOGE/USDT P21_200

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 57 |
| net_profit_factor | 1.2059 |
| net_win_rate | 0.5614 |
| gross_profit_factor | 1.2662 |
| gross_win_rate | 0.5614 |
| sharpe_ratio | 0.4678 |
| sortino_ratio | 0.0516 |
| max_drawdown | 0.0415 |
| cagr | 0.0213 |
| net_avg_win | 99.9456 |
| net_avg_loss | -106.0882 |
| avg_hold_time_bars | 112.2632 |
| exposure | 0.2896 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
