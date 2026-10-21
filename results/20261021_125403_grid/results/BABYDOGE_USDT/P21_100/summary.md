# EMA Hourly Continuation — BABYDOGE/USDT P21_100

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 48 |
| net_profit_factor | 1.0145 |
| net_win_rate | 0.5208 |
| gross_profit_factor | 1.0764 |
| gross_win_rate | 0.5208 |
| sharpe_ratio | 0.0528 |
| sortino_ratio | 0.0053 |
| max_drawdown | 0.0509 |
| cagr | 0.0014 |
| net_avg_win | 95.4705 |
| net_avg_loss | -102.2851 |
| avg_hold_time_bars | 71.0208 |
| exposure | 0.1543 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
