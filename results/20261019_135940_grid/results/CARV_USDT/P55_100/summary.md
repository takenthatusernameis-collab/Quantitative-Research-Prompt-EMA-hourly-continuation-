# EMA Hourly Continuation — CARV/USDT P55_100

**Symbol:** CARV/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.3823 |
| net_win_rate | 0.4204 |
| gross_profit_factor | 0.7071 |
| gross_win_rate | 0.4394 |
| sharpe_ratio | -5.9715 |
| sortino_ratio | -1.9354 |
| max_drawdown | 0.8499 |
| cagr | -0.6021 |
| net_avg_win | 29.5747 |
| net_avg_loss | -56.1162 |
| avg_hold_time_bars | 5.8717 |
| exposure | 0.1391 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
