# EMA Hourly Continuation — BABYDOGE/USDT P55_100

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 19 |
| net_profit_factor | 0.6641 |
| net_win_rate | 0.4211 |
| gross_profit_factor | 0.7223 |
| gross_win_rate | 0.4211 |
| sharpe_ratio | -0.5458 |
| sortino_ratio | -0.0333 |
| max_drawdown | 0.0474 |
| cagr | -0.0153 |
| net_avg_win | 94.1461 |
| net_avg_loss | -103.1037 |
| avg_hold_time_bars | 23.4211 |
| exposure | 0.0201 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
